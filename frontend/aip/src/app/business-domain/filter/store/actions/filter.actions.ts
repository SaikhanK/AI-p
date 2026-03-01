import { createAction, props } from '@ngrx/store';
import { Filter } from '../../../../data-domain/filter.model';

// Action um einen spezifischen Filterwert zu setzen
export const setFilter = createAction(
  '[Filter] Set Filter',
  props<{ key: string; value: string | number | string[] | number[] }>()
);

// Action um alle Filter zu löschen
export const clearFilters = createAction('[Filter] Clear Filters');