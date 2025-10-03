# SNMP MIB module (UBQS-CPU-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-CPU-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:14 2025
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

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiCpuStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36)
)
if mibBuilder.loadTexts:
    ubiCpuStatsMIB.setRevisions(
        ("2015-12-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiCpuStatsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiCpuStatsMIBNotificationPrefix = _UbiCpuStatsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36, 1)
)
_UbiCpuStatsMIBObjects_ObjectIdentity = ObjectIdentity
ubiCpuStatsMIBObjects = _UbiCpuStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36, 2)
)
_UbiCpuStatsTable_Object = MibTable
ubiCpuStatsTable = _UbiCpuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36, 2, 1)
)
if mibBuilder.loadTexts:
    ubiCpuStatsTable.setStatus("current")
_UbiCpuStatsEntry_Object = MibTableRow
ubiCpuStatsEntry = _UbiCpuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36, 2, 1, 1)
)
ubiCpuStatsEntry.setIndexNames(
    (0, "UBQS-CPU-STATS-MIB", "ubiCpuStatsIndex"),
)
if mibBuilder.loadTexts:
    ubiCpuStatsEntry.setStatus("current")
_UbiCpuStatsIndex_Type = Integer32
_UbiCpuStatsIndex_Object = MibTableColumn
ubiCpuStatsIndex = _UbiCpuStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36, 2, 1, 1, 1),
    _UbiCpuStatsIndex_Type()
)
ubiCpuStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiCpuStatsIndex.setStatus("current")
_UbiCpuStatsInPkts_Type = Counter64
_UbiCpuStatsInPkts_Object = MibTableColumn
ubiCpuStatsInPkts = _UbiCpuStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36, 2, 1, 1, 2),
    _UbiCpuStatsInPkts_Type()
)
ubiCpuStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiCpuStatsInPkts.setStatus("current")
_UbiCpuStatsDropPkts_Type = Counter64
_UbiCpuStatsDropPkts_Object = MibTableColumn
ubiCpuStatsDropPkts = _UbiCpuStatsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36, 2, 1, 1, 3),
    _UbiCpuStatsDropPkts_Type()
)
ubiCpuStatsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiCpuStatsDropPkts.setStatus("current")
_UbiCpuStatsMIBConformance_ObjectIdentity = ObjectIdentity
ubiCpuStatsMIBConformance = _UbiCpuStatsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 36, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-CPU-STATS-MIB",
    **{"ubiCpuStatsMIB": ubiCpuStatsMIB,
       "ubiCpuStatsMIBNotificationPrefix": ubiCpuStatsMIBNotificationPrefix,
       "ubiCpuStatsMIBObjects": ubiCpuStatsMIBObjects,
       "ubiCpuStatsTable": ubiCpuStatsTable,
       "ubiCpuStatsEntry": ubiCpuStatsEntry,
       "ubiCpuStatsIndex": ubiCpuStatsIndex,
       "ubiCpuStatsInPkts": ubiCpuStatsInPkts,
       "ubiCpuStatsDropPkts": ubiCpuStatsDropPkts,
       "ubiCpuStatsMIBConformance": ubiCpuStatsMIBConformance}
)
