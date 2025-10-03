# SNMP MIB module (BTI8xx-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bti\BTI8xx-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:37 2025
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

(mainSystem,) = mibBuilder.importSymbols(
    "BTI8xx-TC-MIB",
    "mainSystem")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

interfaceConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5)
)
if mibBuilder.loadTexts:
    interfaceConfig.setRevisions(
        ("2015-11-20 12:00",
         "2015-02-25 15:00",
         "2014-11-14 12:00",
         "2014-10-29 12:00",
         "2014-06-13 12:00",
         "2013-12-27 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InterfaceConfigTable_Object = MibTable
interfaceConfigTable = _InterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    interfaceConfigTable.setStatus("current")
_InterfaceConfigEntry_Object = MibTableRow
interfaceConfigEntry = _InterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1)
)
interfaceConfigEntry.setIndexNames(
    (0, "BTI8xx-INTERFACE-MIB", "interfaceConfigIndex"),
)
if mibBuilder.loadTexts:
    interfaceConfigEntry.setStatus("current")


class _InterfaceConfigIndex_Type(Integer32):
    """Custom type interfaceConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_InterfaceConfigIndex_Type.__name__ = "Integer32"
_InterfaceConfigIndex_Object = MibTableColumn
interfaceConfigIndex = _InterfaceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 1),
    _InterfaceConfigIndex_Type()
)
interfaceConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceConfigIndex.setStatus("current")


class _InterfaceConfigPort_Type(OctetString):
    """Custom type interfaceConfigPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InterfaceConfigPort_Type.__name__ = "OctetString"
_InterfaceConfigPort_Object = MibTableColumn
interfaceConfigPort = _InterfaceConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 2),
    _InterfaceConfigPort_Type()
)
interfaceConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceConfigPort.setStatus("current")


class _InterfaceConfigMTU_Type(Integer32):
    """Custom type interfaceConfigMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_InterfaceConfigMTU_Type.__name__ = "Integer32"
_InterfaceConfigMTU_Object = MibTableColumn
interfaceConfigMTU = _InterfaceConfigMTU_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 3),
    _InterfaceConfigMTU_Type()
)
interfaceConfigMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigMTU.setStatus("current")


class _InterfaceConfigTPID_Type(OctetString):
    """Custom type interfaceConfigTPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_InterfaceConfigTPID_Type.__name__ = "OctetString"
_InterfaceConfigTPID_Object = MibTableColumn
interfaceConfigTPID = _InterfaceConfigTPID_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 4),
    _InterfaceConfigTPID_Type()
)
interfaceConfigTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigTPID.setStatus("current")


class _InterfaceConfigPVID_Type(Integer32):
    """Custom type interfaceConfigPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_InterfaceConfigPVID_Type.__name__ = "Integer32"
_InterfaceConfigPVID_Object = MibTableColumn
interfaceConfigPVID = _InterfaceConfigPVID_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 5),
    _InterfaceConfigPVID_Type()
)
interfaceConfigPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigPVID.setStatus("current")


class _InterfaceConfigAdminStatus_Type(Integer32):
    """Custom type interfaceConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_InterfaceConfigAdminStatus_Type.__name__ = "Integer32"
_InterfaceConfigAdminStatus_Object = MibTableColumn
interfaceConfigAdminStatus = _InterfaceConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 6),
    _InterfaceConfigAdminStatus_Type()
)
interfaceConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigAdminStatus.setStatus("current")


class _InterfaceConfigOperStatus_Type(Integer32):
    """Custom type interfaceConfigOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_InterfaceConfigOperStatus_Type.__name__ = "Integer32"
_InterfaceConfigOperStatus_Object = MibTableColumn
interfaceConfigOperStatus = _InterfaceConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 7),
    _InterfaceConfigOperStatus_Type()
)
interfaceConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceConfigOperStatus.setStatus("current")


class _InterfaceConfigMode_Type(Integer32):
    """Custom type interfaceConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force", 2))
    )


_InterfaceConfigMode_Type.__name__ = "Integer32"
_InterfaceConfigMode_Object = MibTableColumn
interfaceConfigMode = _InterfaceConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 8),
    _InterfaceConfigMode_Type()
)
interfaceConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigMode.setStatus("current")


