import { Component } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { HttpClient } from "@angular/common/http";
import { CommonModule } from "@angular/common";
import { RouterLink } from "@angular/router";

@Component({
    selector: 'app-productdetail',
    standalone: true,
    imports: [CommonModule, RouterLink],
    templateUrl: './productdetail.component.html',
    styleUrl: './productdetail.component.css',
})
export class ProductDetailComponent {
    id: number = 0;
    product: any = null;
    selectedImage: string | null = null;
    quantity: number = 1;

    constructor(private route: ActivatedRoute, private http: HttpClient) {
        this.id = Number(this.route.snapshot.paramMap.get('id'));
        this.getProductDetails();
    }

    getProductDetails() {
        this.http.get<any>(`http://localhost:8000/api/products/${this.id}/`)
            .subscribe({
                next: data => this.product = data,
                error: err => console.error(err)
            });
    }

    selectImage(url: string): void {
        this.selectedImage = url;
    }

    incQty(): void {
        this.quantity++;
    }

    decQty(): void {
        if (this.quantity > 1) this.quantity--;
    }
}