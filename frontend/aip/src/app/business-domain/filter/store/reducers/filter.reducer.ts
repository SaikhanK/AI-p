import { createReducer, on } from '@ngrx/store';
import { StoreFilter, StoreState } from '../../../../data-domain/store.model';
import { setFilter, clearFilters } from '../actions/filter.actions';

// Der Startzustand ist ein leeres Objekt gemäß deinem StoreFilter Interface
export const initialFilterState: StoreFilter = {};

export const filterReducer = createReducer(
  initialFilterState,
  // WICHTIG: Hier muss 'setFilter' stehen (passend zur Action)
  on(setFilter, (state: any, { key, value }: any) => {
    return {
      ...state,      // Kopiert alle alten Filter
      [key]: value   // Fügt den neuen hinzu oder überschreibt ihn
    };
  }),

  
  on(clearFilters, () => ({})) // Leert alle Filter
);