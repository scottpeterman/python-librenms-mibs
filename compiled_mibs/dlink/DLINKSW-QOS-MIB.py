# SNMP MIB module (DLINKSW-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-QOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:47 2025
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

dlinkSwQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61)
)
if mibBuilder.loadTexts:
    dlinkSwQosMIB.setRevisions(
        ("2013-02-21 00:00",
         "2013-05-30 00:00",
         "2013-07-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlinkQosPoliceActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("drop", 1),
          ("permit", 2),
          ("replaceDscp", 3),
          ("replaceCos", 4),
          ("replaceAll", 5))
    )



# MIB Managed Objects in the order of their OIDs

_DQosMIBNotifications_ObjectIdentity = ObjectIdentity
dQosMIBNotifications = _DQosMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 0)
)
_DQosMIBObjects_ObjectIdentity = ObjectIdentity
dQosMIBObjects = _DQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1)
)
_DQosClassMap_ObjectIdentity = ObjectIdentity
dQosClassMap = _DQosClassMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1)
)
_DQosClassMapTable_Object = MibTable
dQosClassMapTable = _DQosClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dQosClassMapTable.setStatus("current")
_DQosClassMapEntry_Object = MibTableRow
dQosClassMapEntry = _DQosClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 1, 1)
)
dQosClassMapEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosClassMapName"),
)
if mibBuilder.loadTexts:
    dQosClassMapEntry.setStatus("current")


class _DQosClassMapName_Type(DisplayString):
    """Custom type dQosClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DQosClassMapName_Type.__name__ = "DisplayString"
_DQosClassMapName_Object = MibTableColumn
dQosClassMapName = _DQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 1, 1, 1),
    _DQosClassMapName_Type()
)
dQosClassMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosClassMapName.setStatus("current")


class _DQosClassMapType_Type(Integer32):
    """Custom type dQosClassMapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAny", 1),
          ("matchAll", 2))
    )


_DQosClassMapType_Type.__name__ = "Integer32"
_DQosClassMapType_Object = MibTableColumn
dQosClassMapType = _DQosClassMapType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 1, 1, 2),
    _DQosClassMapType_Type()
)
dQosClassMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosClassMapType.setStatus("current")
_DQosClassMapRowStaus_Type = RowStatus
_DQosClassMapRowStaus_Object = MibTableColumn
dQosClassMapRowStaus = _DQosClassMapRowStaus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 1, 1, 3),
    _DQosClassMapRowStaus_Type()
)
dQosClassMapRowStaus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosClassMapRowStaus.setStatus("current")
_DQosClassMapCfgTable_Object = MibTable
dQosClassMapCfgTable = _DQosClassMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dQosClassMapCfgTable.setStatus("current")
_DQosClassMapCfgEntry_Object = MibTableRow
dQosClassMapCfgEntry = _DQosClassMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 2, 1)
)
dQosClassMapCfgEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosClassMapName"),
    (0, "DLINKSW-QOS-MIB", "dQosClassMapCfgMatchId"),
)
if mibBuilder.loadTexts:
    dQosClassMapCfgEntry.setStatus("current")


class _DQosClassMapCfgMatchId_Type(Integer32):
    """Custom type dQosClassMapCfgMatchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DQosClassMapCfgMatchId_Type.__name__ = "Integer32"
_DQosClassMapCfgMatchId_Object = MibTableColumn
dQosClassMapCfgMatchId = _DQosClassMapCfgMatchId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 2, 1, 1),
    _DQosClassMapCfgMatchId_Type()
)
dQosClassMapCfgMatchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosClassMapCfgMatchId.setStatus("current")


class _DQosClassMapCfgMatchType_Type(Integer32):
    """Custom type dQosClassMapCfgMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("accessList", 1),
          ("cos", 2),
          ("innerCos", 3),
          ("dscp", 4),
          ("ipDscp", 5),
          ("precedence", 6),
          ("ipPrecedence", 7),
          ("protocol", 8),
          ("vlan", 9),
          ("innerVlan", 10))
    )


_DQosClassMapCfgMatchType_Type.__name__ = "Integer32"
_DQosClassMapCfgMatchType_Object = MibTableColumn
dQosClassMapCfgMatchType = _DQosClassMapCfgMatchType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 2, 1, 2),
    _DQosClassMapCfgMatchType_Type()
)
dQosClassMapCfgMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosClassMapCfgMatchType.setStatus("current")


class _DQosClassMapCfgMatchValue_Type(OctetString):
    """Custom type dQosClassMapCfgMatchValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DQosClassMapCfgMatchValue_Type.__name__ = "OctetString"
_DQosClassMapCfgMatchValue_Object = MibTableColumn
dQosClassMapCfgMatchValue = _DQosClassMapCfgMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 2, 1, 3),
    _DQosClassMapCfgMatchValue_Type()
)
dQosClassMapCfgMatchValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosClassMapCfgMatchValue.setStatus("current")
_DQosClassMapCfgRowStaus_Type = RowStatus
_DQosClassMapCfgRowStaus_Object = MibTableColumn
dQosClassMapCfgRowStaus = _DQosClassMapCfgRowStaus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 1, 2, 1, 5),
    _DQosClassMapCfgRowStaus_Type()
)
dQosClassMapCfgRowStaus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosClassMapCfgRowStaus.setStatus("current")
_DQosPolicyMap_ObjectIdentity = ObjectIdentity
dQosPolicyMap = _DQosPolicyMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2)
)
_DQosPolicyMapTable_Object = MibTable
dQosPolicyMapTable = _DQosPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dQosPolicyMapTable.setStatus("current")
_DQosPolicyMapEntry_Object = MibTableRow
dQosPolicyMapEntry = _DQosPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 1, 1)
)
dQosPolicyMapEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosPolicyMapName"),
)
if mibBuilder.loadTexts:
    dQosPolicyMapEntry.setStatus("current")


class _DQosPolicyMapName_Type(DisplayString):
    """Custom type dQosPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DQosPolicyMapName_Type.__name__ = "DisplayString"
_DQosPolicyMapName_Object = MibTableColumn
dQosPolicyMapName = _DQosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 1, 1, 1),
    _DQosPolicyMapName_Type()
)
dQosPolicyMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosPolicyMapName.setStatus("current")
_DQosPolicyMapRowStatus_Type = RowStatus
_DQosPolicyMapRowStatus_Object = MibTableColumn
dQosPolicyMapRowStatus = _DQosPolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 1, 1, 2),
    _DQosPolicyMapRowStatus_Type()
)
dQosPolicyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPolicyMapRowStatus.setStatus("current")
_DQosPolicyMapCfgTable_Object = MibTable
dQosPolicyMapCfgTable = _DQosPolicyMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dQosPolicyMapCfgTable.setStatus("current")
_DQosPolicyMapCfgEntry_Object = MibTableRow
dQosPolicyMapCfgEntry = _DQosPolicyMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2, 1)
)
dQosPolicyMapCfgEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosPolicyMapName"),
    (0, "DLINKSW-QOS-MIB", "dQosClassMapName"),
)
if mibBuilder.loadTexts:
    dQosPolicyMapCfgEntry.setStatus("current")


class _DQosPolicyMapCfgSetCosQueue_Type(Integer32):
    """Custom type dQosPolicyMapCfgSetCosQueue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DQosPolicyMapCfgSetCosQueue_Type.__name__ = "Integer32"
_DQosPolicyMapCfgSetCosQueue_Object = MibTableColumn
dQosPolicyMapCfgSetCosQueue = _DQosPolicyMapCfgSetCosQueue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2, 1, 1),
    _DQosPolicyMapCfgSetCosQueue_Type()
)
dQosPolicyMapCfgSetCosQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPolicyMapCfgSetCosQueue.setStatus("current")


class _DQosPolicyMapCfgSetCos_Type(Integer32):
    """Custom type dQosPolicyMapCfgSetCos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DQosPolicyMapCfgSetCos_Type.__name__ = "Integer32"
_DQosPolicyMapCfgSetCos_Object = MibTableColumn
dQosPolicyMapCfgSetCos = _DQosPolicyMapCfgSetCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2, 1, 2),
    _DQosPolicyMapCfgSetCos_Type()
)
dQosPolicyMapCfgSetCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPolicyMapCfgSetCos.setStatus("current")


class _DQosPolicyMapCfgSetDscpOnlyIp_Type(TruthValue):
    """Custom type dQosPolicyMapCfgSetDscpOnlyIp based on TruthValue"""
    defaultValue = 2


_DQosPolicyMapCfgSetDscpOnlyIp_Type.__name__ = "TruthValue"
_DQosPolicyMapCfgSetDscpOnlyIp_Object = MibTableColumn
dQosPolicyMapCfgSetDscpOnlyIp = _DQosPolicyMapCfgSetDscpOnlyIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2, 1, 3),
    _DQosPolicyMapCfgSetDscpOnlyIp_Type()
)
dQosPolicyMapCfgSetDscpOnlyIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPolicyMapCfgSetDscpOnlyIp.setStatus("current")


