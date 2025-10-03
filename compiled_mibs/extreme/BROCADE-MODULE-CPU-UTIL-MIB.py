# SNMP MIB module (BROCADE-MODULE-CPU-UTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\BROCADE-MODULE-CPU-UTIL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:12 2025
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

brocadeModuleCpuUtilMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12)
)
if mibBuilder.loadTexts:
    brocadeModuleCpuUtilMIB.setRevisions(
        ("2018-05-29 12:00",
         "2016-11-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcsiModuleCpuUtilNotifications_ObjectIdentity = ObjectIdentity
bcsiModuleCpuUtilNotifications = _BcsiModuleCpuUtilNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 0)
)
_BcsiModuleCpuUtilObjects_ObjectIdentity = ObjectIdentity
bcsiModuleCpuUtilObjects = _BcsiModuleCpuUtilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1)
)
_BcsiModuleCpuUtilTable_Object = MibTable
bcsiModuleCpuUtilTable = _BcsiModuleCpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    bcsiModuleCpuUtilTable.setStatus("current")
_BcsiModuleCpuUtilEntry_Object = MibTableRow
bcsiModuleCpuUtilEntry = _BcsiModuleCpuUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1, 1)
)
bcsiModuleCpuUtilEntry.setIndexNames(
    (0, "BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilSlotNum"),
    (0, "BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilInterval"),
)
if mibBuilder.loadTexts:
    bcsiModuleCpuUtilEntry.setStatus("current")
_BcsiModuleCpuUtilSlotNum_Type = Integer32
_BcsiModuleCpuUtilSlotNum_Object = MibTableColumn
bcsiModuleCpuUtilSlotNum = _BcsiModuleCpuUtilSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1, 1, 1),
    _BcsiModuleCpuUtilSlotNum_Type()
)
bcsiModuleCpuUtilSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiModuleCpuUtilSlotNum.setStatus("current")
_BcsiModuleCpuUtilInterval_Type = Integer32
_BcsiModuleCpuUtilInterval_Object = MibTableColumn
bcsiModuleCpuUtilInterval = _BcsiModuleCpuUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1, 1, 2),
    _BcsiModuleCpuUtilInterval_Type()
)
bcsiModuleCpuUtilInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiModuleCpuUtilInterval.setStatus("current")
_BcsiModuleCpuUtil100thPercent_Type = Gauge32
_BcsiModuleCpuUtil100thPercent_Object = MibTableColumn
bcsiModuleCpuUtil100thPercent = _BcsiModuleCpuUtil100thPercent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1, 1, 3),
    _BcsiModuleCpuUtil100thPercent_Type()
)
bcsiModuleCpuUtil100thPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiModuleCpuUtil100thPercent.setStatus("current")
_BcsiModuleCpuUtilConformance_ObjectIdentity = ObjectIdentity
bcsiModuleCpuUtilConformance = _BcsiModuleCpuUtilConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2)
)
_BcsiModuleCpuUtilCompliances_ObjectIdentity = ObjectIdentity
bcsiModuleCpuUtilCompliances = _BcsiModuleCpuUtilCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2, 1)
)
_BcsiModuleCpuUtilGroups_ObjectIdentity = ObjectIdentity
bcsiModuleCpuUtilGroups = _BcsiModuleCpuUtilGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2, 2)
)

# Managed Objects groups

bcsiModuleCpuUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2, 2, 1)
)
bcsiModuleCpuUtilizationGroup.setObjects(
      *(("BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilSlotNum"),
        ("BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilInterval"),
        ("BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtil100thPercent"))
)
if mibBuilder.loadTexts:
    bcsiModuleCpuUtilizationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bcsiModuleCpuUtilCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2, 1, 1)
)
bcsiModuleCpuUtilCompliance.setObjects(
    ("BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilizationGroup")
)
if mibBuilder.loadTexts:
    bcsiModuleCpuUtilCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-MODULE-CPU-UTIL-MIB",
    **{"brocadeModuleCpuUtilMIB": brocadeModuleCpuUtilMIB,
       "bcsiModuleCpuUtilNotifications": bcsiModuleCpuUtilNotifications,
       "bcsiModuleCpuUtilObjects": bcsiModuleCpuUtilObjects,
       "bcsiModuleCpuUtilTable": bcsiModuleCpuUtilTable,
       "bcsiModuleCpuUtilEntry": bcsiModuleCpuUtilEntry,
       "bcsiModuleCpuUtilSlotNum": bcsiModuleCpuUtilSlotNum,
       "bcsiModuleCpuUtilInterval": bcsiModuleCpuUtilInterval,
       "bcsiModuleCpuUtil100thPercent": bcsiModuleCpuUtil100thPercent,
       "bcsiModuleCpuUtilConformance": bcsiModuleCpuUtilConformance,
       "bcsiModuleCpuUtilCompliances": bcsiModuleCpuUtilCompliances,
       "bcsiModuleCpuUtilCompliance": bcsiModuleCpuUtilCompliance,
       "bcsiModuleCpuUtilGroups": bcsiModuleCpuUtilGroups,
       "bcsiModuleCpuUtilizationGroup": bcsiModuleCpuUtilizationGroup}
)
