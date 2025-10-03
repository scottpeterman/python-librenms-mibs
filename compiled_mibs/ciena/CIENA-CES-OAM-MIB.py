# SNMP MIB module (CIENA-CES-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-OAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:44 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesNotifications,
 cienaCesStatistics) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesNotifications",
    "cienaCesStatistics")

(CienaStatsClear,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaStatsClear")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

cienaCesOamMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cienaCesOamMibModule.setRevisions(
        ("2018-12-05 00:00",
         "2017-06-07 00:00",
         "2017-01-09 00:00",
         "2016-02-19 20:49",
         "2010-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesOamNotifMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesOamNotifMIBNotificationPrefix = _CienaCesOamNotifMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 15)
)
_CienaCesOamNotifMIBNotification_ObjectIdentity = ObjectIdentity
cienaCesOamNotifMIBNotification = _CienaCesOamNotifMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 15, 0)
)
_CienaCesOamMIB_ObjectIdentity = ObjectIdentity
cienaCesOamMIB = _CienaCesOamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1)
)
_CienaCesOamStatistics_ObjectIdentity = ObjectIdentity
cienaCesOamStatistics = _CienaCesOamStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1)
)
_CienaCesOamStatsTable_Object = MibTable
cienaCesOamStatsTable = _CienaCesOamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesOamStatsTable.setStatus("current")
_CienaCesOamStatsEntry_Object = MibTableRow
cienaCesOamStatsEntry = _CienaCesOamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1)
)
cienaCesOamStatsEntry.setIndexNames(
    (0, "CIENA-CES-OAM-MIB", "cienaCesOamStatsPort"),
)
if mibBuilder.loadTexts:
    cienaCesOamStatsEntry.setStatus("current")
_CienaCesOamInformationTx_Type = Counter32
_CienaCesOamInformationTx_Object = MibTableColumn
cienaCesOamInformationTx = _CienaCesOamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 1),
    _CienaCesOamInformationTx_Type()
)
cienaCesOamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamInformationTx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamInformationTx.setUnits("frames")
_CienaCesOamInformationRx_Type = Counter32
_CienaCesOamInformationRx_Object = MibTableColumn
cienaCesOamInformationRx = _CienaCesOamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 2),
    _CienaCesOamInformationRx_Type()
)
cienaCesOamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamInformationRx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamInformationRx.setUnits("frames")
_CienaCesOamUniqueEventNotificationTx_Type = Counter32
_CienaCesOamUniqueEventNotificationTx_Object = MibTableColumn
cienaCesOamUniqueEventNotificationTx = _CienaCesOamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 3),
    _CienaCesOamUniqueEventNotificationTx_Type()
)
cienaCesOamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamUniqueEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamUniqueEventNotificationTx.setUnits("frames")
_CienaCesOamUniqueEventNotificationRx_Type = Counter32
_CienaCesOamUniqueEventNotificationRx_Object = MibTableColumn
cienaCesOamUniqueEventNotificationRx = _CienaCesOamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 4),
    _CienaCesOamUniqueEventNotificationRx_Type()
)
cienaCesOamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamUniqueEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamUniqueEventNotificationRx.setUnits("frames")
_CienaCesOamLoopbackControlTx_Type = Counter32
_CienaCesOamLoopbackControlTx_Object = MibTableColumn
cienaCesOamLoopbackControlTx = _CienaCesOamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 5),
    _CienaCesOamLoopbackControlTx_Type()
)
cienaCesOamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamLoopbackControlTx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamLoopbackControlTx.setUnits("frames")
_CienaCesOamLoopbackControlRx_Type = Counter32
_CienaCesOamLoopbackControlRx_Object = MibTableColumn
cienaCesOamLoopbackControlRx = _CienaCesOamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 6),
    _CienaCesOamLoopbackControlRx_Type()
)
cienaCesOamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamLoopbackControlRx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamLoopbackControlRx.setUnits("frames")
_CienaCesOamVariableRequestTx_Type = Counter32
_CienaCesOamVariableRequestTx_Object = MibTableColumn
cienaCesOamVariableRequestTx = _CienaCesOamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 7),
    _CienaCesOamVariableRequestTx_Type()
)
cienaCesOamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamVariableRequestTx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamVariableRequestTx.setUnits("frames")
_CienaCesOamVariableRequestRx_Type = Counter32
_CienaCesOamVariableRequestRx_Object = MibTableColumn
cienaCesOamVariableRequestRx = _CienaCesOamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 8),
    _CienaCesOamVariableRequestRx_Type()
)
cienaCesOamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamVariableRequestRx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamVariableRequestRx.setUnits("frames")
_CienaCesOamVariableResponseTx_Type = Counter32
_CienaCesOamVariableResponseTx_Object = MibTableColumn
cienaCesOamVariableResponseTx = _CienaCesOamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 9),
    _CienaCesOamVariableResponseTx_Type()
)
cienaCesOamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamVariableResponseTx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamVariableResponseTx.setUnits("frames")
_CienaCesOamVariableResponseRx_Type = Counter32
_CienaCesOamVariableResponseRx_Object = MibTableColumn
cienaCesOamVariableResponseRx = _CienaCesOamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 10),
    _CienaCesOamVariableResponseRx_Type()
)
cienaCesOamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamVariableResponseRx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamVariableResponseRx.setUnits("frames")
_CienaCesOamOrgSpecificTx_Type = Counter32
_CienaCesOamOrgSpecificTx_Object = MibTableColumn
cienaCesOamOrgSpecificTx = _CienaCesOamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 11),
    _CienaCesOamOrgSpecificTx_Type()
)
cienaCesOamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamOrgSpecificTx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamOrgSpecificTx.setUnits("frames")
_CienaCesOamOrgSpecificRx_Type = Counter32
_CienaCesOamOrgSpecificRx_Object = MibTableColumn
cienaCesOamOrgSpecificRx = _CienaCesOamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 12),
    _CienaCesOamOrgSpecificRx_Type()
)
cienaCesOamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamOrgSpecificRx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamOrgSpecificRx.setUnits("frames")
_CienaCesOamUnsupportedCodesTx_Type = Counter32
_CienaCesOamUnsupportedCodesTx_Object = MibTableColumn
cienaCesOamUnsupportedCodesTx = _CienaCesOamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 13),
    _CienaCesOamUnsupportedCodesTx_Type()
)
cienaCesOamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamUnsupportedCodesTx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamUnsupportedCodesTx.setUnits("frames")
_CienaCesOamUnsupportedCodesRx_Type = Counter32
_CienaCesOamUnsupportedCodesRx_Object = MibTableColumn
cienaCesOamUnsupportedCodesRx = _CienaCesOamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 14),
    _CienaCesOamUnsupportedCodesRx_Type()
)
cienaCesOamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamUnsupportedCodesRx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamUnsupportedCodesRx.setUnits("frames")
_CienaCesOamframesLostDueToOam_Type = Counter32
_CienaCesOamframesLostDueToOam_Object = MibTableColumn
cienaCesOamframesLostDueToOam = _CienaCesOamframesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 15),
    _CienaCesOamframesLostDueToOam_Type()
)
cienaCesOamframesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamframesLostDueToOam.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamframesLostDueToOam.setUnits("frames")


