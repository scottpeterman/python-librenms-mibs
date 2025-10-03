# SNMP MIB module (CIENA-CES-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-CFM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:29 2025
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

(cienaCesConfig,
 cienaCesNotifications,
 cienaCesStatistics) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications",
    "cienaCesStatistics")

(CienaGlobalState,
 CienaMacAddress,
 CienaStatsClear) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState",
    "CienaMacAddress",
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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesCfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesCfmMIB.setRevisions(
        ("2017-06-07 00:00",
         "2017-05-03 00:00",
         "2017-05-19 00:00",
         "2017-03-16 00:00",
         "2017-02-23 00:00",
         "2016-10-24 00:00",
         "2016-08-03 00:00",
         "2015-07-27 00:00",
         "2015-05-11 00:00",
         "2015-03-02 00:00",
         "2014-04-10 00:00",
         "2014-01-27 00:00",
         "2014-01-16 00:00",
         "2013-11-05 00:00",
         "2013-10-29 00:00",
         "2011-10-04 00:00",
         "2011-07-26 00:00",
         "2010-12-10 00:00",
         "2010-03-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmDisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )



class CienaCesCfmInterfaceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("subport", 1),
          ("encapPbt", 2),
          ("decapPbt", 3),
          ("pbtService", 4),
          ("mplsVc", 5),
          ("unknown", 99))
    )



class EthType(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )



class CfmFrameLossRatio(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-4"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesCfmMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesCfmMIBObjects = _CienaCesCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1)
)
_CienaCesCfmService_ObjectIdentity = ObjectIdentity
cienaCesCfmService = _CienaCesCfmService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2)
)
_CienaCesCfmServiceTable_Object = MibTable
cienaCesCfmServiceTable = _CienaCesCfmServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmServiceTable.setStatus("current")
_CienaCesCfmServiceEntry_Object = MibTableRow
cienaCesCfmServiceEntry = _CienaCesCfmServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1)
)
cienaCesCfmServiceEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesCfmServiceEntry.setStatus("current")
_CienaCesCfmServiceIndex_Type = Unsigned32
_CienaCesCfmServiceIndex_Object = MibTableColumn
cienaCesCfmServiceIndex = _CienaCesCfmServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 1),
    _CienaCesCfmServiceIndex_Type()
)
cienaCesCfmServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmServiceIndex.setStatus("current")


class _CienaCesCfmServiceType_Type(Integer32):
    """Custom type cienaCesCfmServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("mplsVs", 1),
          ("ethVs", 2),
          ("vlan", 3),
          ("pbtTunnel", 4),
          ("vs", 5),
          ("other", 9))
    )


_CienaCesCfmServiceType_Type.__name__ = "Integer32"
_CienaCesCfmServiceType_Object = MibTableColumn
cienaCesCfmServiceType = _CienaCesCfmServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 2),
    _CienaCesCfmServiceType_Type()
)
cienaCesCfmServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceType.setStatus("current")
_CienaCesCfmServiceValue_Type = Integer32
_CienaCesCfmServiceValue_Object = MibTableColumn
cienaCesCfmServiceValue = _CienaCesCfmServiceValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 3),
    _CienaCesCfmServiceValue_Type()
)
cienaCesCfmServiceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceValue.setStatus("current")
_CienaCesCfmServiceAdminState_Type = CienaGlobalState
_CienaCesCfmServiceAdminState_Object = MibTableColumn
cienaCesCfmServiceAdminState = _CienaCesCfmServiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 4),
    _CienaCesCfmServiceAdminState_Type()
)
cienaCesCfmServiceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceAdminState.setStatus("current")
_CienaCesCfmServiceOperState_Type = CienaGlobalState
_CienaCesCfmServiceOperState_Object = MibTableColumn
cienaCesCfmServiceOperState = _CienaCesCfmServiceOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 5),
    _CienaCesCfmServiceOperState_Type()
)
cienaCesCfmServiceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceOperState.setStatus("current")
_CienaCesCfmServiceName_Type = DisplayString
_CienaCesCfmServiceName_Object = MibTableColumn
cienaCesCfmServiceName = _CienaCesCfmServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 6),
    _CienaCesCfmServiceName_Type()
)
cienaCesCfmServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceName.setStatus("current")
_CienaCesCfmServiceMdLevel_Type = Integer32
_CienaCesCfmServiceMdLevel_Object = MibTableColumn
cienaCesCfmServiceMdLevel = _CienaCesCfmServiceMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 7),
    _CienaCesCfmServiceMdLevel_Type()
)
cienaCesCfmServiceMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceMdLevel.setStatus("current")


class _CienaCesCfmServiceFaultState_Type(CienaGlobalState):
    """Custom type cienaCesCfmServiceFaultState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmServiceFaultState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmServiceFaultState_Object = MibTableColumn
cienaCesCfmServiceFaultState = _CienaCesCfmServiceFaultState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 8),
    _CienaCesCfmServiceFaultState_Type()
)
cienaCesCfmServiceFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceFaultState.setStatus("current")
_CienaCesCfmServiceAlarmTime_Type = Integer32
_CienaCesCfmServiceAlarmTime_Object = MibTableColumn
cienaCesCfmServiceAlarmTime = _CienaCesCfmServiceAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 9),
    _CienaCesCfmServiceAlarmTime_Type()
)
cienaCesCfmServiceAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceAlarmTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmServiceAlarmTime.setUnits("milliseconds")


class _CienaCesCfmServiceCCMInterval_Type(Integer32):
    """Custom type cienaCesCfmServiceCCMInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("i4msecCCM", 1),
          ("i10msecCCM", 2),
          ("i100msecCCM", 3),
          ("i1secCCM", 4),
          ("i10secCCM", 5),
          ("i1minCCM", 6),
          ("i10minCCM", 7),
          ("i3dot33msecCCM", 8))
    )


_CienaCesCfmServiceCCMInterval_Type.__name__ = "Integer32"
_CienaCesCfmServiceCCMInterval_Object = MibTableColumn
cienaCesCfmServiceCCMInterval = _CienaCesCfmServiceCCMInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 10),
    _CienaCesCfmServiceCCMInterval_Type()
)
cienaCesCfmServiceCCMInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceCCMInterval.setStatus("current")


class _CienaCesCfmServiceResetTime_Type(Integer32):
    """Custom type cienaCesCfmServiceResetTime based on Integer32"""
    defaultValue = 3000


_CienaCesCfmServiceResetTime_Type.__name__ = "Integer32"
_CienaCesCfmServiceResetTime_Object = MibTableColumn
cienaCesCfmServiceResetTime = _CienaCesCfmServiceResetTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 11),
    _CienaCesCfmServiceResetTime_Type()
)
cienaCesCfmServiceResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceResetTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmServiceResetTime.setUnits("milliseconds")
_CienaCesCfmServiceLastFaultCCM_Type = CfmDisplayString
_CienaCesCfmServiceLastFaultCCM_Object = MibTableColumn
cienaCesCfmServiceLastFaultCCM = _CienaCesCfmServiceLastFaultCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 12),
    _CienaCesCfmServiceLastFaultCCM_Type()
)
cienaCesCfmServiceLastFaultCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceLastFaultCCM.setStatus("current")
_CienaCesCfmServiceRMEPFailureFlag_Type = TruthValue
_CienaCesCfmServiceRMEPFailureFlag_Object = MibTableColumn
cienaCesCfmServiceRMEPFailureFlag = _CienaCesCfmServiceRMEPFailureFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 13),
    _CienaCesCfmServiceRMEPFailureFlag_Type()
)
cienaCesCfmServiceRMEPFailureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceRMEPFailureFlag.setStatus("current")
_CienaCesCfmServiceCCMErrorFlag_Type = TruthValue
_CienaCesCfmServiceCCMErrorFlag_Object = MibTableColumn
cienaCesCfmServiceCCMErrorFlag = _CienaCesCfmServiceCCMErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 14),
    _CienaCesCfmServiceCCMErrorFlag_Type()
)
cienaCesCfmServiceCCMErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceCCMErrorFlag.setStatus("current")
_CienaCesCfmServiceCrossConnectErrorFlag_Type = TruthValue
_CienaCesCfmServiceCrossConnectErrorFlag_Object = MibTableColumn
cienaCesCfmServiceCrossConnectErrorFlag = _CienaCesCfmServiceCrossConnectErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 15),
    _CienaCesCfmServiceCrossConnectErrorFlag_Type()
)
cienaCesCfmServiceCrossConnectErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceCrossConnectErrorFlag.setStatus("current")
_CienaCesCfmServiceNumMEP_Type = Counter32
_CienaCesCfmServiceNumMEP_Object = MibTableColumn
cienaCesCfmServiceNumMEP = _CienaCesCfmServiceNumMEP_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 16),
    _CienaCesCfmServiceNumMEP_Type()
)
cienaCesCfmServiceNumMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceNumMEP.setStatus("current")
_CienaCesCfmServiceNumRemoteMEP_Type = Counter32
_CienaCesCfmServiceNumRemoteMEP_Object = MibTableColumn
cienaCesCfmServiceNumRemoteMEP = _CienaCesCfmServiceNumRemoteMEP_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 17),
    _CienaCesCfmServiceNumRemoteMEP_Type()
)
cienaCesCfmServiceNumRemoteMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceNumRemoteMEP.setStatus("current")
_CienaCesCfmServiceNumActiveMEP_Type = Counter32
_CienaCesCfmServiceNumActiveMEP_Object = MibTableColumn
cienaCesCfmServiceNumActiveMEP = _CienaCesCfmServiceNumActiveMEP_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 18),
    _CienaCesCfmServiceNumActiveMEP_Type()
)
cienaCesCfmServiceNumActiveMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceNumActiveMEP.setStatus("current")
_CienaCesCfmServiceNextMepId_Type = Unsigned32
_CienaCesCfmServiceNextMepId_Object = MibTableColumn
cienaCesCfmServiceNextMepId = _CienaCesCfmServiceNextMepId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 19),
    _CienaCesCfmServiceNextMepId_Type()
)
cienaCesCfmServiceNextMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceNextMepId.setStatus("current")


class _CienaCesCfmServiceAlarmPriority_Type(Unsigned32):
    """Custom type cienaCesCfmServiceAlarmPriority based on Unsigned32"""
    defaultValue = 3


_CienaCesCfmServiceAlarmPriority_Type.__name__ = "Unsigned32"
_CienaCesCfmServiceAlarmPriority_Object = MibTableColumn
cienaCesCfmServiceAlarmPriority = _CienaCesCfmServiceAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 20),
    _CienaCesCfmServiceAlarmPriority_Type()
)
cienaCesCfmServiceAlarmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceAlarmPriority.setStatus("current")


class _CienaCesCfmServiceNumCCMForFault_Type(Unsigned32):
    """Custom type cienaCesCfmServiceNumCCMForFault based on Unsigned32"""
    defaultValue = 3


_CienaCesCfmServiceNumCCMForFault_Type.__name__ = "Unsigned32"
_CienaCesCfmServiceNumCCMForFault_Object = MibTableColumn
cienaCesCfmServiceNumCCMForFault = _CienaCesCfmServiceNumCCMForFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 21),
    _CienaCesCfmServiceNumCCMForFault_Type()
)
cienaCesCfmServiceNumCCMForFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceNumCCMForFault.setStatus("current")
_CienaCesCfmServiceDMMInterval_Type = Integer32
_CienaCesCfmServiceDMMInterval_Object = MibTableColumn
cienaCesCfmServiceDMMInterval = _CienaCesCfmServiceDMMInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 22),
    _CienaCesCfmServiceDMMInterval_Type()
)
cienaCesCfmServiceDMMInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceDMMInterval.setStatus("current")
_CienaCesCfmServiceLMMInterval_Type = Integer32
_CienaCesCfmServiceLMMInterval_Object = MibTableColumn
cienaCesCfmServiceLMMInterval = _CienaCesCfmServiceLMMInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 23),
    _CienaCesCfmServiceLMMInterval_Type()
)
cienaCesCfmServiceLMMInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceLMMInterval.setStatus("current")


class _CienaCesCfmServiceCCMLossStatsState_Type(CienaGlobalState):
    """Custom type cienaCesCfmServiceCCMLossStatsState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmServiceCCMLossStatsState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmServiceCCMLossStatsState_Object = MibTableColumn
cienaCesCfmServiceCCMLossStatsState = _CienaCesCfmServiceCCMLossStatsState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 24),
    _CienaCesCfmServiceCCMLossStatsState_Type()
)
cienaCesCfmServiceCCMLossStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceCCMLossStatsState.setStatus("current")
_CienaCesCfmServiceCCMLossBucketInterval_Type = Integer32
_CienaCesCfmServiceCCMLossBucketInterval_Object = MibTableColumn
cienaCesCfmServiceCCMLossBucketInterval = _CienaCesCfmServiceCCMLossBucketInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 25),
    _CienaCesCfmServiceCCMLossBucketInterval_Type()
)
cienaCesCfmServiceCCMLossBucketInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceCCMLossBucketInterval.setStatus("current")
_CienaCesCfmServiceY1731_Type = TruthValue
_CienaCesCfmServiceY1731_Object = MibTableColumn
cienaCesCfmServiceY1731 = _CienaCesCfmServiceY1731_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 26),
    _CienaCesCfmServiceY1731_Type()
)
cienaCesCfmServiceY1731.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceY1731.setStatus("current")


class _CienaCesCfmServiceTlvSenderIdType_Type(Integer32):
    """Custom type cienaCesCfmServiceTlvSenderIdType based on Integer32"""
    defaultValue = 2

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
        *(("none", 1),
          ("chassis", 2),
          ("manage", 3),
          ("chassisManage", 4))
    )


_CienaCesCfmServiceTlvSenderIdType_Type.__name__ = "Integer32"
_CienaCesCfmServiceTlvSenderIdType_Object = MibTableColumn
cienaCesCfmServiceTlvSenderIdType = _CienaCesCfmServiceTlvSenderIdType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 27),
    _CienaCesCfmServiceTlvSenderIdType_Type()
)
cienaCesCfmServiceTlvSenderIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceTlvSenderIdType.setStatus("current")


class _CienaCesCfmServiceRMEPHoldTime_Type(Unsigned32):
    """Custom type cienaCesCfmServiceRMEPHoldTime based on Unsigned32"""
    defaultValue = 2500


_CienaCesCfmServiceRMEPHoldTime_Type.__name__ = "Unsigned32"
_CienaCesCfmServiceRMEPHoldTime_Object = MibTableColumn
cienaCesCfmServiceRMEPHoldTime = _CienaCesCfmServiceRMEPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 28),
    _CienaCesCfmServiceRMEPHoldTime_Type()
)
cienaCesCfmServiceRMEPHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceRMEPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmServiceRMEPHoldTime.setUnits("milliseconds")


class _CienaCesCfmServiceCCMTxState_Type(CienaGlobalState):
    """Custom type cienaCesCfmServiceCCMTxState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesCfmServiceCCMTxState_Type.__name__ = "CienaGlobalState"
_CienaCesCfmServiceCCMTxState_Object = MibTableColumn
cienaCesCfmServiceCCMTxState = _CienaCesCfmServiceCCMTxState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 29),
    _CienaCesCfmServiceCCMTxState_Type()
)
cienaCesCfmServiceCCMTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceCCMTxState.setStatus("current")
_CienaCesCfmServicePortStatusFlag_Type = TruthValue
_CienaCesCfmServicePortStatusFlag_Object = MibTableColumn
cienaCesCfmServicePortStatusFlag = _CienaCesCfmServicePortStatusFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 30),
    _CienaCesCfmServicePortStatusFlag_Type()
)
cienaCesCfmServicePortStatusFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServicePortStatusFlag.setStatus("current")
_CienaCesCfmServiceRDIFlag_Type = TruthValue
_CienaCesCfmServiceRDIFlag_Object = MibTableColumn
cienaCesCfmServiceRDIFlag = _CienaCesCfmServiceRDIFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 31),
    _CienaCesCfmServiceRDIFlag_Type()
)
cienaCesCfmServiceRDIFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceRDIFlag.setStatus("current")
_CienaCesCfmServiceInstabilityFlag_Type = TruthValue
_CienaCesCfmServiceInstabilityFlag_Object = MibTableColumn
cienaCesCfmServiceInstabilityFlag = _CienaCesCfmServiceInstabilityFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 32),
    _CienaCesCfmServiceInstabilityFlag_Type()
)
cienaCesCfmServiceInstabilityFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceInstabilityFlag.setStatus("current")
_CienaCesCfmServiceRMEPAging_Type = TruthValue
_CienaCesCfmServiceRMEPAging_Object = MibTableColumn
cienaCesCfmServiceRMEPAging = _CienaCesCfmServiceRMEPAging_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 33),
    _CienaCesCfmServiceRMEPAging_Type()
)
cienaCesCfmServiceRMEPAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceRMEPAging.setStatus("current")
_CienaCesCfmServiceRMEPDiscovery_Type = TruthValue
_CienaCesCfmServiceRMEPDiscovery_Object = MibTableColumn
cienaCesCfmServiceRMEPDiscovery = _CienaCesCfmServiceRMEPDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 34),
    _CienaCesCfmServiceRMEPDiscovery_Type()
)
cienaCesCfmServiceRMEPDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceRMEPDiscovery.setStatus("current")
_CienaCesCfmServiceChargedAgainstGlobalBudget_Type = TruthValue
_CienaCesCfmServiceChargedAgainstGlobalBudget_Object = MibTableColumn
cienaCesCfmServiceChargedAgainstGlobalBudget = _CienaCesCfmServiceChargedAgainstGlobalBudget_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 35),
    _CienaCesCfmServiceChargedAgainstGlobalBudget_Type()
)
cienaCesCfmServiceChargedAgainstGlobalBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceChargedAgainstGlobalBudget.setStatus("current")
_CienaCesCfmServiceControlModuleFrameBudget_Type = Counter32
_CienaCesCfmServiceControlModuleFrameBudget_Object = MibTableColumn
cienaCesCfmServiceControlModuleFrameBudget = _CienaCesCfmServiceControlModuleFrameBudget_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 36),
    _CienaCesCfmServiceControlModuleFrameBudget_Type()
)
cienaCesCfmServiceControlModuleFrameBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceControlModuleFrameBudget.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmServiceControlModuleFrameBudget.setUnits("frames/sec")


class _CienaCesCfmServiceMulticastDa_Type(TruthValue):
    """Custom type cienaCesCfmServiceMulticastDa based on TruthValue"""
    defaultValue = 2


_CienaCesCfmServiceMulticastDa_Type.__name__ = "TruthValue"
_CienaCesCfmServiceMulticastDa_Object = MibTableColumn
cienaCesCfmServiceMulticastDa = _CienaCesCfmServiceMulticastDa_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 37),
    _CienaCesCfmServiceMulticastDa_Type()
)
cienaCesCfmServiceMulticastDa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceMulticastDa.setStatus("current")
_CienaCesCfmServiceCCMRxStats_Type = TruthValue
_CienaCesCfmServiceCCMRxStats_Object = MibTableColumn
cienaCesCfmServiceCCMRxStats = _CienaCesCfmServiceCCMRxStats_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 2, 1, 1, 38),
    _CienaCesCfmServiceCCMRxStats_Type()
)
cienaCesCfmServiceCCMRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceCCMRxStats.setStatus("current")
_CienaCesCfmMEP_ObjectIdentity = ObjectIdentity
cienaCesCfmMEP = _CienaCesCfmMEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3)
)
_CienaCesCfmMEPTable_Object = MibTable
cienaCesCfmMEPTable = _CienaCesCfmMEPTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmMEPTable.setStatus("current")
_CienaCesCfmMEPEntry_Object = MibTableRow
cienaCesCfmMEPEntry = _CienaCesCfmMEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1)
)
cienaCesCfmMEPEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmMEPId"),
)
if mibBuilder.loadTexts:
    cienaCesCfmMEPEntry.setStatus("current")
_CienaCesCfmMEPId_Type = Unsigned32
_CienaCesCfmMEPId_Object = MibTableColumn
cienaCesCfmMEPId = _CienaCesCfmMEPId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 1),
    _CienaCesCfmMEPId_Type()
)
cienaCesCfmMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmMEPId.setStatus("current")
_CienaCesCfmMEPMacAddr_Type = MacAddress
_CienaCesCfmMEPMacAddr_Object = MibTableColumn
cienaCesCfmMEPMacAddr = _CienaCesCfmMEPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 2),
    _CienaCesCfmMEPMacAddr_Type()
)
cienaCesCfmMEPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPMacAddr.setStatus("current")
_CienaCesCfmMEPAdminState_Type = CienaGlobalState
_CienaCesCfmMEPAdminState_Object = MibTableColumn
cienaCesCfmMEPAdminState = _CienaCesCfmMEPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 3),
    _CienaCesCfmMEPAdminState_Type()
)
cienaCesCfmMEPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPAdminState.setStatus("current")
_CienaCesCfmMEPOperState_Type = CienaGlobalState
_CienaCesCfmMEPOperState_Object = MibTableColumn
cienaCesCfmMEPOperState = _CienaCesCfmMEPOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 4),
    _CienaCesCfmMEPOperState_Type()
)
cienaCesCfmMEPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPOperState.setStatus("current")


class _CienaCesCfmMEPDirection_Type(Integer32):
    """Custom type cienaCesCfmMEPDirection based on Integer32"""
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


_CienaCesCfmMEPDirection_Type.__name__ = "Integer32"
_CienaCesCfmMEPDirection_Object = MibTableColumn
cienaCesCfmMEPDirection = _CienaCesCfmMEPDirection_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 5),
    _CienaCesCfmMEPDirection_Type()
)
cienaCesCfmMEPDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPDirection.setStatus("current")
_CienaCesCfmMEPCCMState_Type = CienaGlobalState
_CienaCesCfmMEPCCMState_Object = MibTableColumn
cienaCesCfmMEPCCMState = _CienaCesCfmMEPCCMState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 6),
    _CienaCesCfmMEPCCMState_Type()
)
cienaCesCfmMEPCCMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPCCMState.setStatus("current")
_CienaCesCfmMEPCCMPriority_Type = Integer32
_CienaCesCfmMEPCCMPriority_Object = MibTableColumn
cienaCesCfmMEPCCMPriority = _CienaCesCfmMEPCCMPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 7),
    _CienaCesCfmMEPCCMPriority_Type()
)
cienaCesCfmMEPCCMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPCCMPriority.setStatus("current")
_CienaCesCfmMEPLTMPriority_Type = Integer32
_CienaCesCfmMEPLTMPriority_Object = MibTableColumn
cienaCesCfmMEPLTMPriority = _CienaCesCfmMEPLTMPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 8),
    _CienaCesCfmMEPLTMPriority_Type()
)
cienaCesCfmMEPLTMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPLTMPriority.setStatus("current")


class _CienaCesCfmMEPLiType_Type(Integer32):
    """Custom type cienaCesCfmMEPLiType based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("vs", 1),
          ("pbtService", 2),
          ("mplsStaticPeMeshVC", 3),
          ("mplsDynamicPeMeshVC", 4),
          ("mplsStaticPeSpokeVC", 5),
          ("mplsDynamicPeSpokeVC", 6),
          ("mplsStaticMtuSpokeVC", 7),
          ("mplsDynamicMtuSpokeVC", 8),
          ("none", 99))
    )


_CienaCesCfmMEPLiType_Type.__name__ = "Integer32"
_CienaCesCfmMEPLiType_Object = MibTableColumn
cienaCesCfmMEPLiType = _CienaCesCfmMEPLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 9),
    _CienaCesCfmMEPLiType_Type()
)
cienaCesCfmMEPLiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPLiType.setStatus("current")
_CienaCesCfmMEPLiIndex_Type = Unsigned32
_CienaCesCfmMEPLiIndex_Object = MibTableColumn
cienaCesCfmMEPLiIndex = _CienaCesCfmMEPLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 10),
    _CienaCesCfmMEPLiIndex_Type()
)
cienaCesCfmMEPLiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPLiIndex.setStatus("current")
_CienaCesCfmMEPServiceName_Type = DisplayString
_CienaCesCfmMEPServiceName_Object = MibTableColumn
cienaCesCfmMEPServiceName = _CienaCesCfmMEPServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 11),
    _CienaCesCfmMEPServiceName_Type()
)
cienaCesCfmMEPServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPServiceName.setStatus("current")
_CienaCesCfmMEPSubPortName_Type = DisplayString
_CienaCesCfmMEPSubPortName_Object = MibTableColumn
cienaCesCfmMEPSubPortName = _CienaCesCfmMEPSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 12),
    _CienaCesCfmMEPSubPortName_Type()
)
cienaCesCfmMEPSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPSubPortName.setStatus("current")
_CienaCesCfmMEPVsPbtName_Type = DisplayString
_CienaCesCfmMEPVsPbtName_Object = MibTableColumn
cienaCesCfmMEPVsPbtName = _CienaCesCfmMEPVsPbtName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 13),
    _CienaCesCfmMEPVsPbtName_Type()
)
cienaCesCfmMEPVsPbtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPVsPbtName.setStatus("current")
_CienaCesCfmMEPLogicalPortName_Type = DisplayString
_CienaCesCfmMEPLogicalPortName_Object = MibTableColumn
cienaCesCfmMEPLogicalPortName = _CienaCesCfmMEPLogicalPortName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 14),
    _CienaCesCfmMEPLogicalPortName_Type()
)
cienaCesCfmMEPLogicalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPLogicalPortName.setStatus("current")
_CienaCesCfmMEPSubPortIndex_Type = Unsigned32
_CienaCesCfmMEPSubPortIndex_Object = MibTableColumn
cienaCesCfmMEPSubPortIndex = _CienaCesCfmMEPSubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 15),
    _CienaCesCfmMEPSubPortIndex_Type()
)
cienaCesCfmMEPSubPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPSubPortIndex.setStatus("current")


