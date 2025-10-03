# SNMP MIB module (VIPTELA-APP-ROUTE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-APP-ROUTE
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:58 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_app_route = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 9)
)
if mibBuilder.loadTexts:
    viptela_app_route.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_AppRoute_ObjectIdentity = ObjectIdentity
appRoute = _AppRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 9, 1)
)
_AppRouteStatisticsTable_Object = MibTable
appRouteStatisticsTable = _AppRouteStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2)
)
if mibBuilder.loadTexts:
    appRouteStatisticsTable.setStatus("current")
_AppRouteStatisticsEntry_Object = MibTableRow
appRouteStatisticsEntry = _AppRouteStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1)
)
appRouteStatisticsEntry.setIndexNames(
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsSrcIp"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsDstIp"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsProto"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsSrcPort"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsDstPort"),
)
if mibBuilder.loadTexts:
    appRouteStatisticsEntry.setStatus("current")
_AppRouteStatisticsSrcIp_Type = InetAddressIP
_AppRouteStatisticsSrcIp_Object = MibTableColumn
appRouteStatisticsSrcIp = _AppRouteStatisticsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 1),
    _AppRouteStatisticsSrcIp_Type()
)
appRouteStatisticsSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsSrcIp.setStatus("current")
_AppRouteStatisticsDstIp_Type = InetAddressIP
_AppRouteStatisticsDstIp_Object = MibTableColumn
appRouteStatisticsDstIp = _AppRouteStatisticsDstIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 2),
    _AppRouteStatisticsDstIp_Type()
)
appRouteStatisticsDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsDstIp.setStatus("current")


class _AppRouteStatisticsProto_Type(Integer32):
    """Custom type appRouteStatisticsProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_AppRouteStatisticsProto_Type.__name__ = "Integer32"
_AppRouteStatisticsProto_Object = MibTableColumn
appRouteStatisticsProto = _AppRouteStatisticsProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 3),
    _AppRouteStatisticsProto_Type()
)
appRouteStatisticsProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsProto.setStatus("current")
_AppRouteStatisticsSrcPort_Type = UnsignedShort
_AppRouteStatisticsSrcPort_Object = MibTableColumn
appRouteStatisticsSrcPort = _AppRouteStatisticsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 4),
    _AppRouteStatisticsSrcPort_Type()
)
appRouteStatisticsSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsSrcPort.setStatus("current")
_AppRouteStatisticsDstPort_Type = UnsignedShort
_AppRouteStatisticsDstPort_Object = MibTableColumn
appRouteStatisticsDstPort = _AppRouteStatisticsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 5),
    _AppRouteStatisticsDstPort_Type()
)
appRouteStatisticsDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsDstPort.setStatus("current")
_AppRouteStatisticsRemoteSystemIp_Type = IpAddress
_AppRouteStatisticsRemoteSystemIp_Object = MibTableColumn
appRouteStatisticsRemoteSystemIp = _AppRouteStatisticsRemoteSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 6),
    _AppRouteStatisticsRemoteSystemIp_Type()
)
appRouteStatisticsRemoteSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsRemoteSystemIp.setStatus("current")


class _AppRouteStatisticsLocalColor_Type(Integer32):
    """Custom type appRouteStatisticsLocalColor based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_AppRouteStatisticsLocalColor_Type.__name__ = "Integer32"
_AppRouteStatisticsLocalColor_Object = MibTableColumn
appRouteStatisticsLocalColor = _AppRouteStatisticsLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 7),
    _AppRouteStatisticsLocalColor_Type()
)
appRouteStatisticsLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsLocalColor.setStatus("current")


