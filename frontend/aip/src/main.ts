import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { provideAnimations } from '@angular/platform-browser/animations';
import { provideStore } from '@ngrx/store'; // 1. Importieren
import { routes } from './app/app.routes';
import { filterReducer } from './app/business-domain/filter/store/reducers/filter.reducer';

bootstrapApplication(AppComponent, {
  providers: [
    provideAnimations(),
    provideRouter(routes),
    provideHttpClient(),
    provideStore({
      filter: filterReducer
    })
  ]
}).catch(err => console.error(err));