class _CienaCesOamStatsPort_Type(Integer32):
    """Custom type cienaCesOamStatsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CienaCesOamStatsPort_Type.__name__ = "Integer32"
_CienaCesOamStatsPort_Object = MibTableColumn
cienaCesOamStatsPort = _CienaCesOamStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 16),
    _CienaCesOamStatsPort_Type()
)
cienaCesOamStatsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOamStatsPort.setStatus("current")
_CienaCesOamDuplicateEventNotificationTx_Type = Counter32
_CienaCesOamDuplicateEventNotificationTx_Object = MibTableColumn
cienaCesOamDuplicateEventNotificationTx = _CienaCesOamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 17),
    _CienaCesOamDuplicateEventNotificationTx_Type()
)
cienaCesOamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamDuplicateEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamDuplicateEventNotificationTx.setUnits("frames")
_CienaCesOamDuplicateEventNotificationRx_Type = Counter32
_CienaCesOamDuplicateEventNotificationRx_Object = MibTableColumn
cienaCesOamDuplicateEventNotificationRx = _CienaCesOamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 1, 1, 18),
    _CienaCesOamDuplicateEventNotificationRx_Type()
)
cienaCesOamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamDuplicateEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamDuplicateEventNotificationRx.setUnits("frames")
_CienaCesOamEventLogTable_Object = MibTable
cienaCesOamEventLogTable = _CienaCesOamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesOamEventLogTable.setStatus("current")
_CienaCesOamEventLogEntry_Object = MibTableRow
cienaCesOamEventLogEntry = _CienaCesOamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1)
)
cienaCesOamEventLogEntry.setIndexNames(
    (0, "CIENA-CES-OAM-MIB", "cienaCesOamEventLogPort"),
    (0, "CIENA-CES-OAM-MIB", "cienaCesOamEventLogIndex"),
)
if mibBuilder.loadTexts:
    cienaCesOamEventLogEntry.setStatus("current")
_CienaCesOamEventLogPort_Type = Integer32
_CienaCesOamEventLogPort_Object = MibTableColumn
cienaCesOamEventLogPort = _CienaCesOamEventLogPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 1),
    _CienaCesOamEventLogPort_Type()
)
cienaCesOamEventLogPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOamEventLogPort.setStatus("current")
_CienaCesOamEventLogIndex_Type = Unsigned32
_CienaCesOamEventLogIndex_Object = MibTableColumn
cienaCesOamEventLogIndex = _CienaCesOamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 2),
    _CienaCesOamEventLogIndex_Type()
)
cienaCesOamEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOamEventLogIndex.setStatus("current")
_CienaCesOamEventLogTimestamp_Type = TimeStamp
_CienaCesOamEventLogTimestamp_Object = MibTableColumn
cienaCesOamEventLogTimestamp = _CienaCesOamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 3),
    _CienaCesOamEventLogTimestamp_Type()
)
cienaCesOamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogTimestamp.setStatus("current")


class _CienaCesOamEventLogOui_Type(OctetString):
    """Custom type cienaCesOamEventLogOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_CienaCesOamEventLogOui_Type.__name__ = "OctetString"
_CienaCesOamEventLogOui_Object = MibTableColumn
cienaCesOamEventLogOui = _CienaCesOamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 4),
    _CienaCesOamEventLogOui_Type()
)
cienaCesOamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogOui.setStatus("current")


class _CienaCesOamEventLogType_Type(Integer32):
    """Custom type cienaCesOamEventLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("errFramePeriodEvent", 1),
          ("errFrameEvent", 2),
          ("errFrameSecSummEvent", 3),
          ("linkFaultEvent", 4),
          ("dyingGaspEvent", 5),
          ("criticalLinkEvent", 6),
          ("noEvent", 99))
    )


_CienaCesOamEventLogType_Type.__name__ = "Integer32"
_CienaCesOamEventLogType_Object = MibTableColumn
cienaCesOamEventLogType = _CienaCesOamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 5),
    _CienaCesOamEventLogType_Type()
)
cienaCesOamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogType.setStatus("current")


class _CienaCesOamEventLogLocation_Type(Integer32):
    """Custom type cienaCesOamEventLogLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_CienaCesOamEventLogLocation_Type.__name__ = "Integer32"
