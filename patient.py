from pathlib import Path


class Patient:
    def __init__(self):
        self.ProxID = str
        self.num_id = int
        self.ClinSig = []
        self.T2 = []
        self.ADC = []
        self.DWI = []
        self.KTrans = Path

    def add_labels(self, labels):
        self.ProxID = labels.ProxID
        self.num_id = self.get_patient_index()
        self.ClinSig = labels.ClinSig
        self.T2 = labels.T2
        self.ADC = labels.ADC
        self.DWI = labels.DWI
        self.KTrans = labels.KTrans

    def set_patient_pid(self, filename):
        self.ProxID = filename[:14]
        self.num_id = self.get_patient_index()

    def get_patient_index(self):
        return int(self.ProxID[10:])

    def add_path(self, image_type, path):
        if image_type == 'T2':
            self.T2.append(path)
        elif image_type == 'ADC':
            self.ADC.append(path)
        elif image_type == 'DWI':
            self.DWI.append(path)
        elif image_type == 'KTrans':
            self.KTrans = path

    def get_dataframe_row(self):
        return [
            self.ProxID, self.ClinSig,
            self.T2, self.ADC, self.DWI, self.KTrans
        ]

