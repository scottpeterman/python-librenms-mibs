# SNMP MIB module (BROCADE-MODULE-MEM-UTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\BROCADE-MODULE-MEM-UTIL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:13 2025
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

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

brocadeModuleMemUtilMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13)
)
if mibBuilder.loadTexts:
    brocadeModuleMemUtilMIB.setRevisions(
        ("2018-05-29 12:00",
         "2016-11-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcsiModuleMemUtilNotifications_ObjectIdentity = ObjectIdentity
bcsiModuleMemUtilNotifications = _BcsiModuleMemUtilNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 0)
)
_BcsiModuleMemUtilObjects_ObjectIdentity = ObjectIdentity
bcsiModuleMemUtilObjects = _BcsiModuleMemUtilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1)
)
_BcsiModuleMemUtilTable_Object = MibTable
bcsiModuleMemUtilTable = _BcsiModuleMemUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    bcsiModuleMemUtilTable.setStatus("current")
_BcsiModuleMemUtilEntry_Object = MibTableRow
bcsiModuleMemUtilEntry = _BcsiModuleMemUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1)
)
bcsiModuleMemUtilEntry.setIndexNames(
    (0, "BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemUtilSlotNum"),
)
if mibBuilder.loadTexts:
    bcsiModuleMemUtilEntry.setStatus("current")
_BcsiModuleMemUtilSlotNum_Type = Integer32
_BcsiModuleMemUtilSlotNum_Object = MibTableColumn
bcsiModuleMemUtilSlotNum = _BcsiModuleMemUtilSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1, 1),
    _BcsiModuleMemUtilSlotNum_Type()
)
bcsiModuleMemUtilSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiModuleMemUtilSlotNum.setStatus("current")
_BcsiModuleMemTotal_Type = Unsigned32
_BcsiModuleMemTotal_Object = MibTableColumn
bcsiModuleMemTotal = _BcsiModuleMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1, 2),
    _BcsiModuleMemTotal_Type()
)
bcsiModuleMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiModuleMemTotal.setStatus("current")
if mibBuilder.loadTexts:
    bcsiModuleMemTotal.setUnits("kilo Bytes")
_BcsiModuleMemAvailable_Type = Gauge32
_BcsiModuleMemAvailable_Object = MibTableColumn
bcsiModuleMemAvailable = _BcsiModuleMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1, 3),
    _BcsiModuleMemAvailable_Type()
)
bcsiModuleMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiModuleMemAvailable.setStatus("current")
if mibBuilder.loadTexts:
    bcsiModuleMemAvailable.setUnits("kilo Bytes")
_BcsiModuleMemUtil100thPercent_Type = Gauge32
_BcsiModuleMemUtil100thPercent_Object = MibTableColumn
bcsiModuleMemUtil100thPercent = _BcsiModuleMemUtil100thPercent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1, 4),
    _BcsiModuleMemUtil100thPercent_Type()
)
bcsiModuleMemUtil100thPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiModuleMemUtil100thPercent.setStatus("current")
_BcsiModuleMemUtilConformance_ObjectIdentity = ObjectIdentity
bcsiModuleMemUtilConformance = _BcsiModuleMemUtilConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2)
)
_BcsiModuleMemUtilCompliances_ObjectIdentity = ObjectIdentity
bcsiModuleMemUtilCompliances = _BcsiModuleMemUtilCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2, 1)
)
_BcsiModuleMemUtilGroups_ObjectIdentity = ObjectIdentity
bcsiModuleMemUtilGroups = _BcsiModuleMemUtilGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2, 2)
)

# Managed Objects groups

bcsiModuleMemUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2, 2, 1)
)
bcsiModuleMemUtilizationGroup.setObjects(
      *(("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemUtilSlotNum"),
        ("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemTotal"),
        ("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemAvailable"),
        ("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemUtil100thPercent"))
)
if mibBuilder.loadTexts:
    bcsiModuleMemUtilizationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bcsiModuleMemUtilCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2, 1, 1)
)
bcsiModuleMemUtilCompliance.setObjects(
    ("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemUtilizationGroup")
)
if mibBuilder.loadTexts:
    bcsiModuleMemUtilCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-MODULE-MEM-UTIL-MIB",
    **{"brocadeModuleMemUtilMIB": brocadeModuleMemUtilMIB,
       "bcsiModuleMemUtilNotifications": bcsiModuleMemUtilNotifications,
       "bcsiModuleMemUtilObjects": bcsiModuleMemUtilObjects,
       "bcsiModuleMemUtilTable": bcsiModuleMemUtilTable,
       "bcsiModuleMemUtilEntry": bcsiModuleMemUtilEntry,
       "bcsiModuleMemUtilSlotNum": bcsiModuleMemUtilSlotNum,
       "bcsiModuleMemTotal": bcsiModuleMemTotal,
       "bcsiModuleMemAvailable": bcsiModuleMemAvailable,
       "bcsiModuleMemUtil100thPercent": bcsiModuleMemUtil100thPercent,
       "bcsiModuleMemUtilConformance": bcsiModuleMemUtilConformance,
       "bcsiModuleMemUtilCompliances": bcsiModuleMemUtilCompliances,
       "bcsiModuleMemUtilCompliance": bcsiModuleMemUtilCompliance,
       "bcsiModuleMemUtilGroups": bcsiModuleMemUtilGroups,
       "bcsiModuleMemUtilizationGroup": bcsiModuleMemUtilizationGroup}
)
