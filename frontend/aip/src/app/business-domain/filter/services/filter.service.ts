import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { map } from 'rxjs/operators'
import { Observable } from 'rxjs'
import { CombiendFilter } from '../../../data-domain/filter.model'

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private http: HttpClient) {}

  getCombinedFilter(): Observable<CombiendFilter> {
    return this.http.get<any[]>('http://localhost:8000/api/product/').pipe(
      map(products => {

        const categories = [...new Set(products.map(p => p.category))]
        const brands = [...new Set(products.map(p => p.brand))]
        const colors = [...new Set(products.map(p => p.color))]

        return {
          product: [
            {
              key: 'product_category',
              choices: categories
            },
            {
              key: 'product_brand',
              choices: brands
            },
            {
              key: 'product_color',
              choices: colors
            }
          ]
        }
      })
    )
  }
}