_CienaCesOamEventLogLocation_Object = MibTableColumn
cienaCesOamEventLogLocation = _CienaCesOamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 6),
    _CienaCesOamEventLogLocation_Type()
)
cienaCesOamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogLocation.setStatus("current")
_CienaCesOamEventLogWindowHi_Type = Unsigned32
_CienaCesOamEventLogWindowHi_Object = MibTableColumn
cienaCesOamEventLogWindowHi = _CienaCesOamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 7),
    _CienaCesOamEventLogWindowHi_Type()
)
cienaCesOamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogWindowHi.setStatus("current")
_CienaCesOamEventLogWindowLo_Type = Unsigned32
_CienaCesOamEventLogWindowLo_Object = MibTableColumn
cienaCesOamEventLogWindowLo = _CienaCesOamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 8),
    _CienaCesOamEventLogWindowLo_Type()
)
cienaCesOamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogWindowLo.setStatus("current")
_CienaCesOamEventLogThresholdHi_Type = Unsigned32
_CienaCesOamEventLogThresholdHi_Object = MibTableColumn
cienaCesOamEventLogThresholdHi = _CienaCesOamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 9),
    _CienaCesOamEventLogThresholdHi_Type()
)
cienaCesOamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogThresholdHi.setStatus("current")
_CienaCesOamEventLogThresholdLo_Type = Unsigned32
_CienaCesOamEventLogThresholdLo_Object = MibTableColumn
cienaCesOamEventLogThresholdLo = _CienaCesOamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 10),
    _CienaCesOamEventLogThresholdLo_Type()
)
cienaCesOamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogThresholdLo.setStatus("current")
_CienaCesOamEventLogValue_Type = Counter64
_CienaCesOamEventLogValue_Object = MibTableColumn
cienaCesOamEventLogValue = _CienaCesOamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 11),
    _CienaCesOamEventLogValue_Type()
)
cienaCesOamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogValue.setStatus("current")
_CienaCesOamEventLogRunningTotal_Type = Counter64
_CienaCesOamEventLogRunningTotal_Object = MibTableColumn
cienaCesOamEventLogRunningTotal = _CienaCesOamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 12),
    _CienaCesOamEventLogRunningTotal_Type()
)
cienaCesOamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogRunningTotal.setStatus("current")
_CienaCesOamEventLogEventTotal_Type = Unsigned32
_CienaCesOamEventLogEventTotal_Object = MibTableColumn
cienaCesOamEventLogEventTotal = _CienaCesOamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 13),
    _CienaCesOamEventLogEventTotal_Type()
)
cienaCesOamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamEventLogEventTotal.setStatus("current")


class _CienaCesOamEventNotifChassisIndex_Type(Unsigned32):
    """Custom type cienaCesOamEventNotifChassisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesOamEventNotifChassisIndex_Type.__name__ = "Unsigned32"
_CienaCesOamEventNotifChassisIndex_Object = MibTableColumn
cienaCesOamEventNotifChassisIndex = _CienaCesOamEventNotifChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 14),
    _CienaCesOamEventNotifChassisIndex_Type()
)
cienaCesOamEventNotifChassisIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesOamEventNotifChassisIndex.setStatus("current")


class _CienaCesOamEventNotifShelfIndex_Type(Unsigned32):
    """Custom type cienaCesOamEventNotifShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesOamEventNotifShelfIndex_Type.__name__ = "Unsigned32"
_CienaCesOamEventNotifShelfIndex_Object = MibTableColumn
cienaCesOamEventNotifShelfIndex = _CienaCesOamEventNotifShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 15),
    _CienaCesOamEventNotifShelfIndex_Type()
)
cienaCesOamEventNotifShelfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesOamEventNotifShelfIndex.setStatus("current")


class _CienaCesOamEventNotifSlotIndex_Type(Unsigned32):
    """Custom type cienaCesOamEventNotifSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CienaCesOamEventNotifSlotIndex_Type.__name__ = "Unsigned32"
_CienaCesOamEventNotifSlotIndex_Object = MibTableColumn
cienaCesOamEventNotifSlotIndex = _CienaCesOamEventNotifSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 16),
    _CienaCesOamEventNotifSlotIndex_Type()
)
cienaCesOamEventNotifSlotIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesOamEventNotifSlotIndex.setStatus("current")


class _CienaCesOamEventNotifPortNumber_Type(Unsigned32):
    """Custom type cienaCesOamEventNotifPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesOamEventNotifPortNumber_Type.__name__ = "Unsigned32"
_CienaCesOamEventNotifPortNumber_Object = MibTableColumn
cienaCesOamEventNotifPortNumber = _CienaCesOamEventNotifPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 17),
    _CienaCesOamEventNotifPortNumber_Type()
)
cienaCesOamEventNotifPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesOamEventNotifPortNumber.setStatus("current")
_CienaCesOamEventNotifChannelNumber_Type = Unsigned32
_CienaCesOamEventNotifChannelNumber_Object = MibTableColumn
cienaCesOamEventNotifChannelNumber = _CienaCesOamEventNotifChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 2, 1, 18),
    _CienaCesOamEventNotifChannelNumber_Type()
)
cienaCesOamEventNotifChannelNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesOamEventNotifChannelNumber.setStatus("current")
_CienaCesOamStatsClear_Type = CienaStatsClear
_CienaCesOamStatsClear_Object = MibScalar
cienaCesOamStatsClear = _CienaCesOamStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 3),
    _CienaCesOamStatsClear_Type()
)
cienaCesOamStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesOamStatsClear.setStatus("current")
_CienaCesOamTable_Object = MibTable
cienaCesOamTable = _CienaCesOamTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesOamTable.setStatus("current")
_CienaCesOamEntry_Object = MibTableRow
cienaCesOamEntry = _CienaCesOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1)
)
cienaCesOamEntry.setIndexNames(
    (0, "CIENA-CES-OAM-MIB", "cienaCesOamPort"),
)
if mibBuilder.loadTexts:
    cienaCesOamEntry.setStatus("current")
