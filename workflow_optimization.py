import time

def simulate_approval_process(approvers):
    approvals = {}
    for approver in approvers:
        print(f"Requesting approval from {approver}...")
        # Simulate approval time
        time.sleep(1)
        approval = True  # Simulate approval
        # For simplicity, assume each approver always approves
        if approval:
            print(f"{approver} has approved.")
            approvals[approver] = True
        else:
            print(f"{approver} has denied.")
            approvals[approver] = False
    return approvals

if __name__ == "__main__":
    approvers_list = ["Approver 1", "Approver 2", "Approver 3"]
    approval_results = simulate_approval_process(approvers_list)
    print("\nApproval Results:")
    for approver, result in approval_results.items():
        print(f"{approver}: {'Approved' if result else 'Denied'}")