import { combineReducers } from 'redux';
import expensesReducer from './expenses';
import filtersReducer from './filters';
import authReducer from './auth';

const rootReducer = combineReducers({
  expenses: expensesReducer,
  filters: filtersReducer,
  auth: authReducer
});
export default rootReducer;
