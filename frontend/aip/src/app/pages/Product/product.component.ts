import { Component } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { CommonModule } from "@angular/common";
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
    selector: 'app-product',
    standalone: true,
    imports: [
        CommonModule,
        RouterLink
    ],
    templateUrl: './product.component.html',
    styleUrl: './product.component.css',
})
export class ProductComponent {
    products: any[] = [];

    constructor(private http: HttpClient) {
        this.getProducts();
    }

    getProducts() {
        this.http.get<any[]>('http://localhost:8000/api/product/')
            .subscribe({
                next: data => this.products = data,
                error: err => console.error(err)
            });
    }
}