import abc

"""Clients should not be forced to depend upon interfaces that they do not use"""

class Document(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class IMachine(abc.ABC):
    def print_doc(self, document: Document):
        pass

    def scan_doc(self, document: Document):
        pass

    def fax_doc(self, document: Document):
        pass

    def store_doc(self, document: Document):
        pass


# Multifunction printer can have everything and the below implementation is make sense
class MultiFunctionalPrinter(IMachine):
    def print_doc(self, document: Document):
        print("Printing from {} to {}".format(document.start, document.end))

    def scan_doc(self, document: Document):
        print("Scanning from {} to {}".format(document.start, document.end))

    def fax_doc(self, document: Document):
        print("Fax doc from {} to {}".format(document.start, document.end))

    def store_doc(self, document: Document):
        print("Store Doc from {} to {}".format(document.start, document.end))


# Violating the Interface Segregation Principle
# Basic printer supports only one function, since its inherited other functions has dummy implementation.
class BasicPrinter(IMachine):
    def print_doc(self, document: Document):
        print("From Basic Printer Printing from {} to {}".format(document.start, document.end))

    def scan_doc(self, document: Document):
        pass

    def fax_doc(self, document: Document):
        pass

    def store_doc(self, document: Document):
        pass


# Follow the Interface Segregation Principle
# Solution - Segregate the interfaces
class IPrinter(abc.ABC):
    def print_doc(self, document: Document):
        pass

class IScanner(abc.ABC):
    def scan_doc(self, document: Document):
        pass


# You can use like below
class printer(IPrinter):
    def print_doc(self, document: Document):
        print("from Printer : Printing from {} to {}".format(document.start, document.end))


class scanner(IScanner):
    def scan_doc(self, document: Document):
        print("from Scanner : Scanning from {} to {}".format(document.start, document.end))

class PhotoCopyMachine(IPrinter, IScanner):
    def print_doc(self, document: Document):
        print("from PhotoCopyMachine Printing from {} to {}".format(document.start, document.end))

    def scan_doc(self, document: Document):
        print("Scanning from {} to {}".format(document.start, document.end))

# Better approach of segregation

class IMuliFunctionMachine(IPrinter, IScanner):
    pass

class MuliFunctionMachine(IMuliFunctionMachine):
    def __init__(self, printer: IPrinter, scanner: IScanner):
        self.printer = printer
        self.scanner = scanner

    def print_doc(self, document: Document):
        self.printer.print_doc(document)

    def scan_doc(self, document: Document):
        self.scanner.scan_doc(document)



if __name__ == '__main__':

    doc = Document(1, 10)
    p = printer()
    s = scanner()
    m = MuliFunctionMachine(p, s)
    m.scan_doc(doc)
    m.print_doc(doc)