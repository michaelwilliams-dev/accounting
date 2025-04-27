$w.onReady(() => {
  console.log("✅ Accounting Page: Form loaded");

  $w('#submitQueryButton').onClick(submitQueryButton_click);

  // Set discipline and source context
  $w('#inputDiscipline').value = "Accounting";
  $w('#inputSourceContext').value = "This response is based on UK accounting practices, HMRC guidance, financial reporting standards (FRS), and professional accountancy regulations.";
  $w('#inputJobCode').value = 2011; // Example job code for Accounting

  // Job Titles
  $w('#dropdownJobTitle').options = [
    { label: "Accountant", value: "The user is a qualified accountant preparing financial statements or reports." },
    { label: "Auditor", value: "The user is an internal or external auditor reviewing accounts and compliance." },
    { label: "Tax Specialist", value: "The user specializes in tax planning, compliance, and submissions." },
    { label: "Accounts Assistant", value: "The user supports bookkeeping and financial administration tasks." },
    { label: "Trainee Accountant", value: "The user is training for ACCA, ACA, CIMA, or other professional qualifications." },
    { label: "Finance Manager", value: "The user oversees company finances, reporting, and compliance." },
    { label: "Partner / Director", value: "The user holds a senior leadership position within an accounting or audit firm." },
    { label: "Other", value: "The user works in a finance-related role not listed above." }
  ];

  // Timeline Options
  $w('#dropdownTimeline').options = [
    { label: "Urgent – Filing Deadline Today", value: "Action is required immediately to meet filing deadlines (e.g., tax returns, accounts filing)." },
    { label: "Within 7 Days", value: "The action must be completed within the next 7 days." },
    { label: "Within 30 Days", value: "The action should be completed within the next 30 days." },
    { label: "Within 90 Days", value: "The action relates to a task scheduled in the next quarter." },
    { label: "End of Financial Year", value: "The action relates to closing procedures for year-end accounts." },
    { label: "Historical Review", value: "The query relates to a completed year or historical audit review." },
    { label: "Other", value: "Timeline not listed above." }
  ];

  // Site Name Options
  $w('#dropdownSiteName').options = [
    { label: "Head Office", value: "Head Office" },
    { label: "Branch Office", value: "Branch Office" },
    { label: "Client Premises", value: "Client Premises" },
    { label: "Remote Work / Home Office", value: "Remote Work / Home Office" },
    { label: "Audit Site", value: "Audit Site" },
    { label: "Tax Department", value: "Tax Department" },
    { label: "Other", value: "Other site or situation" }
  ];

  // Search Type
  $w('#dropdownSearchType').options = [
    { label: "Audit Procedures", value: "The user is seeking guidance on auditing standards or procedures." },
    { label: "Accounting Treatment", value: "The user wants clarification on financial reporting under FRS, IFRS, or HMRC rules." },
    { label: "Tax Compliance", value: "The user needs assistance with corporation tax, VAT, or payroll compliance." },
    { label: "Ethics or Regulation", value: "The query relates to professional ethics, Money Laundering Regulations (MLR), or other compliance issues." },
    { label: "Financial Statements Review", value: "The user needs support reviewing or preparing statutory accounts." },
    { label: "Other", value: "The topic does not match any listed above." }
  ];

  // Funnel1 (Task Context)
  $w('#dropdownFunnel1').options = [
    { label: "Help interpreting audit findings", value: "The user needs support interpreting audit results or preparing management letters." },
    { label: "Clarify tax reporting obligations", value: "The user wants clarification on tax filings and submission deadlines." },
    { label: "Assist preparing statutory accounts", value: "The user needs guidance on finalising company accounts in compliance with FRS." },
    { label: "Client advisory support", value: "The user seeks help preparing advisory reports for clients." },
    { label: "Ethics / conflict checking", value: "The user is seeking confirmation of ethical standards and conflict of interest rules." },
    { label: "Other", value: "The user has another accounting-related support need." }
  ];

  // Funnel2 (Internal Confirmation)
  $w('#dropdownFunnel').options = [
    { label: "Internal review completed", value: "An internal review of the issue has already been conducted." },
    { label: "Manager / Partner informed", value: "The issue has been discussed with a manager or partner." },
    { label: "Pre-filing checks completed", value: "All required pre-filing compliance checks have been carried out." },
    { label: "Client confirmation received", value: "The client has confirmed the matter or agreed adjustments." },
    { label: "Regulatory body notified", value: "The relevant regulatory body (e.g., HMRC, FRC) has been notified if required." },
    { label: "Other", value: "Other internal steps have been taken." }
  ];

  // Funnel3 (Pending Matters)
  $w('#dropdownFunnel3').options = [
    { label: "Awaiting client documents", value: "Awaiting necessary documents or information from the client." },
    { label: "Regulatory review pending", value: "Awaiting review or feedback from a regulator or governing body." },
    { label: "Managerial review pending", value: "Awaiting internal review or sign-off by a senior manager or partner." },
    { label: "Awaiting clarification from HMRC", value: "Awaiting formal clarification or ruling from HMRC." },
    { label: "Other", value: "Other pending matters not listed." }
  ];

  // Bonus (Seniority Level)
  $w('#dropdownBonus').options = [
    { label: "Trainee / Junior", value: "Level 1 – Entry-level or trainee accountant or audit assistant." },
    { label: "Qualified Accountant", value: "Level 2 – Fully qualified accountant (ACCA, ACA, CIMA, etc.)." },
    { label: "Senior Accountant", value: "Level 3 – Senior accounting role overseeing staff or processes." },
    { label: "Audit Manager / Supervisor", value: "Level 4 – Audit manager or team leader." },
    { label: "Finance Director / CFO", value: "Level 5 – Senior finance executive, director, or partner in charge of finance or audit matters." }
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
  
    fetch("https://police-procedures-new.onrender.com/generate", {
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
  