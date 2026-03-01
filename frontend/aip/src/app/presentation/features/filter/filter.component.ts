import {Component, OnInit} from "@angular/core";
import { MatTableDataSource } from "@angular/material/table";
import { Store } from '@ngrx/store';
import { FormControl } from '@angular/forms';
import { debounceTime, distinctUntilChanged, map } from 'rxjs/operators';
import { StoreFilter, StoreState } from "../../../data-domain/store.model";
import { selectFilters } from "../../../business-domain/filter/store/selectors/filter.selector";
import { Observable } from "rxjs";
import { CombiendFilter, Filter, combiendfilter } from "../../../data-domain/filter.model";


@Component({
    selector: 'filter',
    standalone: true,
    imports: [],
    templateUrl: './fillter.component.html',
    styleUrl: './fillter.component.scss'
})
export class FilterComponent{
  filters$!: Observable<Filter[]>
  storeFilter!: StoreFilter;
  availableFilters = combiendfilter['product']

  constructor(private store: Store<StoreState>) {}

  onFilterChange(key: string, value: any) {
    console.log(`Filter ${key} geändert auf:`, value);

}
}