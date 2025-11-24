import { Component } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { HttpClient } from "@angular/common/http";
import { CommonModule } from "@angular/common";

@Component({
    selector: 'app-productdetail',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './productdetail.component.html'
})
export class ProductDetailComponent {
    id: number = 0;
    product: any = null;
    constructor(private route: ActivatedRoute, private http: HttpClient) {
        this.id = Number(this.route.snapshot.paramMap.get('id'));
        console.log("ID from URL:", this.id);
        console.log("API URL =", `http://localhost:8000/api/product/${this.id}/`);
        this.getProductDetails();
    }

    getProductDetails() {
        this.http.get<any>(`http://localhost:8000/api/product/${this.id}/`)
            .subscribe({
                next: data => this.product = data,
                error: err => console.error(err)
            });
    }

}