class _CienaCesCfmMEPEncapsulation_Type(Integer32):
    """Custom type cienaCesCfmMEPEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot1d", 1),
          ("pbtCfmEncap", 2))
    )


_CienaCesCfmMEPEncapsulation_Type.__name__ = "Integer32"
_CienaCesCfmMEPEncapsulation_Object = MibTableColumn
cienaCesCfmMEPEncapsulation = _CienaCesCfmMEPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 16),
    _CienaCesCfmMEPEncapsulation_Type()
)
cienaCesCfmMEPEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPEncapsulation.setStatus("current")
_CienaCesCfmMEPLeadPortSlotIndex_Type = Unsigned32
_CienaCesCfmMEPLeadPortSlotIndex_Object = MibTableColumn
cienaCesCfmMEPLeadPortSlotIndex = _CienaCesCfmMEPLeadPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 17),
    _CienaCesCfmMEPLeadPortSlotIndex_Type()
)
cienaCesCfmMEPLeadPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPLeadPortSlotIndex.setStatus("current")
_CienaCesCfmMEPPBTBvid_Type = Unsigned32
_CienaCesCfmMEPPBTBvid_Object = MibTableColumn
cienaCesCfmMEPPBTBvid = _CienaCesCfmMEPPBTBvid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 18),
    _CienaCesCfmMEPPBTBvid_Type()
)
cienaCesCfmMEPPBTBvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPPBTBvid.setStatus("current")
_CienaCesCfmMEPPBTEtype_Type = Unsigned32
_CienaCesCfmMEPPBTEtype_Object = MibTableColumn
cienaCesCfmMEPPBTEtype = _CienaCesCfmMEPPBTEtype_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 19),
    _CienaCesCfmMEPPBTEtype_Type()
)
cienaCesCfmMEPPBTEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPPBTEtype.setStatus("current")


class _CienaCesCfmMEPL2XformType_Type(Integer32):
    """Custom type cienaCesCfmMEPL2XformType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-op", 1),
          ("auto", 2))
    )


_CienaCesCfmMEPL2XformType_Type.__name__ = "Integer32"
_CienaCesCfmMEPL2XformType_Object = MibTableColumn
cienaCesCfmMEPL2XformType = _CienaCesCfmMEPL2XformType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 20),
    _CienaCesCfmMEPL2XformType_Type()
)
cienaCesCfmMEPL2XformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPL2XformType.setStatus("current")


class _CienaCesCfmMEPSignalDegradeMonitoringStatus_Type(TruthValue):
    """Custom type cienaCesCfmMEPSignalDegradeMonitoringStatus based on TruthValue"""
    defaultValue = 2


_CienaCesCfmMEPSignalDegradeMonitoringStatus_Type.__name__ = "TruthValue"
_CienaCesCfmMEPSignalDegradeMonitoringStatus_Object = MibTableColumn
cienaCesCfmMEPSignalDegradeMonitoringStatus = _CienaCesCfmMEPSignalDegradeMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 21),
    _CienaCesCfmMEPSignalDegradeMonitoringStatus_Type()
)
cienaCesCfmMEPSignalDegradeMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPSignalDegradeMonitoringStatus.setStatus("current")


class _CienaCesCfmMEPSignalDegradeTriggerMode_Type(Integer32):
    """Custom type cienaCesCfmMEPSignalDegradeTriggerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nearEnd", 1),
          ("nearFarEnd", 2))
    )


_CienaCesCfmMEPSignalDegradeTriggerMode_Type.__name__ = "Integer32"
_CienaCesCfmMEPSignalDegradeTriggerMode_Object = MibTableColumn
cienaCesCfmMEPSignalDegradeTriggerMode = _CienaCesCfmMEPSignalDegradeTriggerMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 3, 1, 1, 22),
    _CienaCesCfmMEPSignalDegradeTriggerMode_Type()
)
cienaCesCfmMEPSignalDegradeTriggerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPSignalDegradeTriggerMode.setStatus("current")
_CienaCesCfmRemoteMEP_ObjectIdentity = ObjectIdentity
cienaCesCfmRemoteMEP = _CienaCesCfmRemoteMEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4)
)
_CienaCesCfmRemoteMEPTable_Object = MibTable
cienaCesCfmRemoteMEPTable = _CienaCesCfmRemoteMEPTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPTable.setStatus("current")
_CienaCesCfmRemoteMEPEntry_Object = MibTableRow
cienaCesCfmRemoteMEPEntry = _CienaCesCfmRemoteMEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1)
)
cienaCesCfmRemoteMEPEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmRemoteMEPID"),
)
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPEntry.setStatus("current")
_CienaCesCfmRemoteMEPID_Type = Unsigned32
_CienaCesCfmRemoteMEPID_Object = MibTableColumn
cienaCesCfmRemoteMEPID = _CienaCesCfmRemoteMEPID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 1),
    _CienaCesCfmRemoteMEPID_Type()
)
cienaCesCfmRemoteMEPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPID.setStatus("current")
_CienaCesCfmRemoteMEPMacAddr_Type = MacAddress
_CienaCesCfmRemoteMEPMacAddr_Object = MibTableColumn
cienaCesCfmRemoteMEPMacAddr = _CienaCesCfmRemoteMEPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 2),
    _CienaCesCfmRemoteMEPMacAddr_Type()
)
cienaCesCfmRemoteMEPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPMacAddr.setStatus("current")
_CienaCesCfmRemoteMEPAdminState_Type = CienaGlobalState
_CienaCesCfmRemoteMEPAdminState_Object = MibTableColumn
cienaCesCfmRemoteMEPAdminState = _CienaCesCfmRemoteMEPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 3),
    _CienaCesCfmRemoteMEPAdminState_Type()
)
cienaCesCfmRemoteMEPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPAdminState.setStatus("current")


class _CienaCesCfmRemoteMEPOperState_Type(Integer32):
    """Custom type cienaCesCfmRemoteMEPOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("hold", 3))
    )


_CienaCesCfmRemoteMEPOperState_Type.__name__ = "Integer32"
_CienaCesCfmRemoteMEPOperState_Object = MibTableColumn
cienaCesCfmRemoteMEPOperState = _CienaCesCfmRemoteMEPOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 4),
    _CienaCesCfmRemoteMEPOperState_Type()
)
cienaCesCfmRemoteMEPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPOperState.setStatus("current")
_CienaCesCfmRemoteMEPTime_Type = TimeTicks
_CienaCesCfmRemoteMEPTime_Object = MibTableColumn
cienaCesCfmRemoteMEPTime = _CienaCesCfmRemoteMEPTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 5),
    _CienaCesCfmRemoteMEPTime_Type()
)
cienaCesCfmRemoteMEPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPTime.setStatus("current")
_CienaCesCfmRemoteMEPKLastMacStatus_Type = TruthValue
_CienaCesCfmRemoteMEPKLastMacStatus_Object = MibTableColumn
cienaCesCfmRemoteMEPKLastMacStatus = _CienaCesCfmRemoteMEPKLastMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 6),
    _CienaCesCfmRemoteMEPKLastMacStatus_Type()
)
cienaCesCfmRemoteMEPKLastMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPKLastMacStatus.setStatus("current")
_CienaCesCfmRemoteMEPFailureFlag_Type = TruthValue
_CienaCesCfmRemoteMEPFailureFlag_Object = MibTableColumn
cienaCesCfmRemoteMEPFailureFlag = _CienaCesCfmRemoteMEPFailureFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 7),
    _CienaCesCfmRemoteMEPFailureFlag_Type()
)
cienaCesCfmRemoteMEPFailureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPFailureFlag.setStatus("current")
_CienaCesCfmRemoteMEPCCMErrorFlag_Type = TruthValue
_CienaCesCfmRemoteMEPCCMErrorFlag_Object = MibTableColumn
cienaCesCfmRemoteMEPCCMErrorFlag = _CienaCesCfmRemoteMEPCCMErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 8),
    _CienaCesCfmRemoteMEPCCMErrorFlag_Type()
)
cienaCesCfmRemoteMEPCCMErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPCCMErrorFlag.setStatus("current")
_CienaCesCfmRemoteMEPRDIErrorFlag_Type = TruthValue
_CienaCesCfmRemoteMEPRDIErrorFlag_Object = MibTableColumn
cienaCesCfmRemoteMEPRDIErrorFlag = _CienaCesCfmRemoteMEPRDIErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 9),
    _CienaCesCfmRemoteMEPRDIErrorFlag_Type()
)
cienaCesCfmRemoteMEPRDIErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPRDIErrorFlag.setStatus("current")
_CienaCesCfmRemoteMEPSubPortName_Type = DisplayString
_CienaCesCfmRemoteMEPSubPortName_Object = MibTableColumn
cienaCesCfmRemoteMEPSubPortName = _CienaCesCfmRemoteMEPSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 10),
    _CienaCesCfmRemoteMEPSubPortName_Type()
)
cienaCesCfmRemoteMEPSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPSubPortName.setStatus("current")
_CienaCesCfmRemoteMEPServiceName_Type = DisplayString
_CienaCesCfmRemoteMEPServiceName_Object = MibTableColumn
cienaCesCfmRemoteMEPServiceName = _CienaCesCfmRemoteMEPServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 11),
    _CienaCesCfmRemoteMEPServiceName_Type()
)
cienaCesCfmRemoteMEPServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPServiceName.setStatus("current")


class _CienaCesCfmRemoteMEPLastPortStatus_Type(Integer32):
    """Custom type cienaCesCfmRemoteMEPLastPortStatus based on Integer32"""
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
        *(("unknown", 1),
          ("none", 2),
          ("blocked", 3),
          ("up", 4))
    )


_CienaCesCfmRemoteMEPLastPortStatus_Type.__name__ = "Integer32"
_CienaCesCfmRemoteMEPLastPortStatus_Object = MibTableColumn
cienaCesCfmRemoteMEPLastPortStatus = _CienaCesCfmRemoteMEPLastPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 12),
    _CienaCesCfmRemoteMEPLastPortStatus_Type()
)
cienaCesCfmRemoteMEPLastPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPLastPortStatus.setStatus("current")


class _CienaCesCfmRemoteMEPLastInterfaceStatus_Type(Integer32):
    """Custom type cienaCesCfmRemoteMEPLastInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("up", 2),
          ("down", 3),
          ("testing", 4),
          ("dormant", 5),
          ("lowerLayerDown", 6),
          ("notPresent", 7))
    )


_CienaCesCfmRemoteMEPLastInterfaceStatus_Type.__name__ = "Integer32"
_CienaCesCfmRemoteMEPLastInterfaceStatus_Object = MibTableColumn
cienaCesCfmRemoteMEPLastInterfaceStatus = _CienaCesCfmRemoteMEPLastInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 13),
    _CienaCesCfmRemoteMEPLastInterfaceStatus_Type()
)
cienaCesCfmRemoteMEPLastInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPLastInterfaceStatus.setStatus("current")
_CienaCesCfmRemoteMEPCCMLevel_Type = Integer32
_CienaCesCfmRemoteMEPCCMLevel_Object = MibTableColumn
cienaCesCfmRemoteMEPCCMLevel = _CienaCesCfmRemoteMEPCCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 14),
    _CienaCesCfmRemoteMEPCCMLevel_Type()
)
cienaCesCfmRemoteMEPCCMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPCCMLevel.setStatus("current")


class _CienaCesCfmRemoteMEPHoldState_Type(Integer32):
    """Custom type cienaCesCfmRemoteMEPHoldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("lock", 3))
    )


_CienaCesCfmRemoteMEPHoldState_Type.__name__ = "Integer32"
_CienaCesCfmRemoteMEPHoldState_Object = MibTableColumn
cienaCesCfmRemoteMEPHoldState = _CienaCesCfmRemoteMEPHoldState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 4, 1, 1, 15),
    _CienaCesCfmRemoteMEPHoldState_Type()
)
cienaCesCfmRemoteMEPHoldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMEPHoldState.setStatus("current")
_CienaCesCfmDelay_ObjectIdentity = ObjectIdentity
cienaCesCfmDelay = _CienaCesCfmDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5)
)
_CienaCesCfmDelayMsgTable_Object = MibTable
cienaCesCfmDelayMsgTable = _CienaCesCfmDelayMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgTable.setStatus("current")
_CienaCesCfmDelayMsgEntry_Object = MibTableRow
cienaCesCfmDelayMsgEntry = _CienaCesCfmDelayMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1)
)
cienaCesCfmDelayMsgEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
)
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgEntry.setStatus("current")
_CienaCesCfmDelayMsgLocalMEPId_Type = Integer32
_CienaCesCfmDelayMsgLocalMEPId_Object = MibTableColumn
cienaCesCfmDelayMsgLocalMEPId = _CienaCesCfmDelayMsgLocalMEPId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 1),
    _CienaCesCfmDelayMsgLocalMEPId_Type()
)
cienaCesCfmDelayMsgLocalMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgLocalMEPId.setStatus("current")


class _CienaCesCfmDelayMsgTargetMEPID_Type(Unsigned32):
    """Custom type cienaCesCfmDelayMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_CienaCesCfmDelayMsgTargetMEPID_Type.__name__ = "Unsigned32"
_CienaCesCfmDelayMsgTargetMEPID_Object = MibTableColumn
cienaCesCfmDelayMsgTargetMEPID = _CienaCesCfmDelayMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 2),
    _CienaCesCfmDelayMsgTargetMEPID_Type()
)
cienaCesCfmDelayMsgTargetMEPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgTargetMEPID.setStatus("current")


class _CienaCesCfmDelayMsgServiceName_Type(DisplayString):
    """Custom type cienaCesCfmDelayMsgServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesCfmDelayMsgServiceName_Type.__name__ = "DisplayString"
_CienaCesCfmDelayMsgServiceName_Object = MibTableColumn
cienaCesCfmDelayMsgServiceName = _CienaCesCfmDelayMsgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 3),
    _CienaCesCfmDelayMsgServiceName_Type()
)
cienaCesCfmDelayMsgServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgServiceName.setStatus("current")


class _CienaCesCfmDelayMsgAverageDelayThreshold_Type(Integer32):
    """Custom type cienaCesCfmDelayMsgAverageDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesCfmDelayMsgAverageDelayThreshold_Type.__name__ = "Integer32"
_CienaCesCfmDelayMsgAverageDelayThreshold_Object = MibTableColumn
cienaCesCfmDelayMsgAverageDelayThreshold = _CienaCesCfmDelayMsgAverageDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 4),
    _CienaCesCfmDelayMsgAverageDelayThreshold_Type()
)
cienaCesCfmDelayMsgAverageDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageDelayThreshold.setStatus("current")


class _CienaCesCfmDelayMsgAverageJitterThreshold_Type(Integer32):
    """Custom type cienaCesCfmDelayMsgAverageJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesCfmDelayMsgAverageJitterThreshold_Type.__name__ = "Integer32"
_CienaCesCfmDelayMsgAverageJitterThreshold_Object = MibTableColumn
cienaCesCfmDelayMsgAverageJitterThreshold = _CienaCesCfmDelayMsgAverageJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 5),
    _CienaCesCfmDelayMsgAverageJitterThreshold_Type()
)
cienaCesCfmDelayMsgAverageJitterThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageJitterThreshold.setStatus("current")


class _CienaCesCfmDelayMsgMaximumDelayThreshold_Type(Integer32):
    """Custom type cienaCesCfmDelayMsgMaximumDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesCfmDelayMsgMaximumDelayThreshold_Type.__name__ = "Integer32"
_CienaCesCfmDelayMsgMaximumDelayThreshold_Object = MibTableColumn
cienaCesCfmDelayMsgMaximumDelayThreshold = _CienaCesCfmDelayMsgMaximumDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 6),
    _CienaCesCfmDelayMsgMaximumDelayThreshold_Type()
)
cienaCesCfmDelayMsgMaximumDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumDelayThreshold.setStatus("current")


class _CienaCesCfmDelayMsgMaximumJitterThreshold_Type(Integer32):
    """Custom type cienaCesCfmDelayMsgMaximumJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesCfmDelayMsgMaximumJitterThreshold_Type.__name__ = "Integer32"
_CienaCesCfmDelayMsgMaximumJitterThreshold_Object = MibTableColumn
cienaCesCfmDelayMsgMaximumJitterThreshold = _CienaCesCfmDelayMsgMaximumJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 7),
    _CienaCesCfmDelayMsgMaximumJitterThreshold_Type()
)
cienaCesCfmDelayMsgMaximumJitterThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumJitterThreshold.setStatus("current")
_CienaCesCfmDelayMsgAverageDelay_Type = Unsigned32
_CienaCesCfmDelayMsgAverageDelay_Object = MibTableColumn
cienaCesCfmDelayMsgAverageDelay = _CienaCesCfmDelayMsgAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 8),
    _CienaCesCfmDelayMsgAverageDelay_Type()
)
cienaCesCfmDelayMsgAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageDelay.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageDelay.setUnits("microseconds")
_CienaCesCfmDelayMsgAverageJitter_Type = Unsigned32
_CienaCesCfmDelayMsgAverageJitter_Object = MibTableColumn
cienaCesCfmDelayMsgAverageJitter = _CienaCesCfmDelayMsgAverageJitter_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 9),
    _CienaCesCfmDelayMsgAverageJitter_Type()
)
cienaCesCfmDelayMsgAverageJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageJitter.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageJitter.setUnits("microseconds")
_CienaCesCfmDelayMsgMaximumDelay_Type = Unsigned32
_CienaCesCfmDelayMsgMaximumDelay_Object = MibTableColumn
cienaCesCfmDelayMsgMaximumDelay = _CienaCesCfmDelayMsgMaximumDelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 10),
    _CienaCesCfmDelayMsgMaximumDelay_Type()
)
cienaCesCfmDelayMsgMaximumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumDelay.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumDelay.setUnits("microseconds")
_CienaCesCfmDelayMsgMaximumJitter_Type = Unsigned32
_CienaCesCfmDelayMsgMaximumJitter_Object = MibTableColumn
cienaCesCfmDelayMsgMaximumJitter = _CienaCesCfmDelayMsgMaximumJitter_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 11),
    _CienaCesCfmDelayMsgMaximumJitter_Type()
)
cienaCesCfmDelayMsgMaximumJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumJitter.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumJitter.setUnits("microseconds")
_CienaCesCfmDelayMsgMinimumDelay_Type = Unsigned32
_CienaCesCfmDelayMsgMinimumDelay_Object = MibTableColumn
cienaCesCfmDelayMsgMinimumDelay = _CienaCesCfmDelayMsgMinimumDelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 12),
    _CienaCesCfmDelayMsgMinimumDelay_Type()
)
cienaCesCfmDelayMsgMinimumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMinimumDelay.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMinimumDelay.setUnits("microseconds")
_CienaCesCfmDelayMsgMinimumJitter_Type = Unsigned32
_CienaCesCfmDelayMsgMinimumJitter_Object = MibTableColumn
cienaCesCfmDelayMsgMinimumJitter = _CienaCesCfmDelayMsgMinimumJitter_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 13),
    _CienaCesCfmDelayMsgMinimumJitter_Type()
)
cienaCesCfmDelayMsgMinimumJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMinimumJitter.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMinimumJitter.setUnits("microseconds")
_CienaCesCfmDelayMsgAverageDelayVariation_Type = Unsigned32
_CienaCesCfmDelayMsgAverageDelayVariation_Object = MibTableColumn
cienaCesCfmDelayMsgAverageDelayVariation = _CienaCesCfmDelayMsgAverageDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 14),
    _CienaCesCfmDelayMsgAverageDelayVariation_Type()
)
cienaCesCfmDelayMsgAverageDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageDelayVariation.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageDelayVariation.setUnits("microseconds")
_CienaCesCfmDelayMsgMaximumDelayVariation_Type = Unsigned32
_CienaCesCfmDelayMsgMaximumDelayVariation_Object = MibTableColumn
cienaCesCfmDelayMsgMaximumDelayVariation = _CienaCesCfmDelayMsgMaximumDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 15),
    _CienaCesCfmDelayMsgMaximumDelayVariation_Type()
)
cienaCesCfmDelayMsgMaximumDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumDelayVariation.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumDelayVariation.setUnits("microseconds")
_CienaCesCfmDelayMsgMinimumDelayVariation_Type = Unsigned32
_CienaCesCfmDelayMsgMinimumDelayVariation_Object = MibTableColumn
cienaCesCfmDelayMsgMinimumDelayVariation = _CienaCesCfmDelayMsgMinimumDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 16),
    _CienaCesCfmDelayMsgMinimumDelayVariation_Type()
)
cienaCesCfmDelayMsgMinimumDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMinimumDelayVariation.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMinimumDelayVariation.setUnits("microseconds")


class _CienaCesCfmDelayMsgAverageDelayVariationThreshold_Type(Integer32):
    """Custom type cienaCesCfmDelayMsgAverageDelayVariationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CienaCesCfmDelayMsgAverageDelayVariationThreshold_Type.__name__ = "Integer32"
_CienaCesCfmDelayMsgAverageDelayVariationThreshold_Object = MibTableColumn
cienaCesCfmDelayMsgAverageDelayVariationThreshold = _CienaCesCfmDelayMsgAverageDelayVariationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 17),
    _CienaCesCfmDelayMsgAverageDelayVariationThreshold_Type()
)
cienaCesCfmDelayMsgAverageDelayVariationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageDelayVariationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgAverageDelayVariationThreshold.setUnits("microseconds")


class _CienaCesCfmDelayMsgMaximumDelayVariationThreshold_Type(Integer32):
    """Custom type cienaCesCfmDelayMsgMaximumDelayVariationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CienaCesCfmDelayMsgMaximumDelayVariationThreshold_Type.__name__ = "Integer32"
_CienaCesCfmDelayMsgMaximumDelayVariationThreshold_Object = MibTableColumn
cienaCesCfmDelayMsgMaximumDelayVariationThreshold = _CienaCesCfmDelayMsgMaximumDelayVariationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 18),
    _CienaCesCfmDelayMsgMaximumDelayVariationThreshold_Type()
)
cienaCesCfmDelayMsgMaximumDelayVariationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumDelayVariationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgMaximumDelayVariationThreshold.setUnits("microseconds")


class _CienaCesCfmDelayMsgPriority_Type(Unsigned32):
    """Custom type cienaCesCfmDelayMsgPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesCfmDelayMsgPriority_Type.__name__ = "Unsigned32"
_CienaCesCfmDelayMsgPriority_Object = MibTableColumn
cienaCesCfmDelayMsgPriority = _CienaCesCfmDelayMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 19),
    _CienaCesCfmDelayMsgPriority_Type()
)
cienaCesCfmDelayMsgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgPriority.setStatus("current")


class _CienaCesCfmDelayMsgCount_Type(Unsigned32):
    """Custom type cienaCesCfmDelayMsgCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_CienaCesCfmDelayMsgCount_Type.__name__ = "Unsigned32"
_CienaCesCfmDelayMsgCount_Object = MibTableColumn
cienaCesCfmDelayMsgCount = _CienaCesCfmDelayMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 20),
    _CienaCesCfmDelayMsgCount_Type()
)
cienaCesCfmDelayMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgCount.setStatus("current")


class _CienaCesCfmDelayMsgIterations_Type(Unsigned32):
    """Custom type cienaCesCfmDelayMsgIterations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CienaCesCfmDelayMsgIterations_Type.__name__ = "Unsigned32"
_CienaCesCfmDelayMsgIterations_Object = MibTableColumn
cienaCesCfmDelayMsgIterations = _CienaCesCfmDelayMsgIterations_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 21),
    _CienaCesCfmDelayMsgIterations_Type()
)
cienaCesCfmDelayMsgIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgIterations.setStatus("current")


class _CienaCesCfmDelayMsgRepeatDelay_Type(Unsigned32):
    """Custom type cienaCesCfmDelayMsgRepeatDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CienaCesCfmDelayMsgRepeatDelay_Type.__name__ = "Unsigned32"
_CienaCesCfmDelayMsgRepeatDelay_Object = MibTableColumn
cienaCesCfmDelayMsgRepeatDelay = _CienaCesCfmDelayMsgRepeatDelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 22),
    _CienaCesCfmDelayMsgRepeatDelay_Type()
)
cienaCesCfmDelayMsgRepeatDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgRepeatDelay.setStatus("current")


