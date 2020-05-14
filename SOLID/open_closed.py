import enum
import abc

class ColorEnum(enum.Enum):
    red = 0
    green = 1
    yellow = 2

class SizeEnum(enum.Enum):
    small = 0
    mid = 1
    large = 2
    extra_large = 3

class Products(object):
    def __init__(self, product_name: str, color:ColorEnum, size: SizeEnum):
        self.product_name = product_name
        self.color = color
        self.size = size


class ProductFilter(object):
    def __init__(self):
        pass

    def filter_by_color(self, products: [Products], color: ColorEnum) -> Products or None:
        for p in products:
            if p.color == color:
                print("product with selected color is found")
                yield p
        print("Product is not found")
        return None

    def filter_by_size(self, products: [Products], size: SizeEnum) -> Products or None:
        for p in products:
            if p.size == size:
                print("product with selected size is found")
                yield p
        print("Product is not found")
        return None

    # Any new filter existing class should be modified, this violates the OCP
    def filter_by_color_and_size(self, products: [Products], color: ColorEnum, size: SizeEnum) -> Products or None:
        for p in products:
            if p.color == color and p.size == size:
                print("Found Size and color")
                yield p

        print("Could not find the product by given filter")
        return None


"""“Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.”"""

class ISpecification(abc.ABC):
    def is_satisfied(self, p: Products) -> bool:
        pass

class IFilter(abc.ABC):
    def filter(self, p_items: list, spec: ISpecification):
        pass

class ColorSpecification(ISpecification):
    def __init__(self, color: ColorEnum):
        self.color = color

    def is_satisfied(self, p: Products):
        return p.color == self.color

class SizeSpecification(ISpecification):
    def __init__(self, size: SizeEnum):
        self.size = size

    def is_satisfied(self, p: Products):
        return p.size == self.size

# Combination
class AndSpecification(ISpecification):
    def __init__(self, spec_1: ISpecification, spec_2: ISpecification):
        self.spec_1 = spec_1
        self.spec_2 = spec_2

    def is_satisfied(self, p: Products):
        return self.spec_1.is_satisfied(p) and self.spec_2.is_satisfied(p)

class BetterFilter(IFilter):
    def filter(self, p_items: list, spec: ISpecification):
        for p in p_items:
            if spec.is_satisfied(p):
                yield p

if __name__ == '__main__':
    apple = Products("Apple", ColorEnum.green, SizeEnum.small)
    tshirt = Products("shirt", ColorEnum.red, SizeEnum.large)
    Tree = Products("Tree", ColorEnum.green, SizeEnum.extra_large)

    products = [apple, tshirt, Tree]

#     This is without OCP
    pf = ProductFilter()
    print("Green Product is - ", pf.filter_by_color(products, ColorEnum.green))

#     After OCP
    bpf = BetterFilter()
    for p in bpf.filter(products, ColorSpecification(ColorEnum.green)):
        print("Green Product {}".format(p.product_name))

    for p in bpf.filter(products, SizeSpecification(SizeEnum.small)):
        print("Small Size Product {}".format(p.product_name))

    for p in bpf.filter(products, AndSpecification(ColorSpecification(ColorEnum.red), SizeSpecification(SizeEnum.large))):
        print("Red and Large Product {}".format(p.product_name))