class _AppRouteStatisticsRemoteColor_Type(Integer32):
    """Custom type appRouteStatisticsRemoteColor based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_AppRouteStatisticsRemoteColor_Type.__name__ = "Integer32"
_AppRouteStatisticsRemoteColor_Object = MibTableColumn
appRouteStatisticsRemoteColor = _AppRouteStatisticsRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 8),
    _AppRouteStatisticsRemoteColor_Type()
)
appRouteStatisticsRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsRemoteColor.setStatus("current")
_AppRouteStatisticsMeanLoss_Type = UnsignedByte
_AppRouteStatisticsMeanLoss_Object = MibTableColumn
appRouteStatisticsMeanLoss = _AppRouteStatisticsMeanLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 9),
    _AppRouteStatisticsMeanLoss_Type()
)
appRouteStatisticsMeanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsMeanLoss.setStatus("current")
_AppRouteStatisticsMeanLatency_Type = Unsigned32
_AppRouteStatisticsMeanLatency_Object = MibTableColumn
appRouteStatisticsMeanLatency = _AppRouteStatisticsMeanLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 10),
    _AppRouteStatisticsMeanLatency_Type()
)
appRouteStatisticsMeanLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsMeanLatency.setStatus("current")
_AppRouteStatisticsSlaClassIndex_Type = String
_AppRouteStatisticsSlaClassIndex_Object = MibTableColumn
appRouteStatisticsSlaClassIndex = _AppRouteStatisticsSlaClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 11),
    _AppRouteStatisticsSlaClassIndex_Type()
)
appRouteStatisticsSlaClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsSlaClassIndex.setStatus("current")
_AppRouteStatisticsMeanJitter_Type = Unsigned32
_AppRouteStatisticsMeanJitter_Object = MibTableColumn
appRouteStatisticsMeanJitter = _AppRouteStatisticsMeanJitter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 2, 1, 12),
    _AppRouteStatisticsMeanJitter_Type()
)
appRouteStatisticsMeanJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsMeanJitter.setStatus("current")
_AppRouteStatisticsIntervalTable_Object = MibTable
appRouteStatisticsIntervalTable = _AppRouteStatisticsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3)
)
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalTable.setStatus("current")
_AppRouteStatisticsIntervalEntry_Object = MibTableRow
appRouteStatisticsIntervalEntry = _AppRouteStatisticsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3, 1)
)
appRouteStatisticsIntervalEntry.setIndexNames(
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsSrcIp"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsDstIp"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsProto"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsSrcPort"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsDstPort"),
    (0, "VIPTELA-APP-ROUTE", "appRouteStatisticsIntervalIndex"),
)
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalEntry.setStatus("current")
_AppRouteStatisticsIntervalIndex_Type = UnsignedByte
_AppRouteStatisticsIntervalIndex_Object = MibTableColumn
appRouteStatisticsIntervalIndex = _AppRouteStatisticsIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3, 1, 1),
    _AppRouteStatisticsIntervalIndex_Type()
)
appRouteStatisticsIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalIndex.setStatus("current")
_AppRouteStatisticsIntervalTotalPackets_Type = Integer32
_AppRouteStatisticsIntervalTotalPackets_Object = MibTableColumn
appRouteStatisticsIntervalTotalPackets = _AppRouteStatisticsIntervalTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3, 1, 2),
    _AppRouteStatisticsIntervalTotalPackets_Type()
)
appRouteStatisticsIntervalTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalTotalPackets.setStatus("current")
_AppRouteStatisticsIntervalLoss_Type = Integer32
_AppRouteStatisticsIntervalLoss_Object = MibTableColumn
appRouteStatisticsIntervalLoss = _AppRouteStatisticsIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3, 1, 3),
    _AppRouteStatisticsIntervalLoss_Type()
)
appRouteStatisticsIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalLoss.setStatus("current")
_AppRouteStatisticsIntervalAverageLatency_Type = ConfdString
_AppRouteStatisticsIntervalAverageLatency_Object = MibTableColumn
appRouteStatisticsIntervalAverageLatency = _AppRouteStatisticsIntervalAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3, 1, 4),
    _AppRouteStatisticsIntervalAverageLatency_Type()
)
appRouteStatisticsIntervalAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalAverageLatency.setStatus("current")
_AppRouteStatisticsIntervalAverageJitter_Type = ConfdString
_AppRouteStatisticsIntervalAverageJitter_Object = MibTableColumn
appRouteStatisticsIntervalAverageJitter = _AppRouteStatisticsIntervalAverageJitter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3, 1, 5),
    _AppRouteStatisticsIntervalAverageJitter_Type()
)
appRouteStatisticsIntervalAverageJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalAverageJitter.setStatus("current")
_AppRouteStatisticsIntervalTxDataPkts_Type = Counter64
_AppRouteStatisticsIntervalTxDataPkts_Object = MibTableColumn
appRouteStatisticsIntervalTxDataPkts = _AppRouteStatisticsIntervalTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3, 1, 6),
    _AppRouteStatisticsIntervalTxDataPkts_Type()
)
appRouteStatisticsIntervalTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalTxDataPkts.setStatus("current")
_AppRouteStatisticsIntervalRxDataPkts_Type = Counter64
_AppRouteStatisticsIntervalRxDataPkts_Object = MibTableColumn
appRouteStatisticsIntervalRxDataPkts = _AppRouteStatisticsIntervalRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 3, 1, 7),
    _AppRouteStatisticsIntervalRxDataPkts_Type()
)
appRouteStatisticsIntervalRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsIntervalRxDataPkts.setStatus("current")
_AppRouteSlaClassTable_Object = MibTable
appRouteSlaClassTable = _AppRouteSlaClassTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 4)
)
if mibBuilder.loadTexts:
    appRouteSlaClassTable.setStatus("current")
_AppRouteSlaClassEntry_Object = MibTableRow
appRouteSlaClassEntry = _AppRouteSlaClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 4, 1)
)
appRouteSlaClassEntry.setIndexNames(
    (0, "VIPTELA-APP-ROUTE", "appRouteSlaClassIndex"),
)
if mibBuilder.loadTexts:
    appRouteSlaClassEntry.setStatus("current")
_AppRouteSlaClassIndex_Type = UnsignedByte
_AppRouteSlaClassIndex_Object = MibTableColumn
appRouteSlaClassIndex = _AppRouteSlaClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 4, 1, 1),
    _AppRouteSlaClassIndex_Type()
)
appRouteSlaClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteSlaClassIndex.setStatus("current")
_AppRouteSlaClassName_Type = String
_AppRouteSlaClassName_Object = MibTableColumn
appRouteSlaClassName = _AppRouteSlaClassName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 4, 1, 2),
    _AppRouteSlaClassName_Type()
)
appRouteSlaClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteSlaClassName.setStatus("current")
_AppRouteSlaClassLoss_Type = UnsignedByte
_AppRouteSlaClassLoss_Object = MibTableColumn
appRouteSlaClassLoss = _AppRouteSlaClassLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 4, 1, 3),
    _AppRouteSlaClassLoss_Type()
)
appRouteSlaClassLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteSlaClassLoss.setStatus("current")
_AppRouteSlaClassLatency_Type = Unsigned32
_AppRouteSlaClassLatency_Object = MibTableColumn
appRouteSlaClassLatency = _AppRouteSlaClassLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 4, 1, 4),
    _AppRouteSlaClassLatency_Type()
)
appRouteSlaClassLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteSlaClassLatency.setStatus("current")
_AppRouteSlaClassJitter_Type = Unsigned32
_AppRouteSlaClassJitter_Object = MibTableColumn
appRouteSlaClassJitter = _AppRouteSlaClassJitter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 9, 4, 1, 5),
    _AppRouteSlaClassJitter_Type()
)
appRouteSlaClassJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteSlaClassJitter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-APP-ROUTE",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "String": String,
       "InetAddressIP": InetAddressIP,
       "viptela-app-route": viptela_app_route,
       "appRoute": appRoute,
       "appRouteStatisticsTable": appRouteStatisticsTable,
       "appRouteStatisticsEntry": appRouteStatisticsEntry,
       "appRouteStatisticsSrcIp": appRouteStatisticsSrcIp,
       "appRouteStatisticsDstIp": appRouteStatisticsDstIp,
       "appRouteStatisticsProto": appRouteStatisticsProto,
       "appRouteStatisticsSrcPort": appRouteStatisticsSrcPort,
       "appRouteStatisticsDstPort": appRouteStatisticsDstPort,
       "appRouteStatisticsRemoteSystemIp": appRouteStatisticsRemoteSystemIp,
       "appRouteStatisticsLocalColor": appRouteStatisticsLocalColor,
       "appRouteStatisticsRemoteColor": appRouteStatisticsRemoteColor,
       "appRouteStatisticsMeanLoss": appRouteStatisticsMeanLoss,
       "appRouteStatisticsMeanLatency": appRouteStatisticsMeanLatency,
       "appRouteStatisticsSlaClassIndex": appRouteStatisticsSlaClassIndex,
       "appRouteStatisticsMeanJitter": appRouteStatisticsMeanJitter,
       "appRouteStatisticsIntervalTable": appRouteStatisticsIntervalTable,
       "appRouteStatisticsIntervalEntry": appRouteStatisticsIntervalEntry,
       "appRouteStatisticsIntervalIndex": appRouteStatisticsIntervalIndex,
       "appRouteStatisticsIntervalTotalPackets": appRouteStatisticsIntervalTotalPackets,
       "appRouteStatisticsIntervalLoss": appRouteStatisticsIntervalLoss,
       "appRouteStatisticsIntervalAverageLatency": appRouteStatisticsIntervalAverageLatency,
       "appRouteStatisticsIntervalAverageJitter": appRouteStatisticsIntervalAverageJitter,
       "appRouteStatisticsIntervalTxDataPkts": appRouteStatisticsIntervalTxDataPkts,
       "appRouteStatisticsIntervalRxDataPkts": appRouteStatisticsIntervalRxDataPkts,
       "appRouteSlaClassTable": appRouteSlaClassTable,
       "appRouteSlaClassEntry": appRouteSlaClassEntry,
       "appRouteSlaClassIndex": appRouteSlaClassIndex,
       "appRouteSlaClassName": appRouteSlaClassName,
       "appRouteSlaClassLoss": appRouteSlaClassLoss,
       "appRouteSlaClassLatency": appRouteSlaClassLatency,
       "appRouteSlaClassJitter": appRouteSlaClassJitter}
)