class _DQosPolicyMapCfgSetDscp_Type(Integer32):
    """Custom type dQosPolicyMapCfgSetDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_DQosPolicyMapCfgSetDscp_Type.__name__ = "Integer32"
_DQosPolicyMapCfgSetDscp_Object = MibTableColumn
dQosPolicyMapCfgSetDscp = _DQosPolicyMapCfgSetDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2, 1, 4),
    _DQosPolicyMapCfgSetDscp_Type()
)
dQosPolicyMapCfgSetDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPolicyMapCfgSetDscp.setStatus("current")


class _DQosPolicyMapCfgSetPreceOnlyIp_Type(TruthValue):
    """Custom type dQosPolicyMapCfgSetPreceOnlyIp based on TruthValue"""
    defaultValue = 2


_DQosPolicyMapCfgSetPreceOnlyIp_Type.__name__ = "TruthValue"
_DQosPolicyMapCfgSetPreceOnlyIp_Object = MibTableColumn
dQosPolicyMapCfgSetPreceOnlyIp = _DQosPolicyMapCfgSetPreceOnlyIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2, 1, 5),
    _DQosPolicyMapCfgSetPreceOnlyIp_Type()
)
dQosPolicyMapCfgSetPreceOnlyIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPolicyMapCfgSetPreceOnlyIp.setStatus("current")


class _DQosPolicyMapCfgSetPrecedence_Type(Integer32):
    """Custom type dQosPolicyMapCfgSetPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DQosPolicyMapCfgSetPrecedence_Type.__name__ = "Integer32"
_DQosPolicyMapCfgSetPrecedence_Object = MibTableColumn
dQosPolicyMapCfgSetPrecedence = _DQosPolicyMapCfgSetPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2, 1, 6),
    _DQosPolicyMapCfgSetPrecedence_Type()
)
dQosPolicyMapCfgSetPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPolicyMapCfgSetPrecedence.setStatus("current")
_DQosPolicyMapCfgRowStatus_Type = RowStatus
_DQosPolicyMapCfgRowStatus_Object = MibTableColumn
dQosPolicyMapCfgRowStatus = _DQosPolicyMapCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 2, 1, 7),
    _DQosPolicyMapCfgRowStatus_Type()
)
dQosPolicyMapCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPolicyMapCfgRowStatus.setStatus("current")
_DQosAggPolicerTable_Object = MibTable
dQosAggPolicerTable = _DQosAggPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dQosAggPolicerTable.setStatus("current")
_DQosAggPolicerEntry_Object = MibTableRow
dQosAggPolicerEntry = _DQosAggPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1)
)
dQosAggPolicerEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosAggPolicerName"),
)
if mibBuilder.loadTexts:
    dQosAggPolicerEntry.setStatus("current")


class _DQosAggPolicerName_Type(DisplayString):
    """Custom type dQosAggPolicerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DQosAggPolicerName_Type.__name__ = "DisplayString"
_DQosAggPolicerName_Object = MibTableColumn
dQosAggPolicerName = _DQosAggPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 1),
    _DQosAggPolicerName_Type()
)
dQosAggPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosAggPolicerName.setStatus("current")


class _DQosAggPolicerType_Type(Integer32):
    """Custom type dQosAggPolicerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trTcm", 1),
          ("singleRate", 2))
    )


_DQosAggPolicerType_Type.__name__ = "Integer32"
_DQosAggPolicerType_Object = MibTableColumn
dQosAggPolicerType = _DQosAggPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 2),
    _DQosAggPolicerType_Type()
)
dQosAggPolicerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerType.setStatus("current")


class _DQosAggPolicerCir_Type(Unsigned32):
    """Custom type dQosAggPolicerCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240000),
    )


_DQosAggPolicerCir_Type.__name__ = "Unsigned32"
_DQosAggPolicerCir_Object = MibTableColumn
dQosAggPolicerCir = _DQosAggPolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 3),
    _DQosAggPolicerCir_Type()
)
dQosAggPolicerCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerCir.setStatus("current")
if mibBuilder.loadTexts:
    dQosAggPolicerCir.setUnits("kbps")


class _DQosAggPolicerCbs_Type(Unsigned32):
    """Custom type dQosAggPolicerCbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_DQosAggPolicerCbs_Type.__name__ = "Unsigned32"
_DQosAggPolicerCbs_Object = MibTableColumn
dQosAggPolicerCbs = _DQosAggPolicerCbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 4),
    _DQosAggPolicerCbs_Type()
)
dQosAggPolicerCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerCbs.setStatus("current")
if mibBuilder.loadTexts:
    dQosAggPolicerCbs.setUnits("kbyte")


class _DQosAggPolicerSrtcmEbs_Type(Unsigned32):
    """Custom type dQosAggPolicerSrtcmEbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_DQosAggPolicerSrtcmEbs_Type.__name__ = "Unsigned32"
_DQosAggPolicerSrtcmEbs_Object = MibTableColumn
dQosAggPolicerSrtcmEbs = _DQosAggPolicerSrtcmEbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 5),
    _DQosAggPolicerSrtcmEbs_Type()
)
dQosAggPolicerSrtcmEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerSrtcmEbs.setStatus("current")
if mibBuilder.loadTexts:
    dQosAggPolicerSrtcmEbs.setUnits("kbyte")


class _DQosAggPolicerTrtcmPir_Type(Unsigned32):
    """Custom type dQosAggPolicerTrtcmPir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240000),
    )


_DQosAggPolicerTrtcmPir_Type.__name__ = "Unsigned32"
_DQosAggPolicerTrtcmPir_Object = MibTableColumn
dQosAggPolicerTrtcmPir = _DQosAggPolicerTrtcmPir_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 6),
    _DQosAggPolicerTrtcmPir_Type()
)
dQosAggPolicerTrtcmPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerTrtcmPir.setStatus("current")
if mibBuilder.loadTexts:
    dQosAggPolicerTrtcmPir.setUnits("kbps")


class _DQosAggPolicerTrtcmPbs_Type(Unsigned32):
    """Custom type dQosAggPolicerTrtcmPbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_DQosAggPolicerTrtcmPbs_Type.__name__ = "Unsigned32"
_DQosAggPolicerTrtcmPbs_Object = MibTableColumn
dQosAggPolicerTrtcmPbs = _DQosAggPolicerTrtcmPbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 7),
    _DQosAggPolicerTrtcmPbs_Type()
)
dQosAggPolicerTrtcmPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerTrtcmPbs.setStatus("current")
if mibBuilder.loadTexts:
    dQosAggPolicerTrtcmPbs.setUnits("kbyte")
_DQosAggPolicerConformAction_Type = DlinkQosPoliceActionType
_DQosAggPolicerConformAction_Object = MibTableColumn
dQosAggPolicerConformAction = _DQosAggPolicerConformAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 8),
    _DQosAggPolicerConformAction_Type()
)
dQosAggPolicerConformAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerConformAction.setStatus("current")


class _DQosAggPolicerConformReplaceDscp_Type(Unsigned32):
    """Custom type dQosAggPolicerConformReplaceDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosAggPolicerConformReplaceDscp_Type.__name__ = "Unsigned32"
_DQosAggPolicerConformReplaceDscp_Object = MibTableColumn
dQosAggPolicerConformReplaceDscp = _DQosAggPolicerConformReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 9),
    _DQosAggPolicerConformReplaceDscp_Type()
)
dQosAggPolicerConformReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerConformReplaceDscp.setStatus("current")
_DQosAggPolicerExceedAction_Type = DlinkQosPoliceActionType
_DQosAggPolicerExceedAction_Object = MibTableColumn
dQosAggPolicerExceedAction = _DQosAggPolicerExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 10),
    _DQosAggPolicerExceedAction_Type()
)
dQosAggPolicerExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerExceedAction.setStatus("current")


class _DQosAggPolicerExceedReplaceDscp_Type(Unsigned32):
    """Custom type dQosAggPolicerExceedReplaceDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosAggPolicerExceedReplaceDscp_Type.__name__ = "Unsigned32"
_DQosAggPolicerExceedReplaceDscp_Object = MibTableColumn
dQosAggPolicerExceedReplaceDscp = _DQosAggPolicerExceedReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 11),
    _DQosAggPolicerExceedReplaceDscp_Type()
)
dQosAggPolicerExceedReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerExceedReplaceDscp.setStatus("current")
_DQosAggPolicerViolateAction_Type = DlinkQosPoliceActionType
_DQosAggPolicerViolateAction_Object = MibTableColumn
dQosAggPolicerViolateAction = _DQosAggPolicerViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 12),
    _DQosAggPolicerViolateAction_Type()
)
dQosAggPolicerViolateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerViolateAction.setStatus("current")


class _DQosAggPolicerViolateReplaceDscp_Type(Unsigned32):
    """Custom type dQosAggPolicerViolateReplaceDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosAggPolicerViolateReplaceDscp_Type.__name__ = "Unsigned32"
_DQosAggPolicerViolateReplaceDscp_Object = MibTableColumn
dQosAggPolicerViolateReplaceDscp = _DQosAggPolicerViolateReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 13),
    _DQosAggPolicerViolateReplaceDscp_Type()
)
dQosAggPolicerViolateReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerViolateReplaceDscp.setStatus("current")


class _DQosAggPolicerColorAware_Type(TruthValue):
    """Custom type dQosAggPolicerColorAware based on TruthValue"""
    defaultValue = 2


_DQosAggPolicerColorAware_Type.__name__ = "TruthValue"
_DQosAggPolicerColorAware_Object = MibTableColumn
dQosAggPolicerColorAware = _DQosAggPolicerColorAware_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 14),
    _DQosAggPolicerColorAware_Type()
)
dQosAggPolicerColorAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerColorAware.setStatus("current")


