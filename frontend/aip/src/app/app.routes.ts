import { Routes } from '@angular/router';
import { HomeComponent } from './presentation/pages/Home/home.component';
import { ProductComponent } from './presentation/pages/Product/product.component';
import { ProductDetailComponent } from './presentation/pages/ProductDetail/productdetail.component';


export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'product', component: ProductComponent },
    { path: 'productdetail/:id', component: ProductDetailComponent }
];