_CienaCesOamPort_Type = Integer32
_CienaCesOamPort_Object = MibTableColumn
cienaCesOamPort = _CienaCesOamPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 1),
    _CienaCesOamPort_Type()
)
cienaCesOamPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOamPort.setStatus("current")


class _CienaCesOamAdminState_Type(Integer32):
    """Custom type cienaCesOamAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCesOamAdminState_Type.__name__ = "Integer32"
_CienaCesOamAdminState_Object = MibTableColumn
cienaCesOamAdminState = _CienaCesOamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 2),
    _CienaCesOamAdminState_Type()
)
cienaCesOamAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamAdminState.setStatus("current")


class _CienaCesOamOperStatus_Type(Integer32):
    """Custom type cienaCesOamOperStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("linkfault", 2),
          ("passiveWait", 3),
          ("activeSendLocal", 4),
          ("sendLocalAndRemote", 5),
          ("sendLocalAndRemoteOk", 6),
          ("oamPeeringLocallyRejected", 7),
          ("oamPeeringRemotelyRejected", 8),
          ("operational", 9))
    )


_CienaCesOamOperStatus_Type.__name__ = "Integer32"
_CienaCesOamOperStatus_Object = MibTableColumn
cienaCesOamOperStatus = _CienaCesOamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 3),
    _CienaCesOamOperStatus_Type()
)
cienaCesOamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamOperStatus.setStatus("current")


class _CienaCesOamMode_Type(Integer32):
    """Custom type cienaCesOamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_CienaCesOamMode_Type.__name__ = "Integer32"
_CienaCesOamMode_Object = MibTableColumn
cienaCesOamMode = _CienaCesOamMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 4),
    _CienaCesOamMode_Type()
)
cienaCesOamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamMode.setStatus("current")
_CienaCesMaxOamPduSize_Type = Integer32
_CienaCesMaxOamPduSize_Object = MibTableColumn
cienaCesMaxOamPduSize = _CienaCesMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 5),
    _CienaCesMaxOamPduSize_Type()
)
cienaCesMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesMaxOamPduSize.setUnits("bytes")
_CienaCesOamConfigRevision_Type = Unsigned32
_CienaCesOamConfigRevision_Object = MibTableColumn
cienaCesOamConfigRevision = _CienaCesOamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 6),
    _CienaCesOamConfigRevision_Type()
)
cienaCesOamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamConfigRevision.setStatus("current")


class _CienaCesOamFunctionsSupported_Type(Bits):
    """Custom type cienaCesOamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_CienaCesOamFunctionsSupported_Type.__name__ = "Bits"
_CienaCesOamFunctionsSupported_Object = MibTableColumn
cienaCesOamFunctionsSupported = _CienaCesOamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 7),
    _CienaCesOamFunctionsSupported_Type()
)
cienaCesOamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamFunctionsSupported.setStatus("current")


class _CienaCesOamPduTimer_Type(Integer32):
    """Custom type cienaCesOamPduTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CienaCesOamPduTimer_Type.__name__ = "Integer32"
_CienaCesOamPduTimer_Object = MibTableColumn
cienaCesOamPduTimer = _CienaCesOamPduTimer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 8),
    _CienaCesOamPduTimer_Type()
)
cienaCesOamPduTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPduTimer.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamPduTimer.setUnits("milliseconds")


class _CienaCesOamLinkLostTimer_Type(Integer32):
    """Custom type cienaCesOamLinkLostTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 5000),
    )


_CienaCesOamLinkLostTimer_Type.__name__ = "Integer32"
_CienaCesOamLinkLostTimer_Object = MibTableColumn
cienaCesOamLinkLostTimer = _CienaCesOamLinkLostTimer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 4, 1, 9),
    _CienaCesOamLinkLostTimer_Type()
)
cienaCesOamLinkLostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamLinkLostTimer.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamLinkLostTimer.setUnits("milliseconds")
_CienaCesOamPeerTable_Object = MibTable
cienaCesOamPeerTable = _CienaCesOamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesOamPeerTable.setStatus("current")
_CienaCesOamPeerEntry_Object = MibTableRow
cienaCesOamPeerEntry = _CienaCesOamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1)
)
cienaCesOamPeerEntry.setIndexNames(
    (0, "CIENA-CES-OAM-MIB", "cienaCesOamLocalPort"),
)
if mibBuilder.loadTexts:
    cienaCesOamPeerEntry.setStatus("current")
_CienaCesOamLocalPort_Type = Integer32
_CienaCesOamLocalPort_Object = MibTableColumn
cienaCesOamLocalPort = _CienaCesOamLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 1),
    _CienaCesOamLocalPort_Type()
)
cienaCesOamLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOamLocalPort.setStatus("current")