class _DQosAggPolicerConformReplaceCos_Type(Unsigned32):
    """Custom type dQosAggPolicerConformReplaceCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosAggPolicerConformReplaceCos_Type.__name__ = "Unsigned32"
_DQosAggPolicerConformReplaceCos_Object = MibTableColumn
dQosAggPolicerConformReplaceCos = _DQosAggPolicerConformReplaceCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 15),
    _DQosAggPolicerConformReplaceCos_Type()
)
dQosAggPolicerConformReplaceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerConformReplaceCos.setStatus("current")


class _DQosAggPolicerExceedReplaceCos_Type(Unsigned32):
    """Custom type dQosAggPolicerExceedReplaceCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosAggPolicerExceedReplaceCos_Type.__name__ = "Unsigned32"
_DQosAggPolicerExceedReplaceCos_Object = MibTableColumn
dQosAggPolicerExceedReplaceCos = _DQosAggPolicerExceedReplaceCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 16),
    _DQosAggPolicerExceedReplaceCos_Type()
)
dQosAggPolicerExceedReplaceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerExceedReplaceCos.setStatus("current")


class _DQosAggPolicerViolateReplaceCos_Type(Unsigned32):
    """Custom type dQosAggPolicerViolateReplaceCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosAggPolicerViolateReplaceCos_Type.__name__ = "Unsigned32"
_DQosAggPolicerViolateReplaceCos_Object = MibTableColumn
dQosAggPolicerViolateReplaceCos = _DQosAggPolicerViolateReplaceCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 17),
    _DQosAggPolicerViolateReplaceCos_Type()
)
dQosAggPolicerViolateReplaceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerViolateReplaceCos.setStatus("current")
_DQosAggPolicerRowStatus_Type = RowStatus
_DQosAggPolicerRowStatus_Object = MibTableColumn
dQosAggPolicerRowStatus = _DQosAggPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 3, 1, 24),
    _DQosAggPolicerRowStatus_Type()
)
dQosAggPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosAggPolicerRowStatus.setStatus("current")
_DQosPoliceTable_Object = MibTable
dQosPoliceTable = _DQosPoliceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dQosPoliceTable.setStatus("current")
_DQosPoliceEntry_Object = MibTableRow
dQosPoliceEntry = _DQosPoliceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1)
)
dQosPoliceEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosPolicyMapName"),
    (0, "DLINKSW-QOS-MIB", "dQosClassMapName"),
)
if mibBuilder.loadTexts:
    dQosPoliceEntry.setStatus("current")


class _DQosPoliceType_Type(Integer32):
    """Custom type dQosPoliceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trTcm", 1),
          ("singleRate", 2),
          ("aggregate", 3))
    )


_DQosPoliceType_Type.__name__ = "Integer32"
_DQosPoliceType_Object = MibTableColumn
dQosPoliceType = _DQosPoliceType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 1),
    _DQosPoliceType_Type()
)
dQosPoliceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceType.setStatus("current")


class _DQosPoliceNamedAggPolicer_Type(DisplayString):
    """Custom type dQosPoliceNamedAggPolicer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DQosPoliceNamedAggPolicer_Type.__name__ = "DisplayString"
_DQosPoliceNamedAggPolicer_Object = MibTableColumn
dQosPoliceNamedAggPolicer = _DQosPoliceNamedAggPolicer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 2),
    _DQosPoliceNamedAggPolicer_Type()
)
dQosPoliceNamedAggPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceNamedAggPolicer.setStatus("current")


class _DQosPoliceCir_Type(Unsigned32):
    """Custom type dQosPoliceCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240000),
    )


_DQosPoliceCir_Type.__name__ = "Unsigned32"
_DQosPoliceCir_Object = MibTableColumn
dQosPoliceCir = _DQosPoliceCir_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 3),
    _DQosPoliceCir_Type()
)
dQosPoliceCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceCir.setStatus("current")
if mibBuilder.loadTexts:
    dQosPoliceCir.setUnits("kbps")


class _DQosPoliceCbs_Type(Unsigned32):
    """Custom type dQosPoliceCbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_DQosPoliceCbs_Type.__name__ = "Unsigned32"
_DQosPoliceCbs_Object = MibTableColumn
dQosPoliceCbs = _DQosPoliceCbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 4),
    _DQosPoliceCbs_Type()
)
dQosPoliceCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceCbs.setStatus("current")
if mibBuilder.loadTexts:
    dQosPoliceCbs.setUnits("kbyte")


class _DQosPoliceSrtcmEbs_Type(Unsigned32):
    """Custom type dQosPoliceSrtcmEbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_DQosPoliceSrtcmEbs_Type.__name__ = "Unsigned32"
_DQosPoliceSrtcmEbs_Object = MibTableColumn
dQosPoliceSrtcmEbs = _DQosPoliceSrtcmEbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 5),
    _DQosPoliceSrtcmEbs_Type()
)
dQosPoliceSrtcmEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceSrtcmEbs.setStatus("current")
if mibBuilder.loadTexts:
    dQosPoliceSrtcmEbs.setUnits("kbyte")


class _DQosPoliceTrtcmPir_Type(Unsigned32):
    """Custom type dQosPoliceTrtcmPir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240000),
    )


_DQosPoliceTrtcmPir_Type.__name__ = "Unsigned32"
_DQosPoliceTrtcmPir_Object = MibTableColumn
dQosPoliceTrtcmPir = _DQosPoliceTrtcmPir_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 6),
    _DQosPoliceTrtcmPir_Type()
)
dQosPoliceTrtcmPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceTrtcmPir.setStatus("current")
if mibBuilder.loadTexts:
    dQosPoliceTrtcmPir.setUnits("kbps")


class _DQosPoliceTrtcmPbs_Type(Unsigned32):
    """Custom type dQosPoliceTrtcmPbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_DQosPoliceTrtcmPbs_Type.__name__ = "Unsigned32"
_DQosPoliceTrtcmPbs_Object = MibTableColumn
dQosPoliceTrtcmPbs = _DQosPoliceTrtcmPbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 7),
    _DQosPoliceTrtcmPbs_Type()
)
dQosPoliceTrtcmPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceTrtcmPbs.setStatus("current")
if mibBuilder.loadTexts:
    dQosPoliceTrtcmPbs.setUnits("kbyte")
_DQosPoliceConformAction_Type = DlinkQosPoliceActionType
_DQosPoliceConformAction_Object = MibTableColumn
dQosPoliceConformAction = _DQosPoliceConformAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 8),
    _DQosPoliceConformAction_Type()
)
dQosPoliceConformAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceConformAction.setStatus("current")


class _DQosPoliceConformReplaceDscp_Type(Unsigned32):
    """Custom type dQosPoliceConformReplaceDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosPoliceConformReplaceDscp_Type.__name__ = "Unsigned32"
_DQosPoliceConformReplaceDscp_Object = MibTableColumn
dQosPoliceConformReplaceDscp = _DQosPoliceConformReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 9),
    _DQosPoliceConformReplaceDscp_Type()
)
dQosPoliceConformReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceConformReplaceDscp.setStatus("current")
_DQosPoliceExceedAction_Type = DlinkQosPoliceActionType
_DQosPoliceExceedAction_Object = MibTableColumn
dQosPoliceExceedAction = _DQosPoliceExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 10),
    _DQosPoliceExceedAction_Type()
)
dQosPoliceExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceExceedAction.setStatus("current")


class _DQosPoliceExceedReplaceDscp_Type(Unsigned32):
    """Custom type dQosPoliceExceedReplaceDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosPoliceExceedReplaceDscp_Type.__name__ = "Unsigned32"
_DQosPoliceExceedReplaceDscp_Object = MibTableColumn
dQosPoliceExceedReplaceDscp = _DQosPoliceExceedReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 11),
    _DQosPoliceExceedReplaceDscp_Type()
)
dQosPoliceExceedReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceExceedReplaceDscp.setStatus("current")
_DQosPoliceViolateAction_Type = DlinkQosPoliceActionType
_DQosPoliceViolateAction_Object = MibTableColumn
dQosPoliceViolateAction = _DQosPoliceViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 12),
    _DQosPoliceViolateAction_Type()
)
dQosPoliceViolateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceViolateAction.setStatus("current")


class _DQosPoliceViolateReplaceDscp_Type(Unsigned32):
    """Custom type dQosPoliceViolateReplaceDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosPoliceViolateReplaceDscp_Type.__name__ = "Unsigned32"
_DQosPoliceViolateReplaceDscp_Object = MibTableColumn
dQosPoliceViolateReplaceDscp = _DQosPoliceViolateReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 13),
    _DQosPoliceViolateReplaceDscp_Type()
)
dQosPoliceViolateReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceViolateReplaceDscp.setStatus("current")
_DQosPoliceColorAware_Type = TruthValue
_DQosPoliceColorAware_Object = MibTableColumn
dQosPoliceColorAware = _DQosPoliceColorAware_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 14),
    _DQosPoliceColorAware_Type()
)
dQosPoliceColorAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceColorAware.setStatus("current")
_DQosPoliceRowStatus_Type = RowStatus
_DQosPoliceRowStatus_Object = MibTableColumn
dQosPoliceRowStatus = _DQosPoliceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 15),
    _DQosPoliceRowStatus_Type()
)
dQosPoliceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceRowStatus.setStatus("current")


class _DQosPoliceConformReplaceCos_Type(Unsigned32):
    """Custom type dQosPoliceConformReplaceCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosPoliceConformReplaceCos_Type.__name__ = "Unsigned32"
