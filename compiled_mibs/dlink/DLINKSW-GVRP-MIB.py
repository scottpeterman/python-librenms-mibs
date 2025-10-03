# SNMP MIB module (DLINKSW-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-GVRP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:09 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(Dlink2kVlanList,) = mibBuilder.importSymbols(
    "DLINKSW-TC-MIB",
    "Dlink2kVlanList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwGvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33)
)
if mibBuilder.loadTexts:
    dlinkSwGvrpMIB.setRevisions(
        ("2013-04-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DGvrpMIBNotifications_ObjectIdentity = ObjectIdentity
dGvrpMIBNotifications = _DGvrpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 0)
)
_DGvrpMIBObjects_ObjectIdentity = ObjectIdentity
dGvrpMIBObjects = _DGvrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1)
)
_DGvrpGlobalMgmt_ObjectIdentity = ObjectIdentity
dGvrpGlobalMgmt = _DGvrpGlobalMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 1)
)
_DGvrpDynamicVlanCreation_Type = TruthValue
_DGvrpDynamicVlanCreation_Object = MibScalar
dGvrpDynamicVlanCreation = _DGvrpDynamicVlanCreation_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 1, 1),
    _DGvrpDynamicVlanCreation_Type()
)
dGvrpDynamicVlanCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dGvrpDynamicVlanCreation.setStatus("current")


class _DGvrpNniGvrpBpduAddress_Type(Integer32):
    """Custom type dGvrpNniGvrpBpduAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("dot1ad", 2))
    )


_DGvrpNniGvrpBpduAddress_Type.__name__ = "Integer32"
_DGvrpNniGvrpBpduAddress_Object = MibScalar
dGvrpNniGvrpBpduAddress = _DGvrpNniGvrpBpduAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 1, 2),
    _DGvrpNniGvrpBpduAddress_Type()
)
dGvrpNniGvrpBpduAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dGvrpNniGvrpBpduAddress.setStatus("current")
_DGvrpInterface_ObjectIdentity = ObjectIdentity
dGvrpInterface = _DGvrpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 2)
)
_DGvrpInterfaceTable_Object = MibTable
dGvrpInterfaceTable = _DGvrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dGvrpInterfaceTable.setStatus("current")
_DGvrpInterfaceEntry_Object = MibTableRow
dGvrpInterfaceEntry = _DGvrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 2, 1, 1)
)
dGvrpInterfaceEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dGvrpInterfaceEntry.setStatus("current")
_DGvrpIfAdvertiseVlanLstFirst2K_Type = Dlink2kVlanList
_DGvrpIfAdvertiseVlanLstFirst2K_Object = MibTableColumn
dGvrpIfAdvertiseVlanLstFirst2K = _DGvrpIfAdvertiseVlanLstFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 2, 1, 1, 1),
    _DGvrpIfAdvertiseVlanLstFirst2K_Type()
)
dGvrpIfAdvertiseVlanLstFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dGvrpIfAdvertiseVlanLstFirst2K.setStatus("current")
_DGvrpIfAdvertiseVlanLstSecond2K_Type = Dlink2kVlanList
_DGvrpIfAdvertiseVlanLstSecond2K_Object = MibTableColumn
dGvrpIfAdvertiseVlanLstSecond2K = _DGvrpIfAdvertiseVlanLstSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 2, 1, 1, 2),
    _DGvrpIfAdvertiseVlanLstSecond2K_Type()
)
dGvrpIfAdvertiseVlanLstSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dGvrpIfAdvertiseVlanLstSecond2K.setStatus("current")
_DGvrpIfForbiddenVlanLstFirst2K_Type = Dlink2kVlanList
_DGvrpIfForbiddenVlanLstFirst2K_Object = MibTableColumn
dGvrpIfForbiddenVlanLstFirst2K = _DGvrpIfForbiddenVlanLstFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 2, 1, 1, 3),
    _DGvrpIfForbiddenVlanLstFirst2K_Type()
)
dGvrpIfForbiddenVlanLstFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dGvrpIfForbiddenVlanLstFirst2K.setStatus("current")
_DGvrpIfForbiddenVlanLstSecond2K_Type = Dlink2kVlanList
_DGvrpIfForbiddenVlanLstSecond2K_Object = MibTableColumn
dGvrpIfForbiddenVlanLstSecond2K = _DGvrpIfForbiddenVlanLstSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 2, 1, 1, 4),
    _DGvrpIfForbiddenVlanLstSecond2K_Type()
)
dGvrpIfForbiddenVlanLstSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dGvrpIfForbiddenVlanLstSecond2K.setStatus("current")
_DGvrpStatistics_ObjectIdentity = ObjectIdentity
dGvrpStatistics = _DGvrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3)
)


class _DGvrpClearAllStatistics_Type(Integer32):
    """Custom type dGvrpClearAllStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DGvrpClearAllStatistics_Type.__name__ = "Integer32"