class _CienaCesOamPeerStatus_Type(Integer32):
    """Custom type cienaCesOamPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CienaCesOamPeerStatus_Type.__name__ = "Integer32"
_CienaCesOamPeerStatus_Object = MibTableColumn
cienaCesOamPeerStatus = _CienaCesOamPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 2),
    _CienaCesOamPeerStatus_Type()
)
cienaCesOamPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPeerStatus.setStatus("current")


class _CienaCesOamPeerMacAddress_Type(OctetString):
    """Custom type cienaCesOamPeerMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_CienaCesOamPeerMacAddress_Type.__name__ = "OctetString"
_CienaCesOamPeerMacAddress_Object = MibTableColumn
cienaCesOamPeerMacAddress = _CienaCesOamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 3),
    _CienaCesOamPeerMacAddress_Type()
)
cienaCesOamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPeerMacAddress.setStatus("current")


class _CienaCesOamPeerVendorOui_Type(OctetString):
    """Custom type cienaCesOamPeerVendorOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_CienaCesOamPeerVendorOui_Type.__name__ = "OctetString"
_CienaCesOamPeerVendorOui_Object = MibTableColumn
cienaCesOamPeerVendorOui = _CienaCesOamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 4),
    _CienaCesOamPeerVendorOui_Type()
)
cienaCesOamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPeerVendorOui.setStatus("current")
_CienaCesOamPeerVendorInfo_Type = Unsigned32
_CienaCesOamPeerVendorInfo_Object = MibTableColumn
cienaCesOamPeerVendorInfo = _CienaCesOamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 5),
    _CienaCesOamPeerVendorInfo_Type()
)
cienaCesOamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPeerVendorInfo.setStatus("current")


class _CienaCesOamPeerMode_Type(Integer32):
    """Custom type cienaCesOamPeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2),
          ("unknown", 3))
    )


_CienaCesOamPeerMode_Type.__name__ = "Integer32"
_CienaCesOamPeerMode_Object = MibTableColumn
cienaCesOamPeerMode = _CienaCesOamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 6),
    _CienaCesOamPeerMode_Type()
)
cienaCesOamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPeerMode.setStatus("current")
_CienaCesOamPeerMaxOamPduSize_Type = Integer32
_CienaCesOamPeerMaxOamPduSize_Object = MibTableColumn
cienaCesOamPeerMaxOamPduSize = _CienaCesOamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 7),
    _CienaCesOamPeerMaxOamPduSize_Type()
)
cienaCesOamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPeerMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamPeerMaxOamPduSize.setUnits("bytes")
_CienaCesOamPeerConfigRevision_Type = Unsigned32
_CienaCesOamPeerConfigRevision_Object = MibTableColumn
cienaCesOamPeerConfigRevision = _CienaCesOamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 8),
    _CienaCesOamPeerConfigRevision_Type()
)
cienaCesOamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPeerConfigRevision.setStatus("current")


class _CienaCesOamPeerFunctionsSupported_Type(Bits):
    """Custom type cienaCesOamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_CienaCesOamPeerFunctionsSupported_Type.__name__ = "Bits"
_CienaCesOamPeerFunctionsSupported_Object = MibTableColumn
cienaCesOamPeerFunctionsSupported = _CienaCesOamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 5, 1, 9),
    _CienaCesOamPeerFunctionsSupported_Type()
)
cienaCesOamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamPeerFunctionsSupported.setStatus("current")
_CienaCesOamLoopbackTable_Object = MibTable
cienaCesOamLoopbackTable = _CienaCesOamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cienaCesOamLoopbackTable.setStatus("current")
_CienaCesOamLoopbackEntry_Object = MibTableRow
cienaCesOamLoopbackEntry = _CienaCesOamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 6, 1)
)
cienaCesOamLoopbackEntry.setIndexNames(
    (0, "CIENA-CES-OAM-MIB", "cienaCesOamLoopbackPort"),
)
if mibBuilder.loadTexts:
    cienaCesOamLoopbackEntry.setStatus("current")
_CienaCesOamLoopbackPort_Type = Integer32
_CienaCesOamLoopbackPort_Object = MibTableColumn
cienaCesOamLoopbackPort = _CienaCesOamLoopbackPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 6, 1, 1),
    _CienaCesOamLoopbackPort_Type()
)
cienaCesOamLoopbackPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOamLoopbackPort.setStatus("current")


class _CienaCesOamLoopbackCommand_Type(Integer32):
    """Custom type cienaCesOamLoopbackCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("startRemoteLoopback", 2),
          ("stopRemoteLoopback", 3))
    )


_CienaCesOamLoopbackCommand_Type.__name__ = "Integer32"
_CienaCesOamLoopbackCommand_Object = MibTableColumn
cienaCesOamLoopbackCommand = _CienaCesOamLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 6, 1, 2),
    _CienaCesOamLoopbackCommand_Type()
)
cienaCesOamLoopbackCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamLoopbackCommand.setStatus("current")


class _CienaCesOamLoopbackStatus_Type(Integer32):
    """Custom type cienaCesOamLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("initiatingLoopback", 2),
          ("remoteLoopback", 3),
          ("terminatingLoopback", 4),
          ("localLoopback", 5),
          ("unknown", 6))
    )


_CienaCesOamLoopbackStatus_Type.__name__ = "Integer32"
_CienaCesOamLoopbackStatus_Object = MibTableColumn
cienaCesOamLoopbackStatus = _CienaCesOamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 6, 1, 3),
    _CienaCesOamLoopbackStatus_Type()
)
cienaCesOamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamLoopbackStatus.setStatus("current")


class _CienaCesOamLoopbackIgnoreRx_Type(Integer32):
    """Custom type cienaCesOamLoopbackIgnoreRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_CienaCesOamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_CienaCesOamLoopbackIgnoreRx_Object = MibTableColumn
