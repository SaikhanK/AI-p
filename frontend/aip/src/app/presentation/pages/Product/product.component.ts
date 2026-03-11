import { Component, OnInit } from "@angular/core";
import { HttpClient, HttpParams } from "@angular/common/http";
import { CommonModule } from "@angular/common";
import { RouterLink } from '@angular/router';
import { BehaviorSubject, Observable } from "rxjs";
import { switchMap, tap } from "rxjs/operators";
import { StoreFilter, StoreState } from "../../../data-domain/store.model";
import { Store } from '@ngrx/store';

@Component({
    selector: 'app-product',
    standalone: true,
    imports: [CommonModule, RouterLink],
    templateUrl: './product.component.html',
    styleUrl: './product.component.css',
})
export class ProductComponent implements OnInit {
    private filterSubject$ = new BehaviorSubject<StoreFilter>({});
    
    products$: Observable<any> | undefined;

    constructor(private store: Store<StoreState> ,private http: HttpClient) {}

    ngOnInit() {
        this.products$ = this.store.select('filter').pipe(
          switchMap((filter: StoreFilter) => {
            const params = this.buildParams(filter);
            return this.http.get('http://localhost:8000/api/product/', { params });
          }),
          tap(products => console.log('Products', products))
        );
      }
    buildParams(filter: StoreFilter): HttpParams {
        let params = new HttpParams();
      
        Object.entries(filter).forEach(([key, value]) => {
          if (Array.isArray(value)) {
            value.forEach(v => {
              params = params.append(key, v.toString());
            });
          } else {
            params = params.set(key, value.toString());
          }
        });
      
        return params;
      }
    setFilter(key: string, value: any) {
        const current = this.filterSubject$.value;
    
        const updated = { ...current, [key]: value };
        this.filterSubject$.next(updated);
    }
}