class _CienaCesCfmDelayMsgDuration_Type(Unsigned32):
    """Custom type cienaCesCfmDelayMsgDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesCfmDelayMsgDuration_Type.__name__ = "Unsigned32"
_CienaCesCfmDelayMsgDuration_Object = MibTableColumn
cienaCesCfmDelayMsgDuration = _CienaCesCfmDelayMsgDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 5, 1, 1, 23),
    _CienaCesCfmDelayMsgDuration_Type()
)
cienaCesCfmDelayMsgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmDelayMsgDuration.setStatus("current")
_CienaCesCfmFrameLoss_ObjectIdentity = ObjectIdentity
cienaCesCfmFrameLoss = _CienaCesCfmFrameLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6)
)
_CienaCesCfmFrameLossMsgTable_Object = MibTable
cienaCesCfmFrameLossMsgTable = _CienaCesCfmFrameLossMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgTable.setStatus("current")
_CienaCesCfmFrameLossMsgEntry_Object = MibTableRow
cienaCesCfmFrameLossMsgEntry = _CienaCesCfmFrameLossMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1, 1)
)
cienaCesCfmFrameLossMsgEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgLocalMEPId"),
)
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgEntry.setStatus("current")


class _CienaCesCfmFrameLossMsgLocalMEPId_Type(Integer32):
    """Custom type cienaCesCfmFrameLossMsgLocalMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesCfmFrameLossMsgLocalMEPId_Type.__name__ = "Integer32"
_CienaCesCfmFrameLossMsgLocalMEPId_Object = MibTableColumn
cienaCesCfmFrameLossMsgLocalMEPId = _CienaCesCfmFrameLossMsgLocalMEPId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1, 1, 1),
    _CienaCesCfmFrameLossMsgLocalMEPId_Type()
)
cienaCesCfmFrameLossMsgLocalMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgLocalMEPId.setStatus("current")


class _CienaCesCfmFrameLossMsgTargetMEPID_Type(Unsigned32):
    """Custom type cienaCesCfmFrameLossMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_CienaCesCfmFrameLossMsgTargetMEPID_Type.__name__ = "Unsigned32"
_CienaCesCfmFrameLossMsgTargetMEPID_Object = MibTableColumn
cienaCesCfmFrameLossMsgTargetMEPID = _CienaCesCfmFrameLossMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1, 1, 2),
    _CienaCesCfmFrameLossMsgTargetMEPID_Type()
)
cienaCesCfmFrameLossMsgTargetMEPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgTargetMEPID.setStatus("current")


class _CienaCesCfmFrameLossMsgNearLossThreshold_Type(Integer32):
    """Custom type cienaCesCfmFrameLossMsgNearLossThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CienaCesCfmFrameLossMsgNearLossThreshold_Type.__name__ = "Integer32"
_CienaCesCfmFrameLossMsgNearLossThreshold_Object = MibTableColumn
cienaCesCfmFrameLossMsgNearLossThreshold = _CienaCesCfmFrameLossMsgNearLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1, 1, 3),
    _CienaCesCfmFrameLossMsgNearLossThreshold_Type()
)
cienaCesCfmFrameLossMsgNearLossThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgNearLossThreshold.setStatus("current")


class _CienaCesCfmFrameLossMsgFarLossThreshold_Type(Integer32):
    """Custom type cienaCesCfmFrameLossMsgFarLossThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CienaCesCfmFrameLossMsgFarLossThreshold_Type.__name__ = "Integer32"
_CienaCesCfmFrameLossMsgFarLossThreshold_Object = MibTableColumn
cienaCesCfmFrameLossMsgFarLossThreshold = _CienaCesCfmFrameLossMsgFarLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1, 1, 4),
    _CienaCesCfmFrameLossMsgFarLossThreshold_Type()
)
cienaCesCfmFrameLossMsgFarLossThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgFarLossThreshold.setStatus("current")


class _CienaCesCfmFrameLossMsgServiceName_Type(DisplayString):
    """Custom type cienaCesCfmFrameLossMsgServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesCfmFrameLossMsgServiceName_Type.__name__ = "DisplayString"
_CienaCesCfmFrameLossMsgServiceName_Object = MibTableColumn
cienaCesCfmFrameLossMsgServiceName = _CienaCesCfmFrameLossMsgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1, 1, 5),
    _CienaCesCfmFrameLossMsgServiceName_Type()
)
cienaCesCfmFrameLossMsgServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgServiceName.setStatus("current")
_CienaCesCfmFrameLossMsgFrameLossNear_Type = Unsigned32
_CienaCesCfmFrameLossMsgFrameLossNear_Object = MibTableColumn
cienaCesCfmFrameLossMsgFrameLossNear = _CienaCesCfmFrameLossMsgFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1, 1, 6),
    _CienaCesCfmFrameLossMsgFrameLossNear_Type()
)
cienaCesCfmFrameLossMsgFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgFrameLossNear.setStatus("current")
_CienaCesCfmFrameLossMsgFrameLossFar_Type = Unsigned32
_CienaCesCfmFrameLossMsgFrameLossFar_Object = MibTableColumn
cienaCesCfmFrameLossMsgFrameLossFar = _CienaCesCfmFrameLossMsgFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 6, 1, 1, 7),
    _CienaCesCfmFrameLossMsgFrameLossFar_Type()
)
cienaCesCfmFrameLossMsgFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossMsgFrameLossFar.setStatus("current")
_CienaCesCfmServiceFaultNotifAttrs_ObjectIdentity = ObjectIdentity
cienaCesCfmServiceFaultNotifAttrs = _CienaCesCfmServiceFaultNotifAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 7)
)
_CienaCesCfmServiceFaultNotifTable_Object = MibTable
cienaCesCfmServiceFaultNotifTable = _CienaCesCfmServiceFaultNotifTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmServiceFaultNotifTable.setStatus("current")
_CienaCesCfmServiceFaultNotifEntry_Object = MibTableRow
cienaCesCfmServiceFaultNotifEntry = _CienaCesCfmServiceFaultNotifEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 7, 1, 1)
)
cienaCesCfmServiceFaultNotifEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesCfmServiceFaultNotifEntry.setStatus("current")
_CienaCesCfmServiceFaultTime_Type = TimeTicks
_CienaCesCfmServiceFaultTime_Object = MibTableColumn
cienaCesCfmServiceFaultTime = _CienaCesCfmServiceFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 7, 1, 1, 1),
    _CienaCesCfmServiceFaultTime_Type()
)
cienaCesCfmServiceFaultTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesCfmServiceFaultTime.setStatus("current")


class _CienaCesCfmServiceFaultType_Type(Integer32):
    """Custom type cienaCesCfmServiceFaultType based on Integer32"""
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
        *(("none", 1),
          ("errorRDIDefect", 2),
          ("errorMACStatusDefect", 3),
          ("errorRMEPCCMDefect", 4),
          ("errorCCMDefect", 5),
          ("xconCCMDefect", 6))
    )


_CienaCesCfmServiceFaultType_Type.__name__ = "Integer32"
_CienaCesCfmServiceFaultType_Object = MibTableColumn
cienaCesCfmServiceFaultType = _CienaCesCfmServiceFaultType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 7, 1, 1, 2),
    _CienaCesCfmServiceFaultType_Type()
)
cienaCesCfmServiceFaultType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesCfmServiceFaultType.setStatus("current")
_CienaCesCfmServiceFaultDesc_Type = DisplayString
_CienaCesCfmServiceFaultDesc_Object = MibTableColumn
cienaCesCfmServiceFaultDesc = _CienaCesCfmServiceFaultDesc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 7, 1, 1, 3),
    _CienaCesCfmServiceFaultDesc_Type()
)
cienaCesCfmServiceFaultDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesCfmServiceFaultDesc.setStatus("current")


class _CienaCesCfmServiceFaultMep_Type(Integer32):
    """Custom type cienaCesCfmServiceFaultMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_CienaCesCfmServiceFaultMep_Type.__name__ = "Integer32"
_CienaCesCfmServiceFaultMep_Object = MibTableColumn
cienaCesCfmServiceFaultMep = _CienaCesCfmServiceFaultMep_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 7, 1, 1, 4),
    _CienaCesCfmServiceFaultMep_Type()
)
cienaCesCfmServiceFaultMep.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesCfmServiceFaultMep.setStatus("current")


class _CienaCesCfmServiceVsPbtName_Type(DisplayString):
    """Custom type cienaCesCfmServiceVsPbtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CienaCesCfmServiceVsPbtName_Type.__name__ = "DisplayString"
_CienaCesCfmServiceVsPbtName_Object = MibTableColumn
cienaCesCfmServiceVsPbtName = _CienaCesCfmServiceVsPbtName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 7, 1, 1, 5),
    _CienaCesCfmServiceVsPbtName_Type()
)
cienaCesCfmServiceVsPbtName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesCfmServiceVsPbtName.setStatus("current")
_CienaCesCfmMaintenance_ObjectIdentity = ObjectIdentity
cienaCesCfmMaintenance = _CienaCesCfmMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 8)
)
_CienaCesCfmMaintenanceDomainTable_Object = MibTable
cienaCesCfmMaintenanceDomainTable = _CienaCesCfmMaintenanceDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmMaintenanceDomainTable.setStatus("current")
_CienaCesCfmMaintenanceDomainEntry_Object = MibTableRow
cienaCesCfmMaintenanceDomainEntry = _CienaCesCfmMaintenanceDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 8, 1, 1)
)
cienaCesCfmMaintenanceDomainEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmMaintenanceDomainIndex"),
)
if mibBuilder.loadTexts:
    cienaCesCfmMaintenanceDomainEntry.setStatus("current")
_CienaCesCfmMaintenanceDomainIndex_Type = Unsigned32
_CienaCesCfmMaintenanceDomainIndex_Object = MibTableColumn
cienaCesCfmMaintenanceDomainIndex = _CienaCesCfmMaintenanceDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 8, 1, 1, 1),
    _CienaCesCfmMaintenanceDomainIndex_Type()
)
cienaCesCfmMaintenanceDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMaintenanceDomainIndex.setStatus("current")
_CienaCesCfmMaintenanceDomainLevel_Type = Integer32
_CienaCesCfmMaintenanceDomainLevel_Object = MibTableColumn
cienaCesCfmMaintenanceDomainLevel = _CienaCesCfmMaintenanceDomainLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 8, 1, 1, 2),
    _CienaCesCfmMaintenanceDomainLevel_Type()
)
cienaCesCfmMaintenanceDomainLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMaintenanceDomainLevel.setStatus("current")
_CienaCesCfmMaintenanceDomainName_Type = DisplayString
_CienaCesCfmMaintenanceDomainName_Object = MibTableColumn
cienaCesCfmMaintenanceDomainName = _CienaCesCfmMaintenanceDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 8, 1, 1, 3),
    _CienaCesCfmMaintenanceDomainName_Type()
)
cienaCesCfmMaintenanceDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMaintenanceDomainName.setStatus("current")
_CienaCesCfmMaintenanceDomainServiceCount_Type = Unsigned32
_CienaCesCfmMaintenanceDomainServiceCount_Object = MibTableColumn
cienaCesCfmMaintenanceDomainServiceCount = _CienaCesCfmMaintenanceDomainServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 8, 1, 1, 4),
    _CienaCesCfmMaintenanceDomainServiceCount_Type()
)
cienaCesCfmMaintenanceDomainServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMaintenanceDomainServiceCount.setStatus("current")
_CienaCesCfmServiceFrameBudget_ObjectIdentity = ObjectIdentity
cienaCesCfmServiceFrameBudget = _CienaCesCfmServiceFrameBudget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 9)
)
_CienaCesCfmServiceFrameBudgetTable_Object = MibTable
cienaCesCfmServiceFrameBudgetTable = _CienaCesCfmServiceFrameBudgetTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmServiceFrameBudgetTable.setStatus("current")
_CienaCesCfmServiceFrameBudgetEntry_Object = MibTableRow
cienaCesCfmServiceFrameBudgetEntry = _CienaCesCfmServiceFrameBudgetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 9, 1, 1)
)
cienaCesCfmServiceFrameBudgetEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSlotIndex"),
)
if mibBuilder.loadTexts:
    cienaCesCfmServiceFrameBudgetEntry.setStatus("current")


class _CienaCesCfmSlotIndex_Type(Integer32):
    """Custom type cienaCesCfmSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CienaCesCfmSlotIndex_Type.__name__ = "Integer32"
_CienaCesCfmSlotIndex_Object = MibTableColumn
cienaCesCfmSlotIndex = _CienaCesCfmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 9, 1, 1, 1),
    _CienaCesCfmSlotIndex_Type()
)
cienaCesCfmSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSlotIndex.setStatus("current")
_CienaCesCfmServiceFrameBudgetSlot_Type = Counter32
_CienaCesCfmServiceFrameBudgetSlot_Object = MibTableColumn
cienaCesCfmServiceFrameBudgetSlot = _CienaCesCfmServiceFrameBudgetSlot_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 9, 1, 1, 2),
    _CienaCesCfmServiceFrameBudgetSlot_Type()
)
cienaCesCfmServiceFrameBudgetSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceFrameBudgetSlot.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmServiceFrameBudgetSlot.setUnits("frames/sec")
_CienaCesCfmFrameBudgetGlobal_ObjectIdentity = ObjectIdentity
cienaCesCfmFrameBudgetGlobal = _CienaCesCfmFrameBudgetGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 10)
)
_CienaCesCfmGlobalControlModuleFrameBudget_Type = Counter32
_CienaCesCfmGlobalControlModuleFrameBudget_Object = MibScalar
cienaCesCfmGlobalControlModuleFrameBudget = _CienaCesCfmGlobalControlModuleFrameBudget_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 10, 1),
    _CienaCesCfmGlobalControlModuleFrameBudget_Type()
)
cienaCesCfmGlobalControlModuleFrameBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalControlModuleFrameBudget.setStatus("current")
_CienaCesCfmFrameBudgetGlobalTable_Object = MibTable
cienaCesCfmFrameBudgetGlobalTable = _CienaCesCfmFrameBudgetGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 10, 2)
)
if mibBuilder.loadTexts:
    cienaCesCfmFrameBudgetGlobalTable.setStatus("current")
_CienaCesCfmFrameBudgetGlobalEntry_Object = MibTableRow
cienaCesCfmFrameBudgetGlobalEntry = _CienaCesCfmFrameBudgetGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 10, 2, 1)
)
cienaCesCfmFrameBudgetGlobalEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSlotIndex"),
)
if mibBuilder.loadTexts:
    cienaCesCfmFrameBudgetGlobalEntry.setStatus("current")
_CienaCesCfmFrameBudgetGlobalSlot_Type = Counter32
_CienaCesCfmFrameBudgetGlobalSlot_Object = MibTableColumn
cienaCesCfmFrameBudgetGlobalSlot = _CienaCesCfmFrameBudgetGlobalSlot_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 10, 2, 1, 1),
    _CienaCesCfmFrameBudgetGlobalSlot_Type()
)
cienaCesCfmFrameBudgetGlobalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmFrameBudgetGlobalSlot.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmFrameBudgetGlobalSlot.setUnits("frames/sec")
_CienaCesCfmGlobal_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobal = _CienaCesCfmGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 11)
)
_CienaCesCfmState_Type = CienaGlobalState
_CienaCesCfmState_Object = MibScalar
cienaCesCfmState = _CienaCesCfmState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 11, 1),
    _CienaCesCfmState_Type()
)
cienaCesCfmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmState.setStatus("current")
_CienaCesCfmEtherType_Type = EthType
_CienaCesCfmEtherType_Object = MibScalar
cienaCesCfmEtherType = _CienaCesCfmEtherType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 11, 2),
    _CienaCesCfmEtherType_Type()
)
cienaCesCfmEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmEtherType.setStatus("current")
_CienaCesCfmMEPHoldTime_Type = Integer32
_CienaCesCfmMEPHoldTime_Object = MibScalar
cienaCesCfmMEPHoldTime = _CienaCesCfmMEPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 11, 3),
    _CienaCesCfmMEPHoldTime_Type()
)
cienaCesCfmMEPHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMEPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesCfmMEPHoldTime.setUnits("milliseconds")
_CienaCesCfmY1731EtherType_Type = EthType
_CienaCesCfmY1731EtherType_Object = MibScalar
cienaCesCfmY1731EtherType = _CienaCesCfmY1731EtherType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 11, 4),
    _CienaCesCfmY1731EtherType_Type()
)
cienaCesCfmY1731EtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmY1731EtherType.setStatus("current")
_CienaCesCfmGlobalSLMDefaultCount_Type = Integer32
_CienaCesCfmGlobalSLMDefaultCount_Object = MibScalar
cienaCesCfmGlobalSLMDefaultCount = _CienaCesCfmGlobalSLMDefaultCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 11, 5),
    _CienaCesCfmGlobalSLMDefaultCount_Type()
)
cienaCesCfmGlobalSLMDefaultCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSLMDefaultCount.setStatus("current")
_CienaCesCfmGlobalSLMDefaultInterval_Type = Integer32
_CienaCesCfmGlobalSLMDefaultInterval_Object = MibScalar
cienaCesCfmGlobalSLMDefaultInterval = _CienaCesCfmGlobalSLMDefaultInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 11, 6),
    _CienaCesCfmGlobalSLMDefaultInterval_Type()
)
cienaCesCfmGlobalSLMDefaultInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSLMDefaultInterval.setStatus("current")
_CienaCesCfmGlobalSLMDefaultTimeout_Type = Integer32
_CienaCesCfmGlobalSLMDefaultTimeout_Object = MibScalar
cienaCesCfmGlobalSLMDefaultTimeout = _CienaCesCfmGlobalSLMDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 11, 7),
    _CienaCesCfmGlobalSLMDefaultTimeout_Type()
)
cienaCesCfmGlobalSLMDefaultTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSLMDefaultTimeout.setStatus("current")
_CienaCesCfmSyntheticLoss_ObjectIdentity = ObjectIdentity
cienaCesCfmSyntheticLoss = _CienaCesCfmSyntheticLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12)
)
_CienaCesCfmSyntheticLossSessionTable_Object = MibTable
cienaCesCfmSyntheticLossSessionTable = _CienaCesCfmSyntheticLossSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionTable.setStatus("current")
_CienaCesCfmSyntheticLossSessionEntry_Object = MibTableRow
cienaCesCfmSyntheticLossSessionEntry = _CienaCesCfmSyntheticLossSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1)
)
cienaCesCfmSyntheticLossSessionEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionLocalMEPId"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionTargetMEPId"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionTestId"),
)
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionEntry.setStatus("current")


class _CienaCesCfmSyntheticLossSessionServiceIndex_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionServiceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesCfmSyntheticLossSessionServiceIndex_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionServiceIndex_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionServiceIndex = _CienaCesCfmSyntheticLossSessionServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 1),
    _CienaCesCfmSyntheticLossSessionServiceIndex_Type()
)
cienaCesCfmSyntheticLossSessionServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionServiceIndex.setStatus("current")


class _CienaCesCfmSyntheticLossSessionLocalMEPId_Type(Integer32):
    """Custom type cienaCesCfmSyntheticLossSessionLocalMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesCfmSyntheticLossSessionLocalMEPId_Type.__name__ = "Integer32"
_CienaCesCfmSyntheticLossSessionLocalMEPId_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionLocalMEPId = _CienaCesCfmSyntheticLossSessionLocalMEPId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 2),
    _CienaCesCfmSyntheticLossSessionLocalMEPId_Type()
)
cienaCesCfmSyntheticLossSessionLocalMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionLocalMEPId.setStatus("current")


class _CienaCesCfmSyntheticLossSessionTargetMEPId_Type(Integer32):
    """Custom type cienaCesCfmSyntheticLossSessionTargetMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_CienaCesCfmSyntheticLossSessionTargetMEPId_Type.__name__ = "Integer32"
_CienaCesCfmSyntheticLossSessionTargetMEPId_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionTargetMEPId = _CienaCesCfmSyntheticLossSessionTargetMEPId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 3),
    _CienaCesCfmSyntheticLossSessionTargetMEPId_Type()
)
cienaCesCfmSyntheticLossSessionTargetMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionTargetMEPId.setStatus("current")


class _CienaCesCfmSyntheticLossSessionTestId_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesCfmSyntheticLossSessionTestId_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionTestId_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionTestId = _CienaCesCfmSyntheticLossSessionTestId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 4),
    _CienaCesCfmSyntheticLossSessionTestId_Type()
)
cienaCesCfmSyntheticLossSessionTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionTestId.setStatus("current")
_CienaCesCfmSyntheticLossSessionServiceName_Type = DisplayString
_CienaCesCfmSyntheticLossSessionServiceName_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionServiceName = _CienaCesCfmSyntheticLossSessionServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 5),
    _CienaCesCfmSyntheticLossSessionServiceName_Type()
)
cienaCesCfmSyntheticLossSessionServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionServiceName.setStatus("current")


class _CienaCesCfmSyntheticLossSessionPriority_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesCfmSyntheticLossSessionPriority_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionPriority_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionPriority = _CienaCesCfmSyntheticLossSessionPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 6),
    _CienaCesCfmSyntheticLossSessionPriority_Type()
)
cienaCesCfmSyntheticLossSessionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionPriority.setStatus("current")


class _CienaCesCfmSyntheticLossSessionCount_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 65535),
    )


_CienaCesCfmSyntheticLossSessionCount_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionCount_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionCount = _CienaCesCfmSyntheticLossSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 7),
    _CienaCesCfmSyntheticLossSessionCount_Type()
)
cienaCesCfmSyntheticLossSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionCount.setStatus("current")


class _CienaCesCfmSyntheticLossSessionSLMInterval_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionSLMInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 7),
    )


_CienaCesCfmSyntheticLossSessionSLMInterval_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionSLMInterval_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionSLMInterval = _CienaCesCfmSyntheticLossSessionSLMInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 8),
    _CienaCesCfmSyntheticLossSessionSLMInterval_Type()
)
cienaCesCfmSyntheticLossSessionSLMInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionSLMInterval.setStatus("current")


class _CienaCesCfmSyntheticLossSessionIterations_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionIterations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CienaCesCfmSyntheticLossSessionIterations_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionIterations_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionIterations = _CienaCesCfmSyntheticLossSessionIterations_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 9),
    _CienaCesCfmSyntheticLossSessionIterations_Type()
)
cienaCesCfmSyntheticLossSessionIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionIterations.setStatus("current")


class _CienaCesCfmSyntheticLossSessionRepeatDelay_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionRepeatDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CienaCesCfmSyntheticLossSessionRepeatDelay_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionRepeatDelay_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionRepeatDelay = _CienaCesCfmSyntheticLossSessionRepeatDelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 10),
    _CienaCesCfmSyntheticLossSessionRepeatDelay_Type()
)
cienaCesCfmSyntheticLossSessionRepeatDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionRepeatDelay.setStatus("current")


class _CienaCesCfmSyntheticLossSessionFrameSize_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(65, 1400),
    )


_CienaCesCfmSyntheticLossSessionFrameSize_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionFrameSize_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionFrameSize = _CienaCesCfmSyntheticLossSessionFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 11),
    _CienaCesCfmSyntheticLossSessionFrameSize_Type()
)
cienaCesCfmSyntheticLossSessionFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionFrameSize.setStatus("current")


class _CienaCesCfmSyntheticLossSessionTimeout_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 10000),
    )


_CienaCesCfmSyntheticLossSessionTimeout_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionTimeout_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionTimeout = _CienaCesCfmSyntheticLossSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 12),
    _CienaCesCfmSyntheticLossSessionTimeout_Type()
)
cienaCesCfmSyntheticLossSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionTimeout.setStatus("current")


class _CienaCesCfmSyntheticLossSessionDuration_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesCfmSyntheticLossSessionDuration_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionDuration_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionDuration = _CienaCesCfmSyntheticLossSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 13),
    _CienaCesCfmSyntheticLossSessionDuration_Type()
)
cienaCesCfmSyntheticLossSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionDuration.setStatus("current")


class _CienaCesCfmSyntheticLossSessionLossNearThreshold_Type(Integer32):
    """Custom type cienaCesCfmSyntheticLossSessionLossNearThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CienaCesCfmSyntheticLossSessionLossNearThreshold_Type.__name__ = "Integer32"
_CienaCesCfmSyntheticLossSessionLossNearThreshold_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionLossNearThreshold = _CienaCesCfmSyntheticLossSessionLossNearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 14),
    _CienaCesCfmSyntheticLossSessionLossNearThreshold_Type()
)
cienaCesCfmSyntheticLossSessionLossNearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionLossNearThreshold.setStatus("current")