cienaCesOamLoopbackIgnoreRx = _CienaCesOamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 6, 1, 4),
    _CienaCesOamLoopbackIgnoreRx_Type()
)
cienaCesOamLoopbackIgnoreRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamLoopbackIgnoreRx.setStatus("current")


class _CienaCesOamSystemEnableDisable_Type(Integer32):
    """Custom type cienaCesOamSystemEnableDisable based on Integer32"""
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


_CienaCesOamSystemEnableDisable_Type.__name__ = "Integer32"
_CienaCesOamSystemEnableDisable_Object = MibScalar
cienaCesOamSystemEnableDisable = _CienaCesOamSystemEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 7),
    _CienaCesOamSystemEnableDisable_Type()
)
cienaCesOamSystemEnableDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamSystemEnableDisable.setStatus("current")
_CienaCesOamEventConfigTable_Object = MibTable
cienaCesOamEventConfigTable = _CienaCesOamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cienaCesOamEventConfigTable.setStatus("current")
_CienaCesOamEventConfigEntry_Object = MibTableRow
cienaCesOamEventConfigEntry = _CienaCesOamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1)
)
cienaCesOamEventConfigEntry.setIndexNames(
    (0, "CIENA-CES-OAM-MIB", "cienaCesOamEventPort"),
)
if mibBuilder.loadTexts:
    cienaCesOamEventConfigEntry.setStatus("current")
_CienaCesOamEventPort_Type = Integer32
_CienaCesOamEventPort_Object = MibTableColumn
cienaCesOamEventPort = _CienaCesOamEventPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 1),
    _CienaCesOamEventPort_Type()
)
cienaCesOamEventPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOamEventPort.setStatus("current")
_CienaCesOamErrFramePeriodWindow_Type = Unsigned32
_CienaCesOamErrFramePeriodWindow_Object = MibTableColumn
cienaCesOamErrFramePeriodWindow = _CienaCesOamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 2),
    _CienaCesOamErrFramePeriodWindow_Type()
)
cienaCesOamErrFramePeriodWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFramePeriodWindow.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamErrFramePeriodWindow.setUnits("frames")


class _CienaCesOamErrFramePeriodThreshold_Type(Unsigned32):
    """Custom type cienaCesOamErrFramePeriodThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_CienaCesOamErrFramePeriodThreshold_Type.__name__ = "Unsigned32"
_CienaCesOamErrFramePeriodThreshold_Object = MibTableColumn
cienaCesOamErrFramePeriodThreshold = _CienaCesOamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 3),
    _CienaCesOamErrFramePeriodThreshold_Type()
)
cienaCesOamErrFramePeriodThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFramePeriodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamErrFramePeriodThreshold.setUnits("frames")


class _CienaCesOamErrFramePeriodEvNotifEnable_Type(Integer32):
    """Custom type cienaCesOamErrFramePeriodEvNotifEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesOamErrFramePeriodEvNotifEnable_Type.__name__ = "Integer32"
_CienaCesOamErrFramePeriodEvNotifEnable_Object = MibTableColumn
cienaCesOamErrFramePeriodEvNotifEnable = _CienaCesOamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 4),
    _CienaCesOamErrFramePeriodEvNotifEnable_Type()
)
cienaCesOamErrFramePeriodEvNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFramePeriodEvNotifEnable.setStatus("current")


class _CienaCesOamErrFrameWindow_Type(Unsigned32):
    """Custom type cienaCesOamErrFrameWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_CienaCesOamErrFrameWindow_Type.__name__ = "Unsigned32"
_CienaCesOamErrFrameWindow_Object = MibTableColumn
cienaCesOamErrFrameWindow = _CienaCesOamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 5),
    _CienaCesOamErrFrameWindow_Type()
)
cienaCesOamErrFrameWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameWindow.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameWindow.setUnits("tenths of a second")


class _CienaCesOamErrFrameThreshold_Type(Unsigned32):
    """Custom type cienaCesOamErrFrameThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_CienaCesOamErrFrameThreshold_Type.__name__ = "Unsigned32"
_CienaCesOamErrFrameThreshold_Object = MibTableColumn
cienaCesOamErrFrameThreshold = _CienaCesOamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 6),
    _CienaCesOamErrFrameThreshold_Type()
)
cienaCesOamErrFrameThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameThreshold.setUnits("frames")


class _CienaCesOamErrFrameEvNotifEnable_Type(Integer32):
    """Custom type cienaCesOamErrFrameEvNotifEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesOamErrFrameEvNotifEnable_Type.__name__ = "Integer32"
_CienaCesOamErrFrameEvNotifEnable_Object = MibTableColumn
cienaCesOamErrFrameEvNotifEnable = _CienaCesOamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 7),
    _CienaCesOamErrFrameEvNotifEnable_Type()
)
cienaCesOamErrFrameEvNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameEvNotifEnable.setStatus("current")


class _CienaCesOamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type cienaCesOamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_CienaCesOamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_CienaCesOamErrFrameSecsSummaryWindow_Object = MibTableColumn
cienaCesOamErrFrameSecsSummaryWindow = _CienaCesOamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 8),
    _CienaCesOamErrFrameSecsSummaryWindow_Type()
)
cienaCesOamErrFrameSecsSummaryWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameSecsSummaryWindow.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameSecsSummaryWindow.setUnits("tenths of a second")


class _CienaCesOamErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type cienaCesOamErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesOamErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_CienaCesOamErrFrameSecsSummaryThreshold_Object = MibTableColumn
cienaCesOamErrFrameSecsSummaryThreshold = _CienaCesOamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 9),
    _CienaCesOamErrFrameSecsSummaryThreshold_Type()
)
cienaCesOamErrFrameSecsSummaryThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameSecsSummaryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameSecsSummaryThreshold.setUnits("errored frame seconds")


class _CienaCesOamErrFrameSecsEvNotifEnable_Type(Integer32):
    """Custom type cienaCesOamErrFrameSecsEvNotifEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesOamErrFrameSecsEvNotifEnable_Type.__name__ = "Integer32"
