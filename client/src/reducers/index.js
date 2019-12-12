import { combineReducers } from 'redux';
import expensesReducer from './expenses';
import filtersReducer from './filters';
import authReducer from './auth';
import { savingSuccess, savingFail } from './savings';

const rootReducer = combineReducers({
  filters: filtersReducer,
  auth: authReducer,
  savings: savingSuccess,
  saveError: savingFail
});
export default rootReducer;
