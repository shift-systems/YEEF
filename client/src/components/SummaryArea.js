import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import numeral from 'numeral';
import selectExpenses from '../selectors/expenses';
// import selectExpensesTotal from '../selectors/expenses-total';

export const SavingsSummary = ({ savingsCount, savingsTotal }) => {
  const formattedExpensesTotal = numeral(savingsTotal).format('$0,0.00');

  return (
    <div className="page-header">
      <div className="content-container">
        <h1 className="page-header__title">
          Viewing <span>{savingsCount}</span> Savings totalling{' '}
          <span>{formattedExpensesTotal}</span>
        </h1>
        <div className="page-header__actions">
          <Link className="button" to="/save">
            Save Money
          </Link>
        </div>
      </div>
    </div>
  );
};

const mapStateToProps = state => {
  const visibleSavings = selectExpenses(state.savings, state.filters);

  return {
    SavingsCount: visibleSavings.length,
    savingsTotal: 20
    // savingsTotal: selectExpensesTotal(visibleSavings)
  };
  {
  }
};

export default connect(mapStateToProps)(SavingsSummary);
