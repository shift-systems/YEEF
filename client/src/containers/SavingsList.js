import React from 'react';
import { connect } from 'react-redux';
import SavingsListItem from '../components/SavingsListItem';
import selectExpenses from '../selectors/expenses';

export const SavingList = props => (
  <div className="content-container">
    <div className="list-header">
      <div className="show-for-mobile">Savings</div>
      <div className="show-for-desktop">Saving</div>
      <div className="show-for-desktop">Amount</div>
    </div>
    <div className="list-body">
      {props.expenses.length === 0 ? (
        <div className="list-item list-item--message">
          <span>No expenses</span>
        </div>
      ) : (
        props.expenses.map(expense => {
          return <SavingsListItem key={expense.id} {...expense} />;
        })
      )}
    </div>
  </div>
);

const mapStateToProps = state => {
  return {
    expenses: selectExpenses(state.expenses, state.filters)
  };
};

export default connect(mapStateToProps)(SavingList);