class _CienaCesCfmSyntheticLossSessionLossFarThreshold_Type(Integer32):
    """Custom type cienaCesCfmSyntheticLossSessionLossFarThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CienaCesCfmSyntheticLossSessionLossFarThreshold_Type.__name__ = "Integer32"
_CienaCesCfmSyntheticLossSessionLossFarThreshold_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionLossFarThreshold = _CienaCesCfmSyntheticLossSessionLossFarThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 15),
    _CienaCesCfmSyntheticLossSessionLossFarThreshold_Type()
)
cienaCesCfmSyntheticLossSessionLossFarThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionLossFarThreshold.setStatus("current")


class _CienaCesCfmSyntheticLossSessionNumSLMSent_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionNumSLMSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesCfmSyntheticLossSessionNumSLMSent_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionNumSLMSent_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionNumSLMSent = _CienaCesCfmSyntheticLossSessionNumSLMSent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 16),
    _CienaCesCfmSyntheticLossSessionNumSLMSent_Type()
)
cienaCesCfmSyntheticLossSessionNumSLMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionNumSLMSent.setStatus("current")


class _CienaCesCfmSyntheticLossSessionNumSLRReceived_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossSessionNumSLRReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesCfmSyntheticLossSessionNumSLRReceived_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossSessionNumSLRReceived_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionNumSLRReceived = _CienaCesCfmSyntheticLossSessionNumSLRReceived_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 17),
    _CienaCesCfmSyntheticLossSessionNumSLRReceived_Type()
)
cienaCesCfmSyntheticLossSessionNumSLRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionNumSLRReceived.setStatus("current")
_CienaCesCfmSyntheticLossSessionFrameLossNear_Type = Integer32
_CienaCesCfmSyntheticLossSessionFrameLossNear_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionFrameLossNear = _CienaCesCfmSyntheticLossSessionFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 18),
    _CienaCesCfmSyntheticLossSessionFrameLossNear_Type()
)
cienaCesCfmSyntheticLossSessionFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionFrameLossNear.setStatus("current")
_CienaCesCfmSyntheticLossSessionFrameLossFar_Type = Integer32
_CienaCesCfmSyntheticLossSessionFrameLossFar_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionFrameLossFar = _CienaCesCfmSyntheticLossSessionFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 19),
    _CienaCesCfmSyntheticLossSessionFrameLossFar_Type()
)
cienaCesCfmSyntheticLossSessionFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionFrameLossFar.setStatus("current")
_CienaCesCfmSyntheticLossSessionAvgFrameLossNear_Type = Integer32
_CienaCesCfmSyntheticLossSessionAvgFrameLossNear_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionAvgFrameLossNear = _CienaCesCfmSyntheticLossSessionAvgFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 20),
    _CienaCesCfmSyntheticLossSessionAvgFrameLossNear_Type()
)
cienaCesCfmSyntheticLossSessionAvgFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionAvgFrameLossNear.setStatus("current")
_CienaCesCfmSyntheticLossSessionMinFrameLossNear_Type = Integer32
_CienaCesCfmSyntheticLossSessionMinFrameLossNear_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionMinFrameLossNear = _CienaCesCfmSyntheticLossSessionMinFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 21),
    _CienaCesCfmSyntheticLossSessionMinFrameLossNear_Type()
)
cienaCesCfmSyntheticLossSessionMinFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionMinFrameLossNear.setStatus("current")
_CienaCesCfmSyntheticLossSessionMaxFrameLossNear_Type = Integer32
_CienaCesCfmSyntheticLossSessionMaxFrameLossNear_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionMaxFrameLossNear = _CienaCesCfmSyntheticLossSessionMaxFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 22),
    _CienaCesCfmSyntheticLossSessionMaxFrameLossNear_Type()
)
cienaCesCfmSyntheticLossSessionMaxFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionMaxFrameLossNear.setStatus("current")
_CienaCesCfmSyntheticLossSessionAvgFrameLossFar_Type = Integer32
_CienaCesCfmSyntheticLossSessionAvgFrameLossFar_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionAvgFrameLossFar = _CienaCesCfmSyntheticLossSessionAvgFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 23),
    _CienaCesCfmSyntheticLossSessionAvgFrameLossFar_Type()
)
cienaCesCfmSyntheticLossSessionAvgFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionAvgFrameLossFar.setStatus("current")
_CienaCesCfmSyntheticLossSessionMinFrameLossFar_Type = Integer32
_CienaCesCfmSyntheticLossSessionMinFrameLossFar_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionMinFrameLossFar = _CienaCesCfmSyntheticLossSessionMinFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 24),
    _CienaCesCfmSyntheticLossSessionMinFrameLossFar_Type()
)
cienaCesCfmSyntheticLossSessionMinFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionMinFrameLossFar.setStatus("current")
_CienaCesCfmSyntheticLossSessionMaxFrameLossFar_Type = Integer32
_CienaCesCfmSyntheticLossSessionMaxFrameLossFar_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionMaxFrameLossFar = _CienaCesCfmSyntheticLossSessionMaxFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 25),
    _CienaCesCfmSyntheticLossSessionMaxFrameLossFar_Type()
)
cienaCesCfmSyntheticLossSessionMaxFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionMaxFrameLossFar.setStatus("current")
_CienaCesCfmSyntheticLossSessionFrameLossRatioNear_Type = CfmFrameLossRatio
_CienaCesCfmSyntheticLossSessionFrameLossRatioNear_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionFrameLossRatioNear = _CienaCesCfmSyntheticLossSessionFrameLossRatioNear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 26),
    _CienaCesCfmSyntheticLossSessionFrameLossRatioNear_Type()
)
cienaCesCfmSyntheticLossSessionFrameLossRatioNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionFrameLossRatioNear.setStatus("current")
_CienaCesCfmSyntheticLossSessionFrameLossRatioFar_Type = CfmFrameLossRatio
_CienaCesCfmSyntheticLossSessionFrameLossRatioFar_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionFrameLossRatioFar = _CienaCesCfmSyntheticLossSessionFrameLossRatioFar_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 27),
    _CienaCesCfmSyntheticLossSessionFrameLossRatioFar_Type()
)
cienaCesCfmSyntheticLossSessionFrameLossRatioFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionFrameLossRatioFar.setStatus("current")


class _CienaCesCfmSyntheticLossSessionSdSetThreshold_Type(Integer32):
    """Custom type cienaCesCfmSyntheticLossSessionSdSetThreshold based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CienaCesCfmSyntheticLossSessionSdSetThreshold_Type.__name__ = "Integer32"
_CienaCesCfmSyntheticLossSessionSdSetThreshold_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionSdSetThreshold = _CienaCesCfmSyntheticLossSessionSdSetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 28),
    _CienaCesCfmSyntheticLossSessionSdSetThreshold_Type()
)
cienaCesCfmSyntheticLossSessionSdSetThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionSdSetThreshold.setStatus("current")


class _CienaCesCfmSyntheticLossSessionSdClearThreshold_Type(Integer32):
    """Custom type cienaCesCfmSyntheticLossSessionSdClearThreshold based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CienaCesCfmSyntheticLossSessionSdClearThreshold_Type.__name__ = "Integer32"
_CienaCesCfmSyntheticLossSessionSdClearThreshold_Object = MibTableColumn
cienaCesCfmSyntheticLossSessionSdClearThreshold = _CienaCesCfmSyntheticLossSessionSdClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 1, 1, 29),
    _CienaCesCfmSyntheticLossSessionSdClearThreshold_Type()
)
cienaCesCfmSyntheticLossSessionSdClearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionSdClearThreshold.setStatus("current")
_CienaCesCfmSyntheticLossResponderTable_Object = MibTable
cienaCesCfmSyntheticLossResponderTable = _CienaCesCfmSyntheticLossResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2)
)
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderTable.setStatus("current")
_CienaCesCfmSyntheticLossResponderEntry_Object = MibTableRow
cienaCesCfmSyntheticLossResponderEntry = _CienaCesCfmSyntheticLossResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1)
)
cienaCesCfmSyntheticLossResponderEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossResponderServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossResponderLocalMEPId"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossResponderRemoteMEPId"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossResponderTestId"),
)
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderEntry.setStatus("current")


class _CienaCesCfmSyntheticLossResponderServiceIndex_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossResponderServiceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesCfmSyntheticLossResponderServiceIndex_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossResponderServiceIndex_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderServiceIndex = _CienaCesCfmSyntheticLossResponderServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 1),
    _CienaCesCfmSyntheticLossResponderServiceIndex_Type()
)
cienaCesCfmSyntheticLossResponderServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderServiceIndex.setStatus("current")


class _CienaCesCfmSyntheticLossResponderLocalMEPId_Type(Integer32):
    """Custom type cienaCesCfmSyntheticLossResponderLocalMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_CienaCesCfmSyntheticLossResponderLocalMEPId_Type.__name__ = "Integer32"
_CienaCesCfmSyntheticLossResponderLocalMEPId_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderLocalMEPId = _CienaCesCfmSyntheticLossResponderLocalMEPId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 2),
    _CienaCesCfmSyntheticLossResponderLocalMEPId_Type()
)
cienaCesCfmSyntheticLossResponderLocalMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderLocalMEPId.setStatus("current")


class _CienaCesCfmSyntheticLossResponderRemoteMEPId_Type(Integer32):
    """Custom type cienaCesCfmSyntheticLossResponderRemoteMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_CienaCesCfmSyntheticLossResponderRemoteMEPId_Type.__name__ = "Integer32"
_CienaCesCfmSyntheticLossResponderRemoteMEPId_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderRemoteMEPId = _CienaCesCfmSyntheticLossResponderRemoteMEPId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 3),
    _CienaCesCfmSyntheticLossResponderRemoteMEPId_Type()
)
cienaCesCfmSyntheticLossResponderRemoteMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderRemoteMEPId.setStatus("current")


class _CienaCesCfmSyntheticLossResponderTestId_Type(Unsigned32):
    """Custom type cienaCesCfmSyntheticLossResponderTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesCfmSyntheticLossResponderTestId_Type.__name__ = "Unsigned32"