class _InterfaceConfigDuplex_Type(Integer32):
    """Custom type interfaceConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("auto", 3))
    )


_InterfaceConfigDuplex_Type.__name__ = "Integer32"
_InterfaceConfigDuplex_Object = MibTableColumn
interfaceConfigDuplex = _InterfaceConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 9),
    _InterfaceConfigDuplex_Type()
)
interfaceConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigDuplex.setStatus("current")


class _InterfaceConfigSpeed_Type(Integer32):
    """Custom type interfaceConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_InterfaceConfigSpeed_Type.__name__ = "Integer32"
_InterfaceConfigSpeed_Object = MibTableColumn
interfaceConfigSpeed = _InterfaceConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 10),
    _InterfaceConfigSpeed_Type()
)
interfaceConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigSpeed.setStatus("current")


class _InterfaceConfigAdminFlowCtrl_Type(Integer32):
    """Custom type interfaceConfigAdminFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_InterfaceConfigAdminFlowCtrl_Type.__name__ = "Integer32"
_InterfaceConfigAdminFlowCtrl_Object = MibTableColumn
interfaceConfigAdminFlowCtrl = _InterfaceConfigAdminFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 11),
    _InterfaceConfigAdminFlowCtrl_Type()
)
interfaceConfigAdminFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigAdminFlowCtrl.setStatus("current")


class _InterfaceConfigOperFlowCtrl_Type(Integer32):
    """Custom type interfaceConfigOperFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_InterfaceConfigOperFlowCtrl_Type.__name__ = "Integer32"
_InterfaceConfigOperFlowCtrl_Object = MibTableColumn
interfaceConfigOperFlowCtrl = _InterfaceConfigOperFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 12),
    _InterfaceConfigOperFlowCtrl_Type()
)
interfaceConfigOperFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceConfigOperFlowCtrl.setStatus("current")


class _InterfaceConfigAct_Type(Integer32):
    """Custom type interfaceConfigAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("act", 1),
          ("deAct", 2))
    )


_InterfaceConfigAct_Type.__name__ = "Integer32"
_InterfaceConfigAct_Object = MibTableColumn
interfaceConfigAct = _InterfaceConfigAct_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 13),
    _InterfaceConfigAct_Type()
)
interfaceConfigAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceConfigAct.setStatus("current")


class _InterfaceConfigDescription_Type(OctetString):
    """Custom type interfaceConfigDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InterfaceConfigDescription_Type.__name__ = "OctetString"
_InterfaceConfigDescription_Object = MibTableColumn
interfaceConfigDescription = _InterfaceConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 14),
    _InterfaceConfigDescription_Type()
)
interfaceConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigDescription.setStatus("current")


class _InterfaceConfigPriority_Type(Integer32):
    """Custom type interfaceConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_InterfaceConfigPriority_Type.__name__ = "Integer32"
_InterfaceConfigPriority_Object = MibTableColumn
interfaceConfigPriority = _InterfaceConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 15),
    _InterfaceConfigPriority_Type()
)
interfaceConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigPriority.setStatus("current")


class _InterfaceConfigLag_Type(OctetString):
    """Custom type interfaceConfigLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InterfaceConfigLag_Type.__name__ = "OctetString"
_InterfaceConfigLag_Object = MibTableColumn
interfaceConfigLag = _InterfaceConfigLag_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 16),
    _InterfaceConfigLag_Type()
)
interfaceConfigLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceConfigLag.setStatus("current")


class _InterfaceConfigLearning_Type(Integer32):
    """Custom type interfaceConfigLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_InterfaceConfigLearning_Type.__name__ = "Integer32"
_InterfaceConfigLearning_Object = MibTableColumn
interfaceConfigLearning = _InterfaceConfigLearning_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 17),
    _InterfaceConfigLearning_Type()
)
interfaceConfigLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceConfigLearning.setStatus("current")
_InterfaceStatisticsTable_Object = MibTable
interfaceStatisticsTable = _InterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    interfaceStatisticsTable.setStatus("current")
_InterfaceStatisticsEntry_Object = MibTableRow
interfaceStatisticsEntry = _InterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1)
)
interfaceStatisticsEntry.setIndexNames(
    (0, "BTI8xx-INTERFACE-MIB", "interfaceStatisticsIndex"),
)
if mibBuilder.loadTexts:
    interfaceStatisticsEntry.setStatus("current")


class _InterfaceStatisticsIndex_Type(Integer32):
    """Custom type interfaceStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_InterfaceStatisticsIndex_Type.__name__ = "Integer32"
