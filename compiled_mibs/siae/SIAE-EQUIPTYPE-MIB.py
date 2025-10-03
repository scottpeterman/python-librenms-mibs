# SNMP MIB module (SIAE-EQUIPTYPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-EQUIPTYPE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:44 2025
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

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

equipTypeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 501)
)
if mibBuilder.loadTexts:
    equipTypeMib.setRevisions(
        ("2015-04-23 00:00",
         "2014-10-29 00:00",
         "2014-06-23 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EquipTypeList_ObjectIdentity = ObjectIdentity
equipTypeList = _EquipTypeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5)
)
_EquipTypeUnknown_ObjectIdentity = ObjectIdentity
equipTypeUnknown = _EquipTypeUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 1)
)
if mibBuilder.loadTexts:
    equipTypeUnknown.setStatus("current")
_EquipTypeALFO80HD_ObjectIdentity = ObjectIdentity
equipTypeALFO80HD = _EquipTypeALFO80HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 74)
)
if mibBuilder.loadTexts:
    equipTypeALFO80HD.setStatus("current")
_EquipTypeALFO80HDsm_ObjectIdentity = ObjectIdentity
equipTypeALFO80HDsm = _EquipTypeALFO80HDsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 75)
)
if mibBuilder.loadTexts:
    equipTypeALFO80HDsm.setStatus("current")
_EquipTypeAGS20_ObjectIdentity = ObjectIdentity
equipTypeAGS20 = _EquipTypeAGS20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 76)
)
if mibBuilder.loadTexts:
    equipTypeAGS20.setStatus("current")
_EquipTypeALFOplus2_ObjectIdentity = ObjectIdentity
equipTypeALFOplus2 = _EquipTypeALFOplus2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 77)
)
if mibBuilder.loadTexts:
    equipTypeALFOplus2.setStatus("current")
_EquipTypeEasyCellGateway_ObjectIdentity = ObjectIdentity
equipTypeEasyCellGateway = _EquipTypeEasyCellGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 78)
)
if mibBuilder.loadTexts:
    equipTypeEasyCellGateway.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-EQUIPTYPE-MIB",
    **{"equipTypeList": equipTypeList,
       "equipTypeUnknown": equipTypeUnknown,
       "equipTypeALFO80HD": equipTypeALFO80HD,
       "equipTypeALFO80HDsm": equipTypeALFO80HDsm,
       "equipTypeAGS20": equipTypeAGS20,
       "equipTypeALFOplus2": equipTypeALFOplus2,
       "equipTypeEasyCellGateway": equipTypeEasyCellGateway,
       "equipTypeMib": equipTypeMib}
)