_CienaCesCfmSyntheticLossResponderTestId_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderTestId = _CienaCesCfmSyntheticLossResponderTestId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 4),
    _CienaCesCfmSyntheticLossResponderTestId_Type()
)
cienaCesCfmSyntheticLossResponderTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderTestId.setStatus("current")
_CienaCesCfmSyntheticLossResponderServiceName_Type = DisplayString
_CienaCesCfmSyntheticLossResponderServiceName_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderServiceName = _CienaCesCfmSyntheticLossResponderServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 5),
    _CienaCesCfmSyntheticLossResponderServiceName_Type()
)
cienaCesCfmSyntheticLossResponderServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderServiceName.setStatus("current")
_CienaCesCfmSyntheticLossResponderLocalMac_Type = MacAddress
_CienaCesCfmSyntheticLossResponderLocalMac_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderLocalMac = _CienaCesCfmSyntheticLossResponderLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 6),
    _CienaCesCfmSyntheticLossResponderLocalMac_Type()
)
cienaCesCfmSyntheticLossResponderLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderLocalMac.setStatus("current")
_CienaCesCfmSyntheticLossResponderRemoteMac_Type = MacAddress
_CienaCesCfmSyntheticLossResponderRemoteMac_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderRemoteMac = _CienaCesCfmSyntheticLossResponderRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 7),
    _CienaCesCfmSyntheticLossResponderRemoteMac_Type()
)
cienaCesCfmSyntheticLossResponderRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderRemoteMac.setStatus("current")
_CienaCesCfmSyntheticLossResponderNumSLMReceived_Type = Unsigned32
_CienaCesCfmSyntheticLossResponderNumSLMReceived_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderNumSLMReceived = _CienaCesCfmSyntheticLossResponderNumSLMReceived_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 8),
    _CienaCesCfmSyntheticLossResponderNumSLMReceived_Type()
)
cienaCesCfmSyntheticLossResponderNumSLMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderNumSLMReceived.setStatus("current")
_CienaCesCfmSyntheticLossResponderNumSLRSent_Type = Unsigned32
_CienaCesCfmSyntheticLossResponderNumSLRSent_Object = MibTableColumn
cienaCesCfmSyntheticLossResponderNumSLRSent = _CienaCesCfmSyntheticLossResponderNumSLRSent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 4, 1, 12, 2, 1, 9),
    _CienaCesCfmSyntheticLossResponderNumSLRSent_Type()
)
cienaCesCfmSyntheticLossResponderNumSLRSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossResponderNumSLRSent.setStatus("current")
_CienaCesCfmNotifMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesCfmNotifMIBNotificationPrefix = _CienaCesCfmNotifMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5)
)
_CienaCesCfmNotifMIBNotification_ObjectIdentity = ObjectIdentity
cienaCesCfmNotifMIBNotification = _CienaCesCfmNotifMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0)
)
_CienaCesCfmStatisticsMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesCfmStatisticsMIBObjects = _CienaCesCfmStatisticsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4)
)
_CienaCesCfmMibObjects_ObjectIdentity = ObjectIdentity
cienaCesCfmMibObjects = _CienaCesCfmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1)
)
_CienaCesCfmGlobalMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalMIBObjects = _CienaCesCfmGlobalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1)
)
_CienaCesCfmGlobalStatsClear_Type = CienaStatsClear
_CienaCesCfmGlobalStatsClear_Object = MibScalar
cienaCesCfmGlobalStatsClear = _CienaCesCfmGlobalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 1),
    _CienaCesCfmGlobalStatsClear_Type()
)
cienaCesCfmGlobalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsClear.setStatus("current")
_CienaCesCfmGlobalFrameBudget_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalFrameBudget = _CienaCesCfmGlobalFrameBudget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2)
)
_CienaCesCfmGlobalFrameBudgetControlModule_Type = Counter32
_CienaCesCfmGlobalFrameBudgetControlModule_Object = MibScalar
cienaCesCfmGlobalFrameBudgetControlModule = _CienaCesCfmGlobalFrameBudgetControlModule_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 1),
    _CienaCesCfmGlobalFrameBudgetControlModule_Type()
)
cienaCesCfmGlobalFrameBudgetControlModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetControlModule.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot1_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot1_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot1 = _CienaCesCfmGlobalFrameBudgetSlot1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 2),
    _CienaCesCfmGlobalFrameBudgetSlot1_Type()
)
cienaCesCfmGlobalFrameBudgetSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot1.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot2_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot2_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot2 = _CienaCesCfmGlobalFrameBudgetSlot2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 3),
    _CienaCesCfmGlobalFrameBudgetSlot2_Type()
)
cienaCesCfmGlobalFrameBudgetSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot2.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot3_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot3_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot3 = _CienaCesCfmGlobalFrameBudgetSlot3_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 4),
    _CienaCesCfmGlobalFrameBudgetSlot3_Type()
)
cienaCesCfmGlobalFrameBudgetSlot3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot3.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot4_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot4_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot4 = _CienaCesCfmGlobalFrameBudgetSlot4_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 5),
    _CienaCesCfmGlobalFrameBudgetSlot4_Type()
)
cienaCesCfmGlobalFrameBudgetSlot4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot4.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot5_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot5_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot5 = _CienaCesCfmGlobalFrameBudgetSlot5_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 6),
    _CienaCesCfmGlobalFrameBudgetSlot5_Type()
)
cienaCesCfmGlobalFrameBudgetSlot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot5.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot6_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot6_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot6 = _CienaCesCfmGlobalFrameBudgetSlot6_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 7),
    _CienaCesCfmGlobalFrameBudgetSlot6_Type()
)
cienaCesCfmGlobalFrameBudgetSlot6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot6.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot7_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot7_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot7 = _CienaCesCfmGlobalFrameBudgetSlot7_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 8),
    _CienaCesCfmGlobalFrameBudgetSlot7_Type()
)
cienaCesCfmGlobalFrameBudgetSlot7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot7.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot8_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot8_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot8 = _CienaCesCfmGlobalFrameBudgetSlot8_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 9),
    _CienaCesCfmGlobalFrameBudgetSlot8_Type()
)
cienaCesCfmGlobalFrameBudgetSlot8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot8.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot9_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot9_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot9 = _CienaCesCfmGlobalFrameBudgetSlot9_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 10),
    _CienaCesCfmGlobalFrameBudgetSlot9_Type()
)
cienaCesCfmGlobalFrameBudgetSlot9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot9.setStatus("deprecated")
_CienaCesCfmGlobalFrameBudgetSlot10_Type = Counter32
_CienaCesCfmGlobalFrameBudgetSlot10_Object = MibScalar
cienaCesCfmGlobalFrameBudgetSlot10 = _CienaCesCfmGlobalFrameBudgetSlot10_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 2, 11),
    _CienaCesCfmGlobalFrameBudgetSlot10_Type()
)
cienaCesCfmGlobalFrameBudgetSlot10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalFrameBudgetSlot10.setStatus("deprecated")
_CienaCesCfmGlobalStats_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalStats = _CienaCesCfmGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3)
)
_CienaCesCfmGlobalStatsTxTotalFrames_Type = Counter64
_CienaCesCfmGlobalStatsTxTotalFrames_Object = MibScalar
cienaCesCfmGlobalStatsTxTotalFrames = _CienaCesCfmGlobalStatsTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 1),
    _CienaCesCfmGlobalStatsTxTotalFrames_Type()
)
cienaCesCfmGlobalStatsTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsTxTotalFrames.setStatus("current")
_CienaCesCfmGlobalStatsTxFloodedframes_Type = Counter64
_CienaCesCfmGlobalStatsTxFloodedframes_Object = MibScalar
cienaCesCfmGlobalStatsTxFloodedframes = _CienaCesCfmGlobalStatsTxFloodedframes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 2),
    _CienaCesCfmGlobalStatsTxFloodedframes_Type()
)
cienaCesCfmGlobalStatsTxFloodedframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsTxFloodedframes.setStatus("current")
_CienaCesCfmGlobalStatsTxFloodignoredInvalidLevel_Type = Counter64
_CienaCesCfmGlobalStatsTxFloodignoredInvalidLevel_Object = MibScalar
cienaCesCfmGlobalStatsTxFloodignoredInvalidLevel = _CienaCesCfmGlobalStatsTxFloodignoredInvalidLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 3),
    _CienaCesCfmGlobalStatsTxFloodignoredInvalidLevel_Type()
)
cienaCesCfmGlobalStatsTxFloodignoredInvalidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsTxFloodignoredInvalidLevel.setStatus("current")
_CienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist_Type = Counter64
_CienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist_Object = MibScalar
cienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist = _CienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 4),
    _CienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist_Type()
)
cienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist.setStatus("current")
_CienaCesCfmGlobalStatsTxFloodignoredSTPState_Type = Counter64
_CienaCesCfmGlobalStatsTxFloodignoredSTPState_Object = MibScalar
cienaCesCfmGlobalStatsTxFloodignoredSTPState = _CienaCesCfmGlobalStatsTxFloodignoredSTPState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 5),
    _CienaCesCfmGlobalStatsTxFloodignoredSTPState_Type()
)
cienaCesCfmGlobalStatsTxFloodignoredSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsTxFloodignoredSTPState.setStatus("current")
_CienaCesCfmGlobalStatsRxTotalFrames_Type = Counter64
_CienaCesCfmGlobalStatsRxTotalFrames_Object = MibScalar
cienaCesCfmGlobalStatsRxTotalFrames = _CienaCesCfmGlobalStatsRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 6),
    _CienaCesCfmGlobalStatsRxTotalFrames_Type()
)
cienaCesCfmGlobalStatsRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsRxTotalFrames.setStatus("current")
_CienaCesCfmGlobalStatsRxDropInvalidEtype_Type = Counter64
_CienaCesCfmGlobalStatsRxDropInvalidEtype_Object = MibScalar
cienaCesCfmGlobalStatsRxDropInvalidEtype = _CienaCesCfmGlobalStatsRxDropInvalidEtype_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 7),
    _CienaCesCfmGlobalStatsRxDropInvalidEtype_Type()
)
cienaCesCfmGlobalStatsRxDropInvalidEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsRxDropInvalidEtype.setStatus("current")
_CienaCesCfmGlobalStatsRxDropInvalidOpCode_Type = Counter64
_CienaCesCfmGlobalStatsRxDropInvalidOpCode_Object = MibScalar
cienaCesCfmGlobalStatsRxDropInvalidOpCode = _CienaCesCfmGlobalStatsRxDropInvalidOpCode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 8),
    _CienaCesCfmGlobalStatsRxDropInvalidOpCode_Type()
)
cienaCesCfmGlobalStatsRxDropInvalidOpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsRxDropInvalidOpCode.setStatus("current")
_CienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch_Type = Counter64
_CienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch_Object = MibScalar
cienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch = _CienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 9),
    _CienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch_Type()
)
cienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch.setStatus("current")
_CienaCesCfmGlobalStatsRxTotalMalformedFrames_Type = Counter64
_CienaCesCfmGlobalStatsRxTotalMalformedFrames_Object = MibScalar
cienaCesCfmGlobalStatsRxTotalMalformedFrames = _CienaCesCfmGlobalStatsRxTotalMalformedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 3, 10),
    _CienaCesCfmGlobalStatsRxTotalMalformedFrames_Type()
)
cienaCesCfmGlobalStatsRxTotalMalformedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalStatsRxTotalMalformedFrames.setStatus("current")
_CienaCesCfmGlobalCCMStats_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalCCMStats = _CienaCesCfmGlobalCCMStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4)
)
_CienaCesCfmGlobalCCMStatsTxTotalCCM_Type = Counter64
_CienaCesCfmGlobalCCMStatsTxTotalCCM_Object = MibScalar
cienaCesCfmGlobalCCMStatsTxTotalCCM = _CienaCesCfmGlobalCCMStatsTxTotalCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 1),
    _CienaCesCfmGlobalCCMStatsTxTotalCCM_Type()
)
cienaCesCfmGlobalCCMStatsTxTotalCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsTxTotalCCM.setStatus("current")
_CienaCesCfmGlobalCCMStatsTxTotalCCMFlooded_Type = Counter64
_CienaCesCfmGlobalCCMStatsTxTotalCCMFlooded_Object = MibScalar
cienaCesCfmGlobalCCMStatsTxTotalCCMFlooded = _CienaCesCfmGlobalCCMStatsTxTotalCCMFlooded_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 2),
    _CienaCesCfmGlobalCCMStatsTxTotalCCMFlooded_Type()
)
cienaCesCfmGlobalCCMStatsTxTotalCCMFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsTxTotalCCMFlooded.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxTotalCCM_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxTotalCCM_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxTotalCCM = _CienaCesCfmGlobalCCMStatsRxTotalCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 3),
    _CienaCesCfmGlobalCCMStatsRxTotalCCM_Type()
)
cienaCesCfmGlobalCCMStatsRxTotalCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxTotalCCM.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors = _CienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 5),
    _CienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors_Type()
)
cienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxInvalidMAID_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxInvalidMAID_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxInvalidMAID = _CienaCesCfmGlobalCCMStatsRxInvalidMAID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 6),
    _CienaCesCfmGlobalCCMStatsRxInvalidMAID_Type()
)
cienaCesCfmGlobalCCMStatsRxInvalidMAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxInvalidMAID.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxInvalidCCMInterval_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxInvalidCCMInterval_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxInvalidCCMInterval = _CienaCesCfmGlobalCCMStatsRxInvalidCCMInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 7),
    _CienaCesCfmGlobalCCMStatsRxInvalidCCMInterval_Type()
)
cienaCesCfmGlobalCCMStatsRxInvalidCCMInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxInvalidCCMInterval.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset = _CienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 8),
    _CienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset_Type()
)
cienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv = _CienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 9),
    _CienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv_Type()
)
cienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv = _CienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 11),
    _CienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv_Type()
)
cienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface = _CienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 12),
    _CienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface_Type()
)
cienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxInvalidServiceInstance_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxInvalidServiceInstance_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxInvalidServiceInstance = _CienaCesCfmGlobalCCMStatsRxInvalidServiceInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 13),
    _CienaCesCfmGlobalCCMStatsRxInvalidServiceInstance_Type()
)
cienaCesCfmGlobalCCMStatsRxInvalidServiceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxInvalidServiceInstance.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel = _CienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 14),
    _CienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel_Type()
)
cienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxDropAdminDisable_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxDropAdminDisable_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxDropAdminDisable = _CienaCesCfmGlobalCCMStatsRxDropAdminDisable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 15),
    _CienaCesCfmGlobalCCMStatsRxDropAdminDisable_Type()
)
cienaCesCfmGlobalCCMStatsRxDropAdminDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxDropAdminDisable.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding = _CienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 16),
    _CienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding_Type()
)
cienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep = _CienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 17),
    _CienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep_Type()
)
cienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxDropCCMLeakage_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxDropCCMLeakage_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxDropCCMLeakage = _CienaCesCfmGlobalCCMStatsRxDropCCMLeakage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 18),
    _CienaCesCfmGlobalCCMStatsRxDropCCMLeakage_Type()
)
cienaCesCfmGlobalCCMStatsRxDropCCMLeakage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxDropCCMLeakage.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxDropCCMTooLong_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxDropCCMTooLong_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxDropCCMTooLong = _CienaCesCfmGlobalCCMStatsRxDropCCMTooLong_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 19),
    _CienaCesCfmGlobalCCMStatsRxDropCCMTooLong_Type()
)
cienaCesCfmGlobalCCMStatsRxDropCCMTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxDropCCMTooLong.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled = _CienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 20),
    _CienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled_Type()
)
cienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxTotalErrorCCM_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxTotalErrorCCM_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxTotalErrorCCM = _CienaCesCfmGlobalCCMStatsRxTotalErrorCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 21),
    _CienaCesCfmGlobalCCMStatsRxTotalErrorCCM_Type()
)
cienaCesCfmGlobalCCMStatsRxTotalErrorCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxTotalErrorCCM.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxTotalMalformedCCM_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxTotalMalformedCCM_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxTotalMalformedCCM = _CienaCesCfmGlobalCCMStatsRxTotalMalformedCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 22),
    _CienaCesCfmGlobalCCMStatsRxTotalMalformedCCM_Type()
)
cienaCesCfmGlobalCCMStatsRxTotalMalformedCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxTotalMalformedCCM.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxTotalMEPCCM_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxTotalMEPCCM_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxTotalMEPCCM = _CienaCesCfmGlobalCCMStatsRxTotalMEPCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 23),
    _CienaCesCfmGlobalCCMStatsRxTotalMEPCCM_Type()
)
cienaCesCfmGlobalCCMStatsRxTotalMEPCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxTotalMEPCCM.setStatus("current")
_CienaCesCfmGlobalCCMStatsRxTotalMIPCCM_Type = Counter64
_CienaCesCfmGlobalCCMStatsRxTotalMIPCCM_Object = MibScalar
cienaCesCfmGlobalCCMStatsRxTotalMIPCCM = _CienaCesCfmGlobalCCMStatsRxTotalMIPCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 4, 24),
    _CienaCesCfmGlobalCCMStatsRxTotalMIPCCM_Type()
)
cienaCesCfmGlobalCCMStatsRxTotalMIPCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalCCMStatsRxTotalMIPCCM.setStatus("current")
_CienaCesCfmGlobalLoopbackStats_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalLoopbackStats = _CienaCesCfmGlobalLoopbackStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5)
)
_CienaCesCfmGlobalLoopbackStatsTxTotalLBM_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsTxTotalLBM_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsTxTotalLBM = _CienaCesCfmGlobalLoopbackStatsTxTotalLBM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 1),
    _CienaCesCfmGlobalLoopbackStatsTxTotalLBM_Type()
)
cienaCesCfmGlobalLoopbackStatsTxTotalLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsTxTotalLBM.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsTxTotalLBR_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsTxTotalLBR_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsTxTotalLBR = _CienaCesCfmGlobalLoopbackStatsTxTotalLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 2),
    _CienaCesCfmGlobalLoopbackStatsTxTotalLBR_Type()
)
cienaCesCfmGlobalLoopbackStatsTxTotalLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsTxTotalLBR.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxTotalLBM_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxTotalLBM_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxTotalLBM = _CienaCesCfmGlobalLoopbackStatsRxTotalLBM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 3),
    _CienaCesCfmGlobalLoopbackStatsRxTotalLBM_Type()
)
cienaCesCfmGlobalLoopbackStatsRxTotalLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxTotalLBM.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxTotalLBR_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxTotalLBR_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxTotalLBR = _CienaCesCfmGlobalLoopbackStatsRxTotalLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 4),
    _CienaCesCfmGlobalLoopbackStatsRxTotalLBR_Type()
)
cienaCesCfmGlobalLoopbackStatsRxTotalLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxTotalLBR.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR = _CienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 5),
    _CienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR_Type()
)
cienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR = _CienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 6),
    _CienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR_Type()
)
cienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR = _CienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 7),
    _CienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR_Type()
)
cienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR = _CienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 8),
    _CienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR_Type()
)
cienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset = _CienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 9),
    _CienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset_Type()
)
cienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset = _CienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 10),
    _CienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset_Type()
)
cienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM = _CienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 11),
    _CienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM_Type()
)
cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR = _CienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 12),
    _CienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR_Type()
)
cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR.setStatus("current")
_CienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM_Type = Counter64
_CienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM_Object = MibScalar
cienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM = _CienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 5, 13),
    _CienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM_Type()
)
cienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM.setStatus("current")
_CienaCesCfmGlobalLinkTraceStats_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalLinkTraceStats = _CienaCesCfmGlobalLinkTraceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6)
)
_CienaCesCfmGlobalLinkTraceStatsTxTotalLTM_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsTxTotalLTM_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsTxTotalLTM = _CienaCesCfmGlobalLinkTraceStatsTxTotalLTM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 1),
    _CienaCesCfmGlobalLinkTraceStatsTxTotalLTM_Type()
)
cienaCesCfmGlobalLinkTraceStatsTxTotalLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsTxTotalLTM.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsTxTotalLTR_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsTxTotalLTR_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsTxTotalLTR = _CienaCesCfmGlobalLinkTraceStatsTxTotalLTR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 2),
    _CienaCesCfmGlobalLinkTraceStatsTxTotalLTR_Type()
)
cienaCesCfmGlobalLinkTraceStatsTxTotalLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsTxTotalLTR.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsRxTotalLTM_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsRxTotalLTM_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsRxTotalLTM = _CienaCesCfmGlobalLinkTraceStatsRxTotalLTM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 3),
    _CienaCesCfmGlobalLinkTraceStatsRxTotalLTM_Type()
)
cienaCesCfmGlobalLinkTraceStatsRxTotalLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsRxTotalLTM.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsRxTotalLTR_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsRxTotalLTR_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsRxTotalLTR = _CienaCesCfmGlobalLinkTraceStatsRxTotalLTR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 4),
    _CienaCesCfmGlobalLinkTraceStatsRxTotalLTR_Type()
)
cienaCesCfmGlobalLinkTraceStatsRxTotalLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsRxTotalLTR.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR = _CienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 5),
    _CienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR_Type()
)
cienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset = _CienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 6),
    _CienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset_Type()
)
cienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset = _CienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 7),
    _CienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset_Type()
)
cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction = _CienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 8),
    _CienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction_Type()
)
cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM = _CienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 9),
    _CienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM_Type()
)
cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM.setStatus("current")
_CienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR_Type = Counter64
_CienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR_Object = MibScalar
cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR = _CienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 6, 10),
    _CienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR_Type()
)
cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR.setStatus("current")
_CienaCesCfmGlobalDelayMeasurementStats_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalDelayMeasurementStats = _CienaCesCfmGlobalDelayMeasurementStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 7)
)
_CienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM_Type = Counter64
_CienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM_Object = MibScalar
cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM = _CienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 7, 1),
    _CienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM_Type()
)
cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM.setStatus("current")
_CienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR_Type = Counter64
_CienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR_Object = MibScalar
cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR = _CienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 7, 2),
    _CienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR_Type()
)
cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR.setStatus("current")
_CienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM_Type = Counter64
_CienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM_Object = MibScalar
cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM = _CienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 7, 3),
    _CienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM_Type()
)
cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM.setStatus("current")
_CienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR_Type = Counter64
_CienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR_Object = MibScalar
cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR = _CienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 7, 4),
    _CienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR_Type()
)
cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR.setStatus("current")
_CienaCesCfmGlobalLossMeasurementStats_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalLossMeasurementStats = _CienaCesCfmGlobalLossMeasurementStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 8)
)
_CienaCesCfmGlobalLossMeasurementStatsTxTotalLMM_Type = Counter64
_CienaCesCfmGlobalLossMeasurementStatsTxTotalLMM_Object = MibScalar
cienaCesCfmGlobalLossMeasurementStatsTxTotalLMM = _CienaCesCfmGlobalLossMeasurementStatsTxTotalLMM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 8, 1),
    _CienaCesCfmGlobalLossMeasurementStatsTxTotalLMM_Type()
)
cienaCesCfmGlobalLossMeasurementStatsTxTotalLMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLossMeasurementStatsTxTotalLMM.setStatus("current")
_CienaCesCfmGlobalLossMeasurementStatsTxTotalLMR_Type = Counter64
_CienaCesCfmGlobalLossMeasurementStatsTxTotalLMR_Object = MibScalar
cienaCesCfmGlobalLossMeasurementStatsTxTotalLMR = _CienaCesCfmGlobalLossMeasurementStatsTxTotalLMR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 8, 2),
    _CienaCesCfmGlobalLossMeasurementStatsTxTotalLMR_Type()
)
cienaCesCfmGlobalLossMeasurementStatsTxTotalLMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLossMeasurementStatsTxTotalLMR.setStatus("current")
_CienaCesCfmGlobalLossMeasurementStatsRxTotalLMM_Type = Counter64
_CienaCesCfmGlobalLossMeasurementStatsRxTotalLMM_Object = MibScalar
cienaCesCfmGlobalLossMeasurementStatsRxTotalLMM = _CienaCesCfmGlobalLossMeasurementStatsRxTotalLMM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 8, 3),
    _CienaCesCfmGlobalLossMeasurementStatsRxTotalLMM_Type()
)
cienaCesCfmGlobalLossMeasurementStatsRxTotalLMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLossMeasurementStatsRxTotalLMM.setStatus("current")
_CienaCesCfmGlobalLossMeasurementStatsRxTotalLMR_Type = Counter64
_CienaCesCfmGlobalLossMeasurementStatsRxTotalLMR_Object = MibScalar
cienaCesCfmGlobalLossMeasurementStatsRxTotalLMR = _CienaCesCfmGlobalLossMeasurementStatsRxTotalLMR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 8, 4),
    _CienaCesCfmGlobalLossMeasurementStatsRxTotalLMR_Type()
)
cienaCesCfmGlobalLossMeasurementStatsRxTotalLMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalLossMeasurementStatsRxTotalLMR.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStats_ObjectIdentity = ObjectIdentity
cienaCesCfmGlobalSyntheticLossMeasurementStats = _CienaCesCfmGlobalSyntheticLossMeasurementStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9)
)
_CienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM = _CienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 1),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR = _CienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 2),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM = _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 3),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR = _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 4),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM = _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 5),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR = _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 6),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM = _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 7),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR = _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 8),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR.setStatus("current")
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM_Type = Counter64
_CienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM_Object = MibScalar
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM = _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 1, 9, 9),
    _CienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM_Type()
)
cienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM.setStatus("current")
_CienaCesCfmServiceStats_ObjectIdentity = ObjectIdentity
cienaCesCfmServiceStats = _CienaCesCfmServiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2)
)
_CienaCesCfmServiceStatsTable_Object = MibTable
cienaCesCfmServiceStatsTable = _CienaCesCfmServiceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTable.setStatus("current")
_CienaCesCfmServiceStatsEntry_Object = MibTableRow
cienaCesCfmServiceStatsEntry = _CienaCesCfmServiceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1)
)
cienaCesCfmServiceStatsEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsEntry.setStatus("current")
_CienaCesCfmServiceStatsTotalTx_Type = Counter64
_CienaCesCfmServiceStatsTotalTx_Object = MibTableColumn
cienaCesCfmServiceStatsTotalTx = _CienaCesCfmServiceStatsTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 1),
    _CienaCesCfmServiceStatsTotalTx_Type()
)
cienaCesCfmServiceStatsTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalTx.setStatus("current")
_CienaCesCfmServiceStatsTotalRx_Type = Counter64
_CienaCesCfmServiceStatsTotalRx_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRx = _CienaCesCfmServiceStatsTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 2),
    _CienaCesCfmServiceStatsTotalRx_Type()
)
cienaCesCfmServiceStatsTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRx.setStatus("current")
_CienaCesCfmServiceStatsTotalTxLTM_Type = Counter64
_CienaCesCfmServiceStatsTotalTxLTM_Object = MibTableColumn
cienaCesCfmServiceStatsTotalTxLTM = _CienaCesCfmServiceStatsTotalTxLTM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 3),
    _CienaCesCfmServiceStatsTotalTxLTM_Type()
)
cienaCesCfmServiceStatsTotalTxLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalTxLTM.setStatus("current")
_CienaCesCfmServiceStatsTotalTxLTR_Type = Counter64
_CienaCesCfmServiceStatsTotalTxLTR_Object = MibTableColumn
cienaCesCfmServiceStatsTotalTxLTR = _CienaCesCfmServiceStatsTotalTxLTR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 4),
    _CienaCesCfmServiceStatsTotalTxLTR_Type()
)
cienaCesCfmServiceStatsTotalTxLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalTxLTR.setStatus("current")
_CienaCesCfmServiceStatsTotalRxLTM_Type = Counter64
_CienaCesCfmServiceStatsTotalRxLTM_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRxLTM = _CienaCesCfmServiceStatsTotalRxLTM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 5),
    _CienaCesCfmServiceStatsTotalRxLTM_Type()
)
cienaCesCfmServiceStatsTotalRxLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRxLTM.setStatus("current")
_CienaCesCfmServiceStatsTotalRxLTR_Type = Counter64
_CienaCesCfmServiceStatsTotalRxLTR_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRxLTR = _CienaCesCfmServiceStatsTotalRxLTR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 6),
    _CienaCesCfmServiceStatsTotalRxLTR_Type()
)
cienaCesCfmServiceStatsTotalRxLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRxLTR.setStatus("current")
_CienaCesCfmServiceStatsTotalRxUnexpectedLTR_Type = Counter64
_CienaCesCfmServiceStatsTotalRxUnexpectedLTR_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRxUnexpectedLTR = _CienaCesCfmServiceStatsTotalRxUnexpectedLTR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 7),
    _CienaCesCfmServiceStatsTotalRxUnexpectedLTR_Type()
)
cienaCesCfmServiceStatsTotalRxUnexpectedLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRxUnexpectedLTR.setStatus("current")
_CienaCesCfmServiceStatsTotalTxLBM_Type = Counter64
_CienaCesCfmServiceStatsTotalTxLBM_Object = MibTableColumn
cienaCesCfmServiceStatsTotalTxLBM = _CienaCesCfmServiceStatsTotalTxLBM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 8),
    _CienaCesCfmServiceStatsTotalTxLBM_Type()
)
cienaCesCfmServiceStatsTotalTxLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalTxLBM.setStatus("current")
_CienaCesCfmServiceStatsTotalTxLBR_Type = Counter64
_CienaCesCfmServiceStatsTotalTxLBR_Object = MibTableColumn
cienaCesCfmServiceStatsTotalTxLBR = _CienaCesCfmServiceStatsTotalTxLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 9),
    _CienaCesCfmServiceStatsTotalTxLBR_Type()
)
cienaCesCfmServiceStatsTotalTxLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalTxLBR.setStatus("current")
_CienaCesCfmServiceStatsTotalRxLBM_Type = Counter64
_CienaCesCfmServiceStatsTotalRxLBM_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRxLBM = _CienaCesCfmServiceStatsTotalRxLBM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 10),
    _CienaCesCfmServiceStatsTotalRxLBM_Type()
)
cienaCesCfmServiceStatsTotalRxLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRxLBM.setStatus("current")
_CienaCesCfmServiceStatsTotalRxInorderLBR_Type = Counter64
_CienaCesCfmServiceStatsTotalRxInorderLBR_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRxInorderLBR = _CienaCesCfmServiceStatsTotalRxInorderLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 11),
    _CienaCesCfmServiceStatsTotalRxInorderLBR_Type()
)
cienaCesCfmServiceStatsTotalRxInorderLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRxInorderLBR.setStatus("current")
_CienaCesCfmServiceStatsTotalRxOutOforderLBR_Type = Counter64
_CienaCesCfmServiceStatsTotalRxOutOforderLBR_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRxOutOforderLBR = _CienaCesCfmServiceStatsTotalRxOutOforderLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 12),
    _CienaCesCfmServiceStatsTotalRxOutOforderLBR_Type()
)
cienaCesCfmServiceStatsTotalRxOutOforderLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRxOutOforderLBR.setStatus("current")
_CienaCesCfmServiceStatsTotalRxContentMismatchLBR_Type = Counter64
_CienaCesCfmServiceStatsTotalRxContentMismatchLBR_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRxContentMismatchLBR = _CienaCesCfmServiceStatsTotalRxContentMismatchLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 13),
    _CienaCesCfmServiceStatsTotalRxContentMismatchLBR_Type()
)
cienaCesCfmServiceStatsTotalRxContentMismatchLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRxContentMismatchLBR.setStatus("current")
_CienaCesCfmServiceStatsTotalRxUnexpectedLBR_Type = Counter64
_CienaCesCfmServiceStatsTotalRxUnexpectedLBR_Object = MibTableColumn
cienaCesCfmServiceStatsTotalRxUnexpectedLBR = _CienaCesCfmServiceStatsTotalRxUnexpectedLBR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 14),
    _CienaCesCfmServiceStatsTotalRxUnexpectedLBR_Type()
)
cienaCesCfmServiceStatsTotalRxUnexpectedLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsTotalRxUnexpectedLBR.setStatus("current")
_CienaCesCfmServiceStatsClear_Type = CienaStatsClear
_CienaCesCfmServiceStatsClear_Object = MibTableColumn
cienaCesCfmServiceStatsClear = _CienaCesCfmServiceStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 2, 1, 1, 15),
    _CienaCesCfmServiceStatsClear_Type()
)
cienaCesCfmServiceStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmServiceStatsClear.setStatus("current")
_CienaCesCfmMepStats_ObjectIdentity = ObjectIdentity
cienaCesCfmMepStats = _CienaCesCfmMepStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3)
)
_CienaCesCfmMepStatsTable_Object = MibTable
cienaCesCfmMepStatsTable = _CienaCesCfmMepStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTable.setStatus("current")
_CienaCesCfmMepStatsEntry_Object = MibTableRow
cienaCesCfmMepStatsEntry = _CienaCesCfmMepStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1)
)
cienaCesCfmMepStatsEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmMEPId"),
)
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsEntry.setStatus("current")
_CienaCesCfmMepInterfaceType_Type = CienaCesCfmInterfaceType
_CienaCesCfmMepInterfaceType_Object = MibTableColumn
cienaCesCfmMepInterfaceType = _CienaCesCfmMepInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 1),
    _CienaCesCfmMepInterfaceType_Type()
)
cienaCesCfmMepInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepInterfaceType.setStatus("current")
_CienaCesCfmMepInterfaceIndex_Type = Unsigned32
_CienaCesCfmMepInterfaceIndex_Object = MibTableColumn
cienaCesCfmMepInterfaceIndex = _CienaCesCfmMepInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 2),
    _CienaCesCfmMepInterfaceIndex_Type()
)
cienaCesCfmMepInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepInterfaceIndex.setStatus("current")
_CienaCesCfmMepStatsTxTotalCCM_Type = Counter64
_CienaCesCfmMepStatsTxTotalCCM_Object = MibTableColumn
cienaCesCfmMepStatsTxTotalCCM = _CienaCesCfmMepStatsTxTotalCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 3),
    _CienaCesCfmMepStatsTxTotalCCM_Type()
)
cienaCesCfmMepStatsTxTotalCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxTotalCCM.setStatus("current")
_CienaCesCfmMepStatsRxTotalCCM_Type = Counter64
_CienaCesCfmMepStatsRxTotalCCM_Object = MibTableColumn
cienaCesCfmMepStatsRxTotalCCM = _CienaCesCfmMepStatsRxTotalCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 4),
    _CienaCesCfmMepStatsRxTotalCCM_Type()
)
cienaCesCfmMepStatsRxTotalCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxTotalCCM.setStatus("current")
_CienaCesCfmMepStatsTxLoopbackMessages_Type = Counter64
_CienaCesCfmMepStatsTxLoopbackMessages_Object = MibTableColumn
cienaCesCfmMepStatsTxLoopbackMessages = _CienaCesCfmMepStatsTxLoopbackMessages_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 5),
    _CienaCesCfmMepStatsTxLoopbackMessages_Type()
)
cienaCesCfmMepStatsTxLoopbackMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxLoopbackMessages.setStatus("current")
_CienaCesCfmMepStatsTxLoopbackReply_Type = Counter64
_CienaCesCfmMepStatsTxLoopbackReply_Object = MibTableColumn
cienaCesCfmMepStatsTxLoopbackReply = _CienaCesCfmMepStatsTxLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 6),
    _CienaCesCfmMepStatsTxLoopbackReply_Type()
)
cienaCesCfmMepStatsTxLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxLoopbackReply.setStatus("current")
_CienaCesCfmMepStatsRxLoopbackMessages_Type = Counter64
_CienaCesCfmMepStatsRxLoopbackMessages_Object = MibTableColumn
cienaCesCfmMepStatsRxLoopbackMessages = _CienaCesCfmMepStatsRxLoopbackMessages_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 7),
    _CienaCesCfmMepStatsRxLoopbackMessages_Type()
)
cienaCesCfmMepStatsRxLoopbackMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxLoopbackMessages.setStatus("current")
_CienaCesCfmMepStatsRxInorderLoopbackReply_Type = Counter64
_CienaCesCfmMepStatsRxInorderLoopbackReply_Object = MibTableColumn
cienaCesCfmMepStatsRxInorderLoopbackReply = _CienaCesCfmMepStatsRxInorderLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 8),
    _CienaCesCfmMepStatsRxInorderLoopbackReply_Type()
)
cienaCesCfmMepStatsRxInorderLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxInorderLoopbackReply.setStatus("current")
_CienaCesCfmMepStatsRxOutoforderLoopbackReply_Type = Counter64
_CienaCesCfmMepStatsRxOutoforderLoopbackReply_Object = MibTableColumn
cienaCesCfmMepStatsRxOutoforderLoopbackReply = _CienaCesCfmMepStatsRxOutoforderLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 9),
    _CienaCesCfmMepStatsRxOutoforderLoopbackReply_Type()
)
cienaCesCfmMepStatsRxOutoforderLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxOutoforderLoopbackReply.setStatus("current")
_CienaCesCfmMepStatsRxContentMismatchLoopbackReply_Type = Counter64
_CienaCesCfmMepStatsRxContentMismatchLoopbackReply_Object = MibTableColumn
cienaCesCfmMepStatsRxContentMismatchLoopbackReply = _CienaCesCfmMepStatsRxContentMismatchLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 10),
    _CienaCesCfmMepStatsRxContentMismatchLoopbackReply_Type()
)
cienaCesCfmMepStatsRxContentMismatchLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxContentMismatchLoopbackReply.setStatus("current")
_CienaCesCfmMepStatsRxUnexpectedLoopbackReply_Type = Counter64
_CienaCesCfmMepStatsRxUnexpectedLoopbackReply_Object = MibTableColumn
cienaCesCfmMepStatsRxUnexpectedLoopbackReply = _CienaCesCfmMepStatsRxUnexpectedLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 11),
    _CienaCesCfmMepStatsRxUnexpectedLoopbackReply_Type()
)
cienaCesCfmMepStatsRxUnexpectedLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxUnexpectedLoopbackReply.setStatus("current")
_CienaCesCfmMepStatsTxLinktraceMessage_Type = Counter64
_CienaCesCfmMepStatsTxLinktraceMessage_Object = MibTableColumn
cienaCesCfmMepStatsTxLinktraceMessage = _CienaCesCfmMepStatsTxLinktraceMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 12),
    _CienaCesCfmMepStatsTxLinktraceMessage_Type()
)
cienaCesCfmMepStatsTxLinktraceMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxLinktraceMessage.setStatus("current")
_CienaCesCfmMepStatsTxLinktraceReply_Type = Counter64
_CienaCesCfmMepStatsTxLinktraceReply_Object = MibTableColumn
cienaCesCfmMepStatsTxLinktraceReply = _CienaCesCfmMepStatsTxLinktraceReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 13),
    _CienaCesCfmMepStatsTxLinktraceReply_Type()
)
cienaCesCfmMepStatsTxLinktraceReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxLinktraceReply.setStatus("current")
_CienaCesCfmMepStatsRxLinktraceMessage_Type = Counter64
_CienaCesCfmMepStatsRxLinktraceMessage_Object = MibTableColumn
cienaCesCfmMepStatsRxLinktraceMessage = _CienaCesCfmMepStatsRxLinktraceMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 14),
    _CienaCesCfmMepStatsRxLinktraceMessage_Type()
)
cienaCesCfmMepStatsRxLinktraceMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxLinktraceMessage.setStatus("current")
_CienaCesCfmMepStatsRxLinktraceReply_Type = Counter64
_CienaCesCfmMepStatsRxLinktraceReply_Object = MibTableColumn
cienaCesCfmMepStatsRxLinktraceReply = _CienaCesCfmMepStatsRxLinktraceReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 15),
    _CienaCesCfmMepStatsRxLinktraceReply_Type()
)
cienaCesCfmMepStatsRxLinktraceReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxLinktraceReply.setStatus("current")
_CienaCesCfmMepStatsRxUnexpectedLinktraceReply_Type = Counter64
_CienaCesCfmMepStatsRxUnexpectedLinktraceReply_Object = MibTableColumn
cienaCesCfmMepStatsRxUnexpectedLinktraceReply = _CienaCesCfmMepStatsRxUnexpectedLinktraceReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 16),
    _CienaCesCfmMepStatsRxUnexpectedLinktraceReply_Type()
)
cienaCesCfmMepStatsRxUnexpectedLinktraceReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxUnexpectedLinktraceReply.setStatus("current")
_CienaCesCfmMepStatsTxDelayMeasurementMessage_Type = Counter64
_CienaCesCfmMepStatsTxDelayMeasurementMessage_Object = MibTableColumn
cienaCesCfmMepStatsTxDelayMeasurementMessage = _CienaCesCfmMepStatsTxDelayMeasurementMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 17),
    _CienaCesCfmMepStatsTxDelayMeasurementMessage_Type()
)
cienaCesCfmMepStatsTxDelayMeasurementMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxDelayMeasurementMessage.setStatus("current")
_CienaCesCfmMepStatsTxDelayMeasurementReply_Type = Counter64
_CienaCesCfmMepStatsTxDelayMeasurementReply_Object = MibTableColumn
cienaCesCfmMepStatsTxDelayMeasurementReply = _CienaCesCfmMepStatsTxDelayMeasurementReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 18),
    _CienaCesCfmMepStatsTxDelayMeasurementReply_Type()
)
cienaCesCfmMepStatsTxDelayMeasurementReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxDelayMeasurementReply.setStatus("current")
_CienaCesCfmMepStatsRxDelayMeasurementMessage_Type = Counter64
_CienaCesCfmMepStatsRxDelayMeasurementMessage_Object = MibTableColumn
cienaCesCfmMepStatsRxDelayMeasurementMessage = _CienaCesCfmMepStatsRxDelayMeasurementMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 19),
    _CienaCesCfmMepStatsRxDelayMeasurementMessage_Type()
)
cienaCesCfmMepStatsRxDelayMeasurementMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxDelayMeasurementMessage.setStatus("current")
_CienaCesCfmMepStatsRxDelayMeasurementReply_Type = Counter64
_CienaCesCfmMepStatsRxDelayMeasurementReply_Object = MibTableColumn
cienaCesCfmMepStatsRxDelayMeasurementReply = _CienaCesCfmMepStatsRxDelayMeasurementReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 20),
    _CienaCesCfmMepStatsRxDelayMeasurementReply_Type()
)
cienaCesCfmMepStatsRxDelayMeasurementReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxDelayMeasurementReply.setStatus("current")
_CienaCesCfmMepStatsTxLossMeasurementMessage_Type = Counter64
_CienaCesCfmMepStatsTxLossMeasurementMessage_Object = MibTableColumn
cienaCesCfmMepStatsTxLossMeasurementMessage = _CienaCesCfmMepStatsTxLossMeasurementMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 21),
    _CienaCesCfmMepStatsTxLossMeasurementMessage_Type()
)
cienaCesCfmMepStatsTxLossMeasurementMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxLossMeasurementMessage.setStatus("current")
_CienaCesCfmMepStatsTxLossMeasurementReply_Type = Counter64
_CienaCesCfmMepStatsTxLossMeasurementReply_Object = MibTableColumn
cienaCesCfmMepStatsTxLossMeasurementReply = _CienaCesCfmMepStatsTxLossMeasurementReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 22),
    _CienaCesCfmMepStatsTxLossMeasurementReply_Type()
)
cienaCesCfmMepStatsTxLossMeasurementReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxLossMeasurementReply.setStatus("current")
_CienaCesCfmMepStatsRxLossMeasurementMessage_Type = Counter64
_CienaCesCfmMepStatsRxLossMeasurementMessage_Object = MibTableColumn
cienaCesCfmMepStatsRxLossMeasurementMessage = _CienaCesCfmMepStatsRxLossMeasurementMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 23),
    _CienaCesCfmMepStatsRxLossMeasurementMessage_Type()
)
cienaCesCfmMepStatsRxLossMeasurementMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxLossMeasurementMessage.setStatus("current")
_CienaCesCfmMepStatsRxLossMeasurementReply_Type = Counter64
_CienaCesCfmMepStatsRxLossMeasurementReply_Object = MibTableColumn
cienaCesCfmMepStatsRxLossMeasurementReply = _CienaCesCfmMepStatsRxLossMeasurementReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 24),
    _CienaCesCfmMepStatsRxLossMeasurementReply_Type()
)
cienaCesCfmMepStatsRxLossMeasurementReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxLossMeasurementReply.setStatus("current")
_CienaCesCfmMepStatsLastLBMTargetRemoteMepId_Type = Unsigned32
_CienaCesCfmMepStatsLastLBMTargetRemoteMepId_Object = MibTableColumn
cienaCesCfmMepStatsLastLBMTargetRemoteMepId = _CienaCesCfmMepStatsLastLBMTargetRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 25),
    _CienaCesCfmMepStatsLastLBMTargetRemoteMepId_Type()
)
cienaCesCfmMepStatsLastLBMTargetRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLBMTargetRemoteMepId.setStatus("current")
_CienaCesCfmMepStatsLastLBMTargetMacAddress_Type = CienaMacAddress
_CienaCesCfmMepStatsLastLBMTargetMacAddress_Object = MibTableColumn
cienaCesCfmMepStatsLastLBMTargetMacAddress = _CienaCesCfmMepStatsLastLBMTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 26),
    _CienaCesCfmMepStatsLastLBMTargetMacAddress_Type()
)
cienaCesCfmMepStatsLastLBMTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLBMTargetMacAddress.setStatus("current")
_CienaCesCfmMepStatsLastLBMPriority_Type = Unsigned32
_CienaCesCfmMepStatsLastLBMPriority_Object = MibTableColumn
cienaCesCfmMepStatsLastLBMPriority = _CienaCesCfmMepStatsLastLBMPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 27),
    _CienaCesCfmMepStatsLastLBMPriority_Type()
)
cienaCesCfmMepStatsLastLBMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLBMPriority.setStatus("current")
_CienaCesCfmMepStatsLastLBMCount_Type = Unsigned32
_CienaCesCfmMepStatsLastLBMCount_Object = MibTableColumn
cienaCesCfmMepStatsLastLBMCount = _CienaCesCfmMepStatsLastLBMCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 28),
    _CienaCesCfmMepStatsLastLBMCount_Type()
)
cienaCesCfmMepStatsLastLBMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLBMCount.setStatus("current")
_CienaCesCfmMepStatsLastLBMFirstSeqNum_Type = Unsigned32
_CienaCesCfmMepStatsLastLBMFirstSeqNum_Object = MibTableColumn
cienaCesCfmMepStatsLastLBMFirstSeqNum = _CienaCesCfmMepStatsLastLBMFirstSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 29),
    _CienaCesCfmMepStatsLastLBMFirstSeqNum_Type()
)
cienaCesCfmMepStatsLastLBMFirstSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLBMFirstSeqNum.setStatus("current")
_CienaCesCfmMepStatsLastLTMTargetRemoteMepId_Type = Unsigned32
_CienaCesCfmMepStatsLastLTMTargetRemoteMepId_Object = MibTableColumn
cienaCesCfmMepStatsLastLTMTargetRemoteMepId = _CienaCesCfmMepStatsLastLTMTargetRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 30),
    _CienaCesCfmMepStatsLastLTMTargetRemoteMepId_Type()
)
cienaCesCfmMepStatsLastLTMTargetRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLTMTargetRemoteMepId.setStatus("current")
_CienaCesCfmMepStatsLastLTMTargetMacAddress_Type = CienaMacAddress
_CienaCesCfmMepStatsLastLTMTargetMacAddress_Object = MibTableColumn
cienaCesCfmMepStatsLastLTMTargetMacAddress = _CienaCesCfmMepStatsLastLTMTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 31),
    _CienaCesCfmMepStatsLastLTMTargetMacAddress_Type()
)
cienaCesCfmMepStatsLastLTMTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLTMTargetMacAddress.setStatus("current")
_CienaCesCfmMepStatsLastLTMPriority_Type = Unsigned32
_CienaCesCfmMepStatsLastLTMPriority_Object = MibTableColumn
cienaCesCfmMepStatsLastLTMPriority = _CienaCesCfmMepStatsLastLTMPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 32),
    _CienaCesCfmMepStatsLastLTMPriority_Type()
)
cienaCesCfmMepStatsLastLTMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLTMPriority.setStatus("current")
_CienaCesCfmMepStatsLastLTMSeqNum_Type = Unsigned32
_CienaCesCfmMepStatsLastLTMSeqNum_Object = MibTableColumn
cienaCesCfmMepStatsLastLTMSeqNum = _CienaCesCfmMepStatsLastLTMSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 33),
    _CienaCesCfmMepStatsLastLTMSeqNum_Type()
)
cienaCesCfmMepStatsLastLTMSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLTMSeqNum.setStatus("current")
_CienaCesCfmMepStatsLastLTMInitialTTL_Type = Unsigned32
_CienaCesCfmMepStatsLastLTMInitialTTL_Object = MibTableColumn
cienaCesCfmMepStatsLastLTMInitialTTL = _CienaCesCfmMepStatsLastLTMInitialTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 34),
    _CienaCesCfmMepStatsLastLTMInitialTTL_Type()
)
cienaCesCfmMepStatsLastLTMInitialTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLTMInitialTTL.setStatus("current")
_CienaCesCfmMepStatsLastDMMTargetRemoteMepId_Type = Unsigned32
_CienaCesCfmMepStatsLastDMMTargetRemoteMepId_Object = MibTableColumn
cienaCesCfmMepStatsLastDMMTargetRemoteMepId = _CienaCesCfmMepStatsLastDMMTargetRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 35),
    _CienaCesCfmMepStatsLastDMMTargetRemoteMepId_Type()
)
cienaCesCfmMepStatsLastDMMTargetRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastDMMTargetRemoteMepId.setStatus("current")
_CienaCesCfmMepStatsLastDMMTargetMacAddress_Type = CienaMacAddress
_CienaCesCfmMepStatsLastDMMTargetMacAddress_Object = MibTableColumn
cienaCesCfmMepStatsLastDMMTargetMacAddress = _CienaCesCfmMepStatsLastDMMTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 36),
    _CienaCesCfmMepStatsLastDMMTargetMacAddress_Type()
)
cienaCesCfmMepStatsLastDMMTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastDMMTargetMacAddress.setStatus("current")
_CienaCesCfmMepStatsLastDMMPriority_Type = Unsigned32
_CienaCesCfmMepStatsLastDMMPriority_Object = MibTableColumn
cienaCesCfmMepStatsLastDMMPriority = _CienaCesCfmMepStatsLastDMMPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 37),
    _CienaCesCfmMepStatsLastDMMPriority_Type()
)
cienaCesCfmMepStatsLastDMMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastDMMPriority.setStatus("current")
_CienaCesCfmMepStatsLastDMMRepeatInterval_Type = Unsigned32
_CienaCesCfmMepStatsLastDMMRepeatInterval_Object = MibTableColumn
cienaCesCfmMepStatsLastDMMRepeatInterval = _CienaCesCfmMepStatsLastDMMRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 38),
    _CienaCesCfmMepStatsLastDMMRepeatInterval_Type()
)
cienaCesCfmMepStatsLastDMMRepeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastDMMRepeatInterval.setStatus("current")
_CienaCesCfmMepStatsLastDMMNumOfDmmToSend_Type = Unsigned32
_CienaCesCfmMepStatsLastDMMNumOfDmmToSend_Object = MibTableColumn
cienaCesCfmMepStatsLastDMMNumOfDmmToSend = _CienaCesCfmMepStatsLastDMMNumOfDmmToSend_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 39),
    _CienaCesCfmMepStatsLastDMMNumOfDmmToSend_Type()
)
cienaCesCfmMepStatsLastDMMNumOfDmmToSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastDMMNumOfDmmToSend.setStatus("current")
_CienaCesCfmMepStatsLastLMMTargetRemoteMepId_Type = Unsigned32
_CienaCesCfmMepStatsLastLMMTargetRemoteMepId_Object = MibTableColumn
cienaCesCfmMepStatsLastLMMTargetRemoteMepId = _CienaCesCfmMepStatsLastLMMTargetRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 40),
    _CienaCesCfmMepStatsLastLMMTargetRemoteMepId_Type()
)
cienaCesCfmMepStatsLastLMMTargetRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLMMTargetRemoteMepId.setStatus("current")
_CienaCesCfmMepStatsLastLMMTargetMacAddress_Type = CienaMacAddress
_CienaCesCfmMepStatsLastLMMTargetMacAddress_Object = MibTableColumn
cienaCesCfmMepStatsLastLMMTargetMacAddress = _CienaCesCfmMepStatsLastLMMTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 41),
    _CienaCesCfmMepStatsLastLMMTargetMacAddress_Type()
)
cienaCesCfmMepStatsLastLMMTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLMMTargetMacAddress.setStatus("current")
_CienaCesCfmMepStatsLastLMMPriority_Type = Unsigned32
_CienaCesCfmMepStatsLastLMMPriority_Object = MibTableColumn
cienaCesCfmMepStatsLastLMMPriority = _CienaCesCfmMepStatsLastLMMPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 42),
    _CienaCesCfmMepStatsLastLMMPriority_Type()
)
cienaCesCfmMepStatsLastLMMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLMMPriority.setStatus("current")
_CienaCesCfmMepStatsLastLMMRepeatInterval_Type = Unsigned32
_CienaCesCfmMepStatsLastLMMRepeatInterval_Object = MibTableColumn
cienaCesCfmMepStatsLastLMMRepeatInterval = _CienaCesCfmMepStatsLastLMMRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 43),
    _CienaCesCfmMepStatsLastLMMRepeatInterval_Type()
)
cienaCesCfmMepStatsLastLMMRepeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLMMRepeatInterval.setStatus("current")
_CienaCesCfmMepStatsLastLMMNumOfLmmToSend_Type = Unsigned32
_CienaCesCfmMepStatsLastLMMNumOfLmmToSend_Object = MibTableColumn
cienaCesCfmMepStatsLastLMMNumOfLmmToSend = _CienaCesCfmMepStatsLastLMMNumOfLmmToSend_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 44),
    _CienaCesCfmMepStatsLastLMMNumOfLmmToSend_Type()
)
cienaCesCfmMepStatsLastLMMNumOfLmmToSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsLastLMMNumOfLmmToSend.setStatus("current")
_CienaCesCfmMepStatsNextLBMSeqNumber_Type = Counter32
_CienaCesCfmMepStatsNextLBMSeqNumber_Object = MibTableColumn
cienaCesCfmMepStatsNextLBMSeqNumber = _CienaCesCfmMepStatsNextLBMSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 45),
    _CienaCesCfmMepStatsNextLBMSeqNumber_Type()
)
cienaCesCfmMepStatsNextLBMSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsNextLBMSeqNumber.setStatus("current")
_CienaCesCfmMepStatsNextLTMSeqNumber_Type = Counter32
_CienaCesCfmMepStatsNextLTMSeqNumber_Object = MibTableColumn
cienaCesCfmMepStatsNextLTMSeqNumber = _CienaCesCfmMepStatsNextLTMSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 46),
    _CienaCesCfmMepStatsNextLTMSeqNumber_Type()
)
cienaCesCfmMepStatsNextLTMSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsNextLTMSeqNumber.setStatus("current")
_CienaCesCfmMepStatsTxSyntheticLossMeasurementMessage_Type = Counter64
_CienaCesCfmMepStatsTxSyntheticLossMeasurementMessage_Object = MibTableColumn
cienaCesCfmMepStatsTxSyntheticLossMeasurementMessage = _CienaCesCfmMepStatsTxSyntheticLossMeasurementMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 47),
    _CienaCesCfmMepStatsTxSyntheticLossMeasurementMessage_Type()
)
cienaCesCfmMepStatsTxSyntheticLossMeasurementMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxSyntheticLossMeasurementMessage.setStatus("current")
_CienaCesCfmMepStatsTxSyntheticLossMeasurementReply_Type = Counter64
_CienaCesCfmMepStatsTxSyntheticLossMeasurementReply_Object = MibTableColumn
cienaCesCfmMepStatsTxSyntheticLossMeasurementReply = _CienaCesCfmMepStatsTxSyntheticLossMeasurementReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 48),
    _CienaCesCfmMepStatsTxSyntheticLossMeasurementReply_Type()
)
cienaCesCfmMepStatsTxSyntheticLossMeasurementReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsTxSyntheticLossMeasurementReply.setStatus("current")
_CienaCesCfmMepStatsRxSyntheticLossMeasurementMessage_Type = Counter64
_CienaCesCfmMepStatsRxSyntheticLossMeasurementMessage_Object = MibTableColumn
cienaCesCfmMepStatsRxSyntheticLossMeasurementMessage = _CienaCesCfmMepStatsRxSyntheticLossMeasurementMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 49),
    _CienaCesCfmMepStatsRxSyntheticLossMeasurementMessage_Type()
)
cienaCesCfmMepStatsRxSyntheticLossMeasurementMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxSyntheticLossMeasurementMessage.setStatus("current")
_CienaCesCfmMepStatsRxSyntheticLossMeasurementReply_Type = Counter64
_CienaCesCfmMepStatsRxSyntheticLossMeasurementReply_Object = MibTableColumn
cienaCesCfmMepStatsRxSyntheticLossMeasurementReply = _CienaCesCfmMepStatsRxSyntheticLossMeasurementReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 50),
    _CienaCesCfmMepStatsRxSyntheticLossMeasurementReply_Type()
)
cienaCesCfmMepStatsRxSyntheticLossMeasurementReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxSyntheticLossMeasurementReply.setStatus("current")
_CienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage_Type = Counter64
_CienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage_Object = MibTableColumn
cienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage = _CienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 51),
    _CienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage_Type()
)
cienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage.setStatus("current")
_CienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply_Type = Counter64
_CienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply_Object = MibTableColumn
cienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply = _CienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 52),
    _CienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply_Type()
)
cienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply.setStatus("current")
_CienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage_Type = Counter64
_CienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage_Object = MibTableColumn
cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage = _CienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 53),
    _CienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage_Type()
)
cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage.setStatus("current")
_CienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply_Type = Counter64
_CienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply_Object = MibTableColumn
cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply = _CienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 54),
    _CienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply_Type()
)
cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply.setStatus("current")
_CienaCesCfmMepStatsRxCCMWithErrorCCMFault_Type = Counter64
_CienaCesCfmMepStatsRxCCMWithErrorCCMFault_Object = MibTableColumn
cienaCesCfmMepStatsRxCCMWithErrorCCMFault = _CienaCesCfmMepStatsRxCCMWithErrorCCMFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 55),
    _CienaCesCfmMepStatsRxCCMWithErrorCCMFault_Type()
)
cienaCesCfmMepStatsRxCCMWithErrorCCMFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxCCMWithErrorCCMFault.setStatus("current")
_CienaCesCfmMepStatsRxCCMWithXCONFault_Type = Counter64
_CienaCesCfmMepStatsRxCCMWithXCONFault_Object = MibTableColumn
cienaCesCfmMepStatsRxCCMWithXCONFault = _CienaCesCfmMepStatsRxCCMWithXCONFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 56),
    _CienaCesCfmMepStatsRxCCMWithXCONFault_Type()
)
cienaCesCfmMepStatsRxCCMWithXCONFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxCCMWithXCONFault.setStatus("current")
_CienaCesCfmMepStatsRxCCMWithRMEPLOCFault_Type = Counter64
_CienaCesCfmMepStatsRxCCMWithRMEPLOCFault_Object = MibTableColumn
cienaCesCfmMepStatsRxCCMWithRMEPLOCFault = _CienaCesCfmMepStatsRxCCMWithRMEPLOCFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 57),
    _CienaCesCfmMepStatsRxCCMWithRMEPLOCFault_Type()
)
cienaCesCfmMepStatsRxCCMWithRMEPLOCFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxCCMWithRMEPLOCFault.setStatus("current")
_CienaCesCfmMepStatsRxCCMWithRDI0_Type = Counter64
_CienaCesCfmMepStatsRxCCMWithRDI0_Object = MibTableColumn
cienaCesCfmMepStatsRxCCMWithRDI0 = _CienaCesCfmMepStatsRxCCMWithRDI0_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 58),
    _CienaCesCfmMepStatsRxCCMWithRDI0_Type()
)
cienaCesCfmMepStatsRxCCMWithRDI0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxCCMWithRDI0.setStatus("current")
_CienaCesCfmMepStatsRxCCMWithRDI1_Type = Counter64
_CienaCesCfmMepStatsRxCCMWithRDI1_Object = MibTableColumn
cienaCesCfmMepStatsRxCCMWithRDI1 = _CienaCesCfmMepStatsRxCCMWithRDI1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 59),
    _CienaCesCfmMepStatsRxCCMWithRDI1_Type()
)
cienaCesCfmMepStatsRxCCMWithRDI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxCCMWithRDI1.setStatus("current")
_CienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch_Type = Counter64
_CienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch_Object = MibTableColumn
cienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch = _CienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 60),
    _CienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch_Type()
)
cienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch.setStatus("current")
_CienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv_Type = Counter64
_CienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv_Object = MibTableColumn
cienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv = _CienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 61),
    _CienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv_Type()
)
cienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv.setStatus("current")
_CienaCesCfmMepStatsToTxLoopbackMessages_Type = Counter64
_CienaCesCfmMepStatsToTxLoopbackMessages_Object = MibTableColumn
cienaCesCfmMepStatsToTxLoopbackMessages = _CienaCesCfmMepStatsToTxLoopbackMessages_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 1, 1, 62),
    _CienaCesCfmMepStatsToTxLoopbackMessages_Type()
)
cienaCesCfmMepStatsToTxLoopbackMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmMepStatsToTxLoopbackMessages.setStatus("current")
_CienaCesCfmRemoteMepStatsTable_Object = MibTable
cienaCesCfmRemoteMepStatsTable = _CienaCesCfmRemoteMepStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMepStatsTable.setStatus("current")
_CienaCesCfmRemoteMepStatsEntry_Object = MibTableRow
cienaCesCfmRemoteMepStatsEntry = _CienaCesCfmRemoteMepStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 2, 1)
)
cienaCesCfmRemoteMepStatsEntry.setIndexNames(
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmServiceIndex"),
    (0, "CIENA-CES-CFM-MIB", "cienaCesCfmRemoteMEPID"),
)
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMepStatsEntry.setStatus("current")
_CienaCesCfmRemoteMepStatsRxTotalCCM_Type = Counter32
_CienaCesCfmRemoteMepStatsRxTotalCCM_Object = MibTableColumn
cienaCesCfmRemoteMepStatsRxTotalCCM = _CienaCesCfmRemoteMepStatsRxTotalCCM_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 2, 1, 1),
    _CienaCesCfmRemoteMepStatsRxTotalCCM_Type()
)
cienaCesCfmRemoteMepStatsRxTotalCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMepStatsRxTotalCCM.setStatus("current")
_CienaCesCfmRemoteMepStatsLastSeqNum_Type = Unsigned32
_CienaCesCfmRemoteMepStatsLastSeqNum_Object = MibTableColumn
cienaCesCfmRemoteMepStatsLastSeqNum = _CienaCesCfmRemoteMepStatsLastSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 2, 1, 2),
    _CienaCesCfmRemoteMepStatsLastSeqNum_Type()
)
cienaCesCfmRemoteMepStatsLastSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMepStatsLastSeqNum.setStatus("current")
_CienaCesCfmRemoteMepStatsCCMSeqErrors_Type = Unsigned32
_CienaCesCfmRemoteMepStatsCCMSeqErrors_Object = MibTableColumn
cienaCesCfmRemoteMepStatsCCMSeqErrors = _CienaCesCfmRemoteMepStatsCCMSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 2, 1, 3),
    _CienaCesCfmRemoteMepStatsCCMSeqErrors_Type()
)
cienaCesCfmRemoteMepStatsCCMSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMepStatsCCMSeqErrors.setStatus("current")
_CienaCesCfmRemoteMepStatsClear_Type = CienaStatsClear
_CienaCesCfmRemoteMepStatsClear_Object = MibTableColumn
cienaCesCfmRemoteMepStatsClear = _CienaCesCfmRemoteMepStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 4, 1, 3, 2, 1, 4),
    _CienaCesCfmRemoteMepStatsClear_Type()
)
cienaCesCfmRemoteMepStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesCfmRemoteMepStatsClear.setStatus("current")