_DGvrpClearAllStatistics_Object = MibScalar
dGvrpClearAllStatistics = _DGvrpClearAllStatistics_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 1),
    _DGvrpClearAllStatistics_Type()
)
dGvrpClearAllStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dGvrpClearAllStatistics.setStatus("current")
_DGvrpIfStatisticsTable_Object = MibTable
dGvrpIfStatisticsTable = _DGvrpIfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dGvrpIfStatisticsTable.setStatus("current")
_DGvrpIfStatisticsEntry_Object = MibTableRow
dGvrpIfStatisticsEntry = _DGvrpIfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1)
)
dGvrpIfStatisticsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dGvrpIfStatisticsEntry.setStatus("current")
_DGvrpIfStatRxJoinEmpty_Type = Unsigned32
_DGvrpIfStatRxJoinEmpty_Object = MibTableColumn
dGvrpIfStatRxJoinEmpty = _DGvrpIfStatRxJoinEmpty_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 1),
    _DGvrpIfStatRxJoinEmpty_Type()
)
dGvrpIfStatRxJoinEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatRxJoinEmpty.setStatus("current")
_DGvrpIfStatRxJoinIn_Type = Unsigned32
_DGvrpIfStatRxJoinIn_Object = MibTableColumn
dGvrpIfStatRxJoinIn = _DGvrpIfStatRxJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 2),
    _DGvrpIfStatRxJoinIn_Type()
)
dGvrpIfStatRxJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatRxJoinIn.setStatus("current")
_DGvrpIfStatRxLeaveEmpty_Type = Unsigned32
_DGvrpIfStatRxLeaveEmpty_Object = MibTableColumn
dGvrpIfStatRxLeaveEmpty = _DGvrpIfStatRxLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 3),
    _DGvrpIfStatRxLeaveEmpty_Type()
)
dGvrpIfStatRxLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatRxLeaveEmpty.setStatus("current")
_DGvrpIfStatRxLeaveIn_Type = Unsigned32
_DGvrpIfStatRxLeaveIn_Object = MibTableColumn
dGvrpIfStatRxLeaveIn = _DGvrpIfStatRxLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 4),
    _DGvrpIfStatRxLeaveIn_Type()
)
dGvrpIfStatRxLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatRxLeaveIn.setStatus("current")
_DGvrpIfStatRxLeaveAll_Type = Unsigned32
_DGvrpIfStatRxLeaveAll_Object = MibTableColumn
dGvrpIfStatRxLeaveAll = _DGvrpIfStatRxLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 5),
    _DGvrpIfStatRxLeaveAll_Type()
)
dGvrpIfStatRxLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatRxLeaveAll.setStatus("current")
_DGvrpIfStatRxEmpty_Type = Unsigned32
_DGvrpIfStatRxEmpty_Object = MibTableColumn
dGvrpIfStatRxEmpty = _DGvrpIfStatRxEmpty_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 6),
    _DGvrpIfStatRxEmpty_Type()
)
dGvrpIfStatRxEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatRxEmpty.setStatus("current")
_DGvrpIfStatTxJoinEmpty_Type = Unsigned32
_DGvrpIfStatTxJoinEmpty_Object = MibTableColumn
dGvrpIfStatTxJoinEmpty = _DGvrpIfStatTxJoinEmpty_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 7),
    _DGvrpIfStatTxJoinEmpty_Type()
)
dGvrpIfStatTxJoinEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatTxJoinEmpty.setStatus("current")
_DGvrpIfStatTxJoinIn_Type = Unsigned32
_DGvrpIfStatTxJoinIn_Object = MibTableColumn
dGvrpIfStatTxJoinIn = _DGvrpIfStatTxJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 8),
    _DGvrpIfStatTxJoinIn_Type()
)
dGvrpIfStatTxJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatTxJoinIn.setStatus("current")
_DGvrpIfStatTxLeaveEmpty_Type = Unsigned32
_DGvrpIfStatTxLeaveEmpty_Object = MibTableColumn
dGvrpIfStatTxLeaveEmpty = _DGvrpIfStatTxLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 9),
    _DGvrpIfStatTxLeaveEmpty_Type()
)
dGvrpIfStatTxLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatTxLeaveEmpty.setStatus("current")
_DGvrpIfStatTxLeaveIn_Type = Unsigned32
_DGvrpIfStatTxLeaveIn_Object = MibTableColumn
dGvrpIfStatTxLeaveIn = _DGvrpIfStatTxLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 10),
    _DGvrpIfStatTxLeaveIn_Type()
)
dGvrpIfStatTxLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatTxLeaveIn.setStatus("current")
_DGvrpIfStatTxLeaveAll_Type = Unsigned32
_DGvrpIfStatTxLeaveAll_Object = MibTableColumn
dGvrpIfStatTxLeaveAll = _DGvrpIfStatTxLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 11),
    _DGvrpIfStatTxLeaveAll_Type()
)
dGvrpIfStatTxLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatTxLeaveAll.setStatus("current")
_DGvrpIfStatTxEmpty_Type = Unsigned32
_DGvrpIfStatTxEmpty_Object = MibTableColumn
dGvrpIfStatTxEmpty = _DGvrpIfStatTxEmpty_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 12),
    _DGvrpIfStatTxEmpty_Type()
)
dGvrpIfStatTxEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGvrpIfStatTxEmpty.setStatus("current")