_DQosPoliceConformReplaceCos_Object = MibTableColumn
dQosPoliceConformReplaceCos = _DQosPoliceConformReplaceCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 16),
    _DQosPoliceConformReplaceCos_Type()
)
dQosPoliceConformReplaceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceConformReplaceCos.setStatus("current")


class _DQosPoliceExceedReplaceCos_Type(Unsigned32):
    """Custom type dQosPoliceExceedReplaceCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosPoliceExceedReplaceCos_Type.__name__ = "Unsigned32"
_DQosPoliceExceedReplaceCos_Object = MibTableColumn
dQosPoliceExceedReplaceCos = _DQosPoliceExceedReplaceCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 17),
    _DQosPoliceExceedReplaceCos_Type()
)
dQosPoliceExceedReplaceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceExceedReplaceCos.setStatus("current")


class _DQosPoliceViolateReplaceCos_Type(Unsigned32):
    """Custom type dQosPoliceViolateReplaceCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosPoliceViolateReplaceCos_Type.__name__ = "Unsigned32"
_DQosPoliceViolateReplaceCos_Object = MibTableColumn
dQosPoliceViolateReplaceCos = _DQosPoliceViolateReplaceCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 2, 4, 1, 18),
    _DQosPoliceViolateReplaceCos_Type()
)
dQosPoliceViolateReplaceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosPoliceViolateReplaceCos.setStatus("current")
_DQosServicePolicy_ObjectIdentity = ObjectIdentity
dQosServicePolicy = _DQosServicePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 3)
)
_DQosServicePolicyTable_Object = MibTable
dQosServicePolicyTable = _DQosServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dQosServicePolicyTable.setStatus("current")
_DQosServicePolicyEntry_Object = MibTableRow
dQosServicePolicyEntry = _DQosServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 3, 1, 1)
)
dQosServicePolicyEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "DLINKSW-QOS-MIB", "dQosServicePolicyDirection"),
)
if mibBuilder.loadTexts:
    dQosServicePolicyEntry.setStatus("current")


class _DQosServicePolicyDirection_Type(Integer32):
    """Custom type dQosServicePolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_DQosServicePolicyDirection_Type.__name__ = "Integer32"
_DQosServicePolicyDirection_Object = MibTableColumn
dQosServicePolicyDirection = _DQosServicePolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 3, 1, 1, 1),
    _DQosServicePolicyDirection_Type()
)
dQosServicePolicyDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosServicePolicyDirection.setStatus("current")


class _DQosServicePolicyName_Type(DisplayString):
    """Custom type dQosServicePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DQosServicePolicyName_Type.__name__ = "DisplayString"
_DQosServicePolicyName_Object = MibTableColumn
dQosServicePolicyName = _DQosServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 3, 1, 1, 2),
    _DQosServicePolicyName_Type()
)
dQosServicePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosServicePolicyName.setStatus("current")
_DQosServicePolicyRowStaus_Type = RowStatus
_DQosServicePolicyRowStaus_Object = MibTableColumn
dQosServicePolicyRowStaus = _DQosServicePolicyRowStaus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 3, 1, 1, 3),
    _DQosServicePolicyRowStaus_Type()
)
dQosServicePolicyRowStaus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosServicePolicyRowStaus.setStatus("current")
_DQosScheduling_ObjectIdentity = ObjectIdentity
dQosScheduling = _DQosScheduling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4)
)
_DQosSchedulingModeTable_Object = MibTable
dQosSchedulingModeTable = _DQosSchedulingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dQosSchedulingModeTable.setStatus("current")
_DQosSchedulingModeEntry_Object = MibTableRow
dQosSchedulingModeEntry = _DQosSchedulingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 1, 1)
)
dQosSchedulingModeEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dQosSchedulingModeEntry.setStatus("current")


class _DQosSchedulingMode_Type(Integer32):
    """Custom type dQosSchedulingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("rr", 2),
          ("wrr", 3),
          ("wdrr", 4))
    )


_DQosSchedulingMode_Type.__name__ = "Integer32"
_DQosSchedulingMode_Object = MibTableColumn
dQosSchedulingMode = _DQosSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 1, 1, 2),
    _DQosSchedulingMode_Type()
)
dQosSchedulingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosSchedulingMode.setStatus("current")
_DQosScheduleWrrWeightTable_Object = MibTable
dQosScheduleWrrWeightTable = _DQosScheduleWrrWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dQosScheduleWrrWeightTable.setStatus("current")
_DQosScheduleWrrWeightEntry_Object = MibTableRow
dQosScheduleWrrWeightEntry = _DQosScheduleWrrWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 2, 1)
)
dQosScheduleWrrWeightEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "DLINKSW-QOS-MIB", "dQosScheduleWrrWeightQueueId"),
)
if mibBuilder.loadTexts:
    dQosScheduleWrrWeightEntry.setStatus("current")


class _DQosScheduleWrrWeightQueueId_Type(Unsigned32):
    """Custom type dQosScheduleWrrWeightQueueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DQosScheduleWrrWeightQueueId_Type.__name__ = "Unsigned32"
_DQosScheduleWrrWeightQueueId_Object = MibTableColumn
dQosScheduleWrrWeightQueueId = _DQosScheduleWrrWeightQueueId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 2, 1, 1),
    _DQosScheduleWrrWeightQueueId_Type()
)
dQosScheduleWrrWeightQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosScheduleWrrWeightQueueId.setStatus("current")


class _DQosScheduleWrrWeightValue_Type(Unsigned32):
    """Custom type dQosScheduleWrrWeightValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DQosScheduleWrrWeightValue_Type.__name__ = "Unsigned32"
_DQosScheduleWrrWeightValue_Object = MibTableColumn
dQosScheduleWrrWeightValue = _DQosScheduleWrrWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 2, 1, 2),
    _DQosScheduleWrrWeightValue_Type()
)
dQosScheduleWrrWeightValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosScheduleWrrWeightValue.setStatus("current")
_DQosScheduleWdrrWeightTable_Object = MibTable
dQosScheduleWdrrWeightTable = _DQosScheduleWdrrWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dQosScheduleWdrrWeightTable.setStatus("current")
_DQosScheduleWdrrWeightEntry_Object = MibTableRow
dQosScheduleWdrrWeightEntry = _DQosScheduleWdrrWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 3, 1)
)
dQosScheduleWdrrWeightEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "DLINKSW-QOS-MIB", "dQosScheduleWdrrWeightQueueId"),
)
if mibBuilder.loadTexts:
    dQosScheduleWdrrWeightEntry.setStatus("current")


class _DQosScheduleWdrrWeightQueueId_Type(Unsigned32):
    """Custom type dQosScheduleWdrrWeightQueueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DQosScheduleWdrrWeightQueueId_Type.__name__ = "Unsigned32"
_DQosScheduleWdrrWeightQueueId_Object = MibTableColumn
dQosScheduleWdrrWeightQueueId = _DQosScheduleWdrrWeightQueueId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 3, 1, 1),
    _DQosScheduleWdrrWeightQueueId_Type()
)
dQosScheduleWdrrWeightQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosScheduleWdrrWeightQueueId.setStatus("current")


class _DQosScheduleWdrrWeightValue_Type(Unsigned32):
    """Custom type dQosScheduleWdrrWeightValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DQosScheduleWdrrWeightValue_Type.__name__ = "Unsigned32"
_DQosScheduleWdrrWeightValue_Object = MibTableColumn
dQosScheduleWdrrWeightValue = _DQosScheduleWdrrWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 4, 3, 1, 2),
    _DQosScheduleWdrrWeightValue_Type()
)
dQosScheduleWdrrWeightValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosScheduleWdrrWeightValue.setStatus("current")
_DQosBandwidthCtrl_ObjectIdentity = ObjectIdentity
dQosBandwidthCtrl = _DQosBandwidthCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5)
)
_DQosBandwidthCtrlTable_Object = MibTable
dQosBandwidthCtrlTable = _DQosBandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dQosBandwidthCtrlTable.setStatus("current")
_DQosBandwidthCtrlEntry_Object = MibTableRow
dQosBandwidthCtrlEntry = _DQosBandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5, 1, 1)
)
dQosBandwidthCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dQosBandwidthCtrlEntry.setStatus("current")


class _DQosBandwidthRxRate_Type(Integer32):
    """Custom type dQosBandwidthRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10240000),
    )


_DQosBandwidthRxRate_Type.__name__ = "Integer32"
_DQosBandwidthRxRate_Object = MibTableColumn
dQosBandwidthRxRate = _DQosBandwidthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5, 1, 1, 2),
    _DQosBandwidthRxRate_Type()
)
dQosBandwidthRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosBandwidthRxRate.setStatus("current")


