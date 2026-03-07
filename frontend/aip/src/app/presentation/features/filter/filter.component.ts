import {Component, OnInit} from "@angular/core";
import { MatTableDataSource } from "@angular/material/table";
import { Store } from '@ngrx/store';
import { FormControl } from '@angular/forms';
import { debounceTime, distinctUntilChanged, map } from 'rxjs/operators';
import { StoreFilter, StoreState } from "../../../data-domain/store.model";
import { selectFilters } from "../../../business-domain/filter/store/selectors/filter.selector";
import { Observable } from "rxjs";
import { CombiendFilter, Filter, combiendfilter } from "../../../data-domain/filter.model";
import { HttpClient } from "@angular/common/http";
import { CommonModule } from "@angular/common";
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatCardModule } from '@angular/material/card';
import { MatSelectModule } from '@angular/material/select';
import { setFilter } from "../../../business-domain/filter/store/actions/filter.actions";


@Component({
    selector: 'filter',
    standalone: true,
    imports: [
      CommonModule,
    MatFormFieldModule,
    MatSelectModule
    ],
    templateUrl: './filter.component.html',
    styleUrl: './filter.component.scss'
})
export class FilterComponent{
  filters$!: Observable<Filter[]>
  storeFilter!: StoreFilter;
  availableFilters = combiendfilter['product']

  constructor(private store: Store<StoreState>, private http: HttpClient) {}

  ngOnInit() {

    this.http.get<any>('http://localhost:8000/api/product/')
      .subscribe(res => {
  
        this.availableFilters.forEach(filter => {
          if (filter.key === 'product_category') {
            filter.choices = res.category
          }
          if (filter.key === 'product_brand') {
            filter.choices = res.brand
          }
        })
      })
  
  }
  onFilterSelect(key: string, value: any) {
    this.store.dispatch(setFilter({ key, value }));
    console.log(`Store Update: ${key} = ${value}`);
  }


}