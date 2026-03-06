import { Component, OnInit } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { Store } from '@ngrx/store';

import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatCardModule } from '@angular/material/card';
import { MatSelectModule } from '@angular/material/select';
import { combiendfilter } from './data-domain/filter.model';
import { CommonModule } from '@angular/common'; // Für @for/ @if
import { setFilter } from './business-domain/filter/store/actions/filter.actions';
import { StoreState } from './data-domain/store.model';
import { HttpClient } from '@angular/common/http';
import { FilterComponent } from './presentation/features/filter/filter.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule, 
    ReactiveFormsModule, 
    MatFormFieldModule, 
    MatInputModule, 
    MatSelectModule,
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    ReactiveFormsModule,
    FilterComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent{
  filterControl = new FormControl<string>('', { nonNullable: true });

  productFilters = combiendfilter['product']; 
  constructor(private store: Store<StoreState>, private http: HttpClient) {}
}