_InterfaceStatisticsIndex_Object = MibTableColumn
interfaceStatisticsIndex = _InterfaceStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 1),
    _InterfaceStatisticsIndex_Type()
)
interfaceStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsIndex.setStatus("current")


class _InterfaceStatisticsInOctets_Type(Unsigned32):
    """Custom type interfaceStatisticsInOctets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsInOctets_Type.__name__ = "Unsigned32"
_InterfaceStatisticsInOctets_Object = MibTableColumn
interfaceStatisticsInOctets = _InterfaceStatisticsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 2),
    _InterfaceStatisticsInOctets_Type()
)
interfaceStatisticsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInOctets.setStatus("current")


class _InterfaceStatisticsInFrames_Type(Unsigned32):
    """Custom type interfaceStatisticsInFrames based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsInFrames_Type.__name__ = "Unsigned32"
_InterfaceStatisticsInFrames_Object = MibTableColumn
interfaceStatisticsInFrames = _InterfaceStatisticsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 3),
    _InterfaceStatisticsInFrames_Type()
)
interfaceStatisticsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInFrames.setStatus("current")


class _InterfaceStatisticsInUcastPkts_Type(Unsigned32):
    """Custom type interfaceStatisticsInUcastPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsInUcastPkts_Type.__name__ = "Unsigned32"
_InterfaceStatisticsInUcastPkts_Object = MibTableColumn
interfaceStatisticsInUcastPkts = _InterfaceStatisticsInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 4),
    _InterfaceStatisticsInUcastPkts_Type()
)
interfaceStatisticsInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInUcastPkts.setStatus("current")


class _InterfaceStatisticsInMulticastPkts_Type(Unsigned32):
    """Custom type interfaceStatisticsInMulticastPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsInMulticastPkts_Type.__name__ = "Unsigned32"
_InterfaceStatisticsInMulticastPkts_Object = MibTableColumn
interfaceStatisticsInMulticastPkts = _InterfaceStatisticsInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 5),
    _InterfaceStatisticsInMulticastPkts_Type()
)
interfaceStatisticsInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInMulticastPkts.setStatus("current")


class _InterfaceStatisticsInBroadcastPkts_Type(Unsigned32):
    """Custom type interfaceStatisticsInBroadcastPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsInBroadcastPkts_Type.__name__ = "Unsigned32"
_InterfaceStatisticsInBroadcastPkts_Object = MibTableColumn
interfaceStatisticsInBroadcastPkts = _InterfaceStatisticsInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 6),
    _InterfaceStatisticsInBroadcastPkts_Type()
)
interfaceStatisticsInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInBroadcastPkts.setStatus("current")


class _InterfaceStatisticsOutOctets_Type(Unsigned32):
    """Custom type interfaceStatisticsOutOctets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsOutOctets_Type.__name__ = "Unsigned32"
_InterfaceStatisticsOutOctets_Object = MibTableColumn
interfaceStatisticsOutOctets = _InterfaceStatisticsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 7),
    _InterfaceStatisticsOutOctets_Type()
)
interfaceStatisticsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsOutOctets.setStatus("current")


class _InterfaceStatisticsOutFrames_Type(Unsigned32):
    """Custom type interfaceStatisticsOutFrames based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsOutFrames_Type.__name__ = "Unsigned32"
_InterfaceStatisticsOutFrames_Object = MibTableColumn
interfaceStatisticsOutFrames = _InterfaceStatisticsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 8),
    _InterfaceStatisticsOutFrames_Type()
)
interfaceStatisticsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsOutFrames.setStatus("current")


class _InterfaceStatisticsOutUcastPkts_Type(Unsigned32):
    """Custom type interfaceStatisticsOutUcastPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsOutUcastPkts_Type.__name__ = "Unsigned32"
_InterfaceStatisticsOutUcastPkts_Object = MibTableColumn
interfaceStatisticsOutUcastPkts = _InterfaceStatisticsOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 9),
    _InterfaceStatisticsOutUcastPkts_Type()
)
interfaceStatisticsOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsOutUcastPkts.setStatus("current")


