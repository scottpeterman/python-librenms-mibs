# SNMP MIB module (ARRIS-C3-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:08 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

(docsIfCmtsServiceEntry,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsServiceEntry")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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

cmtsC3StatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxUpstreamStatsObjects_ObjectIdentity = ObjectIdentity
dcxUpstreamStatsObjects = _DcxUpstreamStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1)
)
_DcxUpstreamStatsTable_Object = MibTable
dcxUpstreamStatsTable = _DcxUpstreamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcxUpstreamStatsTable.setStatus("current")
_DcxUpstreamStatsEntry_Object = MibTableRow
dcxUpstreamStatsEntry = _DcxUpstreamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1)
)
dcxUpstreamStatsEntry.setIndexNames(
    (0, "ARRIS-C3-STATS-MIB", "dcxUsStatsIfIndex"),
)
if mibBuilder.loadTexts:
    dcxUpstreamStatsEntry.setStatus("current")
_DcxUsStatsOther_Type = Counter32
_DcxUsStatsOther_Object = MibTableColumn
dcxUsStatsOther = _DcxUsStatsOther_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 1),
    _DcxUsStatsOther_Type()
)
dcxUsStatsOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxUsStatsOther.setStatus("current")
_DcxUsStatsRanging_Type = Counter32
_DcxUsStatsRanging_Object = MibTableColumn
dcxUsStatsRanging = _DcxUsStatsRanging_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 2),
    _DcxUsStatsRanging_Type()
)
dcxUsStatsRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxUsStatsRanging.setStatus("current")
_DcxUsStatsRngAborted_Type = Counter32
_DcxUsStatsRngAborted_Object = MibTableColumn
dcxUsStatsRngAborted = _DcxUsStatsRngAborted_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 3),
    _DcxUsStatsRngAborted_Type()
)
dcxUsStatsRngAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxUsStatsRngAborted.setStatus("current")
_DcxUsStatsRngComplete_Type = Counter32
_DcxUsStatsRngComplete_Object = MibTableColumn
dcxUsStatsRngComplete = _DcxUsStatsRngComplete_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 4),
    _DcxUsStatsRngComplete_Type()
)
dcxUsStatsRngComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxUsStatsRngComplete.setStatus("current")
_DcxUsStatsIpComplete_Type = Counter32
_DcxUsStatsIpComplete_Object = MibTableColumn
dcxUsStatsIpComplete = _DcxUsStatsIpComplete_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 5),
    _DcxUsStatsIpComplete_Type()
)
dcxUsStatsIpComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxUsStatsIpComplete.setStatus("current")
_DcxUsStatsRegComplete_Type = Counter32
_DcxUsStatsRegComplete_Object = MibTableColumn
dcxUsStatsRegComplete = _DcxUsStatsRegComplete_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 6),
    _DcxUsStatsRegComplete_Type()
)
dcxUsStatsRegComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxUsStatsRegComplete.setStatus("current")
_DcxUsStatsAccessDenied_Type = Counter32
_DcxUsStatsAccessDenied_Object = MibTableColumn
dcxUsStatsAccessDenied = _DcxUsStatsAccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 7),
    _DcxUsStatsAccessDenied_Type()
)
dcxUsStatsAccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxUsStatsAccessDenied.setStatus("current")
_DcxUsStatsIfIndex_Type = InterfaceIndexOrZero
_DcxUsStatsIfIndex_Object = MibTableColumn
dcxUsStatsIfIndex = _DcxUsStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 1, 1, 1, 8),
    _DcxUsStatsIfIndex_Type()
)
dcxUsStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxUsStatsIfIndex.setStatus("current")
_DcxCmtsServiceStatsObjects_ObjectIdentity = ObjectIdentity
dcxCmtsServiceStatsObjects = _DcxCmtsServiceStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2)
)
_DcxCmtsServiceTable_Object = MibTable
dcxCmtsServiceTable = _DcxCmtsServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dcxCmtsServiceTable.setStatus("current")
_DcxCmtsServiceEntry_Object = MibTableRow
dcxCmtsServiceEntry = _DcxCmtsServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dcxCmtsServiceEntry.setStatus("current")
_DcxCmtsServiceOutOctets_Type = Counter32
_DcxCmtsServiceOutOctets_Object = MibTableColumn
dcxCmtsServiceOutOctets = _DcxCmtsServiceOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1, 1),
    _DcxCmtsServiceOutOctets_Type()
)
dcxCmtsServiceOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCmtsServiceOutOctets.setStatus("current")
_DcxCmtsServiceOutPackets_Type = Counter32
_DcxCmtsServiceOutPackets_Object = MibTableColumn
dcxCmtsServiceOutPackets = _DcxCmtsServiceOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1, 2),
    _DcxCmtsServiceOutPackets_Type()
)
dcxCmtsServiceOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCmtsServiceOutPackets.setStatus("current")
_CdxCmtsServiceUpBWExcessReqs_Type = Counter32
_CdxCmtsServiceUpBWExcessReqs_Object = MibTableColumn
cdxCmtsServiceUpBWExcessReqs = _CdxCmtsServiceUpBWExcessReqs_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1, 3),
    _CdxCmtsServiceUpBWExcessReqs_Type()
)
cdxCmtsServiceUpBWExcessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsServiceUpBWExcessReqs.setStatus("current")
_CdxCmtsServiceDownBWExcessPkts_Type = Counter32
_CdxCmtsServiceDownBWExcessPkts_Object = MibTableColumn
cdxCmtsServiceDownBWExcessPkts = _CdxCmtsServiceDownBWExcessPkts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 1, 2, 1, 1, 4),
    _CdxCmtsServiceDownBWExcessPkts_Type()
)
cdxCmtsServiceDownBWExcessPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsServiceDownBWExcessPkts.setStatus("current")
docsIfCmtsServiceEntry.registerAugmentions(
    ("ARRIS-C3-STATS-MIB",
     "dcxCmtsServiceEntry")
)
dcxCmtsServiceEntry.setIndexNames(*docsIfCmtsServiceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-STATS-MIB",
    **{"cmtsC3StatsMIB": cmtsC3StatsMIB,
       "dcxUpstreamStatsObjects": dcxUpstreamStatsObjects,
       "dcxUpstreamStatsTable": dcxUpstreamStatsTable,
       "dcxUpstreamStatsEntry": dcxUpstreamStatsEntry,
       "dcxUsStatsOther": dcxUsStatsOther,
       "dcxUsStatsRanging": dcxUsStatsRanging,
       "dcxUsStatsRngAborted": dcxUsStatsRngAborted,
       "dcxUsStatsRngComplete": dcxUsStatsRngComplete,
       "dcxUsStatsIpComplete": dcxUsStatsIpComplete,
       "dcxUsStatsRegComplete": dcxUsStatsRegComplete,
       "dcxUsStatsAccessDenied": dcxUsStatsAccessDenied,
       "dcxUsStatsIfIndex": dcxUsStatsIfIndex,
       "dcxCmtsServiceStatsObjects": dcxCmtsServiceStatsObjects,
       "dcxCmtsServiceTable": dcxCmtsServiceTable,
       "dcxCmtsServiceEntry": dcxCmtsServiceEntry,
       "dcxCmtsServiceOutOctets": dcxCmtsServiceOutOctets,
       "dcxCmtsServiceOutPackets": dcxCmtsServiceOutPackets,
       "cdxCmtsServiceUpBWExcessReqs": cdxCmtsServiceUpBWExcessReqs,
       "cdxCmtsServiceDownBWExcessPkts": cdxCmtsServiceDownBWExcessPkts}
)
