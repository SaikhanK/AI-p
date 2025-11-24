import { Routes } from '@angular/router';
import { HomeComponent } from './pages/Home/home.component';
import { ProductComponent } from './pages/Product/product.component';
import { ProductDetailComponent } from './pages/ProductDetail/productdetail.component';


export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'product', component: ProductComponent },
    { path: 'productdetail/:id', component: ProductDetailComponent }
];