class _DQosBandwidthRxBurst_Type(Integer32):
    """Custom type dQosBandwidthRxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 128000),
    )


_DQosBandwidthRxBurst_Type.__name__ = "Integer32"
_DQosBandwidthRxBurst_Object = MibTableColumn
dQosBandwidthRxBurst = _DQosBandwidthRxBurst_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5, 1, 1, 3),
    _DQosBandwidthRxBurst_Type()
)
dQosBandwidthRxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosBandwidthRxBurst.setStatus("current")
if mibBuilder.loadTexts:
    dQosBandwidthRxBurst.setUnits("kbyte")


class _DQosBandwidthTxRate_Type(Integer32):
    """Custom type dQosBandwidthTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10240000),
    )


_DQosBandwidthTxRate_Type.__name__ = "Integer32"
_DQosBandwidthTxRate_Object = MibTableColumn
dQosBandwidthTxRate = _DQosBandwidthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5, 1, 1, 4),
    _DQosBandwidthTxRate_Type()
)
dQosBandwidthTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosBandwidthTxRate.setStatus("current")


class _DQosBandwidthTxBurst_Type(Integer32):
    """Custom type dQosBandwidthTxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 128000),
    )


_DQosBandwidthTxBurst_Type.__name__ = "Integer32"
_DQosBandwidthTxBurst_Object = MibTableColumn
dQosBandwidthTxBurst = _DQosBandwidthTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5, 1, 1, 5),
    _DQosBandwidthTxBurst_Type()
)
dQosBandwidthTxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosBandwidthTxBurst.setStatus("current")
if mibBuilder.loadTexts:
    dQosBandwidthTxBurst.setUnits("kbyte")


class _DQosBandwidthRxRateMode_Type(Integer32):
    """Custom type dQosBandwidthRxRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate", 1),
          ("percent", 2))
    )


_DQosBandwidthRxRateMode_Type.__name__ = "Integer32"
_DQosBandwidthRxRateMode_Object = MibTableColumn
dQosBandwidthRxRateMode = _DQosBandwidthRxRateMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5, 1, 1, 6),
    _DQosBandwidthRxRateMode_Type()
)
dQosBandwidthRxRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosBandwidthRxRateMode.setStatus("current")


class _DQosBandwidthTxRateMode_Type(Integer32):
    """Custom type dQosBandwidthTxRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate", 1),
          ("percent", 2))
    )


_DQosBandwidthTxRateMode_Type.__name__ = "Integer32"
_DQosBandwidthTxRateMode_Object = MibTableColumn
dQosBandwidthTxRateMode = _DQosBandwidthTxRateMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 5, 1, 1, 7),
    _DQosBandwidthTxRateMode_Type()
)
dQosBandwidthTxRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosBandwidthTxRateMode.setStatus("current")
_DQosQueueBandwidthCtrl_ObjectIdentity = ObjectIdentity
dQosQueueBandwidthCtrl = _DQosQueueBandwidthCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 6)
)
_DQosQueueBandwidthCtrlTable_Object = MibTable
dQosQueueBandwidthCtrlTable = _DQosQueueBandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dQosQueueBandwidthCtrlTable.setStatus("current")
_DQosQueueBandwidthCtrlEntry_Object = MibTableRow
dQosQueueBandwidthCtrlEntry = _DQosQueueBandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 6, 1, 1)
)
dQosQueueBandwidthCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "DLINKSW-QOS-MIB", "dQosQueueBandwidthQueId"),
)
if mibBuilder.loadTexts:
    dQosQueueBandwidthCtrlEntry.setStatus("current")


class _DQosQueueBandwidthQueId_Type(Unsigned32):
    """Custom type dQosQueueBandwidthQueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DQosQueueBandwidthQueId_Type.__name__ = "Unsigned32"
_DQosQueueBandwidthQueId_Object = MibTableColumn
dQosQueueBandwidthQueId = _DQosQueueBandwidthQueId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 6, 1, 1, 1),
    _DQosQueueBandwidthQueId_Type()
)
dQosQueueBandwidthQueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosQueueBandwidthQueId.setStatus("current")


class _DQosQueueBandwidthMinRate_Type(Integer32):
    """Custom type dQosQueueBandwidthMinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10240000),
    )


_DQosQueueBandwidthMinRate_Type.__name__ = "Integer32"
_DQosQueueBandwidthMinRate_Object = MibTableColumn
dQosQueueBandwidthMinRate = _DQosQueueBandwidthMinRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 6, 1, 1, 2),
    _DQosQueueBandwidthMinRate_Type()
)
dQosQueueBandwidthMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosQueueBandwidthMinRate.setStatus("current")


class _DQosQueueBandwidthMaxRate_Type(Integer32):
    """Custom type dQosQueueBandwidthMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10240000),
    )


_DQosQueueBandwidthMaxRate_Type.__name__ = "Integer32"
_DQosQueueBandwidthMaxRate_Object = MibTableColumn
dQosQueueBandwidthMaxRate = _DQosQueueBandwidthMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 6, 1, 1, 3),
    _DQosQueueBandwidthMaxRate_Type()
)
dQosQueueBandwidthMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosQueueBandwidthMaxRate.setStatus("current")


class _DQosQueueBandwidthMinRateMode_Type(Integer32):
    """Custom type dQosQueueBandwidthMinRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate", 1),
          ("percent", 2))
    )


_DQosQueueBandwidthMinRateMode_Type.__name__ = "Integer32"
_DQosQueueBandwidthMinRateMode_Object = MibTableColumn
dQosQueueBandwidthMinRateMode = _DQosQueueBandwidthMinRateMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 6, 1, 1, 4),
    _DQosQueueBandwidthMinRateMode_Type()
)
dQosQueueBandwidthMinRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosQueueBandwidthMinRateMode.setStatus("current")


class _DQosQueueBandwidthMaxRateMode_Type(Integer32):
    """Custom type dQosQueueBandwidthMaxRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate", 1),
          ("percent", 2))
    )


_DQosQueueBandwidthMaxRateMode_Type.__name__ = "Integer32"
_DQosQueueBandwidthMaxRateMode_Object = MibTableColumn
dQosQueueBandwidthMaxRateMode = _DQosQueueBandwidthMaxRateMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 6, 1, 1, 5),
    _DQosQueueBandwidthMaxRateMode_Type()
)
dQosQueueBandwidthMaxRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosQueueBandwidthMaxRateMode.setStatus("current")
_DQosQueuingCfg_ObjectIdentity = ObjectIdentity
dQosQueuingCfg = _DQosQueuingCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 7)
)
_DQosPortIfQueuingTable_Object = MibTable
dQosPortIfQueuingTable = _DQosPortIfQueuingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 7, 1)
)
if mibBuilder.loadTexts:
    dQosPortIfQueuingTable.setStatus("current")
_DQosPortIfQueuingEntry_Object = MibTableRow
dQosPortIfQueuingEntry = _DQosPortIfQueuingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 7, 1, 1)
)
dQosPortIfQueuingEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dQosPortIfQueuingEntry.setStatus("current")
_DQosPortIf8021pOverride_Type = TruthValue
_DQosPortIf8021pOverride_Object = MibTableColumn
dQosPortIf8021pOverride = _DQosPortIf8021pOverride_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 7, 1, 1, 1),
    _DQosPortIf8021pOverride_Type()
)
dQosPortIf8021pOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosPortIf8021pOverride.setStatus("current")


class _DQosPortIfTrustMode_Type(Integer32):
    """Custom type dQosPortIfTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("dscp", 2))
    )


_DQosPortIfTrustMode_Type.__name__ = "Integer32"
_DQosPortIfTrustMode_Object = MibTableColumn
dQosPortIfTrustMode = _DQosPortIfTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 7, 1, 1, 2),
    _DQosPortIfTrustMode_Type()
)
dQosPortIfTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosPortIfTrustMode.setStatus("current")
_DQosDscpMap_ObjectIdentity = ObjectIdentity
dQosDscpMap = _DQosDscpMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8)
)
_DQosDscpMutationMapTable_Object = MibTable
dQosDscpMutationMapTable = _DQosDscpMutationMapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 1)
)
if mibBuilder.loadTexts:
    dQosDscpMutationMapTable.setStatus("current")
_DQosDscpMutationMapEntry_Object = MibTableRow
dQosDscpMutationMapEntry = _DQosDscpMutationMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 1, 1)
)
dQosDscpMutationMapEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosDscpMutationMapName"),
)
if mibBuilder.loadTexts:
    dQosDscpMutationMapEntry.setStatus("current")


class _DQosDscpMutationMapName_Type(DisplayString):
    """Custom type dQosDscpMutationMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DQosDscpMutationMapName_Type.__name__ = "DisplayString"
_DQosDscpMutationMapName_Object = MibTableColumn
dQosDscpMutationMapName = _DQosDscpMutationMapName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 1, 1, 1),
    _DQosDscpMutationMapName_Type()
)
dQosDscpMutationMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosDscpMutationMapName.setStatus("current")
_DQosDscpMutationMapRowStatus_Type = RowStatus
_DQosDscpMutationMapRowStatus_Object = MibTableColumn
dQosDscpMutationMapRowStatus = _DQosDscpMutationMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 1, 1, 2),
    _DQosDscpMutationMapRowStatus_Type()
)
dQosDscpMutationMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dQosDscpMutationMapRowStatus.setStatus("current")
_DQosDscpMutationMapCfgTable_Object = MibTable
dQosDscpMutationMapCfgTable = _DQosDscpMutationMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 2)
)
if mibBuilder.loadTexts:
    dQosDscpMutationMapCfgTable.setStatus("current")