class _DGvrpIfStatClear_Type(Integer32):
    """Custom type dGvrpIfStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DGvrpIfStatClear_Type.__name__ = "Integer32"
_DGvrpIfStatClear_Object = MibTableColumn
dGvrpIfStatClear = _DGvrpIfStatClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 1, 3, 2, 1, 13),
    _DGvrpIfStatClear_Type()
)
dGvrpIfStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dGvrpIfStatClear.setStatus("current")
_DGvrpMIBConformance_ObjectIdentity = ObjectIdentity
dGvrpMIBConformance = _DGvrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 2)
)
_DGvrpCompliances_ObjectIdentity = ObjectIdentity
dGvrpCompliances = _DGvrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 2, 1)
)
_DGvrpGroups_ObjectIdentity = ObjectIdentity
dGvrpGroups = _DGvrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 2, 2)
)

# Managed Objects groups

dGvrpBasicCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 2, 2, 1)
)
dGvrpBasicCfgGroup.setObjects(
      *(("DLINKSW-GVRP-MIB", "dGvrpDynamicVlanCreation"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfAdvertiseVlanLstFirst2K"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfAdvertiseVlanLstSecond2K"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfForbiddenVlanLstFirst2K"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfForbiddenVlanLstSecond2K"))
)
if mibBuilder.loadTexts:
    dGvrpBasicCfgGroup.setStatus("current")

dGvrpServiceProviderCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 2, 2, 2)
)
dGvrpServiceProviderCfgGroup.setObjects(
    ("DLINKSW-GVRP-MIB", "dGvrpNniGvrpBpduAddress")
)
if mibBuilder.loadTexts:
    dGvrpServiceProviderCfgGroup.setStatus("current")

dGvrpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 2, 2, 4)
)
dGvrpStatisticsGroup.setObjects(
      *(("DLINKSW-GVRP-MIB", "dGvrpClearAllStatistics"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatRxJoinEmpty"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatRxJoinIn"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatRxLeaveEmpty"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatRxLeaveIn"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatRxLeaveAll"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatRxEmpty"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatTxJoinEmpty"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatTxJoinIn"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatTxLeaveEmpty"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatTxLeaveIn"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatTxLeaveAll"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatTxEmpty"),
        ("DLINKSW-GVRP-MIB", "dGvrpIfStatClear"))
)
if mibBuilder.loadTexts:
    dGvrpStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dGvrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 33, 2, 1, 1)
)
dGvrpCompliance.setObjects(
      *(("DLINKSW-GVRP-MIB", "dGvrpBasicCfgGroup"),
        ("DLINKSW-GVRP-MIB", "dGvrpServiceProviderCfgGroup"),
        ("DLINKSW-GVRP-MIB", "dGvrpStatisticsGroup"))
)
if mibBuilder.loadTexts:
    dGvrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-GVRP-MIB",
    **{"dlinkSwGvrpMIB": dlinkSwGvrpMIB,
       "dGvrpMIBNotifications": dGvrpMIBNotifications,
       "dGvrpMIBObjects": dGvrpMIBObjects,
       "dGvrpGlobalMgmt": dGvrpGlobalMgmt,
       "dGvrpDynamicVlanCreation": dGvrpDynamicVlanCreation,
       "dGvrpNniGvrpBpduAddress": dGvrpNniGvrpBpduAddress,
       "dGvrpInterface": dGvrpInterface,
       "dGvrpInterfaceTable": dGvrpInterfaceTable,
       "dGvrpInterfaceEntry": dGvrpInterfaceEntry,
       "dGvrpIfAdvertiseVlanLstFirst2K": dGvrpIfAdvertiseVlanLstFirst2K,
       "dGvrpIfAdvertiseVlanLstSecond2K": dGvrpIfAdvertiseVlanLstSecond2K,
       "dGvrpIfForbiddenVlanLstFirst2K": dGvrpIfForbiddenVlanLstFirst2K,
       "dGvrpIfForbiddenVlanLstSecond2K": dGvrpIfForbiddenVlanLstSecond2K,
       "dGvrpStatistics": dGvrpStatistics,
       "dGvrpClearAllStatistics": dGvrpClearAllStatistics,
       "dGvrpIfStatisticsTable": dGvrpIfStatisticsTable,
       "dGvrpIfStatisticsEntry": dGvrpIfStatisticsEntry,
       "dGvrpIfStatRxJoinEmpty": dGvrpIfStatRxJoinEmpty,
       "dGvrpIfStatRxJoinIn": dGvrpIfStatRxJoinIn,
       "dGvrpIfStatRxLeaveEmpty": dGvrpIfStatRxLeaveEmpty,
       "dGvrpIfStatRxLeaveIn": dGvrpIfStatRxLeaveIn,
       "dGvrpIfStatRxLeaveAll": dGvrpIfStatRxLeaveAll,
       "dGvrpIfStatRxEmpty": dGvrpIfStatRxEmpty,
       "dGvrpIfStatTxJoinEmpty": dGvrpIfStatTxJoinEmpty,
       "dGvrpIfStatTxJoinIn": dGvrpIfStatTxJoinIn,
       "dGvrpIfStatTxLeaveEmpty": dGvrpIfStatTxLeaveEmpty,
       "dGvrpIfStatTxLeaveIn": dGvrpIfStatTxLeaveIn,
       "dGvrpIfStatTxLeaveAll": dGvrpIfStatTxLeaveAll,
       "dGvrpIfStatTxEmpty": dGvrpIfStatTxEmpty,
       "dGvrpIfStatClear": dGvrpIfStatClear,
       "dGvrpMIBConformance": dGvrpMIBConformance,
       "dGvrpCompliances": dGvrpCompliances,
       "dGvrpCompliance": dGvrpCompliance,
       "dGvrpGroups": dGvrpGroups,
       "dGvrpBasicCfgGroup": dGvrpBasicCfgGroup,
       "dGvrpServiceProviderCfgGroup": dGvrpServiceProviderCfgGroup,
       "dGvrpStatisticsGroup": dGvrpStatisticsGroup}
)
