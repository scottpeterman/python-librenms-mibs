# SNMP MIB module (GREENBONE-PRODUCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\greenbone\GREENBONE-PRODUCT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:00 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

greenboneProduct = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35847, 1)
)
if mibBuilder.loadTexts:
    greenboneProduct.setRevisions(
        ("2017-05-15 00:01",
         "2015-01-06 00:01",
         "2014-12-31 00:01",
         "2012-03-26 00:01")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProductName_Type = DisplayString
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 35847, 1, 1),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_ProductHardware_ObjectIdentity = ObjectIdentity
productHardware = _ProductHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35847, 1, 2)
)
_HwName_Type = DisplayString
_HwName_Object = MibScalar
hwName = _HwName_Object(
    (1, 3, 6, 1, 4, 1, 35847, 1, 2, 1),
    _HwName_Type()
)
hwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwName.setStatus("current")
_ProductSoftware_ObjectIdentity = ObjectIdentity
productSoftware = _ProductSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35847, 1, 3)
)
_SwName_Type = DisplayString
_SwName_Object = MibScalar
swName = _SwName_Object(
    (1, 3, 6, 1, 4, 1, 35847, 1, 3, 1),
    _SwName_Type()
)
swName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swName.setStatus("current")
_SwVersion_ObjectIdentity = ObjectIdentity
swVersion = _SwVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35847, 1, 3, 2)
)
_SwVersionString_Type = DisplayString
_SwVersionString_Object = MibScalar
swVersionString = _SwVersionString_Object(
    (1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 1),
    _SwVersionString_Type()
)
swVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionString.setStatus("current")
_SwVersionMajor_Type = Integer32
_SwVersionMajor_Object = MibScalar
swVersionMajor = _SwVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 2),
    _SwVersionMajor_Type()
)
swVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionMajor.setStatus("current")
_SwVersionMinor_Type = Integer32
_SwVersionMinor_Object = MibScalar
swVersionMinor = _SwVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 3),
    _SwVersionMinor_Type()
)
swVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionMinor.setStatus("current")
_SwVersionPatch_Type = Integer32
_SwVersionPatch_Object = MibScalar
swVersionPatch = _SwVersionPatch_Object(
    (1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 4),
    _SwVersionPatch_Type()
)
swVersionPatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionPatch.setStatus("current")
_SwVersionRevision_Type = Integer32
_SwVersionRevision_Object = MibScalar
swVersionRevision = _SwVersionRevision_Object(
    (1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 5),
    _SwVersionRevision_Type()
)
swVersionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionRevision.setStatus("current")
_ProductGroups_ObjectIdentity = ObjectIdentity
productGroups = _ProductGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35847, 1, 4)
)

# Managed Objects groups

greenboneProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35847, 1, 4, 1)
)
greenboneProductGroup.setObjects(
      *(("GREENBONE-PRODUCT-MIB", "productName"),
        ("GREENBONE-PRODUCT-MIB", "hwName"),
        ("GREENBONE-PRODUCT-MIB", "swName"),
        ("GREENBONE-PRODUCT-MIB", "swVersionString"),
        ("GREENBONE-PRODUCT-MIB", "swVersionMajor"),
        ("GREENBONE-PRODUCT-MIB", "swVersionMinor"),
        ("GREENBONE-PRODUCT-MIB", "swVersionPatch"),
        ("GREENBONE-PRODUCT-MIB", "swVersionRevision"))
)
if mibBuilder.loadTexts:
    greenboneProductGroup.setStatus("current")

greenboneProductHWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35847, 1, 4, 2)
)
greenboneProductHWGroup.setObjects(
    ("GREENBONE-PRODUCT-MIB", "hwName")
)
if mibBuilder.loadTexts:
    greenboneProductHWGroup.setStatus("current")

greenboneProductSWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35847, 1, 4, 3)
)
greenboneProductSWGroup.setObjects(
      *(("GREENBONE-PRODUCT-MIB", "swName"),
        ("GREENBONE-PRODUCT-MIB", "swVersionString"),
        ("GREENBONE-PRODUCT-MIB", "swVersionMajor"),
        ("GREENBONE-PRODUCT-MIB", "swVersionMinor"),
        ("GREENBONE-PRODUCT-MIB", "swVersionPatch"),
        ("GREENBONE-PRODUCT-MIB", "swVersionRevision"))
)
if mibBuilder.loadTexts:
    greenboneProductSWGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GREENBONE-PRODUCT-MIB",
    **{"greenboneProduct": greenboneProduct,
       "productName": productName,
       "productHardware": productHardware,
       "hwName": hwName,
       "productSoftware": productSoftware,
       "swName": swName,
       "swVersion": swVersion,
       "swVersionString": swVersionString,
       "swVersionMajor": swVersionMajor,
       "swVersionMinor": swVersionMinor,
       "swVersionPatch": swVersionPatch,
       "swVersionRevision": swVersionRevision,
       "productGroups": productGroups,
       "greenboneProductGroup": greenboneProductGroup,
       "greenboneProductHWGroup": greenboneProductHWGroup,
       "greenboneProductSWGroup": greenboneProductSWGroup}
)