class _InterfaceStatisticsOutMulticastPkts_Type(Unsigned32):
    """Custom type interfaceStatisticsOutMulticastPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsOutMulticastPkts_Type.__name__ = "Unsigned32"
_InterfaceStatisticsOutMulticastPkts_Object = MibTableColumn
interfaceStatisticsOutMulticastPkts = _InterfaceStatisticsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 10),
    _InterfaceStatisticsOutMulticastPkts_Type()
)
interfaceStatisticsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsOutMulticastPkts.setStatus("current")


class _InterfaceStatisticsOutBroadcastPkts_Type(Unsigned32):
    """Custom type interfaceStatisticsOutBroadcastPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsOutBroadcastPkts_Type.__name__ = "Unsigned32"
_InterfaceStatisticsOutBroadcastPkts_Object = MibTableColumn
interfaceStatisticsOutBroadcastPkts = _InterfaceStatisticsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 11),
    _InterfaceStatisticsOutBroadcastPkts_Type()
)
interfaceStatisticsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsOutBroadcastPkts.setStatus("current")


class _InterfaceStatisticsDropEvents_Type(Unsigned32):
    """Custom type interfaceStatisticsDropEvents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsDropEvents_Type.__name__ = "Unsigned32"
_InterfaceStatisticsDropEvents_Object = MibTableColumn
interfaceStatisticsDropEvents = _InterfaceStatisticsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 12),
    _InterfaceStatisticsDropEvents_Type()
)
interfaceStatisticsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsDropEvents.setStatus("current")


class _InterfaceStatisticsFCSErrors_Type(Unsigned32):
    """Custom type interfaceStatisticsFCSErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsFCSErrors_Type.__name__ = "Unsigned32"
_InterfaceStatisticsFCSErrors_Object = MibTableColumn
interfaceStatisticsFCSErrors = _InterfaceStatisticsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 13),
    _InterfaceStatisticsFCSErrors_Type()
)
interfaceStatisticsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsFCSErrors.setStatus("current")


class _InterfaceStatisticsUndersizePkts_Type(Unsigned32):
    """Custom type interfaceStatisticsUndersizePkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsUndersizePkts_Type.__name__ = "Unsigned32"
_InterfaceStatisticsUndersizePkts_Object = MibTableColumn
interfaceStatisticsUndersizePkts = _InterfaceStatisticsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 14),
    _InterfaceStatisticsUndersizePkts_Type()
)
interfaceStatisticsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsUndersizePkts.setStatus("current")


class _InterfaceStatisticsOversizePkts_Type(Unsigned32):
    """Custom type interfaceStatisticsOversizePkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsOversizePkts_Type.__name__ = "Unsigned32"
_InterfaceStatisticsOversizePkts_Object = MibTableColumn
interfaceStatisticsOversizePkts = _InterfaceStatisticsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 15),
    _InterfaceStatisticsOversizePkts_Type()
)
interfaceStatisticsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsOversizePkts.setStatus("current")


class _InterfaceStatisticsFragments_Type(Unsigned32):
    """Custom type interfaceStatisticsFragments based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsFragments_Type.__name__ = "Unsigned32"
_InterfaceStatisticsFragments_Object = MibTableColumn
interfaceStatisticsFragments = _InterfaceStatisticsFragments_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 16),
    _InterfaceStatisticsFragments_Type()
)
interfaceStatisticsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsFragments.setStatus("current")


class _InterfaceStatisticsJabbers_Type(Unsigned32):
    """Custom type interfaceStatisticsJabbers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsJabbers_Type.__name__ = "Unsigned32"
_InterfaceStatisticsJabbers_Object = MibTableColumn
interfaceStatisticsJabbers = _InterfaceStatisticsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 17),
    _InterfaceStatisticsJabbers_Type()
)
interfaceStatisticsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsJabbers.setStatus("current")