_CienaCesOamErrFrameSecsEvNotifEnable_Object = MibTableColumn
cienaCesOamErrFrameSecsEvNotifEnable = _CienaCesOamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 10),
    _CienaCesOamErrFrameSecsEvNotifEnable_Type()
)
cienaCesOamErrFrameSecsEvNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamErrFrameSecsEvNotifEnable.setStatus("current")


class _CienaCesOamDyingGaspEnable_Type(Integer32):
    """Custom type cienaCesOamDyingGaspEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesOamDyingGaspEnable_Type.__name__ = "Integer32"
_CienaCesOamDyingGaspEnable_Object = MibTableColumn
cienaCesOamDyingGaspEnable = _CienaCesOamDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 11),
    _CienaCesOamDyingGaspEnable_Type()
)
cienaCesOamDyingGaspEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamDyingGaspEnable.setStatus("current")


class _CienaCesOamCriticalEventEnable_Type(Integer32):
    """Custom type cienaCesOamCriticalEventEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesOamCriticalEventEnable_Type.__name__ = "Integer32"
_CienaCesOamCriticalEventEnable_Object = MibTableColumn
cienaCesOamCriticalEventEnable = _CienaCesOamCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 1, 8, 1, 12),
    _CienaCesOamCriticalEventEnable_Type()
)
cienaCesOamCriticalEventEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOamCriticalEventEnable.setStatus("current")
_CienaCesOamConformance_ObjectIdentity = ObjectIdentity
cienaCesOamConformance = _CienaCesOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 2)
)
_CienaCesOamCompliances_ObjectIdentity = ObjectIdentity
cienaCesOamCompliances = _CienaCesOamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 2, 1)
)
_CienaCesOamGroups_ObjectIdentity = ObjectIdentity
cienaCesOamGroups = _CienaCesOamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 5, 1, 2, 2)
)

# Managed Objects groups


# Notification objects

cienaCesOamLinkEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 15, 0, 1)
)
cienaCesOamLinkEventTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-OAM-MIB", "cienaCesOamEventNotifChassisIndex"),
        ("CIENA-CES-OAM-MIB", "cienaCesOamEventNotifShelfIndex"),
        ("CIENA-CES-OAM-MIB", "cienaCesOamEventNotifSlotIndex"),
        ("CIENA-CES-OAM-MIB", "cienaCesOamEventNotifPortNumber"),
        ("CIENA-CES-OAM-MIB", "cienaCesOamEventLogType"),
        ("CIENA-CES-OAM-MIB", "cienaCesOamEventLogLocation"),
        ("CIENA-CES-OAM-MIB", "cienaCesOamEventNotifChannelNumber"))
)
if mibBuilder.loadTexts:
    cienaCesOamLinkEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-OAM-MIB",
    **{"cienaCesOamNotifMIBNotificationPrefix": cienaCesOamNotifMIBNotificationPrefix,
       "cienaCesOamNotifMIBNotification": cienaCesOamNotifMIBNotification,
       "cienaCesOamLinkEventTrap": cienaCesOamLinkEventTrap,
       "cienaCesOamMibModule": cienaCesOamMibModule,
       "cienaCesOamMIB": cienaCesOamMIB,
       "cienaCesOamStatistics": cienaCesOamStatistics,
       "cienaCesOamStatsTable": cienaCesOamStatsTable,
       "cienaCesOamStatsEntry": cienaCesOamStatsEntry,
       "cienaCesOamInformationTx": cienaCesOamInformationTx,
       "cienaCesOamInformationRx": cienaCesOamInformationRx,
       "cienaCesOamUniqueEventNotificationTx": cienaCesOamUniqueEventNotificationTx,
       "cienaCesOamUniqueEventNotificationRx": cienaCesOamUniqueEventNotificationRx,
       "cienaCesOamLoopbackControlTx": cienaCesOamLoopbackControlTx,
       "cienaCesOamLoopbackControlRx": cienaCesOamLoopbackControlRx,
       "cienaCesOamVariableRequestTx": cienaCesOamVariableRequestTx,
       "cienaCesOamVariableRequestRx": cienaCesOamVariableRequestRx,
       "cienaCesOamVariableResponseTx": cienaCesOamVariableResponseTx,
       "cienaCesOamVariableResponseRx": cienaCesOamVariableResponseRx,
       "cienaCesOamOrgSpecificTx": cienaCesOamOrgSpecificTx,
       "cienaCesOamOrgSpecificRx": cienaCesOamOrgSpecificRx,
       "cienaCesOamUnsupportedCodesTx": cienaCesOamUnsupportedCodesTx,
       "cienaCesOamUnsupportedCodesRx": cienaCesOamUnsupportedCodesRx,
       "cienaCesOamframesLostDueToOam": cienaCesOamframesLostDueToOam,
       "cienaCesOamStatsPort": cienaCesOamStatsPort,
       "cienaCesOamDuplicateEventNotificationTx": cienaCesOamDuplicateEventNotificationTx,
       "cienaCesOamDuplicateEventNotificationRx": cienaCesOamDuplicateEventNotificationRx,
       "cienaCesOamEventLogTable": cienaCesOamEventLogTable,
       "cienaCesOamEventLogEntry": cienaCesOamEventLogEntry,
       "cienaCesOamEventLogPort": cienaCesOamEventLogPort,
       "cienaCesOamEventLogIndex": cienaCesOamEventLogIndex,
       "cienaCesOamEventLogTimestamp": cienaCesOamEventLogTimestamp,
       "cienaCesOamEventLogOui": cienaCesOamEventLogOui,
       "cienaCesOamEventLogType": cienaCesOamEventLogType,
       "cienaCesOamEventLogLocation": cienaCesOamEventLogLocation,
       "cienaCesOamEventLogWindowHi": cienaCesOamEventLogWindowHi,
       "cienaCesOamEventLogWindowLo": cienaCesOamEventLogWindowLo,
       "cienaCesOamEventLogThresholdHi": cienaCesOamEventLogThresholdHi,
       "cienaCesOamEventLogThresholdLo": cienaCesOamEventLogThresholdLo,
       "cienaCesOamEventLogValue": cienaCesOamEventLogValue,
       "cienaCesOamEventLogRunningTotal": cienaCesOamEventLogRunningTotal,
       "cienaCesOamEventLogEventTotal": cienaCesOamEventLogEventTotal,
       "cienaCesOamEventNotifChassisIndex": cienaCesOamEventNotifChassisIndex,
       "cienaCesOamEventNotifShelfIndex": cienaCesOamEventNotifShelfIndex,
       "cienaCesOamEventNotifSlotIndex": cienaCesOamEventNotifSlotIndex,
       "cienaCesOamEventNotifPortNumber": cienaCesOamEventNotifPortNumber,
       "cienaCesOamEventNotifChannelNumber": cienaCesOamEventNotifChannelNumber,
       "cienaCesOamStatsClear": cienaCesOamStatsClear,
       "cienaCesOamTable": cienaCesOamTable,
       "cienaCesOamEntry": cienaCesOamEntry,
       "cienaCesOamPort": cienaCesOamPort,
       "cienaCesOamAdminState": cienaCesOamAdminState,
       "cienaCesOamOperStatus": cienaCesOamOperStatus,
       "cienaCesOamMode": cienaCesOamMode,
       "cienaCesMaxOamPduSize": cienaCesMaxOamPduSize,
       "cienaCesOamConfigRevision": cienaCesOamConfigRevision,
       "cienaCesOamFunctionsSupported": cienaCesOamFunctionsSupported,
       "cienaCesOamPduTimer": cienaCesOamPduTimer,
       "cienaCesOamLinkLostTimer": cienaCesOamLinkLostTimer,
       "cienaCesOamPeerTable": cienaCesOamPeerTable,
       "cienaCesOamPeerEntry": cienaCesOamPeerEntry,
       "cienaCesOamLocalPort": cienaCesOamLocalPort,
       "cienaCesOamPeerStatus": cienaCesOamPeerStatus,
       "cienaCesOamPeerMacAddress": cienaCesOamPeerMacAddress,
       "cienaCesOamPeerVendorOui": cienaCesOamPeerVendorOui,
       "cienaCesOamPeerVendorInfo": cienaCesOamPeerVendorInfo,
       "cienaCesOamPeerMode": cienaCesOamPeerMode,
       "cienaCesOamPeerMaxOamPduSize": cienaCesOamPeerMaxOamPduSize,
       "cienaCesOamPeerConfigRevision": cienaCesOamPeerConfigRevision,
       "cienaCesOamPeerFunctionsSupported": cienaCesOamPeerFunctionsSupported,
       "cienaCesOamLoopbackTable": cienaCesOamLoopbackTable,
       "cienaCesOamLoopbackEntry": cienaCesOamLoopbackEntry,
       "cienaCesOamLoopbackPort": cienaCesOamLoopbackPort,
       "cienaCesOamLoopbackCommand": cienaCesOamLoopbackCommand,
       "cienaCesOamLoopbackStatus": cienaCesOamLoopbackStatus,
       "cienaCesOamLoopbackIgnoreRx": cienaCesOamLoopbackIgnoreRx,
       "cienaCesOamSystemEnableDisable": cienaCesOamSystemEnableDisable,
       "cienaCesOamEventConfigTable": cienaCesOamEventConfigTable,
       "cienaCesOamEventConfigEntry": cienaCesOamEventConfigEntry,
       "cienaCesOamEventPort": cienaCesOamEventPort,
       "cienaCesOamErrFramePeriodWindow": cienaCesOamErrFramePeriodWindow,
       "cienaCesOamErrFramePeriodThreshold": cienaCesOamErrFramePeriodThreshold,
       "cienaCesOamErrFramePeriodEvNotifEnable": cienaCesOamErrFramePeriodEvNotifEnable,
       "cienaCesOamErrFrameWindow": cienaCesOamErrFrameWindow,
       "cienaCesOamErrFrameThreshold": cienaCesOamErrFrameThreshold,
       "cienaCesOamErrFrameEvNotifEnable": cienaCesOamErrFrameEvNotifEnable,
       "cienaCesOamErrFrameSecsSummaryWindow": cienaCesOamErrFrameSecsSummaryWindow,
       "cienaCesOamErrFrameSecsSummaryThreshold": cienaCesOamErrFrameSecsSummaryThreshold,
       "cienaCesOamErrFrameSecsEvNotifEnable": cienaCesOamErrFrameSecsEvNotifEnable,
       "cienaCesOamDyingGaspEnable": cienaCesOamDyingGaspEnable,
       "cienaCesOamCriticalEventEnable": cienaCesOamCriticalEventEnable,
       "cienaCesOamConformance": cienaCesOamConformance,
       "cienaCesOamCompliances": cienaCesOamCompliances,
       "cienaCesOamGroups": cienaCesOamGroups}
)