_DQosDscpMutationMapCfgEntry_Object = MibTableRow
dQosDscpMutationMapCfgEntry = _DQosDscpMutationMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 2, 1)
)
dQosDscpMutationMapCfgEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosDscpMutationMapName"),
    (0, "DLINKSW-QOS-MIB", "dQosDscpMutationOldDscp"),
)
if mibBuilder.loadTexts:
    dQosDscpMutationMapCfgEntry.setStatus("current")


class _DQosDscpMutationOldDscp_Type(Unsigned32):
    """Custom type dQosDscpMutationOldDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosDscpMutationOldDscp_Type.__name__ = "Unsigned32"
_DQosDscpMutationOldDscp_Object = MibTableColumn
dQosDscpMutationOldDscp = _DQosDscpMutationOldDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 2, 1, 1),
    _DQosDscpMutationOldDscp_Type()
)
dQosDscpMutationOldDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosDscpMutationOldDscp.setStatus("current")


class _DQosDscpMutationNewDscp_Type(Unsigned32):
    """Custom type dQosDscpMutationNewDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosDscpMutationNewDscp_Type.__name__ = "Unsigned32"
_DQosDscpMutationNewDscp_Object = MibTableColumn
dQosDscpMutationNewDscp = _DQosDscpMutationNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 2, 1, 2),
    _DQosDscpMutationNewDscp_Type()
)
dQosDscpMutationNewDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosDscpMutationNewDscp.setStatus("current")
_DQosDscpMutationMapAttachTable_Object = MibTable
dQosDscpMutationMapAttachTable = _DQosDscpMutationMapAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 3)
)
if mibBuilder.loadTexts:
    dQosDscpMutationMapAttachTable.setStatus("current")
_DQosDscpMutationMapAttachEntry_Object = MibTableRow
dQosDscpMutationMapAttachEntry = _DQosDscpMutationMapAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 3, 1)
)
dQosDscpMutationMapAttachEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dQosDscpMutationMapAttachEntry.setStatus("current")


class _DQosDscpMutationMapAttachName_Type(DisplayString):
    """Custom type dQosDscpMutationMapAttachName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DQosDscpMutationMapAttachName_Type.__name__ = "DisplayString"
_DQosDscpMutationMapAttachName_Object = MibTableColumn
dQosDscpMutationMapAttachName = _DQosDscpMutationMapAttachName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 3, 1, 1),
    _DQosDscpMutationMapAttachName_Type()
)
dQosDscpMutationMapAttachName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosDscpMutationMapAttachName.setStatus("current")
_DQosDscpMapCtrlTable_Object = MibTable
dQosDscpMapCtrlTable = _DQosDscpMapCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 4)
)
if mibBuilder.loadTexts:
    dQosDscpMapCtrlTable.setStatus("current")
_DQosDscpMapCtrlEntry_Object = MibTableRow
dQosDscpMapCtrlEntry = _DQosDscpMapCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 4, 1)
)
dQosDscpMapCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "DLINKSW-QOS-MIB", "dQosDscpMapCtrlDscp"),
)
if mibBuilder.loadTexts:
    dQosDscpMapCtrlEntry.setStatus("current")


class _DQosDscpMapCtrlDscp_Type(Unsigned32):
    """Custom type dQosDscpMapCtrlDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DQosDscpMapCtrlDscp_Type.__name__ = "Unsigned32"
_DQosDscpMapCtrlDscp_Object = MibTableColumn
dQosDscpMapCtrlDscp = _DQosDscpMapCtrlDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 4, 1, 1),
    _DQosDscpMapCtrlDscp_Type()
)
dQosDscpMapCtrlDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosDscpMapCtrlDscp.setStatus("current")


class _DQosDscpMapCtrlCos_Type(Unsigned32):
    """Custom type dQosDscpMapCtrlCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosDscpMapCtrlCos_Type.__name__ = "Unsigned32"
_DQosDscpMapCtrlCos_Object = MibTableColumn
dQosDscpMapCtrlCos = _DQosDscpMapCtrlCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 4, 1, 2),
    _DQosDscpMapCtrlCos_Type()
)
dQosDscpMapCtrlCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosDscpMapCtrlCos.setStatus("current")


class _DQosDscpMapCtrlColor_Type(Integer32):
    """Custom type dQosDscpMapCtrlColor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_DQosDscpMapCtrlColor_Type.__name__ = "Integer32"
_DQosDscpMapCtrlColor_Object = MibTableColumn
dQosDscpMapCtrlColor = _DQosDscpMapCtrlColor_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 8, 4, 1, 3),
    _DQosDscpMapCtrlColor_Type()
)
dQosDscpMapCtrlColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosDscpMapCtrlColor.setStatus("current")
_DQosCosMap_ObjectIdentity = ObjectIdentity
dQosCosMap = _DQosCosMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9)
)
_DQosCosToColorMapTable_Object = MibTable
dQosCosToColorMapTable = _DQosCosToColorMapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9, 1)
)
if mibBuilder.loadTexts:
    dQosCosToColorMapTable.setStatus("current")
_DQosCosToColorMapEntry_Object = MibTableRow
dQosCosToColorMapEntry = _DQosCosToColorMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9, 1, 1)
)
dQosCosToColorMapEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "DLINKSW-QOS-MIB", "dQosCosMapCos"),
)
if mibBuilder.loadTexts:
    dQosCosToColorMapEntry.setStatus("current")


class _DQosCosMapCos_Type(Unsigned32):
    """Custom type dQosCosMapCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosCosMapCos_Type.__name__ = "Unsigned32"
_DQosCosMapCos_Object = MibTableColumn
dQosCosMapCos = _DQosCosMapCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9, 1, 1, 1),
    _DQosCosMapCos_Type()
)
dQosCosMapCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosCosMapCos.setStatus("current")


class _DQosCosMapColor_Type(Integer32):
    """Custom type dQosCosMapColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_DQosCosMapColor_Type.__name__ = "Integer32"
_DQosCosMapColor_Object = MibTableColumn
dQosCosMapColor = _DQosCosMapColor_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9, 1, 1, 2),
    _DQosCosMapColor_Type()
)
dQosCosMapColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosCosMapColor.setStatus("current")
_DQosCosToQueueMapTable_Object = MibTable
dQosCosToQueueMapTable = _DQosCosToQueueMapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9, 2)
)
if mibBuilder.loadTexts:
    dQosCosToQueueMapTable.setStatus("current")
_DQosCosToQueueMapEntry_Object = MibTableRow
dQosCosToQueueMapEntry = _DQosCosToQueueMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9, 2, 1)
)
dQosCosToQueueMapEntry.setIndexNames(
    (0, "DLINKSW-QOS-MIB", "dQosCosToQueueCos"),
)
if mibBuilder.loadTexts:
    dQosCosToQueueMapEntry.setStatus("current")


