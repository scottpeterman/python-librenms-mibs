# SNMP MIB module (PRVT-EPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-EPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:50 2025
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

(Dot1agCfmMDLevelOrNone,
 Dot1agCfmMepIdOrZero) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMDLevelOrNone",
    "Dot1agCfmMepIdOrZero")

(sdpInfoEntry,) = mibBuilder.importSymbols(
    "PRVT-SERV-MIB",
    "sdpInfoEntry")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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

prvtEpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132)
)
if mibBuilder.loadTexts:
    prvtEpsMib.setRevisions(
        ("2011-03-23 00:00",
         "2010-04-17 00:00",
         "2009-07-15 00:00",
         "2009-03-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtEpsRequestStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              4,
              5,
              6,
              7,
              9,
              11,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("rsNone", -1),
          ("rsNoRequest", 0),
          ("rsDoNotRevert", 1),
          ("rsReverseRequest", 2),
          ("rsExercise", 4),
          ("rsWaitToRestore", 5),
          ("rsClear", 6),
          ("rsManualSwitch", 7),
          ("rsSignalDegrade", 9),
          ("rsSignalFail", 11),
          ("rsForcedSwitch", 13),
          ("rsSignalFailForProtection", 14),
          ("rsLockoutOfProtection", 15))
    )



class PrvtEpsProtectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pt1Plus1", 0),
          ("pt1To1", 1))
    )



class PrvtEpsDirectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtUnidirectional", 0),
          ("dtBidirectional", 1))
    )



class PrvtEpsActivePathType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("working", 0),
          ("protection", 1))
    )



class PrvtEpsMonitoringType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cfmPM", 1),
          ("saa", 2))
    )



class PrvtEpsDefectFopType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("fullyIncompatibleProvisioning", 0),
          ("protectionSwitchingIncomplete", 1),
          ("protectionConfigurationMismatch", 2),
          ("epsConfigurationMismatch", 3))
    )


class PrvtEpsPathStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("psOk", 0),
          ("psFailed", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtEpsMibNotifications_ObjectIdentity = ObjectIdentity
prvtEpsMibNotifications = _PrvtEpsMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0)
)
_PrvtEpsMibObjects_ObjectIdentity = ObjectIdentity
prvtEpsMibObjects = _PrvtEpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1)
)
_PrvtEpsService_ObjectIdentity = ObjectIdentity
prvtEpsService = _PrvtEpsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1)
)
_PrvtEpsServiceTable_Object = MibTable
prvtEpsServiceTable = _PrvtEpsServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtEpsServiceTable.setStatus("current")
_PrvtEpsServiceEntry_Object = MibTableRow
prvtEpsServiceEntry = _PrvtEpsServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1)
)
prvtEpsServiceEntry.setIndexNames(
    (0, "PRVT-EPS-MIB", "prvtEpsSvcId"),
)
if mibBuilder.loadTexts:
    prvtEpsServiceEntry.setStatus("current")


class _PrvtEpsSvcId_Type(Unsigned32):
    """Custom type prvtEpsSvcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PrvtEpsSvcId_Type.__name__ = "Unsigned32"
_PrvtEpsSvcId_Object = MibTableColumn
prvtEpsSvcId = _PrvtEpsSvcId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 1),
    _PrvtEpsSvcId_Type()
)
prvtEpsSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsSvcId.setStatus("current")


class _PrvtEpsServiceCfmMdLevel_Type(Dot1agCfmMDLevelOrNone):
    """Custom type prvtEpsServiceCfmMdLevel based on Dot1agCfmMDLevelOrNone"""
    defaultValue = -1


_PrvtEpsServiceCfmMdLevel_Type.__name__ = "Dot1agCfmMDLevelOrNone"
_PrvtEpsServiceCfmMdLevel_Object = MibTableColumn
prvtEpsServiceCfmMdLevel = _PrvtEpsServiceCfmMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 2),
    _PrvtEpsServiceCfmMdLevel_Type()
)
prvtEpsServiceCfmMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceCfmMdLevel.setStatus("current")


class _PrvtEpsServicePrimaryLocalCfmMep_Type(Dot1agCfmMepIdOrZero):
    """Custom type prvtEpsServicePrimaryLocalCfmMep based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_PrvtEpsServicePrimaryLocalCfmMep_Type.__name__ = "Dot1agCfmMepIdOrZero"
