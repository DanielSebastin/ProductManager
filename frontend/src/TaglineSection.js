import React from 'react';
import './TaglineSection.css';

const TaglineSection = () => {
  return (
    <div className="tagline-card">
      <div className="tagline-content">
        <h3>AWS RDS DEMO</h3>
        <p>This is an demo of RDS POSTGRESQL.</p>
        <div className="company-badge">
          <span className="powered-by">Powered by</span>
          <span className="company-name">AWS SERVICES</span>
        </div>
      </div>
    </div>
  );
};

export default TaglineSection;