class _InterfaceStatisticsSymbolErrors_Type(Unsigned32):
    """Custom type interfaceStatisticsSymbolErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_InterfaceStatisticsSymbolErrors_Type.__name__ = "Unsigned32"
_InterfaceStatisticsSymbolErrors_Object = MibTableColumn
interfaceStatisticsSymbolErrors = _InterfaceStatisticsSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 18),
    _InterfaceStatisticsSymbolErrors_Type()
)
interfaceStatisticsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsSymbolErrors.setStatus("current")
_RemotePortIdTable_Object = MibTable
remotePortIdTable = _RemotePortIdTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    remotePortIdTable.setStatus("current")
_RemotePortIdEntry_Object = MibTableRow
remotePortIdEntry = _RemotePortIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1)
)
remotePortIdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    remotePortIdEntry.setStatus("current")


class _RemotePortIdLocalPort_Type(OctetString):
    """Custom type remotePortIdLocalPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RemotePortIdLocalPort_Type.__name__ = "OctetString"
_RemotePortIdLocalPort_Object = MibTableColumn
remotePortIdLocalPort = _RemotePortIdLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 1),
    _RemotePortIdLocalPort_Type()
)
remotePortIdLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortIdLocalPort.setStatus("current")


class _RemotePortIdLocalType_Type(OctetString):
    """Custom type remotePortIdLocalType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RemotePortIdLocalType_Type.__name__ = "OctetString"
_RemotePortIdLocalType_Object = MibTableColumn
remotePortIdLocalType = _RemotePortIdLocalType_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 2),
    _RemotePortIdLocalType_Type()
)
remotePortIdLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortIdLocalType.setStatus("current")


class _RemotePortIdDesc_Type(OctetString):
    """Custom type remotePortIdDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemotePortIdDesc_Type.__name__ = "OctetString"
_RemotePortIdDesc_Object = MibTableColumn
remotePortIdDesc = _RemotePortIdDesc_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 3),
    _RemotePortIdDesc_Type()
)
remotePortIdDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remotePortIdDesc.setStatus("current")
_RateLimitTable_Object = MibTable
rateLimitTable = _RateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    rateLimitTable.setStatus("current")
_RateLimitEntry_Object = MibTableRow
rateLimitEntry = _RateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1)
)
rateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rateLimitEntry.setStatus("current")


class _RateLimitPort_Type(OctetString):
    """Custom type rateLimitPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RateLimitPort_Type.__name__ = "OctetString"
_RateLimitPort_Object = MibTableColumn
rateLimitPort = _RateLimitPort_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 1),
    _RateLimitPort_Type()
)
rateLimitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitPort.setStatus("current")


class _RateLimitIngressRate_Type(Integer32):
    """Custom type rateLimitIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RateLimitIngressRate_Type.__name__ = "Integer32"
_RateLimitIngressRate_Object = MibTableColumn
rateLimitIngressRate = _RateLimitIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 2),
    _RateLimitIngressRate_Type()
)
rateLimitIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitIngressRate.setStatus("current")


class _RateLimitIngressBurst_Type(Integer32):
    """Custom type rateLimitIngressBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RateLimitIngressBurst_Type.__name__ = "Integer32"
_RateLimitIngressBurst_Object = MibTableColumn
rateLimitIngressBurst = _RateLimitIngressBurst_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 3),
    _RateLimitIngressBurst_Type()
)
rateLimitIngressBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitIngressBurst.setStatus("current")


class _RateLimitIngressState_Type(Integer32):
    """Custom type rateLimitIngressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RateLimitIngressState_Type.__name__ = "Integer32"
_RateLimitIngressState_Object = MibTableColumn
rateLimitIngressState = _RateLimitIngressState_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 4),
    _RateLimitIngressState_Type()
)
rateLimitIngressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitIngressState.setStatus("current")


class _RateLimitEgressRate_Type(Integer32):
    """Custom type rateLimitEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RateLimitEgressRate_Type.__name__ = "Integer32"
_RateLimitEgressRate_Object = MibTableColumn
rateLimitEgressRate = _RateLimitEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 5),
    _RateLimitEgressRate_Type()
)
rateLimitEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitEgressRate.setStatus("current")


class _RateLimitEgressBurst_Type(Integer32):
    """Custom type rateLimitEgressBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RateLimitEgressBurst_Type.__name__ = "Integer32"
_RateLimitEgressBurst_Object = MibTableColumn
rateLimitEgressBurst = _RateLimitEgressBurst_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 6),
    _RateLimitEgressBurst_Type()
)
rateLimitEgressBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitEgressBurst.setStatus("current")


