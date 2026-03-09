import { Component, OnInit } from "@angular/core";
import { HttpClient, HttpParams } from "@angular/common/http";
import { CommonModule } from "@angular/common";
import { RouterLink } from '@angular/router';
import { BehaviorSubject, Observable } from "rxjs";
import { switchMap, tap } from "rxjs/operators";
import { StoreFilter } from "../../../data-domain/store.model";

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

    constructor(private http: HttpClient) {}

    ngOnInit() {
        this.products$ = this.filterSubject$.pipe(
            tap(currentFilter => console.log('Sende Anfrage mit Filtern:', currentFilter)),
            switchMap(activeFilters => {
                let params = new HttpParams();
                
                Object.keys(activeFilters).forEach(key => {
                    const value = activeFilters[key];
                    if (value) {
                        if (Array.isArray(value)) {
                            value.forEach(v => params = params.append(key, v.toString()));
                        } else {
                            params = params.set(key, value.toString());
                        }
                    }
                });

                return this.http.get<any>('http://localhost:8000/api/product/', { params });
            })
        );
    }

    setFilter(key: string, value: any) {
        const current = this.filterSubject$.value;
    
        const updated = { ...current, [key]: value };
        this.filterSubject$.next(updated);
    }
}