_PrvtEpsServicePrimaryLocalCfmMep_Object = MibTableColumn
prvtEpsServicePrimaryLocalCfmMep = _PrvtEpsServicePrimaryLocalCfmMep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 3),
    _PrvtEpsServicePrimaryLocalCfmMep_Type()
)
prvtEpsServicePrimaryLocalCfmMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServicePrimaryLocalCfmMep.setStatus("current")


class _PrvtEpsServicePrimaryRemoteCfmMep_Type(Dot1agCfmMepIdOrZero):
    """Custom type prvtEpsServicePrimaryRemoteCfmMep based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_PrvtEpsServicePrimaryRemoteCfmMep_Type.__name__ = "Dot1agCfmMepIdOrZero"
_PrvtEpsServicePrimaryRemoteCfmMep_Object = MibTableColumn
prvtEpsServicePrimaryRemoteCfmMep = _PrvtEpsServicePrimaryRemoteCfmMep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 4),
    _PrvtEpsServicePrimaryRemoteCfmMep_Type()
)
prvtEpsServicePrimaryRemoteCfmMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServicePrimaryRemoteCfmMep.setStatus("current")


class _PrvtEpsServiceSecondaryLocalCfmMep_Type(Dot1agCfmMepIdOrZero):
    """Custom type prvtEpsServiceSecondaryLocalCfmMep based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_PrvtEpsServiceSecondaryLocalCfmMep_Type.__name__ = "Dot1agCfmMepIdOrZero"
_PrvtEpsServiceSecondaryLocalCfmMep_Object = MibTableColumn
prvtEpsServiceSecondaryLocalCfmMep = _PrvtEpsServiceSecondaryLocalCfmMep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 5),
    _PrvtEpsServiceSecondaryLocalCfmMep_Type()
)
prvtEpsServiceSecondaryLocalCfmMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceSecondaryLocalCfmMep.setStatus("current")


class _PrvtEpsServiceSecondaryRemoteCfmMep_Type(Dot1agCfmMepIdOrZero):
    """Custom type prvtEpsServiceSecondaryRemoteCfmMep based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_PrvtEpsServiceSecondaryRemoteCfmMep_Type.__name__ = "Dot1agCfmMepIdOrZero"
_PrvtEpsServiceSecondaryRemoteCfmMep_Object = MibTableColumn
prvtEpsServiceSecondaryRemoteCfmMep = _PrvtEpsServiceSecondaryRemoteCfmMep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 6),
    _PrvtEpsServiceSecondaryRemoteCfmMep_Type()
)
prvtEpsServiceSecondaryRemoteCfmMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceSecondaryRemoteCfmMep.setStatus("current")
_PrvtEpsServiceLocalState_Type = PrvtEpsRequestStateType
_PrvtEpsServiceLocalState_Object = MibTableColumn
prvtEpsServiceLocalState = _PrvtEpsServiceLocalState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 7),
    _PrvtEpsServiceLocalState_Type()
)
prvtEpsServiceLocalState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceLocalState.setStatus("current")


class _PrvtEpsServiceHoldOffTimer_Type(Unsigned32):
    """Custom type prvtEpsServiceHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PrvtEpsServiceHoldOffTimer_Type.__name__ = "Unsigned32"
_PrvtEpsServiceHoldOffTimer_Object = MibTableColumn
prvtEpsServiceHoldOffTimer = _PrvtEpsServiceHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 8),
    _PrvtEpsServiceHoldOffTimer_Type()
)
prvtEpsServiceHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceHoldOffTimer.setStatus("current")