# Managed Objects groups


# Notification objects

cienaCesCfmFaultTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 1)
)
cienaCesCfmFaultTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceType"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceValue"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceAdminState"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceOperState"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceMdLevel"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceFaultTime"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceFaultType"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceFaultDesc"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceFaultMep"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceVsPbtName"))
)
if mibBuilder.loadTexts:
    cienaCesCfmFaultTrapSet.setStatus(
        "current"
    )

cienaCesCfmFaultTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 2)
)
cienaCesCfmFaultTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceType"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceValue"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceAdminState"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceOperState"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceMdLevel"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceVsPbtName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceFaultTime"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceFaultType"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceFaultDesc"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceFaultMep"))
)
if mibBuilder.loadTexts:
    cienaCesCfmFaultTrapClear.setStatus(
        "current"
    )

cienaCesCfmAverageDelayFaultTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 3)
)
cienaCesCfmAverageDelayFaultTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageDelayThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageDelay"))
)
if mibBuilder.loadTexts:
    cienaCesCfmAverageDelayFaultTrapSet.setStatus(
        "current"
    )

cienaCesCfmAverageDelayFaultTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 4)
)
cienaCesCfmAverageDelayFaultTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageDelayThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageDelay"))
)
if mibBuilder.loadTexts:
    cienaCesCfmAverageDelayFaultTrapClear.setStatus(
        "current"
    )

cienaCesCfmMaximumDelayFaultTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 5)
)
cienaCesCfmMaximumDelayFaultTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumDelayThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumDelay"))
)
if mibBuilder.loadTexts:
    cienaCesCfmMaximumDelayFaultTrapSet.setStatus(
        "current"
    )

cienaCesCfmMaximumDelayFaultTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 6)
)
cienaCesCfmMaximumDelayFaultTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumDelayThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumDelay"))
)
if mibBuilder.loadTexts:
    cienaCesCfmMaximumDelayFaultTrapClear.setStatus(
        "current"
    )

cienaCesCfmAverageJitterTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 7)
)
cienaCesCfmAverageJitterTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageJitterThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageJitter"))
)
if mibBuilder.loadTexts:
    cienaCesCfmAverageJitterTrapSet.setStatus(
        "current"
    )

cienaCesCfmAverageJitterTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 8)
)
cienaCesCfmAverageJitterTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageJitterThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageJitter"))
)
if mibBuilder.loadTexts:
    cienaCesCfmAverageJitterTrapClear.setStatus(
        "current"
    )

cienaCesCfmMaximumJitterTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 9)
)
cienaCesCfmMaximumJitterTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumJitterThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumJitter"))
)
if mibBuilder.loadTexts:
    cienaCesCfmMaximumJitterTrapSet.setStatus(
        "current"
    )

cienaCesCfmMaximumJitterTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 10)
)
cienaCesCfmMaximumJitterTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumJitterThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumJitter"))
)
if mibBuilder.loadTexts:
    cienaCesCfmMaximumJitterTrapClear.setStatus(
        "current"
    )

cienaCesCfmFrameLossNearTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 11)
)
cienaCesCfmFrameLossNearTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgNearLossThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgFrameLossNear"))
)
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossNearTrapSet.setStatus(
        "current"
    )

cienaCesCfmFrameLossNearTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 12)
)
cienaCesCfmFrameLossNearTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgNearLossThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgFrameLossNear"))
)
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossNearTrapClear.setStatus(
        "current"
    )

cienaCesCfmFrameLossFarTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 13)
)
cienaCesCfmFrameLossFarTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgFarLossThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgFrameLossFar"))
)
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossFarTrapSet.setStatus(
        "current"
    )

cienaCesCfmFrameLossFarTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 14)
)
cienaCesCfmFrameLossFarTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgFarLossThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmFrameLossMsgFrameLossFar"))
)
if mibBuilder.loadTexts:
    cienaCesCfmFrameLossFarTrapClear.setStatus(
        "current"
    )

cienaCesSyntheticLossSessionNearFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 15)
)
cienaCesSyntheticLossSessionNearFaultTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionFrameLossNear"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionLossNearThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesSyntheticLossSessionNearFaultTrap.setStatus(
        "current"
    )

cienaCesSyntheticLossSessionFarFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 16)
)
cienaCesSyntheticLossSessionFarFaultTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionFrameLossFar"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionLossFarThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesSyntheticLossSessionFarFaultTrap.setStatus(
        "current"
    )

cienaCesSyntheticLossSessionNearFaultClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 17)
)
cienaCesSyntheticLossSessionNearFaultClearTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionFrameLossNear"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionLossNearThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesSyntheticLossSessionNearFaultClearTrap.setStatus(
        "current"
    )

cienaCesSyntheticLossSessionFarFaultClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 18)
)
cienaCesSyntheticLossSessionFarFaultClearTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionFrameLossFar"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionLossFarThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesSyntheticLossSessionFarFaultClearTrap.setStatus(
        "current"
    )

cienaCesCfmAverageDelayVariationTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 19)
)
cienaCesCfmAverageDelayVariationTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageDelayVariationThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageDelayVariation"))
)
if mibBuilder.loadTexts:
    cienaCesCfmAverageDelayVariationTrapSet.setStatus(
        "current"
    )

cienaCesCfmAverageDelayVariationTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 20)
)
cienaCesCfmAverageDelayVariationTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageDelayVariationThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgAverageDelayVariation"))
)
if mibBuilder.loadTexts:
    cienaCesCfmAverageDelayVariationTrapClear.setStatus(
        "current"
    )

cienaCesCfmMaximumDelayVariationTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 21)
)
cienaCesCfmMaximumDelayVariationTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumDelayVariationThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumDelayVariation"))
)
if mibBuilder.loadTexts:
    cienaCesCfmMaximumDelayVariationTrapSet.setStatus(
        "current"
    )

cienaCesCfmMaximumDelayVariationTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 22)
)
cienaCesCfmMaximumDelayVariationTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgLocalMEPId"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumDelayVariationThreshold"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmDelayMsgMaximumDelayVariation"))
)
if mibBuilder.loadTexts:
    cienaCesCfmMaximumDelayVariationTrapClear.setStatus(
        "current"
    )

cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 23)
)
cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionFrameLossNear"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionFrameLossFar"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionSdSetThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapSet.setStatus(
        "current"
    )

cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 5, 0, 24)
)
cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmServiceName"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionFrameLossNear"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionFrameLossFar"),
        ("CIENA-CES-CFM-MIB", "cienaCesCfmSyntheticLossSessionSdClearThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-CFM-MIB",
    **{"CfmDisplayString": CfmDisplayString,
       "CienaCesCfmInterfaceType": CienaCesCfmInterfaceType,
       "EthType": EthType,
       "CfmFrameLossRatio": CfmFrameLossRatio,
       "cienaCesCfmMIB": cienaCesCfmMIB,
       "cienaCesCfmMIBObjects": cienaCesCfmMIBObjects,
       "cienaCesCfmService": cienaCesCfmService,
       "cienaCesCfmServiceTable": cienaCesCfmServiceTable,
       "cienaCesCfmServiceEntry": cienaCesCfmServiceEntry,
       "cienaCesCfmServiceIndex": cienaCesCfmServiceIndex,
       "cienaCesCfmServiceType": cienaCesCfmServiceType,
       "cienaCesCfmServiceValue": cienaCesCfmServiceValue,
       "cienaCesCfmServiceAdminState": cienaCesCfmServiceAdminState,
       "cienaCesCfmServiceOperState": cienaCesCfmServiceOperState,
       "cienaCesCfmServiceName": cienaCesCfmServiceName,
       "cienaCesCfmServiceMdLevel": cienaCesCfmServiceMdLevel,
       "cienaCesCfmServiceFaultState": cienaCesCfmServiceFaultState,
       "cienaCesCfmServiceAlarmTime": cienaCesCfmServiceAlarmTime,
       "cienaCesCfmServiceCCMInterval": cienaCesCfmServiceCCMInterval,
       "cienaCesCfmServiceResetTime": cienaCesCfmServiceResetTime,
       "cienaCesCfmServiceLastFaultCCM": cienaCesCfmServiceLastFaultCCM,
       "cienaCesCfmServiceRMEPFailureFlag": cienaCesCfmServiceRMEPFailureFlag,
       "cienaCesCfmServiceCCMErrorFlag": cienaCesCfmServiceCCMErrorFlag,
       "cienaCesCfmServiceCrossConnectErrorFlag": cienaCesCfmServiceCrossConnectErrorFlag,
       "cienaCesCfmServiceNumMEP": cienaCesCfmServiceNumMEP,
       "cienaCesCfmServiceNumRemoteMEP": cienaCesCfmServiceNumRemoteMEP,
       "cienaCesCfmServiceNumActiveMEP": cienaCesCfmServiceNumActiveMEP,
       "cienaCesCfmServiceNextMepId": cienaCesCfmServiceNextMepId,
       "cienaCesCfmServiceAlarmPriority": cienaCesCfmServiceAlarmPriority,
       "cienaCesCfmServiceNumCCMForFault": cienaCesCfmServiceNumCCMForFault,
       "cienaCesCfmServiceDMMInterval": cienaCesCfmServiceDMMInterval,
       "cienaCesCfmServiceLMMInterval": cienaCesCfmServiceLMMInterval,
       "cienaCesCfmServiceCCMLossStatsState": cienaCesCfmServiceCCMLossStatsState,
       "cienaCesCfmServiceCCMLossBucketInterval": cienaCesCfmServiceCCMLossBucketInterval,
       "cienaCesCfmServiceY1731": cienaCesCfmServiceY1731,
       "cienaCesCfmServiceTlvSenderIdType": cienaCesCfmServiceTlvSenderIdType,
       "cienaCesCfmServiceRMEPHoldTime": cienaCesCfmServiceRMEPHoldTime,
       "cienaCesCfmServiceCCMTxState": cienaCesCfmServiceCCMTxState,
       "cienaCesCfmServicePortStatusFlag": cienaCesCfmServicePortStatusFlag,
       "cienaCesCfmServiceRDIFlag": cienaCesCfmServiceRDIFlag,
       "cienaCesCfmServiceInstabilityFlag": cienaCesCfmServiceInstabilityFlag,
       "cienaCesCfmServiceRMEPAging": cienaCesCfmServiceRMEPAging,
       "cienaCesCfmServiceRMEPDiscovery": cienaCesCfmServiceRMEPDiscovery,
       "cienaCesCfmServiceChargedAgainstGlobalBudget": cienaCesCfmServiceChargedAgainstGlobalBudget,
       "cienaCesCfmServiceControlModuleFrameBudget": cienaCesCfmServiceControlModuleFrameBudget,
       "cienaCesCfmServiceMulticastDa": cienaCesCfmServiceMulticastDa,
       "cienaCesCfmServiceCCMRxStats": cienaCesCfmServiceCCMRxStats,
       "cienaCesCfmMEP": cienaCesCfmMEP,
       "cienaCesCfmMEPTable": cienaCesCfmMEPTable,
       "cienaCesCfmMEPEntry": cienaCesCfmMEPEntry,
       "cienaCesCfmMEPId": cienaCesCfmMEPId,
       "cienaCesCfmMEPMacAddr": cienaCesCfmMEPMacAddr,
       "cienaCesCfmMEPAdminState": cienaCesCfmMEPAdminState,
       "cienaCesCfmMEPOperState": cienaCesCfmMEPOperState,
       "cienaCesCfmMEPDirection": cienaCesCfmMEPDirection,
       "cienaCesCfmMEPCCMState": cienaCesCfmMEPCCMState,
       "cienaCesCfmMEPCCMPriority": cienaCesCfmMEPCCMPriority,
       "cienaCesCfmMEPLTMPriority": cienaCesCfmMEPLTMPriority,
       "cienaCesCfmMEPLiType": cienaCesCfmMEPLiType,
       "cienaCesCfmMEPLiIndex": cienaCesCfmMEPLiIndex,
       "cienaCesCfmMEPServiceName": cienaCesCfmMEPServiceName,
       "cienaCesCfmMEPSubPortName": cienaCesCfmMEPSubPortName,
       "cienaCesCfmMEPVsPbtName": cienaCesCfmMEPVsPbtName,
       "cienaCesCfmMEPLogicalPortName": cienaCesCfmMEPLogicalPortName,
       "cienaCesCfmMEPSubPortIndex": cienaCesCfmMEPSubPortIndex,
       "cienaCesCfmMEPEncapsulation": cienaCesCfmMEPEncapsulation,
       "cienaCesCfmMEPLeadPortSlotIndex": cienaCesCfmMEPLeadPortSlotIndex,
       "cienaCesCfmMEPPBTBvid": cienaCesCfmMEPPBTBvid,
       "cienaCesCfmMEPPBTEtype": cienaCesCfmMEPPBTEtype,
       "cienaCesCfmMEPL2XformType": cienaCesCfmMEPL2XformType,
       "cienaCesCfmMEPSignalDegradeMonitoringStatus": cienaCesCfmMEPSignalDegradeMonitoringStatus,
       "cienaCesCfmMEPSignalDegradeTriggerMode": cienaCesCfmMEPSignalDegradeTriggerMode,
       "cienaCesCfmRemoteMEP": cienaCesCfmRemoteMEP,
       "cienaCesCfmRemoteMEPTable": cienaCesCfmRemoteMEPTable,
       "cienaCesCfmRemoteMEPEntry": cienaCesCfmRemoteMEPEntry,
       "cienaCesCfmRemoteMEPID": cienaCesCfmRemoteMEPID,
       "cienaCesCfmRemoteMEPMacAddr": cienaCesCfmRemoteMEPMacAddr,
       "cienaCesCfmRemoteMEPAdminState": cienaCesCfmRemoteMEPAdminState,
       "cienaCesCfmRemoteMEPOperState": cienaCesCfmRemoteMEPOperState,
       "cienaCesCfmRemoteMEPTime": cienaCesCfmRemoteMEPTime,
       "cienaCesCfmRemoteMEPKLastMacStatus": cienaCesCfmRemoteMEPKLastMacStatus,
       "cienaCesCfmRemoteMEPFailureFlag": cienaCesCfmRemoteMEPFailureFlag,
       "cienaCesCfmRemoteMEPCCMErrorFlag": cienaCesCfmRemoteMEPCCMErrorFlag,
       "cienaCesCfmRemoteMEPRDIErrorFlag": cienaCesCfmRemoteMEPRDIErrorFlag,
       "cienaCesCfmRemoteMEPSubPortName": cienaCesCfmRemoteMEPSubPortName,
       "cienaCesCfmRemoteMEPServiceName": cienaCesCfmRemoteMEPServiceName,
       "cienaCesCfmRemoteMEPLastPortStatus": cienaCesCfmRemoteMEPLastPortStatus,
       "cienaCesCfmRemoteMEPLastInterfaceStatus": cienaCesCfmRemoteMEPLastInterfaceStatus,
       "cienaCesCfmRemoteMEPCCMLevel": cienaCesCfmRemoteMEPCCMLevel,
       "cienaCesCfmRemoteMEPHoldState": cienaCesCfmRemoteMEPHoldState,
       "cienaCesCfmDelay": cienaCesCfmDelay,
       "cienaCesCfmDelayMsgTable": cienaCesCfmDelayMsgTable,
       "cienaCesCfmDelayMsgEntry": cienaCesCfmDelayMsgEntry,
       "cienaCesCfmDelayMsgLocalMEPId": cienaCesCfmDelayMsgLocalMEPId,
       "cienaCesCfmDelayMsgTargetMEPID": cienaCesCfmDelayMsgTargetMEPID,
       "cienaCesCfmDelayMsgServiceName": cienaCesCfmDelayMsgServiceName,
       "cienaCesCfmDelayMsgAverageDelayThreshold": cienaCesCfmDelayMsgAverageDelayThreshold,
       "cienaCesCfmDelayMsgAverageJitterThreshold": cienaCesCfmDelayMsgAverageJitterThreshold,
       "cienaCesCfmDelayMsgMaximumDelayThreshold": cienaCesCfmDelayMsgMaximumDelayThreshold,
       "cienaCesCfmDelayMsgMaximumJitterThreshold": cienaCesCfmDelayMsgMaximumJitterThreshold,
       "cienaCesCfmDelayMsgAverageDelay": cienaCesCfmDelayMsgAverageDelay,
       "cienaCesCfmDelayMsgAverageJitter": cienaCesCfmDelayMsgAverageJitter,
       "cienaCesCfmDelayMsgMaximumDelay": cienaCesCfmDelayMsgMaximumDelay,
       "cienaCesCfmDelayMsgMaximumJitter": cienaCesCfmDelayMsgMaximumJitter,
       "cienaCesCfmDelayMsgMinimumDelay": cienaCesCfmDelayMsgMinimumDelay,
       "cienaCesCfmDelayMsgMinimumJitter": cienaCesCfmDelayMsgMinimumJitter,
       "cienaCesCfmDelayMsgAverageDelayVariation": cienaCesCfmDelayMsgAverageDelayVariation,
       "cienaCesCfmDelayMsgMaximumDelayVariation": cienaCesCfmDelayMsgMaximumDelayVariation,
       "cienaCesCfmDelayMsgMinimumDelayVariation": cienaCesCfmDelayMsgMinimumDelayVariation,
       "cienaCesCfmDelayMsgAverageDelayVariationThreshold": cienaCesCfmDelayMsgAverageDelayVariationThreshold,
       "cienaCesCfmDelayMsgMaximumDelayVariationThreshold": cienaCesCfmDelayMsgMaximumDelayVariationThreshold,
       "cienaCesCfmDelayMsgPriority": cienaCesCfmDelayMsgPriority,
       "cienaCesCfmDelayMsgCount": cienaCesCfmDelayMsgCount,
       "cienaCesCfmDelayMsgIterations": cienaCesCfmDelayMsgIterations,
       "cienaCesCfmDelayMsgRepeatDelay": cienaCesCfmDelayMsgRepeatDelay,
       "cienaCesCfmDelayMsgDuration": cienaCesCfmDelayMsgDuration,
       "cienaCesCfmFrameLoss": cienaCesCfmFrameLoss,
       "cienaCesCfmFrameLossMsgTable": cienaCesCfmFrameLossMsgTable,
       "cienaCesCfmFrameLossMsgEntry": cienaCesCfmFrameLossMsgEntry,
       "cienaCesCfmFrameLossMsgLocalMEPId": cienaCesCfmFrameLossMsgLocalMEPId,
       "cienaCesCfmFrameLossMsgTargetMEPID": cienaCesCfmFrameLossMsgTargetMEPID,
       "cienaCesCfmFrameLossMsgNearLossThreshold": cienaCesCfmFrameLossMsgNearLossThreshold,
       "cienaCesCfmFrameLossMsgFarLossThreshold": cienaCesCfmFrameLossMsgFarLossThreshold,
       "cienaCesCfmFrameLossMsgServiceName": cienaCesCfmFrameLossMsgServiceName,
       "cienaCesCfmFrameLossMsgFrameLossNear": cienaCesCfmFrameLossMsgFrameLossNear,
       "cienaCesCfmFrameLossMsgFrameLossFar": cienaCesCfmFrameLossMsgFrameLossFar,
       "cienaCesCfmServiceFaultNotifAttrs": cienaCesCfmServiceFaultNotifAttrs,
       "cienaCesCfmServiceFaultNotifTable": cienaCesCfmServiceFaultNotifTable,
       "cienaCesCfmServiceFaultNotifEntry": cienaCesCfmServiceFaultNotifEntry,
       "cienaCesCfmServiceFaultTime": cienaCesCfmServiceFaultTime,
       "cienaCesCfmServiceFaultType": cienaCesCfmServiceFaultType,
       "cienaCesCfmServiceFaultDesc": cienaCesCfmServiceFaultDesc,
       "cienaCesCfmServiceFaultMep": cienaCesCfmServiceFaultMep,
       "cienaCesCfmServiceVsPbtName": cienaCesCfmServiceVsPbtName,
       "cienaCesCfmMaintenance": cienaCesCfmMaintenance,
       "cienaCesCfmMaintenanceDomainTable": cienaCesCfmMaintenanceDomainTable,
       "cienaCesCfmMaintenanceDomainEntry": cienaCesCfmMaintenanceDomainEntry,
       "cienaCesCfmMaintenanceDomainIndex": cienaCesCfmMaintenanceDomainIndex,
       "cienaCesCfmMaintenanceDomainLevel": cienaCesCfmMaintenanceDomainLevel,
       "cienaCesCfmMaintenanceDomainName": cienaCesCfmMaintenanceDomainName,
       "cienaCesCfmMaintenanceDomainServiceCount": cienaCesCfmMaintenanceDomainServiceCount,
       "cienaCesCfmServiceFrameBudget": cienaCesCfmServiceFrameBudget,
       "cienaCesCfmServiceFrameBudgetTable": cienaCesCfmServiceFrameBudgetTable,
       "cienaCesCfmServiceFrameBudgetEntry": cienaCesCfmServiceFrameBudgetEntry,
       "cienaCesCfmSlotIndex": cienaCesCfmSlotIndex,
       "cienaCesCfmServiceFrameBudgetSlot": cienaCesCfmServiceFrameBudgetSlot,
       "cienaCesCfmFrameBudgetGlobal": cienaCesCfmFrameBudgetGlobal,
       "cienaCesCfmGlobalControlModuleFrameBudget": cienaCesCfmGlobalControlModuleFrameBudget,
       "cienaCesCfmFrameBudgetGlobalTable": cienaCesCfmFrameBudgetGlobalTable,
       "cienaCesCfmFrameBudgetGlobalEntry": cienaCesCfmFrameBudgetGlobalEntry,
       "cienaCesCfmFrameBudgetGlobalSlot": cienaCesCfmFrameBudgetGlobalSlot,
       "cienaCesCfmGlobal": cienaCesCfmGlobal,
       "cienaCesCfmState": cienaCesCfmState,
       "cienaCesCfmEtherType": cienaCesCfmEtherType,
       "cienaCesCfmMEPHoldTime": cienaCesCfmMEPHoldTime,
       "cienaCesCfmY1731EtherType": cienaCesCfmY1731EtherType,
       "cienaCesCfmGlobalSLMDefaultCount": cienaCesCfmGlobalSLMDefaultCount,
       "cienaCesCfmGlobalSLMDefaultInterval": cienaCesCfmGlobalSLMDefaultInterval,
       "cienaCesCfmGlobalSLMDefaultTimeout": cienaCesCfmGlobalSLMDefaultTimeout,
       "cienaCesCfmSyntheticLoss": cienaCesCfmSyntheticLoss,
       "cienaCesCfmSyntheticLossSessionTable": cienaCesCfmSyntheticLossSessionTable,
       "cienaCesCfmSyntheticLossSessionEntry": cienaCesCfmSyntheticLossSessionEntry,
       "cienaCesCfmSyntheticLossSessionServiceIndex": cienaCesCfmSyntheticLossSessionServiceIndex,
       "cienaCesCfmSyntheticLossSessionLocalMEPId": cienaCesCfmSyntheticLossSessionLocalMEPId,
       "cienaCesCfmSyntheticLossSessionTargetMEPId": cienaCesCfmSyntheticLossSessionTargetMEPId,
       "cienaCesCfmSyntheticLossSessionTestId": cienaCesCfmSyntheticLossSessionTestId,
       "cienaCesCfmSyntheticLossSessionServiceName": cienaCesCfmSyntheticLossSessionServiceName,
       "cienaCesCfmSyntheticLossSessionPriority": cienaCesCfmSyntheticLossSessionPriority,
       "cienaCesCfmSyntheticLossSessionCount": cienaCesCfmSyntheticLossSessionCount,
       "cienaCesCfmSyntheticLossSessionSLMInterval": cienaCesCfmSyntheticLossSessionSLMInterval,
       "cienaCesCfmSyntheticLossSessionIterations": cienaCesCfmSyntheticLossSessionIterations,
       "cienaCesCfmSyntheticLossSessionRepeatDelay": cienaCesCfmSyntheticLossSessionRepeatDelay,
       "cienaCesCfmSyntheticLossSessionFrameSize": cienaCesCfmSyntheticLossSessionFrameSize,
       "cienaCesCfmSyntheticLossSessionTimeout": cienaCesCfmSyntheticLossSessionTimeout,
       "cienaCesCfmSyntheticLossSessionDuration": cienaCesCfmSyntheticLossSessionDuration,
       "cienaCesCfmSyntheticLossSessionLossNearThreshold": cienaCesCfmSyntheticLossSessionLossNearThreshold,
       "cienaCesCfmSyntheticLossSessionLossFarThreshold": cienaCesCfmSyntheticLossSessionLossFarThreshold,
       "cienaCesCfmSyntheticLossSessionNumSLMSent": cienaCesCfmSyntheticLossSessionNumSLMSent,
       "cienaCesCfmSyntheticLossSessionNumSLRReceived": cienaCesCfmSyntheticLossSessionNumSLRReceived,
       "cienaCesCfmSyntheticLossSessionFrameLossNear": cienaCesCfmSyntheticLossSessionFrameLossNear,
       "cienaCesCfmSyntheticLossSessionFrameLossFar": cienaCesCfmSyntheticLossSessionFrameLossFar,
       "cienaCesCfmSyntheticLossSessionAvgFrameLossNear": cienaCesCfmSyntheticLossSessionAvgFrameLossNear,
       "cienaCesCfmSyntheticLossSessionMinFrameLossNear": cienaCesCfmSyntheticLossSessionMinFrameLossNear,
       "cienaCesCfmSyntheticLossSessionMaxFrameLossNear": cienaCesCfmSyntheticLossSessionMaxFrameLossNear,
       "cienaCesCfmSyntheticLossSessionAvgFrameLossFar": cienaCesCfmSyntheticLossSessionAvgFrameLossFar,
       "cienaCesCfmSyntheticLossSessionMinFrameLossFar": cienaCesCfmSyntheticLossSessionMinFrameLossFar,
       "cienaCesCfmSyntheticLossSessionMaxFrameLossFar": cienaCesCfmSyntheticLossSessionMaxFrameLossFar,
       "cienaCesCfmSyntheticLossSessionFrameLossRatioNear": cienaCesCfmSyntheticLossSessionFrameLossRatioNear,
       "cienaCesCfmSyntheticLossSessionFrameLossRatioFar": cienaCesCfmSyntheticLossSessionFrameLossRatioFar,
       "cienaCesCfmSyntheticLossSessionSdSetThreshold": cienaCesCfmSyntheticLossSessionSdSetThreshold,
       "cienaCesCfmSyntheticLossSessionSdClearThreshold": cienaCesCfmSyntheticLossSessionSdClearThreshold,
       "cienaCesCfmSyntheticLossResponderTable": cienaCesCfmSyntheticLossResponderTable,
       "cienaCesCfmSyntheticLossResponderEntry": cienaCesCfmSyntheticLossResponderEntry,
       "cienaCesCfmSyntheticLossResponderServiceIndex": cienaCesCfmSyntheticLossResponderServiceIndex,
       "cienaCesCfmSyntheticLossResponderLocalMEPId": cienaCesCfmSyntheticLossResponderLocalMEPId,
       "cienaCesCfmSyntheticLossResponderRemoteMEPId": cienaCesCfmSyntheticLossResponderRemoteMEPId,
       "cienaCesCfmSyntheticLossResponderTestId": cienaCesCfmSyntheticLossResponderTestId,
       "cienaCesCfmSyntheticLossResponderServiceName": cienaCesCfmSyntheticLossResponderServiceName,
       "cienaCesCfmSyntheticLossResponderLocalMac": cienaCesCfmSyntheticLossResponderLocalMac,
       "cienaCesCfmSyntheticLossResponderRemoteMac": cienaCesCfmSyntheticLossResponderRemoteMac,
       "cienaCesCfmSyntheticLossResponderNumSLMReceived": cienaCesCfmSyntheticLossResponderNumSLMReceived,
       "cienaCesCfmSyntheticLossResponderNumSLRSent": cienaCesCfmSyntheticLossResponderNumSLRSent,
       "cienaCesCfmNotifMIBNotificationPrefix": cienaCesCfmNotifMIBNotificationPrefix,
       "cienaCesCfmNotifMIBNotification": cienaCesCfmNotifMIBNotification,
       "cienaCesCfmFaultTrapSet": cienaCesCfmFaultTrapSet,
       "cienaCesCfmFaultTrapClear": cienaCesCfmFaultTrapClear,
       "cienaCesCfmAverageDelayFaultTrapSet": cienaCesCfmAverageDelayFaultTrapSet,
       "cienaCesCfmAverageDelayFaultTrapClear": cienaCesCfmAverageDelayFaultTrapClear,
       "cienaCesCfmMaximumDelayFaultTrapSet": cienaCesCfmMaximumDelayFaultTrapSet,
       "cienaCesCfmMaximumDelayFaultTrapClear": cienaCesCfmMaximumDelayFaultTrapClear,
       "cienaCesCfmAverageJitterTrapSet": cienaCesCfmAverageJitterTrapSet,
       "cienaCesCfmAverageJitterTrapClear": cienaCesCfmAverageJitterTrapClear,
       "cienaCesCfmMaximumJitterTrapSet": cienaCesCfmMaximumJitterTrapSet,
       "cienaCesCfmMaximumJitterTrapClear": cienaCesCfmMaximumJitterTrapClear,
       "cienaCesCfmFrameLossNearTrapSet": cienaCesCfmFrameLossNearTrapSet,
       "cienaCesCfmFrameLossNearTrapClear": cienaCesCfmFrameLossNearTrapClear,
       "cienaCesCfmFrameLossFarTrapSet": cienaCesCfmFrameLossFarTrapSet,
       "cienaCesCfmFrameLossFarTrapClear": cienaCesCfmFrameLossFarTrapClear,
       "cienaCesSyntheticLossSessionNearFaultTrap": cienaCesSyntheticLossSessionNearFaultTrap,
       "cienaCesSyntheticLossSessionFarFaultTrap": cienaCesSyntheticLossSessionFarFaultTrap,
       "cienaCesSyntheticLossSessionNearFaultClearTrap": cienaCesSyntheticLossSessionNearFaultClearTrap,
       "cienaCesSyntheticLossSessionFarFaultClearTrap": cienaCesSyntheticLossSessionFarFaultClearTrap,
       "cienaCesCfmAverageDelayVariationTrapSet": cienaCesCfmAverageDelayVariationTrapSet,
       "cienaCesCfmAverageDelayVariationTrapClear": cienaCesCfmAverageDelayVariationTrapClear,
       "cienaCesCfmMaximumDelayVariationTrapSet": cienaCesCfmMaximumDelayVariationTrapSet,
       "cienaCesCfmMaximumDelayVariationTrapClear": cienaCesCfmMaximumDelayVariationTrapClear,
       "cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapSet": cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapSet,
       "cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapClear": cienaCesCfmSyntheticLossSessionSignalDegradeFaultTrapClear,
       "cienaCesCfmStatisticsMIBObjects": cienaCesCfmStatisticsMIBObjects,
       "cienaCesCfmMibObjects": cienaCesCfmMibObjects,
       "cienaCesCfmGlobalMIBObjects": cienaCesCfmGlobalMIBObjects,
       "cienaCesCfmGlobalStatsClear": cienaCesCfmGlobalStatsClear,
       "cienaCesCfmGlobalFrameBudget": cienaCesCfmGlobalFrameBudget,
       "cienaCesCfmGlobalFrameBudgetControlModule": cienaCesCfmGlobalFrameBudgetControlModule,
       "cienaCesCfmGlobalFrameBudgetSlot1": cienaCesCfmGlobalFrameBudgetSlot1,
       "cienaCesCfmGlobalFrameBudgetSlot2": cienaCesCfmGlobalFrameBudgetSlot2,
       "cienaCesCfmGlobalFrameBudgetSlot3": cienaCesCfmGlobalFrameBudgetSlot3,
       "cienaCesCfmGlobalFrameBudgetSlot4": cienaCesCfmGlobalFrameBudgetSlot4,
       "cienaCesCfmGlobalFrameBudgetSlot5": cienaCesCfmGlobalFrameBudgetSlot5,
       "cienaCesCfmGlobalFrameBudgetSlot6": cienaCesCfmGlobalFrameBudgetSlot6,
       "cienaCesCfmGlobalFrameBudgetSlot7": cienaCesCfmGlobalFrameBudgetSlot7,
       "cienaCesCfmGlobalFrameBudgetSlot8": cienaCesCfmGlobalFrameBudgetSlot8,
       "cienaCesCfmGlobalFrameBudgetSlot9": cienaCesCfmGlobalFrameBudgetSlot9,
       "cienaCesCfmGlobalFrameBudgetSlot10": cienaCesCfmGlobalFrameBudgetSlot10,
       "cienaCesCfmGlobalStats": cienaCesCfmGlobalStats,
       "cienaCesCfmGlobalStatsTxTotalFrames": cienaCesCfmGlobalStatsTxTotalFrames,
       "cienaCesCfmGlobalStatsTxFloodedframes": cienaCesCfmGlobalStatsTxFloodedframes,
       "cienaCesCfmGlobalStatsTxFloodignoredInvalidLevel": cienaCesCfmGlobalStatsTxFloodignoredInvalidLevel,
       "cienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist": cienaCesCfmGlobalStatsTxFloodignoredHighLevelMepExist,
       "cienaCesCfmGlobalStatsTxFloodignoredSTPState": cienaCesCfmGlobalStatsTxFloodignoredSTPState,
       "cienaCesCfmGlobalStatsRxTotalFrames": cienaCesCfmGlobalStatsRxTotalFrames,
       "cienaCesCfmGlobalStatsRxDropInvalidEtype": cienaCesCfmGlobalStatsRxDropInvalidEtype,
       "cienaCesCfmGlobalStatsRxDropInvalidOpCode": cienaCesCfmGlobalStatsRxDropInvalidOpCode,
       "cienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch": cienaCesCfmGlobalStatsRxDropL2DAHeaderLevelMismatch,
       "cienaCesCfmGlobalStatsRxTotalMalformedFrames": cienaCesCfmGlobalStatsRxTotalMalformedFrames,
       "cienaCesCfmGlobalCCMStats": cienaCesCfmGlobalCCMStats,
       "cienaCesCfmGlobalCCMStatsTxTotalCCM": cienaCesCfmGlobalCCMStatsTxTotalCCM,
       "cienaCesCfmGlobalCCMStatsTxTotalCCMFlooded": cienaCesCfmGlobalCCMStatsTxTotalCCMFlooded,
       "cienaCesCfmGlobalCCMStatsRxTotalCCM": cienaCesCfmGlobalCCMStatsRxTotalCCM,
       "cienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors": cienaCesCfmGlobalCCMStatsRxTotalCCMSequenceErrors,
       "cienaCesCfmGlobalCCMStatsRxInvalidMAID": cienaCesCfmGlobalCCMStatsRxInvalidMAID,
       "cienaCesCfmGlobalCCMStatsRxInvalidCCMInterval": cienaCesCfmGlobalCCMStatsRxInvalidCCMInterval,
       "cienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset": cienaCesCfmGlobalCCMStatsRxInvalidFirstTlvOffset,
       "cienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv": cienaCesCfmGlobalCCMStatsRxInvalidPortStatusTlv,
       "cienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv": cienaCesCfmGlobalCCMStatsRxInvalidInterfaceStatusTlv,
       "cienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface": cienaCesCfmGlobalCCMStatsRxInvalidLogicalInterface,
       "cienaCesCfmGlobalCCMStatsRxInvalidServiceInstance": cienaCesCfmGlobalCCMStatsRxInvalidServiceInstance,
       "cienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel": cienaCesCfmGlobalCCMStatsRxInvalidPBTEncapTunnel,
       "cienaCesCfmGlobalCCMStatsRxDropAdminDisable": cienaCesCfmGlobalCCMStatsRxDropAdminDisable,
       "cienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding": cienaCesCfmGlobalCCMStatsRxDropSTPstatenotForwarding,
       "cienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep": cienaCesCfmGlobalCCMStatsRxDropCCMBlockedbyOppMep,
       "cienaCesCfmGlobalCCMStatsRxDropCCMLeakage": cienaCesCfmGlobalCCMStatsRxDropCCMLeakage,
       "cienaCesCfmGlobalCCMStatsRxDropCCMTooLong": cienaCesCfmGlobalCCMStatsRxDropCCMTooLong,
       "cienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled": cienaCesCfmGlobalCCMStatsRxDropCCMServiceDisabled,
       "cienaCesCfmGlobalCCMStatsRxTotalErrorCCM": cienaCesCfmGlobalCCMStatsRxTotalErrorCCM,
       "cienaCesCfmGlobalCCMStatsRxTotalMalformedCCM": cienaCesCfmGlobalCCMStatsRxTotalMalformedCCM,
       "cienaCesCfmGlobalCCMStatsRxTotalMEPCCM": cienaCesCfmGlobalCCMStatsRxTotalMEPCCM,
       "cienaCesCfmGlobalCCMStatsRxTotalMIPCCM": cienaCesCfmGlobalCCMStatsRxTotalMIPCCM,
       "cienaCesCfmGlobalLoopbackStats": cienaCesCfmGlobalLoopbackStats,
       "cienaCesCfmGlobalLoopbackStatsTxTotalLBM": cienaCesCfmGlobalLoopbackStatsTxTotalLBM,
       "cienaCesCfmGlobalLoopbackStatsTxTotalLBR": cienaCesCfmGlobalLoopbackStatsTxTotalLBR,
       "cienaCesCfmGlobalLoopbackStatsRxTotalLBM": cienaCesCfmGlobalLoopbackStatsRxTotalLBM,
       "cienaCesCfmGlobalLoopbackStatsRxTotalLBR": cienaCesCfmGlobalLoopbackStatsRxTotalLBR,
       "cienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR": cienaCesCfmGlobalLoopbackStatsRxTotalInOrderLBR,
       "cienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR": cienaCesCfmGlobalLoopbackStatsRxTotalOutOfOrderLBR,
       "cienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR": cienaCesCfmGlobalLoopbackStatsRxTotalContentMismatchLBR,
       "cienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR": cienaCesCfmGlobalLoopbackStatsRxTotalUnexpectedLBR,
       "cienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset": cienaCesCfmGlobalLoopbackStatsRxLBMInvalidFirstTLVOffset,
       "cienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset": cienaCesCfmGlobalLoopbackStatsRxLBRInvalidFirstTLVOffset,
       "cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM": cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBM,
       "cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR": cienaCesCfmGlobalLoopbackStatsRxUnresolvedLBR,
       "cienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM": cienaCesCfmGlobalLoopbackStatsRxTotalMalformedLBM,
       "cienaCesCfmGlobalLinkTraceStats": cienaCesCfmGlobalLinkTraceStats,
       "cienaCesCfmGlobalLinkTraceStatsTxTotalLTM": cienaCesCfmGlobalLinkTraceStatsTxTotalLTM,
       "cienaCesCfmGlobalLinkTraceStatsTxTotalLTR": cienaCesCfmGlobalLinkTraceStatsTxTotalLTR,
       "cienaCesCfmGlobalLinkTraceStatsRxTotalLTM": cienaCesCfmGlobalLinkTraceStatsRxTotalLTM,
       "cienaCesCfmGlobalLinkTraceStatsRxTotalLTR": cienaCesCfmGlobalLinkTraceStatsRxTotalLTR,
       "cienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR": cienaCesCfmGlobalLinkTraceStatsRxTotalUnexpectedLTR,
       "cienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset": cienaCesCfmGlobalLinkTraceStatsRxLTMInvalidFirstTLVOffset,
       "cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset": cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidFirstTLVOffset,
       "cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction": cienaCesCfmGlobalLinkTraceStatsRxLTRInvalidRelayAction,
       "cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM": cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTM,
       "cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR": cienaCesCfmGlobalLinkTraceStatsRxUnresolvedLTR,
       "cienaCesCfmGlobalDelayMeasurementStats": cienaCesCfmGlobalDelayMeasurementStats,
       "cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM": cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMM,
       "cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR": cienaCesCfmGlobalDelayMeasurementStatsTxTotalDMR,
       "cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM": cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMM,
       "cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR": cienaCesCfmGlobalDelayMeasurementStatsRxTotalDMR,
       "cienaCesCfmGlobalLossMeasurementStats": cienaCesCfmGlobalLossMeasurementStats,
       "cienaCesCfmGlobalLossMeasurementStatsTxTotalLMM": cienaCesCfmGlobalLossMeasurementStatsTxTotalLMM,
       "cienaCesCfmGlobalLossMeasurementStatsTxTotalLMR": cienaCesCfmGlobalLossMeasurementStatsTxTotalLMR,
       "cienaCesCfmGlobalLossMeasurementStatsRxTotalLMM": cienaCesCfmGlobalLossMeasurementStatsRxTotalLMM,
       "cienaCesCfmGlobalLossMeasurementStatsRxTotalLMR": cienaCesCfmGlobalLossMeasurementStatsRxTotalLMR,
       "cienaCesCfmGlobalSyntheticLossMeasurementStats": cienaCesCfmGlobalSyntheticLossMeasurementStats,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM": cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLM,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR": cienaCesCfmGlobalSyntheticLossMeasurementStatsTxTotalSLR,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM": cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLM,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR": cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalSLR,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM": cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLM,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR": cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalValidSLR,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM": cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLM,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR": cienaCesCfmGlobalSyntheticLossMeasurementStatsRxTotalInvalidSLR,
       "cienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM": cienaCesCfmGlobalSyntheticLossMeasurementStatsRxDropSLM,
       "cienaCesCfmServiceStats": cienaCesCfmServiceStats,
       "cienaCesCfmServiceStatsTable": cienaCesCfmServiceStatsTable,
       "cienaCesCfmServiceStatsEntry": cienaCesCfmServiceStatsEntry,
       "cienaCesCfmServiceStatsTotalTx": cienaCesCfmServiceStatsTotalTx,
       "cienaCesCfmServiceStatsTotalRx": cienaCesCfmServiceStatsTotalRx,
       "cienaCesCfmServiceStatsTotalTxLTM": cienaCesCfmServiceStatsTotalTxLTM,
       "cienaCesCfmServiceStatsTotalTxLTR": cienaCesCfmServiceStatsTotalTxLTR,
       "cienaCesCfmServiceStatsTotalRxLTM": cienaCesCfmServiceStatsTotalRxLTM,
       "cienaCesCfmServiceStatsTotalRxLTR": cienaCesCfmServiceStatsTotalRxLTR,
       "cienaCesCfmServiceStatsTotalRxUnexpectedLTR": cienaCesCfmServiceStatsTotalRxUnexpectedLTR,
       "cienaCesCfmServiceStatsTotalTxLBM": cienaCesCfmServiceStatsTotalTxLBM,
       "cienaCesCfmServiceStatsTotalTxLBR": cienaCesCfmServiceStatsTotalTxLBR,
       "cienaCesCfmServiceStatsTotalRxLBM": cienaCesCfmServiceStatsTotalRxLBM,
       "cienaCesCfmServiceStatsTotalRxInorderLBR": cienaCesCfmServiceStatsTotalRxInorderLBR,
       "cienaCesCfmServiceStatsTotalRxOutOforderLBR": cienaCesCfmServiceStatsTotalRxOutOforderLBR,
       "cienaCesCfmServiceStatsTotalRxContentMismatchLBR": cienaCesCfmServiceStatsTotalRxContentMismatchLBR,
       "cienaCesCfmServiceStatsTotalRxUnexpectedLBR": cienaCesCfmServiceStatsTotalRxUnexpectedLBR,
       "cienaCesCfmServiceStatsClear": cienaCesCfmServiceStatsClear,
       "cienaCesCfmMepStats": cienaCesCfmMepStats,
       "cienaCesCfmMepStatsTable": cienaCesCfmMepStatsTable,
       "cienaCesCfmMepStatsEntry": cienaCesCfmMepStatsEntry,
       "cienaCesCfmMepInterfaceType": cienaCesCfmMepInterfaceType,
       "cienaCesCfmMepInterfaceIndex": cienaCesCfmMepInterfaceIndex,
       "cienaCesCfmMepStatsTxTotalCCM": cienaCesCfmMepStatsTxTotalCCM,
       "cienaCesCfmMepStatsRxTotalCCM": cienaCesCfmMepStatsRxTotalCCM,
       "cienaCesCfmMepStatsTxLoopbackMessages": cienaCesCfmMepStatsTxLoopbackMessages,
       "cienaCesCfmMepStatsTxLoopbackReply": cienaCesCfmMepStatsTxLoopbackReply,
       "cienaCesCfmMepStatsRxLoopbackMessages": cienaCesCfmMepStatsRxLoopbackMessages,
       "cienaCesCfmMepStatsRxInorderLoopbackReply": cienaCesCfmMepStatsRxInorderLoopbackReply,
       "cienaCesCfmMepStatsRxOutoforderLoopbackReply": cienaCesCfmMepStatsRxOutoforderLoopbackReply,
       "cienaCesCfmMepStatsRxContentMismatchLoopbackReply": cienaCesCfmMepStatsRxContentMismatchLoopbackReply,
       "cienaCesCfmMepStatsRxUnexpectedLoopbackReply": cienaCesCfmMepStatsRxUnexpectedLoopbackReply,
       "cienaCesCfmMepStatsTxLinktraceMessage": cienaCesCfmMepStatsTxLinktraceMessage,
       "cienaCesCfmMepStatsTxLinktraceReply": cienaCesCfmMepStatsTxLinktraceReply,
       "cienaCesCfmMepStatsRxLinktraceMessage": cienaCesCfmMepStatsRxLinktraceMessage,
       "cienaCesCfmMepStatsRxLinktraceReply": cienaCesCfmMepStatsRxLinktraceReply,
       "cienaCesCfmMepStatsRxUnexpectedLinktraceReply": cienaCesCfmMepStatsRxUnexpectedLinktraceReply,
       "cienaCesCfmMepStatsTxDelayMeasurementMessage": cienaCesCfmMepStatsTxDelayMeasurementMessage,
       "cienaCesCfmMepStatsTxDelayMeasurementReply": cienaCesCfmMepStatsTxDelayMeasurementReply,
       "cienaCesCfmMepStatsRxDelayMeasurementMessage": cienaCesCfmMepStatsRxDelayMeasurementMessage,
       "cienaCesCfmMepStatsRxDelayMeasurementReply": cienaCesCfmMepStatsRxDelayMeasurementReply,
       "cienaCesCfmMepStatsTxLossMeasurementMessage": cienaCesCfmMepStatsTxLossMeasurementMessage,
       "cienaCesCfmMepStatsTxLossMeasurementReply": cienaCesCfmMepStatsTxLossMeasurementReply,
       "cienaCesCfmMepStatsRxLossMeasurementMessage": cienaCesCfmMepStatsRxLossMeasurementMessage,
       "cienaCesCfmMepStatsRxLossMeasurementReply": cienaCesCfmMepStatsRxLossMeasurementReply,
       "cienaCesCfmMepStatsLastLBMTargetRemoteMepId": cienaCesCfmMepStatsLastLBMTargetRemoteMepId,
       "cienaCesCfmMepStatsLastLBMTargetMacAddress": cienaCesCfmMepStatsLastLBMTargetMacAddress,
       "cienaCesCfmMepStatsLastLBMPriority": cienaCesCfmMepStatsLastLBMPriority,
       "cienaCesCfmMepStatsLastLBMCount": cienaCesCfmMepStatsLastLBMCount,
       "cienaCesCfmMepStatsLastLBMFirstSeqNum": cienaCesCfmMepStatsLastLBMFirstSeqNum,
       "cienaCesCfmMepStatsLastLTMTargetRemoteMepId": cienaCesCfmMepStatsLastLTMTargetRemoteMepId,
       "cienaCesCfmMepStatsLastLTMTargetMacAddress": cienaCesCfmMepStatsLastLTMTargetMacAddress,
       "cienaCesCfmMepStatsLastLTMPriority": cienaCesCfmMepStatsLastLTMPriority,
       "cienaCesCfmMepStatsLastLTMSeqNum": cienaCesCfmMepStatsLastLTMSeqNum,
       "cienaCesCfmMepStatsLastLTMInitialTTL": cienaCesCfmMepStatsLastLTMInitialTTL,
       "cienaCesCfmMepStatsLastDMMTargetRemoteMepId": cienaCesCfmMepStatsLastDMMTargetRemoteMepId,
       "cienaCesCfmMepStatsLastDMMTargetMacAddress": cienaCesCfmMepStatsLastDMMTargetMacAddress,
       "cienaCesCfmMepStatsLastDMMPriority": cienaCesCfmMepStatsLastDMMPriority,
       "cienaCesCfmMepStatsLastDMMRepeatInterval": cienaCesCfmMepStatsLastDMMRepeatInterval,
       "cienaCesCfmMepStatsLastDMMNumOfDmmToSend": cienaCesCfmMepStatsLastDMMNumOfDmmToSend,
       "cienaCesCfmMepStatsLastLMMTargetRemoteMepId": cienaCesCfmMepStatsLastLMMTargetRemoteMepId,
       "cienaCesCfmMepStatsLastLMMTargetMacAddress": cienaCesCfmMepStatsLastLMMTargetMacAddress,
       "cienaCesCfmMepStatsLastLMMPriority": cienaCesCfmMepStatsLastLMMPriority,
       "cienaCesCfmMepStatsLastLMMRepeatInterval": cienaCesCfmMepStatsLastLMMRepeatInterval,
       "cienaCesCfmMepStatsLastLMMNumOfLmmToSend": cienaCesCfmMepStatsLastLMMNumOfLmmToSend,
       "cienaCesCfmMepStatsNextLBMSeqNumber": cienaCesCfmMepStatsNextLBMSeqNumber,
       "cienaCesCfmMepStatsNextLTMSeqNumber": cienaCesCfmMepStatsNextLTMSeqNumber,
       "cienaCesCfmMepStatsTxSyntheticLossMeasurementMessage": cienaCesCfmMepStatsTxSyntheticLossMeasurementMessage,
       "cienaCesCfmMepStatsTxSyntheticLossMeasurementReply": cienaCesCfmMepStatsTxSyntheticLossMeasurementReply,
       "cienaCesCfmMepStatsRxSyntheticLossMeasurementMessage": cienaCesCfmMepStatsRxSyntheticLossMeasurementMessage,
       "cienaCesCfmMepStatsRxSyntheticLossMeasurementReply": cienaCesCfmMepStatsRxSyntheticLossMeasurementReply,
       "cienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage": cienaCesCfmMepStatsRxValidSyntheticLossMeasurementMessage,
       "cienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply": cienaCesCfmMepStatsRxValidSyntheticLossMeasurementReply,
       "cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage": cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementMessage,
       "cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply": cienaCesCfmMepStatsRxInvalidSyntheticLossMeasurementReply,
       "cienaCesCfmMepStatsRxCCMWithErrorCCMFault": cienaCesCfmMepStatsRxCCMWithErrorCCMFault,
       "cienaCesCfmMepStatsRxCCMWithXCONFault": cienaCesCfmMepStatsRxCCMWithXCONFault,
       "cienaCesCfmMepStatsRxCCMWithRMEPLOCFault": cienaCesCfmMepStatsRxCCMWithRMEPLOCFault,
       "cienaCesCfmMepStatsRxCCMWithRDI0": cienaCesCfmMepStatsRxCCMWithRDI0,
       "cienaCesCfmMepStatsRxCCMWithRDI1": cienaCesCfmMepStatsRxCCMWithRDI1,
       "cienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch": cienaCesCfmMepStatsRxCCMWithSequenceNumberMismatch,
       "cienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv": cienaCesCfmMepStatsRxCCMDroppedWithMalformedTlv,
       "cienaCesCfmMepStatsToTxLoopbackMessages": cienaCesCfmMepStatsToTxLoopbackMessages,
       "cienaCesCfmRemoteMepStatsTable": cienaCesCfmRemoteMepStatsTable,
       "cienaCesCfmRemoteMepStatsEntry": cienaCesCfmRemoteMepStatsEntry,
       "cienaCesCfmRemoteMepStatsRxTotalCCM": cienaCesCfmRemoteMepStatsRxTotalCCM,
       "cienaCesCfmRemoteMepStatsLastSeqNum": cienaCesCfmRemoteMepStatsLastSeqNum,
       "cienaCesCfmRemoteMepStatsCCMSeqErrors": cienaCesCfmRemoteMepStatsCCMSeqErrors,
       "cienaCesCfmRemoteMepStatsClear": cienaCesCfmRemoteMepStatsClear}
)
