$w.onReady(() => {
    console.log("✅ Bookkeeping Page: Form loaded");
  
    $w('#submitQueryButton').onClick(submitQueryButton_click);
  
    // Set discipline and source context
    $w('#inputDiscipline').value = "Bookkeeping";
    $w('#inputSourceContext').value = "This response is based on UK bookkeeping practices, small business accounting standards, HMRC guidance, and applicable Financial Reporting Standards (FRS).";
    $w('#inputJobCode').value = 3011; // Example job code for Bookkeeping
  
    // Job Titles
    $w('#dropdownJobTitle').options = [
      { label: "Bookkeeper", value: "The user is a professional bookkeeper handling daily financial records." },
      { label: "Accounts Assistant", value: "The user is an accounts assistant supporting financial operations." },
      { label: "Payroll Clerk", value: "The user handles payroll and employee payment records." },
      { label: "Junior Accountant", value: "The user is an entry-level accountant involved in bookkeeping tasks." },
      { label: "Self-Employed / Sole Trader", value: "The user manages their own business finances and record-keeping." },
      { label: "Finance Manager", value: "The user oversees bookkeeping processes in a small business environment." },
      { label: "Other", value: "The user has a bookkeeping-related role not listed above." }
    ];
  
    // Timeline Options
    $w('#dropdownTimeline').options = [
      { label: "Urgent – VAT Return Due Today", value: "The matter requires immediate action to submit VAT returns or financial filings." },
      { label: "Month-End Close", value: "The matter relates to the closing procedures for the current month." },
      { label: "Quarter-End Review", value: "The matter is part of a quarterly accounting review or filing requirement." },
      { label: "Year-End Preparation", value: "The matter relates to preparing for end-of-year accounts." },
      { label: "Within 30 Days", value: "Action is required within the next 30 days." },
      { label: "Historical Record Review", value: "The query relates to reviewing previous financial periods or correcting entries." },
      { label: "Other", value: "Timeline not listed here." }
    ];
  
    // Site Name Options
    $w('#dropdownSiteName').options = [
      { label: "Main Office", value: "Main Office" },
      { label: "Branch Office", value: "Branch Office" },
      { label: "Client Premises", value: "Client Premises" },
      { label: "Remote Work / Home Office", value: "Remote Work / Home Office" },
      { label: "Co-Working Space", value: "Co-Working Space" },
      { label: "Other", value: "Other location not listed" }
    ];
  
    // Search Type (Expanded for VAT, CIS, FRS)
    $w('#dropdownSearchType').options = [
      { label: "VAT Submission Queries", value: "The user needs assistance completing or correcting VAT returns." },
      { label: "CIS Tax Queries", value: "The user needs support handling CIS returns, deductions, and HMRC submissions." },
      { label: "Bank Reconciliation", value: "The user needs help reconciling bank statements with financial records." },
      { label: "Payroll Processing", value: "The user needs guidance on payroll records, PAYE, and compliance." },
      { label: "Invoicing and Credit Control", value: "The user seeks help managing invoices, customer payments, and overdue debt." },
      { label: "Accounts Payable Management", value: "The user needs support managing supplier invoices, credit terms, and payments." },
      { label: "MTD for VAT or Income Tax", value: "The user needs help complying with Making Tax Digital requirements for VAT or Income Tax Self Assessment." },
      { label: "FRS 102 Reporting Queries", value: "The user needs assistance with financial reporting under FRS 102 standards." },
      { label: "FRS 105 Micro-Entity Queries", value: "The user needs assistance preparing accounts under FRS 105 micro-entity standards." },
      { label: "Disclosure Requirements", value: "The user is seeking guidance on financial statement disclosure requirements under UK GAAP." },
      { label: "Revenue Recognition (FRS 102)", value: "The user needs clarification on revenue recognition policies in compliance with FRS 102 Section 23." },
      { label: "Lease Accounting (FRS 102)", value: "The user needs assistance on the accounting treatment of leases under FRS 102 Section 20." },
      { label: "Other", value: "The user has a bookkeeping or financial compliance issue not listed above." }
    ];
  
    // Funnel1 (Task Support Expanded)
    $w('#dropdownFunnel1').options = [
      { label: "Help completing VAT return", value: "The user needs assistance completing a VAT return for the quarter." },
      { label: "Help completing CIS monthly return", value: "The user needs assistance completing or checking CIS filings." },
      { label: "Clarify ledger postings or journals", value: "The user needs clarification on double-entry bookkeeping, journal adjustments, or postings." },
      { label: "Prepare FRS-compliant financial statements", value: "The user is preparing statutory financial statements compliant with FRS 102 or FRS 105." },
      { label: "Clarify FRS 102 disclosure requirements", value: "The user needs clarification on note disclosures and accounting policy statements under FRS 102." },
      { label: "Assist preparing management accounts", value: "The user is preparing management accounts or internal financial summaries." },
      { label: "Registering subcontractors under CIS", value: "The user is seeking guidance on registering subcontractors correctly under CIS." },
      { label: "Other", value: "Other bookkeeping or accounting support task." }
    ];
  
    // Funnel2 (Internal confirmations)
    $w('#dropdownFunnel').options = [
      { label: "Bank feed synchronisation completed", value: "Bank feeds have been successfully synchronised with financial records." },
      { label: "Client confirmation received", value: "The client has confirmed figures or adjustments." },
      { label: "Payroll journal posted", value: "Payroll journal entries have been posted to the ledger." },
      { label: "Aged debtor review completed", value: "The user has reviewed the aged debtor report for outstanding balances." },
      { label: "Regulatory body notification completed", value: "Notifications or filings with HMRC or Companies House have been completed." },
      { label: "Other", value: "Other internal actions completed." }
    ];
  
    // Funnel3 (Pending Actions)
    $w('#dropdownFunnel3').options = [
      { label: "Awaiting bank feed update", value: "Awaiting updated transactions or reconciliations from the bank feed." },
      { label: "Awaiting client invoices or receipts", value: "Awaiting submission of invoices, receipts, or expenses from the client." },
      { label: "Awaiting VAT submission acknowledgment", value: "Awaiting acknowledgment from HMRC confirming VAT submission received." },
      { label: "Awaiting final year-end approval", value: "Awaiting final sign-off from client or partner for year-end accounts." },
      { label: "Awaiting subcontractor CIS verification", value: "Awaiting CIS status confirmation from HMRC for subcontractors." },
      { label: "Other", value: "Other pending or delayed matters not listed." }
    ];
  
    // Rank Level (Bookkeeping job levels)
    $w('#dropdownBonus').options = [
      { label: "Trainee / Junior", value: "Level 1 – Entry-level bookkeeper or accounting assistant." },
      { label: "Bookkeeper", value: "Level 2 – Qualified or experienced bookkeeper handling day-to-day operations." },
      { label: "Senior Bookkeeper", value: "Level 3 – Senior bookkeeper managing others or multiple accounts." },
      { label: "Finance Supervisor", value: "Level 4 – Supervisor overseeing bookkeeping or finance teams." },
      { label: "Finance Manager", value: "Level 5 – Manager responsible for financial operations and compliance." }
    ];
  });

  
  function getValue(id) {
    return $w(`#${id}`).value || "";
  }
  
  export function submitQueryButton_click(event) {
    console.log("🚨 Submit button clicked");
  
    const fullName = $w('#inputName').value.trim();
    const email = $w('#inputEmail').value.trim();
    const queryText = $w('#inputQuery').value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  
    if (!fullName || !email || !queryText) {
      $w('#statusText').text = "❌ Please enter your name, email, and a query before submitting.";
      return;
    }
  
    if (!emailRegex.test(email)) {
      $w('#statusText').text = "❌ Please enter a valid email address.";
      return;
    }
  
    const payload = {
      full_name: fullName,
      user_email: email,
      query: queryText,
      job_title: getValue("dropdownJobTitle") || "Not provided",
      discipline: $w('#inputDiscipline').value,
      timeline: getValue("dropdownTimeline") || "Not specified",
      site: getValue("dropdownSiteName") || "Not provided",
      search_type: getValue("dropdownSearchType") || "Not provided",
      funnel_1: getValue("dropdownFunnel1") || "Not answered",
      funnel_2: getValue("dropdownFunnel") || "Not answered",
      funnel_3: getValue("dropdownFunnel3") || "Not answered",
      rank_level: getValue("dropdownBonus") || "Not specified",
      job_code: Number($w('#inputJobCode').value || 0),
      requires_action_sheet: true,
      source_context: $w('#inputSourceContext').value,
      supervisor_name: $w('#inputSupervisorName')?.value || "Not provided",
      supervisor_email: $w('#inputSupervisorEmail')?.value || "Not provided",
      hr_email: $w('#inputHrEmail')?.value || "Not provided"
    };
  
    $w('#statusText').text = "⏳ Sending your query...";
    $w('#submitQueryButton').disable();
  
    console.log("📤 Sending payload:", payload);
  
    fetch("https://accounting-1es7.onrender.com/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })
   
      .then(response => {
        if (!response.ok) throw new Error("Server error: " + response.status);
        return response.json();
      })
      .then(result => {
        console.log("✅ API Response:", result);
        const message = result.message || "✅ Submitted successfully.";
        $w('#statusText').text = message;
      })
      .catch(error => {
        console.error("❌ Fetch error:", error);
        $w('#statusText').text = "❌ Something went wrong: " + error.message;
      })
      .finally(() => {
        $w('#submitQueryButton').enable();
      });
  }
  