class _RateLimitEgressState_Type(Integer32):
    """Custom type rateLimitEgressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RateLimitEgressState_Type.__name__ = "Integer32"
_RateLimitEgressState_Object = MibTableColumn
rateLimitEgressState = _RateLimitEgressState_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 7),
    _RateLimitEgressState_Type()
)
rateLimitEgressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitEgressState.setStatus("current")


class _RateLimitShapingMode_Type(Integer32):
    """Custom type rateLimitShapingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("layer1", 0),
          ("layer2", 1))
    )


_RateLimitShapingMode_Type.__name__ = "Integer32"
_RateLimitShapingMode_Object = MibTableColumn
rateLimitShapingMode = _RateLimitShapingMode_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 8),
    _RateLimitShapingMode_Type()
)
rateLimitShapingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitShapingMode.setStatus("current")
_StormCtrlTable_Object = MibTable
stormCtrlTable = _StormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    stormCtrlTable.setStatus("current")
_StormCtrlEntry_Object = MibTableRow
stormCtrlEntry = _StormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1)
)
stormCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    stormCtrlEntry.setStatus("current")


class _StormCtrlPort_Type(OctetString):
    """Custom type stormCtrlPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_StormCtrlPort_Type.__name__ = "OctetString"
_StormCtrlPort_Object = MibTableColumn
stormCtrlPort = _StormCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 1),
    _StormCtrlPort_Type()
)
stormCtrlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormCtrlPort.setStatus("current")


class _StormCtrlBroadcastPps_Type(Integer32):
    """Custom type stormCtrlBroadcastPps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_StormCtrlBroadcastPps_Type.__name__ = "Integer32"
_StormCtrlBroadcastPps_Object = MibTableColumn
stormCtrlBroadcastPps = _StormCtrlBroadcastPps_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 2),
    _StormCtrlBroadcastPps_Type()
)
stormCtrlBroadcastPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlBroadcastPps.setStatus("current")


class _StormCtrlBroadcastState_Type(Integer32):
    """Custom type stormCtrlBroadcastState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_StormCtrlBroadcastState_Type.__name__ = "Integer32"
_StormCtrlBroadcastState_Object = MibTableColumn
stormCtrlBroadcastState = _StormCtrlBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 3),
    _StormCtrlBroadcastState_Type()
)
stormCtrlBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlBroadcastState.setStatus("current")


class _StormCtrlMulticastPps_Type(Integer32):
    """Custom type stormCtrlMulticastPps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_StormCtrlMulticastPps_Type.__name__ = "Integer32"
_StormCtrlMulticastPps_Object = MibTableColumn
stormCtrlMulticastPps = _StormCtrlMulticastPps_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 4),
    _StormCtrlMulticastPps_Type()
)
stormCtrlMulticastPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlMulticastPps.setStatus("current")


class _StormCtrlMulticastState_Type(Integer32):
    """Custom type stormCtrlMulticastState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_StormCtrlMulticastState_Type.__name__ = "Integer32"
_StormCtrlMulticastState_Object = MibTableColumn
stormCtrlMulticastState = _StormCtrlMulticastState_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 5),
    _StormCtrlMulticastState_Type()
)
stormCtrlMulticastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlMulticastState.setStatus("current")


class _StormCtrlDlfPps_Type(Integer32):
    """Custom type stormCtrlDlfPps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_StormCtrlDlfPps_Type.__name__ = "Integer32"
_StormCtrlDlfPps_Object = MibTableColumn
stormCtrlDlfPps = _StormCtrlDlfPps_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 6),
    _StormCtrlDlfPps_Type()
)
stormCtrlDlfPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlDlfPps.setStatus("current")