class _DQosCosToQueueCos_Type(Unsigned32):
    """Custom type dQosCosToQueueCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DQosCosToQueueCos_Type.__name__ = "Unsigned32"
_DQosCosToQueueCos_Object = MibTableColumn
dQosCosToQueueCos = _DQosCosToQueueCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9, 2, 1, 1),
    _DQosCosToQueueCos_Type()
)
dQosCosToQueueCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dQosCosToQueueCos.setStatus("current")
_DQosCosToQueueQID_Type = Unsigned32
_DQosCosToQueueQID_Object = MibTableColumn
dQosCosToQueueQID = _DQosCosToQueueQID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 1, 9, 2, 1, 2),
    _DQosCosToQueueQID_Type()
)
dQosCosToQueueQID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dQosCosToQueueQID.setStatus("current")
_DQosMIBConformance_ObjectIdentity = ObjectIdentity
dQosMIBConformance = _DQosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2)
)
_DQosCompliances_ObjectIdentity = ObjectIdentity
dQosCompliances = _DQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 1)
)
_DQosGroups_ObjectIdentity = ObjectIdentity
dQosGroups = _DQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2)
)

# Managed Objects groups

dQosPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 1)
)
dQosPolicyGroup.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosClassMapType"),
        ("DLINKSW-QOS-MIB", "dQosClassMapRowStaus"),
        ("DLINKSW-QOS-MIB", "dQosClassMapCfgMatchType"),
        ("DLINKSW-QOS-MIB", "dQosClassMapCfgMatchValue"),
        ("DLINKSW-QOS-MIB", "dQosClassMapCfgRowStaus"),
        ("DLINKSW-QOS-MIB", "dQosPolicyMapRowStatus"),
        ("DLINKSW-QOS-MIB", "dQosPolicyMapCfgSetCosQueue"),
        ("DLINKSW-QOS-MIB", "dQosPolicyMapCfgSetCos"),
        ("DLINKSW-QOS-MIB", "dQosPolicyMapCfgSetDscpOnlyIp"),
        ("DLINKSW-QOS-MIB", "dQosPolicyMapCfgSetDscp"),
        ("DLINKSW-QOS-MIB", "dQosPolicyMapCfgSetPreceOnlyIp"),
        ("DLINKSW-QOS-MIB", "dQosPolicyMapCfgSetPrecedence"),
        ("DLINKSW-QOS-MIB", "dQosPolicyMapCfgRowStatus"),
        ("DLINKSW-QOS-MIB", "dQosServicePolicyDirection"),
        ("DLINKSW-QOS-MIB", "dQosServicePolicyName"),
        ("DLINKSW-QOS-MIB", "dQosServicePolicyRowStaus"))
)
if mibBuilder.loadTexts:
    dQosPolicyGroup.setStatus("current")

dQosSchedulingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 2)
)
dQosSchedulingGroup.setObjects(
    ("DLINKSW-QOS-MIB", "dQosSchedulingMode")
)
if mibBuilder.loadTexts:
    dQosSchedulingGroup.setStatus("current")

dQosWrrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 3)
)
dQosWrrGroup.setObjects(
    ("DLINKSW-QOS-MIB", "dQosScheduleWrrWeightValue")
)
if mibBuilder.loadTexts:
    dQosWrrGroup.setStatus("current")

dQosWdrrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 4)
)
dQosWdrrGroup.setObjects(
    ("DLINKSW-QOS-MIB", "dQosScheduleWdrrWeightValue")
)
if mibBuilder.loadTexts:
    dQosWdrrGroup.setStatus("current")

dQosPortBandwidthCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 5)
)
dQosPortBandwidthCtrlGroup.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosBandwidthRxRate"),
        ("DLINKSW-QOS-MIB", "dQosBandwidthRxBurst"),
        ("DLINKSW-QOS-MIB", "dQosBandwidthTxRate"),
        ("DLINKSW-QOS-MIB", "dQosBandwidthTxBurst"),
        ("DLINKSW-QOS-MIB", "dQosBandwidthRxRateMode"),
        ("DLINKSW-QOS-MIB", "dQosBandwidthTxRateMode"))
)
if mibBuilder.loadTexts:
    dQosPortBandwidthCtrlGroup.setStatus("current")

dQosQueueBandwidthCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 6)
)
dQosQueueBandwidthCtrlGroup.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosQueueBandwidthMinRate"),
        ("DLINKSW-QOS-MIB", "dQosQueueBandwidthMaxRate"),
        ("DLINKSW-QOS-MIB", "dQosQueueBandwidthMinRateMode"),
        ("DLINKSW-QOS-MIB", "dQosQueueBandwidthMaxRateMode"))
)
if mibBuilder.loadTexts:
    dQosQueueBandwidthCtrlGroup.setStatus("current")

dQosAggregatePolicingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 7)
)
dQosAggregatePolicingGroup.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosAggPolicerType"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerCir"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerCbs"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerSrtcmEbs"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerTrtcmPir"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerTrtcmPbs"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerConformAction"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerConformReplaceDscp"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerExceedAction"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerExceedReplaceDscp"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerViolateAction"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerViolateReplaceDscp"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerColorAware"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerRowStatus"),
        ("DLINKSW-QOS-MIB", "dQosPoliceNamedAggPolicer"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerConformReplaceCos"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerExceedReplaceCos"),
        ("DLINKSW-QOS-MIB", "dQosAggPolicerViolateReplaceCos"))
)
if mibBuilder.loadTexts:
    dQosAggregatePolicingGroup.setStatus("current")

dQosPolicingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 8)
)
dQosPolicingGroup.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosPoliceType"),
        ("DLINKSW-QOS-MIB", "dQosPoliceCir"),
        ("DLINKSW-QOS-MIB", "dQosPoliceCbs"),
        ("DLINKSW-QOS-MIB", "dQosPoliceSrtcmEbs"),
        ("DLINKSW-QOS-MIB", "dQosPoliceTrtcmPir"),
        ("DLINKSW-QOS-MIB", "dQosPoliceTrtcmPbs"),
        ("DLINKSW-QOS-MIB", "dQosPoliceConformAction"),
        ("DLINKSW-QOS-MIB", "dQosPoliceConformReplaceDscp"),
        ("DLINKSW-QOS-MIB", "dQosPoliceExceedAction"),
        ("DLINKSW-QOS-MIB", "dQosPoliceExceedReplaceDscp"),
        ("DLINKSW-QOS-MIB", "dQosPoliceViolateAction"),
        ("DLINKSW-QOS-MIB", "dQosPoliceViolateReplaceDscp"),
        ("DLINKSW-QOS-MIB", "dQosPoliceRowStatus"),
        ("DLINKSW-QOS-MIB", "dQosDscpMapCtrlColor"),
        ("DLINKSW-QOS-MIB", "dQosPoliceConformReplaceCos"),
        ("DLINKSW-QOS-MIB", "dQosPoliceExceedReplaceCos"),
        ("DLINKSW-QOS-MIB", "dQosPoliceViolateReplaceCos"))
)
if mibBuilder.loadTexts:
    dQosPolicingGroup.setStatus("current")

dQosColorAwarePolicingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 9)
)
dQosColorAwarePolicingGroup.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosPoliceColorAware"),
        ("DLINKSW-QOS-MIB", "dQosDscpMapCtrlColor"),
        ("DLINKSW-QOS-MIB", "dQosCosMapColor"))
)
if mibBuilder.loadTexts:
    dQosColorAwarePolicingGroup.setStatus("current")

dQosQueuingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 10)
)
dQosQueuingGroup.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosPortIf8021pOverride"),
        ("DLINKSW-QOS-MIB", "dQosPortIfTrustMode"),
        ("DLINKSW-QOS-MIB", "dQosDscpMapCtrlCos"),
        ("DLINKSW-QOS-MIB", "dQosCosToQueueQID"))
)
if mibBuilder.loadTexts:
    dQosQueuingGroup.setStatus("current")

dQosDscpMutationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 2, 11)
)
dQosDscpMutationGroup.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosDscpMutationMapRowStatus"),
        ("DLINKSW-QOS-MIB", "dQosDscpMutationNewDscp"),
        ("DLINKSW-QOS-MIB", "dQosDscpMutationMapAttachName"))
)
if mibBuilder.loadTexts:
    dQosDscpMutationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 61, 2, 1, 1)
)
dQosCompliance.setObjects(
      *(("DLINKSW-QOS-MIB", "dQosPolicyGroup"),
        ("DLINKSW-QOS-MIB", "dQosSchedulingGroup"),
        ("DLINKSW-QOS-MIB", "dQosWrrGroup"),
        ("DLINKSW-QOS-MIB", "dQosWdrrGroup"),
        ("DLINKSW-QOS-MIB", "dQosPortBandwidthCtrlGroup"),
        ("DLINKSW-QOS-MIB", "dQosQueueBandwidthCtrlGroup"),
        ("DLINKSW-QOS-MIB", "dQosAggregatePolicingGroup"),
        ("DLINKSW-QOS-MIB", "dQosPolicingGroup"),
        ("DLINKSW-QOS-MIB", "dQosColorAwarePolicingGroup"),
        ("DLINKSW-QOS-MIB", "dQosQueuingGroup"),
        ("DLINKSW-QOS-MIB", "dQosDscpMutationGroup"))
)
if mibBuilder.loadTexts:
    dQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-QOS-MIB",
    **{"DlinkQosPoliceActionType": DlinkQosPoliceActionType,
       "dlinkSwQosMIB": dlinkSwQosMIB,
       "dQosMIBNotifications": dQosMIBNotifications,
       "dQosMIBObjects": dQosMIBObjects,
       "dQosClassMap": dQosClassMap,
       "dQosClassMapTable": dQosClassMapTable,
       "dQosClassMapEntry": dQosClassMapEntry,
       "dQosClassMapName": dQosClassMapName,
       "dQosClassMapType": dQosClassMapType,
       "dQosClassMapRowStaus": dQosClassMapRowStaus,
       "dQosClassMapCfgTable": dQosClassMapCfgTable,
       "dQosClassMapCfgEntry": dQosClassMapCfgEntry,
       "dQosClassMapCfgMatchId": dQosClassMapCfgMatchId,
       "dQosClassMapCfgMatchType": dQosClassMapCfgMatchType,
       "dQosClassMapCfgMatchValue": dQosClassMapCfgMatchValue,
       "dQosClassMapCfgRowStaus": dQosClassMapCfgRowStaus,
       "dQosPolicyMap": dQosPolicyMap,
       "dQosPolicyMapTable": dQosPolicyMapTable,
       "dQosPolicyMapEntry": dQosPolicyMapEntry,
       "dQosPolicyMapName": dQosPolicyMapName,
       "dQosPolicyMapRowStatus": dQosPolicyMapRowStatus,
       "dQosPolicyMapCfgTable": dQosPolicyMapCfgTable,
       "dQosPolicyMapCfgEntry": dQosPolicyMapCfgEntry,
       "dQosPolicyMapCfgSetCosQueue": dQosPolicyMapCfgSetCosQueue,
       "dQosPolicyMapCfgSetCos": dQosPolicyMapCfgSetCos,
       "dQosPolicyMapCfgSetDscpOnlyIp": dQosPolicyMapCfgSetDscpOnlyIp,
       "dQosPolicyMapCfgSetDscp": dQosPolicyMapCfgSetDscp,
       "dQosPolicyMapCfgSetPreceOnlyIp": dQosPolicyMapCfgSetPreceOnlyIp,
       "dQosPolicyMapCfgSetPrecedence": dQosPolicyMapCfgSetPrecedence,
       "dQosPolicyMapCfgRowStatus": dQosPolicyMapCfgRowStatus,
       "dQosAggPolicerTable": dQosAggPolicerTable,
       "dQosAggPolicerEntry": dQosAggPolicerEntry,
       "dQosAggPolicerName": dQosAggPolicerName,
       "dQosAggPolicerType": dQosAggPolicerType,
       "dQosAggPolicerCir": dQosAggPolicerCir,
       "dQosAggPolicerCbs": dQosAggPolicerCbs,
       "dQosAggPolicerSrtcmEbs": dQosAggPolicerSrtcmEbs,
       "dQosAggPolicerTrtcmPir": dQosAggPolicerTrtcmPir,
       "dQosAggPolicerTrtcmPbs": dQosAggPolicerTrtcmPbs,
       "dQosAggPolicerConformAction": dQosAggPolicerConformAction,
       "dQosAggPolicerConformReplaceDscp": dQosAggPolicerConformReplaceDscp,
       "dQosAggPolicerExceedAction": dQosAggPolicerExceedAction,
       "dQosAggPolicerExceedReplaceDscp": dQosAggPolicerExceedReplaceDscp,
       "dQosAggPolicerViolateAction": dQosAggPolicerViolateAction,
       "dQosAggPolicerViolateReplaceDscp": dQosAggPolicerViolateReplaceDscp,
       "dQosAggPolicerColorAware": dQosAggPolicerColorAware,
       "dQosAggPolicerConformReplaceCos": dQosAggPolicerConformReplaceCos,
       "dQosAggPolicerExceedReplaceCos": dQosAggPolicerExceedReplaceCos,
       "dQosAggPolicerViolateReplaceCos": dQosAggPolicerViolateReplaceCos,
       "dQosAggPolicerRowStatus": dQosAggPolicerRowStatus,
       "dQosPoliceTable": dQosPoliceTable,
       "dQosPoliceEntry": dQosPoliceEntry,
       "dQosPoliceType": dQosPoliceType,
       "dQosPoliceNamedAggPolicer": dQosPoliceNamedAggPolicer,
       "dQosPoliceCir": dQosPoliceCir,
       "dQosPoliceCbs": dQosPoliceCbs,
       "dQosPoliceSrtcmEbs": dQosPoliceSrtcmEbs,
       "dQosPoliceTrtcmPir": dQosPoliceTrtcmPir,
       "dQosPoliceTrtcmPbs": dQosPoliceTrtcmPbs,
       "dQosPoliceConformAction": dQosPoliceConformAction,
       "dQosPoliceConformReplaceDscp": dQosPoliceConformReplaceDscp,
       "dQosPoliceExceedAction": dQosPoliceExceedAction,
       "dQosPoliceExceedReplaceDscp": dQosPoliceExceedReplaceDscp,
       "dQosPoliceViolateAction": dQosPoliceViolateAction,
       "dQosPoliceViolateReplaceDscp": dQosPoliceViolateReplaceDscp,
       "dQosPoliceColorAware": dQosPoliceColorAware,
       "dQosPoliceRowStatus": dQosPoliceRowStatus,
       "dQosPoliceConformReplaceCos": dQosPoliceConformReplaceCos,
       "dQosPoliceExceedReplaceCos": dQosPoliceExceedReplaceCos,
       "dQosPoliceViolateReplaceCos": dQosPoliceViolateReplaceCos,
       "dQosServicePolicy": dQosServicePolicy,
       "dQosServicePolicyTable": dQosServicePolicyTable,
       "dQosServicePolicyEntry": dQosServicePolicyEntry,
       "dQosServicePolicyDirection": dQosServicePolicyDirection,
       "dQosServicePolicyName": dQosServicePolicyName,
       "dQosServicePolicyRowStaus": dQosServicePolicyRowStaus,
       "dQosScheduling": dQosScheduling,
       "dQosSchedulingModeTable": dQosSchedulingModeTable,
       "dQosSchedulingModeEntry": dQosSchedulingModeEntry,
       "dQosSchedulingMode": dQosSchedulingMode,
       "dQosScheduleWrrWeightTable": dQosScheduleWrrWeightTable,
       "dQosScheduleWrrWeightEntry": dQosScheduleWrrWeightEntry,
       "dQosScheduleWrrWeightQueueId": dQosScheduleWrrWeightQueueId,
       "dQosScheduleWrrWeightValue": dQosScheduleWrrWeightValue,
       "dQosScheduleWdrrWeightTable": dQosScheduleWdrrWeightTable,
       "dQosScheduleWdrrWeightEntry": dQosScheduleWdrrWeightEntry,
       "dQosScheduleWdrrWeightQueueId": dQosScheduleWdrrWeightQueueId,
       "dQosScheduleWdrrWeightValue": dQosScheduleWdrrWeightValue,
       "dQosBandwidthCtrl": dQosBandwidthCtrl,
       "dQosBandwidthCtrlTable": dQosBandwidthCtrlTable,
       "dQosBandwidthCtrlEntry": dQosBandwidthCtrlEntry,
       "dQosBandwidthRxRate": dQosBandwidthRxRate,
       "dQosBandwidthRxBurst": dQosBandwidthRxBurst,
       "dQosBandwidthTxRate": dQosBandwidthTxRate,
       "dQosBandwidthTxBurst": dQosBandwidthTxBurst,
       "dQosBandwidthRxRateMode": dQosBandwidthRxRateMode,
       "dQosBandwidthTxRateMode": dQosBandwidthTxRateMode,
       "dQosQueueBandwidthCtrl": dQosQueueBandwidthCtrl,
       "dQosQueueBandwidthCtrlTable": dQosQueueBandwidthCtrlTable,
       "dQosQueueBandwidthCtrlEntry": dQosQueueBandwidthCtrlEntry,
       "dQosQueueBandwidthQueId": dQosQueueBandwidthQueId,
       "dQosQueueBandwidthMinRate": dQosQueueBandwidthMinRate,
       "dQosQueueBandwidthMaxRate": dQosQueueBandwidthMaxRate,
       "dQosQueueBandwidthMinRateMode": dQosQueueBandwidthMinRateMode,
       "dQosQueueBandwidthMaxRateMode": dQosQueueBandwidthMaxRateMode,
       "dQosQueuingCfg": dQosQueuingCfg,
       "dQosPortIfQueuingTable": dQosPortIfQueuingTable,
       "dQosPortIfQueuingEntry": dQosPortIfQueuingEntry,
       "dQosPortIf8021pOverride": dQosPortIf8021pOverride,
       "dQosPortIfTrustMode": dQosPortIfTrustMode,
       "dQosDscpMap": dQosDscpMap,
       "dQosDscpMutationMapTable": dQosDscpMutationMapTable,
       "dQosDscpMutationMapEntry": dQosDscpMutationMapEntry,
       "dQosDscpMutationMapName": dQosDscpMutationMapName,
       "dQosDscpMutationMapRowStatus": dQosDscpMutationMapRowStatus,
       "dQosDscpMutationMapCfgTable": dQosDscpMutationMapCfgTable,
       "dQosDscpMutationMapCfgEntry": dQosDscpMutationMapCfgEntry,
       "dQosDscpMutationOldDscp": dQosDscpMutationOldDscp,
       "dQosDscpMutationNewDscp": dQosDscpMutationNewDscp,
       "dQosDscpMutationMapAttachTable": dQosDscpMutationMapAttachTable,
       "dQosDscpMutationMapAttachEntry": dQosDscpMutationMapAttachEntry,
       "dQosDscpMutationMapAttachName": dQosDscpMutationMapAttachName,
       "dQosDscpMapCtrlTable": dQosDscpMapCtrlTable,
       "dQosDscpMapCtrlEntry": dQosDscpMapCtrlEntry,
       "dQosDscpMapCtrlDscp": dQosDscpMapCtrlDscp,
       "dQosDscpMapCtrlCos": dQosDscpMapCtrlCos,
       "dQosDscpMapCtrlColor": dQosDscpMapCtrlColor,
       "dQosCosMap": dQosCosMap,
       "dQosCosToColorMapTable": dQosCosToColorMapTable,
       "dQosCosToColorMapEntry": dQosCosToColorMapEntry,
       "dQosCosMapCos": dQosCosMapCos,
       "dQosCosMapColor": dQosCosMapColor,
       "dQosCosToQueueMapTable": dQosCosToQueueMapTable,
       "dQosCosToQueueMapEntry": dQosCosToQueueMapEntry,
       "dQosCosToQueueCos": dQosCosToQueueCos,
       "dQosCosToQueueQID": dQosCosToQueueQID,
       "dQosMIBConformance": dQosMIBConformance,
       "dQosCompliances": dQosCompliances,
       "dQosCompliance": dQosCompliance,
       "dQosGroups": dQosGroups,
       "dQosPolicyGroup": dQosPolicyGroup,
       "dQosSchedulingGroup": dQosSchedulingGroup,
       "dQosWrrGroup": dQosWrrGroup,
       "dQosWdrrGroup": dQosWdrrGroup,
       "dQosPortBandwidthCtrlGroup": dQosPortBandwidthCtrlGroup,
       "dQosQueueBandwidthCtrlGroup": dQosQueueBandwidthCtrlGroup,
       "dQosAggregatePolicingGroup": dQosAggregatePolicingGroup,
       "dQosPolicingGroup": dQosPolicingGroup,
       "dQosColorAwarePolicingGroup": dQosColorAwarePolicingGroup,
       "dQosQueuingGroup": dQosQueuingGroup,
       "dQosDscpMutationGroup": dQosDscpMutationGroup}
)