class _PrvtEpsServiceWaitToRestoreTimer_Type(Unsigned32):
    """Custom type prvtEpsServiceWaitToRestoreTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 12),
    )


_PrvtEpsServiceWaitToRestoreTimer_Type.__name__ = "Unsigned32"
_PrvtEpsServiceWaitToRestoreTimer_Object = MibTableColumn
prvtEpsServiceWaitToRestoreTimer = _PrvtEpsServiceWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 9),
    _PrvtEpsServiceWaitToRestoreTimer_Type()
)
prvtEpsServiceWaitToRestoreTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceWaitToRestoreTimer.setStatus("current")
_PrvtEpsServiceApsChannel_Type = TruthValue
_PrvtEpsServiceApsChannel_Object = MibTableColumn
prvtEpsServiceApsChannel = _PrvtEpsServiceApsChannel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 10),
    _PrvtEpsServiceApsChannel_Type()
)
prvtEpsServiceApsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceApsChannel.setStatus("current")
_PrvtEpsServiceProtection_Type = PrvtEpsProtectionType
_PrvtEpsServiceProtection_Object = MibTableColumn
prvtEpsServiceProtection = _PrvtEpsServiceProtection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 11),
    _PrvtEpsServiceProtection_Type()
)
prvtEpsServiceProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceProtection.setStatus("current")
_PrvtEpsServiceDirection_Type = PrvtEpsDirectionType
_PrvtEpsServiceDirection_Object = MibTableColumn
prvtEpsServiceDirection = _PrvtEpsServiceDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 12),
    _PrvtEpsServiceDirection_Type()
)
prvtEpsServiceDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceDirection.setStatus("current")
_PrvtEpsServiceRevertive_Type = TruthValue
_PrvtEpsServiceRevertive_Object = MibTableColumn
prvtEpsServiceRevertive = _PrvtEpsServiceRevertive_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 13),
    _PrvtEpsServiceRevertive_Type()
)
prvtEpsServiceRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceRevertive.setStatus("current")


class _PrvtEpsServiceActivePath_Type(PrvtEpsActivePathType):
    """Custom type prvtEpsServiceActivePath based on PrvtEpsActivePathType"""
    defaultValue = 0


_PrvtEpsServiceActivePath_Type.__name__ = "PrvtEpsActivePathType"
_PrvtEpsServiceActivePath_Object = MibTableColumn
prvtEpsServiceActivePath = _PrvtEpsServiceActivePath_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 14),
    _PrvtEpsServiceActivePath_Type()
)
prvtEpsServiceActivePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceActivePath.setStatus("current")


class _PrvtEpsServiceDegradeTestType_Type(PrvtEpsMonitoringType):
    """Custom type prvtEpsServiceDegradeTestType based on PrvtEpsMonitoringType"""
    defaultValue = 0


_PrvtEpsServiceDegradeTestType_Type.__name__ = "PrvtEpsMonitoringType"
_PrvtEpsServiceDegradeTestType_Object = MibTableColumn
prvtEpsServiceDegradeTestType = _PrvtEpsServiceDegradeTestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 15),
    _PrvtEpsServiceDegradeTestType_Type()
)
prvtEpsServiceDegradeTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceDegradeTestType.setStatus("current")


class _PrvtEpsServiceDegradeTestOwner_Type(OctetString):
    """Custom type prvtEpsServiceDegradeTestOwner based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtEpsServiceDegradeTestOwner_Type.__name__ = "OctetString"
_PrvtEpsServiceDegradeTestOwner_Object = MibTableColumn
prvtEpsServiceDegradeTestOwner = _PrvtEpsServiceDegradeTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 16),
    _PrvtEpsServiceDegradeTestOwner_Type()
)
prvtEpsServiceDegradeTestOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceDegradeTestOwner.setStatus("current")