class _StormCtrlDlfState_Type(Integer32):
    """Custom type stormCtrlDlfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_StormCtrlDlfState_Type.__name__ = "Integer32"
_StormCtrlDlfState_Object = MibTableColumn
stormCtrlDlfState = _StormCtrlDlfState_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 7),
    _StormCtrlDlfState_Type()
)
stormCtrlDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlDlfState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI8xx-INTERFACE-MIB",
    **{"interfaceConfig": interfaceConfig,
       "interfaceConfigTable": interfaceConfigTable,
       "interfaceConfigEntry": interfaceConfigEntry,
       "interfaceConfigIndex": interfaceConfigIndex,
       "interfaceConfigPort": interfaceConfigPort,
       "interfaceConfigMTU": interfaceConfigMTU,
       "interfaceConfigTPID": interfaceConfigTPID,
       "interfaceConfigPVID": interfaceConfigPVID,
       "interfaceConfigAdminStatus": interfaceConfigAdminStatus,
       "interfaceConfigOperStatus": interfaceConfigOperStatus,
       "interfaceConfigMode": interfaceConfigMode,
       "interfaceConfigDuplex": interfaceConfigDuplex,
       "interfaceConfigSpeed": interfaceConfigSpeed,
       "interfaceConfigAdminFlowCtrl": interfaceConfigAdminFlowCtrl,
       "interfaceConfigOperFlowCtrl": interfaceConfigOperFlowCtrl,
       "interfaceConfigAct": interfaceConfigAct,
       "interfaceConfigDescription": interfaceConfigDescription,
       "interfaceConfigPriority": interfaceConfigPriority,
       "interfaceConfigLag": interfaceConfigLag,
       "interfaceConfigLearning": interfaceConfigLearning,
       "interfaceStatisticsTable": interfaceStatisticsTable,
       "interfaceStatisticsEntry": interfaceStatisticsEntry,
       "interfaceStatisticsIndex": interfaceStatisticsIndex,
       "interfaceStatisticsInOctets": interfaceStatisticsInOctets,
       "interfaceStatisticsInFrames": interfaceStatisticsInFrames,
       "interfaceStatisticsInUcastPkts": interfaceStatisticsInUcastPkts,
       "interfaceStatisticsInMulticastPkts": interfaceStatisticsInMulticastPkts,
       "interfaceStatisticsInBroadcastPkts": interfaceStatisticsInBroadcastPkts,
       "interfaceStatisticsOutOctets": interfaceStatisticsOutOctets,
       "interfaceStatisticsOutFrames": interfaceStatisticsOutFrames,
       "interfaceStatisticsOutUcastPkts": interfaceStatisticsOutUcastPkts,
       "interfaceStatisticsOutMulticastPkts": interfaceStatisticsOutMulticastPkts,
       "interfaceStatisticsOutBroadcastPkts": interfaceStatisticsOutBroadcastPkts,
       "interfaceStatisticsDropEvents": interfaceStatisticsDropEvents,
       "interfaceStatisticsFCSErrors": interfaceStatisticsFCSErrors,
       "interfaceStatisticsUndersizePkts": interfaceStatisticsUndersizePkts,
       "interfaceStatisticsOversizePkts": interfaceStatisticsOversizePkts,
       "interfaceStatisticsFragments": interfaceStatisticsFragments,
       "interfaceStatisticsJabbers": interfaceStatisticsJabbers,
       "interfaceStatisticsSymbolErrors": interfaceStatisticsSymbolErrors,
       "remotePortIdTable": remotePortIdTable,
       "remotePortIdEntry": remotePortIdEntry,
       "remotePortIdLocalPort": remotePortIdLocalPort,
       "remotePortIdLocalType": remotePortIdLocalType,
       "remotePortIdDesc": remotePortIdDesc,
       "rateLimitTable": rateLimitTable,
       "rateLimitEntry": rateLimitEntry,
       "rateLimitPort": rateLimitPort,
       "rateLimitIngressRate": rateLimitIngressRate,
       "rateLimitIngressBurst": rateLimitIngressBurst,
       "rateLimitIngressState": rateLimitIngressState,
       "rateLimitEgressRate": rateLimitEgressRate,
       "rateLimitEgressBurst": rateLimitEgressBurst,
       "rateLimitEgressState": rateLimitEgressState,
       "rateLimitShapingMode": rateLimitShapingMode,
       "stormCtrlTable": stormCtrlTable,
       "stormCtrlEntry": stormCtrlEntry,
       "stormCtrlPort": stormCtrlPort,
       "stormCtrlBroadcastPps": stormCtrlBroadcastPps,
       "stormCtrlBroadcastState": stormCtrlBroadcastState,
       "stormCtrlMulticastPps": stormCtrlMulticastPps,
       "stormCtrlMulticastState": stormCtrlMulticastState,
       "stormCtrlDlfPps": stormCtrlDlfPps,
       "stormCtrlDlfState": stormCtrlDlfState}
)