class _PrvtEpsServiceDegradeTestName_Type(OctetString):
    """Custom type prvtEpsServiceDegradeTestName based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtEpsServiceDegradeTestName_Type.__name__ = "OctetString"
_PrvtEpsServiceDegradeTestName_Object = MibTableColumn
prvtEpsServiceDegradeTestName = _PrvtEpsServiceDegradeTestName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 17),
    _PrvtEpsServiceDegradeTestName_Type()
)
prvtEpsServiceDegradeTestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceDegradeTestName.setStatus("current")


class _PrvtEpsServiceDegradeTestEnable_Type(TruthValue):
    """Custom type prvtEpsServiceDegradeTestEnable based on TruthValue"""
    defaultValue = 2


_PrvtEpsServiceDegradeTestEnable_Type.__name__ = "TruthValue"
_PrvtEpsServiceDegradeTestEnable_Object = MibTableColumn
prvtEpsServiceDegradeTestEnable = _PrvtEpsServiceDegradeTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 18),
    _PrvtEpsServiceDegradeTestEnable_Type()
)
prvtEpsServiceDegradeTestEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceDegradeTestEnable.setStatus("current")
_PrvtEpsServiceDefectFop_Type = PrvtEpsDefectFopType
_PrvtEpsServiceDefectFop_Object = MibTableColumn
prvtEpsServiceDefectFop = _PrvtEpsServiceDefectFop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 19),
    _PrvtEpsServiceDefectFop_Type()
)
prvtEpsServiceDefectFop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceDefectFop.setStatus("current")
_PrvtEpsServiceOperationalStatus_Type = TruthValue
_PrvtEpsServiceOperationalStatus_Object = MibTableColumn
prvtEpsServiceOperationalStatus = _PrvtEpsServiceOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 20),
    _PrvtEpsServiceOperationalStatus_Type()
)
prvtEpsServiceOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceOperationalStatus.setStatus("current")
_PrvtEpsServicePrimaryStatus_Type = PrvtEpsPathStatusType
_PrvtEpsServicePrimaryStatus_Object = MibTableColumn
prvtEpsServicePrimaryStatus = _PrvtEpsServicePrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 21),
    _PrvtEpsServicePrimaryStatus_Type()
)
prvtEpsServicePrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServicePrimaryStatus.setStatus("current")
_PrvtEpsServiceSecondaryStatus_Type = PrvtEpsPathStatusType
_PrvtEpsServiceSecondaryStatus_Object = MibTableColumn
prvtEpsServiceSecondaryStatus = _PrvtEpsServiceSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 22),
    _PrvtEpsServiceSecondaryStatus_Type()
)
prvtEpsServiceSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceSecondaryStatus.setStatus("current")
_PrvtEpsServiceRemoteState_Type = PrvtEpsRequestStateType
_PrvtEpsServiceRemoteState_Object = MibTableColumn
prvtEpsServiceRemoteState = _PrvtEpsServiceRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 23),
    _PrvtEpsServiceRemoteState_Type()
)
prvtEpsServiceRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceRemoteState.setStatus("current")
_PrvtEpsServiceRemoteApsChannel_Type = TruthValue
_PrvtEpsServiceRemoteApsChannel_Object = MibTableColumn
prvtEpsServiceRemoteApsChannel = _PrvtEpsServiceRemoteApsChannel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 24),
    _PrvtEpsServiceRemoteApsChannel_Type()
)
prvtEpsServiceRemoteApsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceRemoteApsChannel.setStatus("current")
_PrvtEpsServiceRemoteProtection_Type = PrvtEpsProtectionType
_PrvtEpsServiceRemoteProtection_Object = MibTableColumn
prvtEpsServiceRemoteProtection = _PrvtEpsServiceRemoteProtection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 25),
    _PrvtEpsServiceRemoteProtection_Type()
)
prvtEpsServiceRemoteProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceRemoteProtection.setStatus("current")
_PrvtEpsServiceRemoteDirection_Type = PrvtEpsDirectionType
_PrvtEpsServiceRemoteDirection_Object = MibTableColumn
prvtEpsServiceRemoteDirection = _PrvtEpsServiceRemoteDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 26),
    _PrvtEpsServiceRemoteDirection_Type()
)
prvtEpsServiceRemoteDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceRemoteDirection.setStatus("current")
_PrvtEpsServiceRemoteRevertive_Type = TruthValue
_PrvtEpsServiceRemoteRevertive_Object = MibTableColumn
prvtEpsServiceRemoteRevertive = _PrvtEpsServiceRemoteRevertive_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 27),
    _PrvtEpsServiceRemoteRevertive_Type()
)
prvtEpsServiceRemoteRevertive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceRemoteRevertive.setStatus("current")


class _PrvtEpsServiceAdminFreeze_Type(TruthValue):
    """Custom type prvtEpsServiceAdminFreeze based on TruthValue"""
    defaultValue = 2


_PrvtEpsServiceAdminFreeze_Type.__name__ = "TruthValue"
_PrvtEpsServiceAdminFreeze_Object = MibTableColumn
prvtEpsServiceAdminFreeze = _PrvtEpsServiceAdminFreeze_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 28),
    _PrvtEpsServiceAdminFreeze_Type()
)
prvtEpsServiceAdminFreeze.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceAdminFreeze.setStatus("current")


class _PrvtEpsServiceAdminStatus_Type(Integer32):
    """Custom type prvtEpsServiceAdminStatus based on Integer32"""
    defaultValue = 2

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


_PrvtEpsServiceAdminStatus_Type.__name__ = "Integer32"
_PrvtEpsServiceAdminStatus_Object = MibTableColumn
prvtEpsServiceAdminStatus = _PrvtEpsServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 29),
    _PrvtEpsServiceAdminStatus_Type()
)
prvtEpsServiceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceAdminStatus.setStatus("current")
_PrvtEpsServiceRowStatus_Type = RowStatus
_PrvtEpsServiceRowStatus_Object = MibTableColumn
prvtEpsServiceRowStatus = _PrvtEpsServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 30),
    _PrvtEpsServiceRowStatus_Type()
)
prvtEpsServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEpsServiceRowStatus.setStatus("current")
_PrvtEpsServiceProtectionCounter_Type = Unsigned32
_PrvtEpsServiceProtectionCounter_Object = MibTableColumn
prvtEpsServiceProtectionCounter = _PrvtEpsServiceProtectionCounter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 31),
    _PrvtEpsServiceProtectionCounter_Type()
)
prvtEpsServiceProtectionCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEpsServiceProtectionCounter.setStatus("current")

# Managed Objects groups


# Notification objects

prvtEpsDefectAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 1)
)
prvtEpsDefectAlarm.setObjects(
      *(("PRVT-EPS-MIB", "prvtEpsServiceOperationalStatus"),
        ("PRVT-EPS-MIB", "prvtEpsServiceDefectFop"))
)
if mibBuilder.loadTexts:
    prvtEpsDefectAlarm.setStatus(
        "current"
    )

prvtEpsSwitchoverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 2)
)
prvtEpsSwitchoverAlarm.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsServiceActivePath")
)
if mibBuilder.loadTexts:
    prvtEpsSwitchoverAlarm.setStatus(
        "current"
    )

prvtEpsLostCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 3)
)
prvtEpsLostCommunication.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsSvcId")
)
if mibBuilder.loadTexts:
    prvtEpsLostCommunication.setStatus(
        "current"
    )

prvtEpsRestoredCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 4)
)
prvtEpsRestoredCommunication.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsSvcId")
)
if mibBuilder.loadTexts:
    prvtEpsRestoredCommunication.setStatus(
        "current"
    )

prvtEpsSignalFailDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 5)
)
prvtEpsSignalFailDetected.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsSvcId")
)
if mibBuilder.loadTexts:
    prvtEpsSignalFailDetected.setStatus(
        "current"
    )

prvtEpsSignalDegradeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 6)
)
prvtEpsSignalDegradeDetected.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsSvcId")
)
if mibBuilder.loadTexts:
    prvtEpsSignalDegradeDetected.setStatus(
        "current"
    )

prvtEpsProtctSignalFailDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 7)
)
prvtEpsProtctSignalFailDetected.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsSvcId")
)
if mibBuilder.loadTexts:
    prvtEpsProtctSignalFailDetected.setStatus(
        "current"
    )

prvtEpsSignalFailRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 8)
)
prvtEpsSignalFailRecovery.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsSvcId")
)
if mibBuilder.loadTexts:
    prvtEpsSignalFailRecovery.setStatus(
        "current"
    )

prvtEpsSignalDegradeRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 9)
)
prvtEpsSignalDegradeRecovery.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsSvcId")
)
if mibBuilder.loadTexts:
    prvtEpsSignalDegradeRecovery.setStatus(
        "current"
    )

prvtEpsProtctSignalFailRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 10)
)
prvtEpsProtctSignalFailRecovery.setObjects(
    ("PRVT-EPS-MIB", "prvtEpsSvcId")
)
if mibBuilder.loadTexts:
    prvtEpsProtctSignalFailRecovery.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-EPS-MIB",
    **{"PrvtEpsRequestStateType": PrvtEpsRequestStateType,
       "PrvtEpsProtectionType": PrvtEpsProtectionType,
       "PrvtEpsDirectionType": PrvtEpsDirectionType,
       "PrvtEpsActivePathType": PrvtEpsActivePathType,
       "PrvtEpsMonitoringType": PrvtEpsMonitoringType,
       "PrvtEpsDefectFopType": PrvtEpsDefectFopType,
       "PrvtEpsPathStatusType": PrvtEpsPathStatusType,
       "prvtEpsMib": prvtEpsMib,
       "prvtEpsMibNotifications": prvtEpsMibNotifications,
       "prvtEpsDefectAlarm": prvtEpsDefectAlarm,
       "prvtEpsSwitchoverAlarm": prvtEpsSwitchoverAlarm,
       "prvtEpsLostCommunication": prvtEpsLostCommunication,
       "prvtEpsRestoredCommunication": prvtEpsRestoredCommunication,
       "prvtEpsSignalFailDetected": prvtEpsSignalFailDetected,
       "prvtEpsSignalDegradeDetected": prvtEpsSignalDegradeDetected,
       "prvtEpsProtctSignalFailDetected": prvtEpsProtctSignalFailDetected,
       "prvtEpsSignalFailRecovery": prvtEpsSignalFailRecovery,
       "prvtEpsSignalDegradeRecovery": prvtEpsSignalDegradeRecovery,
       "prvtEpsProtctSignalFailRecovery": prvtEpsProtctSignalFailRecovery,
       "prvtEpsMibObjects": prvtEpsMibObjects,
       "prvtEpsService": prvtEpsService,
       "prvtEpsServiceTable": prvtEpsServiceTable,
       "prvtEpsServiceEntry": prvtEpsServiceEntry,
       "prvtEpsSvcId": prvtEpsSvcId,
       "prvtEpsServiceCfmMdLevel": prvtEpsServiceCfmMdLevel,
       "prvtEpsServicePrimaryLocalCfmMep": prvtEpsServicePrimaryLocalCfmMep,
       "prvtEpsServicePrimaryRemoteCfmMep": prvtEpsServicePrimaryRemoteCfmMep,
       "prvtEpsServiceSecondaryLocalCfmMep": prvtEpsServiceSecondaryLocalCfmMep,
       "prvtEpsServiceSecondaryRemoteCfmMep": prvtEpsServiceSecondaryRemoteCfmMep,
       "prvtEpsServiceLocalState": prvtEpsServiceLocalState,
       "prvtEpsServiceHoldOffTimer": prvtEpsServiceHoldOffTimer,
       "prvtEpsServiceWaitToRestoreTimer": prvtEpsServiceWaitToRestoreTimer,
       "prvtEpsServiceApsChannel": prvtEpsServiceApsChannel,
       "prvtEpsServiceProtection": prvtEpsServiceProtection,
       "prvtEpsServiceDirection": prvtEpsServiceDirection,
       "prvtEpsServiceRevertive": prvtEpsServiceRevertive,
       "prvtEpsServiceActivePath": prvtEpsServiceActivePath,
       "prvtEpsServiceDegradeTestType": prvtEpsServiceDegradeTestType,
       "prvtEpsServiceDegradeTestOwner": prvtEpsServiceDegradeTestOwner,
       "prvtEpsServiceDegradeTestName": prvtEpsServiceDegradeTestName,
       "prvtEpsServiceDegradeTestEnable": prvtEpsServiceDegradeTestEnable,
       "prvtEpsServiceDefectFop": prvtEpsServiceDefectFop,
       "prvtEpsServiceOperationalStatus": prvtEpsServiceOperationalStatus,
       "prvtEpsServicePrimaryStatus": prvtEpsServicePrimaryStatus,
       "prvtEpsServiceSecondaryStatus": prvtEpsServiceSecondaryStatus,
       "prvtEpsServiceRemoteState": prvtEpsServiceRemoteState,
       "prvtEpsServiceRemoteApsChannel": prvtEpsServiceRemoteApsChannel,
       "prvtEpsServiceRemoteProtection": prvtEpsServiceRemoteProtection,
       "prvtEpsServiceRemoteDirection": prvtEpsServiceRemoteDirection,
       "prvtEpsServiceRemoteRevertive": prvtEpsServiceRemoteRevertive,
       "prvtEpsServiceAdminFreeze": prvtEpsServiceAdminFreeze,
       "prvtEpsServiceAdminStatus": prvtEpsServiceAdminStatus,
       "prvtEpsServiceRowStatus": prvtEpsServiceRowStatus,
       "prvtEpsServiceProtectionCounter": prvtEpsServiceProtectionCounter}
)
