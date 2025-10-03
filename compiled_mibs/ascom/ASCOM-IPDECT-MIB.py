# SNMP MIB module (ASCOM-IPDECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ascom\ASCOM-IPDECT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:35 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ascomIpdectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ascomIpdectMIB.setRevisions(
        ("1917-06-27 00:00",
         "1917-02-15 00:00",
         "1914-01-17 00:00",
         "1913-10-07 00:00",
         "1913-10-04 00:00",
         "1913-05-14 00:00",
         "1913-05-07 00:00",
         "1913-04-22 00:00",
         "1912-09-11 00:00",
         "1912-08-31 00:00",
         "1910-11-23 00:00",
         "1910-06-17 00:00",
         "1908-09-25 00:00",
         "1907-12-01 00:00",
         "1907-12-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ascom_ObjectIdentity = ObjectIdentity
ascom = _Ascom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27614)
)
_AscomTraps_ObjectIdentity = ObjectIdentity
ascomTraps = _AscomTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27614, 0)
)
_AscomMibs_ObjectIdentity = ObjectIdentity
ascomMibs = _AscomMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27614, 1)
)
_AscomIpdect_ObjectIdentity = ObjectIdentity
ascomIpdect = _AscomIpdect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1)
)
_IpDectAttr_ObjectIdentity = ObjectIdentity
ipDectAttr = _IpDectAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 1)
)
_IpDectFaultLogEntries_Type = Integer32
_IpDectFaultLogEntries_Object = MibScalar
ipDectFaultLogEntries = _IpDectFaultLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 1, 1),
    _IpDectFaultLogEntries_Type()
)
ipDectFaultLogEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultLogEntries.setStatus("current")
_IpDectAlarmLogEntries_Type = Integer32
_IpDectAlarmLogEntries_Object = MibScalar
ipDectAlarmLogEntries = _IpDectAlarmLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 1, 2),
    _IpDectAlarmLogEntries_Type()
)
ipDectAlarmLogEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectAlarmLogEntries.setStatus("current")
_IpDectLastErrorCode_Type = Integer32
_IpDectLastErrorCode_Object = MibScalar
ipDectLastErrorCode = _IpDectLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 1, 3),
    _IpDectLastErrorCode_Type()
)
ipDectLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectLastErrorCode.setStatus("current")
_IpDectFaults_ObjectIdentity = ObjectIdentity
ipDectFaults = _IpDectFaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2)
)
_IpDectFaultLogTable_Object = MibTable
ipDectFaultLogTable = _IpDectFaultLogTable_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipDectFaultLogTable.setStatus("current")
_IpDectFaultLogEntry_Object = MibTableRow
ipDectFaultLogEntry = _IpDectFaultLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1)
)
ipDectFaultLogEntry.setIndexNames(
    (0, "ASCOM-IPDECT-MIB", "ipDectFaultIndex"),
)
if mibBuilder.loadTexts:
    ipDectFaultLogEntry.setStatus("current")


class _IpDectFaultIndex_Type(Integer32):
    """Custom type ipDectFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpDectFaultIndex_Type.__name__ = "Integer32"
_IpDectFaultIndex_Object = MibTableColumn
ipDectFaultIndex = _IpDectFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 1),
    _IpDectFaultIndex_Type()
)
ipDectFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultIndex.setStatus("current")
_IpDectFaultDate_Type = OctetString
_IpDectFaultDate_Object = MibTableColumn
ipDectFaultDate = _IpDectFaultDate_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 2),
    _IpDectFaultDate_Type()
)
ipDectFaultDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultDate.setStatus("current")
_IpDectFaultTime_Type = OctetString
_IpDectFaultTime_Object = MibTableColumn
ipDectFaultTime = _IpDectFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 3),
    _IpDectFaultTime_Type()
)
ipDectFaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultTime.setStatus("current")


class _IpDectFaultActivity_Type(Integer32):
    """Custom type ipDectFaultActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("alarmCleared", 1),
          ("alarmTimeout", 2),
          ("error", 3))
    )


_IpDectFaultActivity_Type.__name__ = "Integer32"
_IpDectFaultActivity_Object = MibTableColumn
ipDectFaultActivity = _IpDectFaultActivity_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 4),
    _IpDectFaultActivity_Type()
)
ipDectFaultActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultActivity.setStatus("current")


class _IpDectFaultCode_Type(Integer32):
    """Custom type ipDectFaultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65537,
              65538,
              65539,
              196609,
              196865,
              197121,
              197122,
              197123,
              197124,
              197125,
              197126,
              197127,
              197128,
              197136,
              197377,
              197378,
              197379,
              197380,
              197633,
              327681,
              327682,
              327683,
              327684,
              327686,
              327688,
              327689,
              393217,
              393218,
              393219,
              393220,
              393221,
              393222,
              458753,
              458755,
              458756,
              458757,
              458759,
              458763,
              524289,
              524290,
              720897,
              786954,
              786964,
              786965,
              786966,
              786974,
              786984,
              786985,
              786986,
              786987,
              786988,
              786989,
              786990,
              786991,
              786992,
              786993,
              786994,
              786995,
              787004,
              787014,
              787015,
              787024,
              787034,
              787044,
              787459,
              787462,
              787463,
              790528,
              790529,
              917505,
              917506,
              917507,
              917508,
              917509,
              917510,
              917512,
              917513,
              917514,
              983041,
              983042,
              983044,
              983048,
              983056,
              1048577,
              1048578,
              1048580,
              1048584,
              1114112,
              1114113,
              1114114,
              1114137,
              1114138,
              1114139,
              1114177,
              1114182,
              1114183,
              1114185,
              1114192,
              1114193,
              1114195,
              1114202,
              1114203,
              1114204,
              1114205,
              1114206,
              1114207,
              1179649,
              1310721,
              1310821,
              1310822,
              1310823,
              1376257,
              1638401,
              1638402,
              1703937,
              1704192,
              2097152,
              2162689,
              2162690,
              2162691,
              2162692,
              2162693,
              2162694)
        )
    )
    namedValues = NamedValues(
        *(("gwInterfaceDown", 65537),
          ("gwRegDown", 65538),
          ("gwProtocolError", 65539),
          ("usersTheLdapReplicatorIsNotConnected", 196609),
          ("radioCpuResourcesAreNotAvailable", 196865),
          ("masterStandbyActive", 197121),
          ("masterUserRegDown", 197122),
          ("masterEmergencyRegDown", 197123),
          ("masterRadioRegDown", 197124),
          ("masterPrimaryOrRedundantTrunkIsDown", 197125),
          ("masterActive", 197126),
          ("masterInactive", 197127),
          ("masterLimitStaticRadiosReached", 197128),
          ("masterAbnormalCallRelease", 197136),
          ("mobmInboundMobmRegDown", 197377),
          ("mobmOutboundMobmRegDown", 197378),
          ("mobmMasterRegDown", 197379),
          ("mobmStandbyActive", 197380),
          ("cmInboundMobmRegDown", 197633),
          ("rtpNoMediaDataReceived", 327681),
          ("rtpExcessiveLossOfData", 327682),
          ("rtpWrongPayloadTypeReceived", 327683),
          ("rtpStunFailure", 327684),
          ("rtpSrtcpAuthFailure", 327686),
          ("rtpIceFailure", 327688),
          ("rtpSrtpAuthFailure", 327689),
          ("h323UnexpectedMessageReceived", 393217),
          ("h323StatusEnquiry", 393218),
          ("h323SignalingTCPFailed", 393219),
          ("h323SignalingTimeout", 393220),
          ("h323SrtpKeyMismatch", 393221),
          ("h323MediaIncompatible", 393222),
          ("sipNatDiscoverFailure", 458753),
          ("sipOverloadDetected", 458755),
          ("sipCoderSelectionFailure", 458756),
          ("sipMediaConfigFailure", 458757),
          ("sipIntMediaNegotiationFailed", 458759),
          ("sipDnsFailed", 458763),
          ("webmInvalidUrl", 524289),
          ("webmCoderMissingInUrl", 524290),
          ("cmdRestart", 720897),
          ("tlsUnexpectedMessage", 786954),
          ("tlsBadMac", 786964),
          ("tlsDecryptionFailed", 786965),
          ("tlsRecordOverflow", 786966),
          ("tlsDecompressionFailure", 786974),
          ("tlsHandshakeFailure", 786984),
          ("tlsNoCertificate", 786985),
          ("tlsBadCertificate", 786986),
          ("tlsUnsupportedCertificate", 786987),
          ("tlsRevocedCertificate", 786988),
          ("tlsExpiredCertificate", 786989),
          ("tlsUnknownCertificate", 786990),
          ("tlsIllegalParameter", 786991),
          ("tlsUnknownCA", 786992),
          ("tlsAccessDenied", 786993),
          ("tlsDecodeError", 786994),
          ("tlsDecryptionError", 786995),
          ("tlsExportRestriction", 787004),
          ("tlsProtocolVersion", 787014),
          ("tlsInsufficientSecurity", 787015),
          ("tlsInternalError", 787024),
          ("tlsUserCancelled", 787034),
          ("tlsNoRenegotiation", 787044),
          ("kerberosServiceNotFound", 787459),
          ("kerberosServerUnreachable", 787462),
          ("kerberosCrossRealmFailure", 787463),
          ("x509SystemTimeNotSet", 790528),
          ("x509CertificateNearExpiration", 790529),
          ("rfpDisconnected", 917505),
          ("rfpMalfunctioning", 917506),
          ("rfpDisabled", 917507),
          ("rfpSwDlFailed", 917508),
          ("rfpUnsynchronized", 917509),
          ("rfpAlienSyncLost", 917510),
          ("rfpDetectedSysidCollision", 917512),
          ("rfpSyncMasterFailedToResynchronizeToReference", 917513),
          ("rfpRestarted", 917514),
          ("envHighTemperature", 983041),
          ("envHighPowerConsumption", 983042),
          ("envSupplyVoltageLow", 983044),
          ("envSupplyVoltageHigh", 983048),
          ("envFanFailure", 983056),
          ("syncRingBroken", 1048577),
          ("syncRefSignalLost", 1048578),
          ("syncLost", 1048580),
          ("syncUnsynchronizedToReference", 1048584),
          ("ipInterfaceDown", 1114112),
          ("ipInterfaceNotConfigured", 1114113),
          ("ipDhcpServerNotResponding", 1114114),
          ("ipInvalidUdpRtpPortRange", 1114137),
          ("ipInvalidUdpNatPortRange", 1114138),
          ("ipInvalidNatPortRange", 1114139),
          ("ipArpPoisoningDetected", 1114177),
          ("ipOutOfTcpNatPorts", 1114182),
          ("ipOutOfTcpPorts", 1114183),
          ("ipTcpBindError", 1114185),
          ("ipOutOfUdpRtpPorts", 1114192),
          ("ipOutOfUdpPorts", 1114193),
          ("ipUdpBindError", 1114195),
          ("ipNoRouteToDestination", 1114202),
          ("ipNoRouteToDestinationIfDown", 1114203),
          ("ipNoRouteToDestinationIfUnknown", 1114204),
          ("ipNoRouteToDestinationIfNotConfigured", 1114205),
          ("ipNoRouteToDestinationNoGateway", 1114206),
          ("ipNoRouteToDestinationLoop", 1114207),
          ("boxMemoryLow", 1179649),
          ("rfpBusyForSpeech", 1310721),
          ("dectDefEncKeyTimeout", 1310821),
          ("dectCipherTimeout", 1310822),
          ("dectMasterConnectionTimeout", 1310823),
          ("sysBusyForSpeech", 1376257),
          ("provisioningDataCommunicationsError", 1638401),
          ("provisioningDataCommunicationsPutError", 1638402),
          ("uniteCommunicationFailure", 1703937),
          ("cuniteCommunicationFailure", 1704192),
          ("icpConnectionDown", 2097152),
          ("updateScriptGetFailed", 2162689),
          ("bootGetFailed", 2162690),
          ("firmwareGetFailed", 2162691),
          ("configGetFailed", 2162692),
          ("bmcGetFailed", 2162693),
          ("configPutFailed", 2162694))
    )


_IpDectFaultCode_Type.__name__ = "Integer32"
_IpDectFaultCode_Object = MibTableColumn
ipDectFaultCode = _IpDectFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 5),
    _IpDectFaultCode_Type()
)
ipDectFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultCode.setStatus("current")


class _IpDectFaultSeverity_Type(Integer32):
    """Custom type ipDectFaultSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 0),
          ("major", 1),
          ("critical", 2),
          ("none", 99))
    )


_IpDectFaultSeverity_Type.__name__ = "Integer32"
_IpDectFaultSeverity_Object = MibTableColumn
ipDectFaultSeverity = _IpDectFaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 6),
    _IpDectFaultSeverity_Type()
)
ipDectFaultSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultSeverity.setStatus("current")
_IpDectFaultSource_Type = OctetString
_IpDectFaultSource_Object = MibTableColumn
ipDectFaultSource = _IpDectFaultSource_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 7),
    _IpDectFaultSource_Type()
)
ipDectFaultSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultSource.setStatus("current")
_IpDectFaultIp_Type = IpAddress
_IpDectFaultIp_Object = MibTableColumn
ipDectFaultIp = _IpDectFaultIp_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 8),
    _IpDectFaultIp_Type()
)
ipDectFaultIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultIp.setStatus("current")
_IpDectFaultDescription_Type = OctetString
_IpDectFaultDescription_Object = MibTableColumn
ipDectFaultDescription = _IpDectFaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 1, 1, 9),
    _IpDectFaultDescription_Type()
)
ipDectFaultDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectFaultDescription.setStatus("current")
_IpDectActiveAlarmsTable_Object = MibTable
ipDectActiveAlarmsTable = _IpDectActiveAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipDectActiveAlarmsTable.setStatus("current")
_IpDectActiveAlarmsEntry_Object = MibTableRow
ipDectActiveAlarmsEntry = _IpDectActiveAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1)
)
ipDectActiveAlarmsEntry.setIndexNames(
    (0, "ASCOM-IPDECT-MIB", "ipDectActiveAlarmsIndex"),
)
if mibBuilder.loadTexts:
    ipDectActiveAlarmsEntry.setStatus("current")


class _IpDectActiveAlarmsIndex_Type(Integer32):
    """Custom type ipDectActiveAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpDectActiveAlarmsIndex_Type.__name__ = "Integer32"
_IpDectActiveAlarmsIndex_Object = MibTableColumn
ipDectActiveAlarmsIndex = _IpDectActiveAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 1),
    _IpDectActiveAlarmsIndex_Type()
)
ipDectActiveAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectActiveAlarmsIndex.setStatus("current")
_IpDectAlarmDate_Type = OctetString
_IpDectAlarmDate_Object = MibTableColumn
ipDectAlarmDate = _IpDectAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 2),
    _IpDectAlarmDate_Type()
)
ipDectAlarmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectAlarmDate.setStatus("current")
_IpDectAlarmTime_Type = OctetString
_IpDectAlarmTime_Object = MibTableColumn
ipDectAlarmTime = _IpDectAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 3),
    _IpDectAlarmTime_Type()
)
ipDectAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectAlarmTime.setStatus("current")


class _IpDectAlarmCode_Type(Integer32):
    """Custom type ipDectAlarmCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65537,
              65538,
              65539,
              196609,
              196865,
              197121,
              197122,
              197123,
              197124,
              197125,
              197126,
              197127,
              197128,
              197136,
              197377,
              197378,
              197379,
              197380,
              197633,
              327681,
              327682,
              327683,
              327684,
              327686,
              327688,
              327689,
              393217,
              393218,
              393219,
              393220,
              393221,
              393222,
              458753,
              458755,
              458756,
              458757,
              458759,
              458763,
              524289,
              524290,
              720897,
              786954,
              786964,
              786965,
              786966,
              786974,
              786984,
              786985,
              786986,
              786987,
              786988,
              786989,
              786990,
              786991,
              786992,
              786993,
              786994,
              786995,
              787004,
              787014,
              787015,
              787024,
              787034,
              787044,
              787459,
              787462,
              787463,
              790528,
              790529,
              917505,
              917506,
              917507,
              917508,
              917509,
              917510,
              917512,
              917513,
              917514,
              983041,
              983042,
              983044,
              983048,
              983056,
              1048577,
              1048578,
              1048580,
              1048584,
              1114112,
              1114113,
              1114114,
              1114137,
              1114138,
              1114139,
              1114177,
              1114182,
              1114183,
              1114185,
              1114192,
              1114193,
              1114195,
              1114202,
              1114203,
              1114204,
              1114205,
              1114206,
              1114207,
              1179649,
              1310721,
              1310821,
              1310822,
              1310823,
              1376257,
              1638401,
              1638402,
              1703937,
              1704192,
              2097152,
              2162689,
              2162690,
              2162691,
              2162692,
              2162693,
              2162694)
        )
    )
    namedValues = NamedValues(
        *(("gwInterfaceDown", 65537),
          ("gwRegDown", 65538),
          ("gwProtocolError", 65539),
          ("usersTheLdapReplicatorIsNotConnected", 196609),
          ("radioCpuResourcesAreNotAvailable", 196865),
          ("masterStandbyActive", 197121),
          ("masterUserRegDown", 197122),
          ("masterEmergencyRegDown", 197123),
          ("masterRadioRegDown", 197124),
          ("masterPrimaryOrRedundantTrunkIsDown", 197125),
          ("masterActive", 197126),
          ("masterInactive", 197127),
          ("masterLimitStaticRadiosReached", 197128),
          ("masterAbnormalCallRelease", 197136),
          ("mobmInboundMobmRegDown", 197377),
          ("mobmOutboundMobmRegDown", 197378),
          ("mobmMasterRegDown", 197379),
          ("mobmStandbyActive", 197380),
          ("cmInboundMobmRegDown", 197633),
          ("rtpNoMediaDataReceived", 327681),
          ("rtpExcessiveLossOfData", 327682),
          ("rtpWrongPayloadTypeReceived", 327683),
          ("rtpStunFailure", 327684),
          ("rtpSrtcpAuthFailure", 327686),
          ("rtpIceFailure", 327688),
          ("rtpSrtpAuthFailure", 327689),
          ("h323UnexpectedMessageReceived", 393217),
          ("h323StatusEnquiry", 393218),
          ("h323SignalingTCPFailed", 393219),
          ("h323SignalingTimeout", 393220),
          ("h323SrtpKeyMismatch", 393221),
          ("h323MediaIncompatible", 393222),
          ("sipNatDiscoverFailure", 458753),
          ("sipOverloadDetected", 458755),
          ("sipCoderSelectionFailure", 458756),
          ("sipMediaConfigFailure", 458757),
          ("sipIntMediaNegotiationFailed", 458759),
          ("sipDnsFailed", 458763),
          ("webmInvalidUrl", 524289),
          ("webmCoderMissingInUrl", 524290),
          ("cmdRestart", 720897),
          ("tlsUnexpectedMessage", 786954),
          ("tlsBadMac", 786964),
          ("tlsDecryptionFailed", 786965),
          ("tlsRecordOverflow", 786966),
          ("tlsDecompressionFailure", 786974),
          ("tlsHandshakeFailure", 786984),
          ("tlsNoCertificate", 786985),
          ("tlsBadCertificate", 786986),
          ("tlsUnsupportedCertificate", 786987),
          ("tlsRevocedCertificate", 786988),
          ("tlsExpiredCertificate", 786989),
          ("tlsUnknownCertificate", 786990),
          ("tlsIllegalParameter", 786991),
          ("tlsUnknownCA", 786992),
          ("tlsAccessDenied", 786993),
          ("tlsDecodeError", 786994),
          ("tlsDecryptionError", 786995),
          ("tlsExportRestriction", 787004),
          ("tlsProtocolVersion", 787014),
          ("tlsInsufficientSecurity", 787015),
          ("tlsInternalError", 787024),
          ("tlsUserCancelled", 787034),
          ("tlsNoRenegotiation", 787044),
          ("kerberosServiceNotFound", 787459),
          ("kerberosServerUnreachable", 787462),
          ("kerberosCrossRealmFailure", 787463),
          ("x509SystemTimeNotSet", 790528),
          ("x509CertificateNearExpiration", 790529),
          ("rfpDisconnected", 917505),
          ("rfpMalfunctioning", 917506),
          ("rfpDisabled", 917507),
          ("rfpSwDlFailed", 917508),
          ("rfpUnsynchronized", 917509),
          ("rfpAlienSyncLost", 917510),
          ("rfpDetectedSysidCollision", 917512),
          ("rfpSyncMasterFailedToResynchronizeToReference", 917513),
          ("rfpRestarted", 917514),
          ("envHighTemperature", 983041),
          ("envHighPowerConsumption", 983042),
          ("envSupplyVoltageLow", 983044),
          ("envSupplyVoltageHigh", 983048),
          ("envFanFailure", 983056),
          ("syncRingBroken", 1048577),
          ("syncRefSignalLost", 1048578),
          ("syncLost", 1048580),
          ("syncUnsynchronizedToReference", 1048584),
          ("ipInterfaceDown", 1114112),
          ("ipInterfaceNotConfigured", 1114113),
          ("ipDhcpServerNotResponding", 1114114),
          ("ipInvalidUdpRtpPortRange", 1114137),
          ("ipInvalidUdpNatPortRange", 1114138),
          ("ipInvalidNatPortRange", 1114139),
          ("ipArpPoisoningDetected", 1114177),
          ("ipOutOfTcpNatPorts", 1114182),
          ("ipOutOfTcpPorts", 1114183),
          ("ipTcpBindError", 1114185),
          ("ipOutOfUdpRtpPorts", 1114192),
          ("ipOutOfUdpPorts", 1114193),
          ("ipUdpBindError", 1114195),
          ("ipNoRouteToDestination", 1114202),
          ("ipNoRouteToDestinationIfDown", 1114203),
          ("ipNoRouteToDestinationIfUnknown", 1114204),
          ("ipNoRouteToDestinationIfNotConfigured", 1114205),
          ("ipNoRouteToDestinationNoGateway", 1114206),
          ("ipNoRouteToDestinationLoop", 1114207),
          ("boxMemoryLow", 1179649),
          ("rfpBusyForSpeech", 1310721),
          ("dectDefEncKeyTimeout", 1310821),
          ("dectCipherTimeout", 1310822),
          ("dectMasterConnectionTimeout", 1310823),
          ("sysBusyForSpeech", 1376257),
          ("provisioningDataCommunicationsError", 1638401),
          ("provisioningDataCommunicationsPutError", 1638402),
          ("uniteCommunicationFailure", 1703937),
          ("cuniteCommunicationFailure", 1704192),
          ("icpConnectionDown", 2097152),
          ("updateScriptGetFailed", 2162689),
          ("bootGetFailed", 2162690),
          ("firmwareGetFailed", 2162691),
          ("configGetFailed", 2162692),
          ("bmcGetFailed", 2162693),
          ("configPutFailed", 2162694))
    )


_IpDectAlarmCode_Type.__name__ = "Integer32"
_IpDectAlarmCode_Object = MibTableColumn
ipDectAlarmCode = _IpDectAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 4),
    _IpDectAlarmCode_Type()
)
ipDectAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectAlarmCode.setStatus("current")


class _IpDectAlarmSeverity_Type(Integer32):
    """Custom type ipDectAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 0),
          ("major", 1),
          ("critical", 2))
    )


_IpDectAlarmSeverity_Type.__name__ = "Integer32"
_IpDectAlarmSeverity_Object = MibTableColumn
ipDectAlarmSeverity = _IpDectAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 5),
    _IpDectAlarmSeverity_Type()
)
ipDectAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectAlarmSeverity.setStatus("current")
_IpDectAlarmSource_Type = OctetString
_IpDectAlarmSource_Object = MibTableColumn
ipDectAlarmSource = _IpDectAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 6),
    _IpDectAlarmSource_Type()
)
ipDectAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectAlarmSource.setStatus("current")
_IpDectAlarmIp_Type = IpAddress
_IpDectAlarmIp_Object = MibTableColumn
ipDectAlarmIp = _IpDectAlarmIp_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 7),
    _IpDectAlarmIp_Type()
)
ipDectAlarmIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectAlarmIp.setStatus("current")
_IpDectAlarmDescription_Type = OctetString
_IpDectAlarmDescription_Object = MibTableColumn
ipDectAlarmDescription = _IpDectAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 27614, 1, 1, 1, 2, 2, 1, 8),
    _IpDectAlarmDescription_Type()
)
ipDectAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDectAlarmDescription.setStatus("current")

# Managed Objects groups


# Notification objects

ascomColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 0)
)
if mibBuilder.loadTexts:
    ascomColdStart.setStatus(
        "current"
    )

ascomWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 1)
)
if mibBuilder.loadTexts:
    ascomWarmStart.setStatus(
        "current"
    )

ascomLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 2)
)
ascomLinkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ascomLinkDown.setStatus(
        "current"
    )

ascomLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 3)
)
ascomLinkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ascomLinkUp.setStatus(
        "current"
    )

ascomAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 4)
)
if mibBuilder.loadTexts:
    ascomAuthenticationFailure.setStatus(
        "current"
    )

ipDectSetCriticalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 11)
)
ipDectSetCriticalAlarmTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectSetCriticalAlarmTrap.setStatus(
        "current"
    )

ipDectSetMajorAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 12)
)
ipDectSetMajorAlarmTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectSetMajorAlarmTrap.setStatus(
        "current"
    )

ipDectSetMinorAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 13)
)
ipDectSetMinorAlarmTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectSetMinorAlarmTrap.setStatus(
        "current"
    )

ipDectSetIndeterminateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 14)
)
ipDectSetIndeterminateAlarmTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectSetIndeterminateAlarmTrap.setStatus(
        "current"
    )

ipDectClearAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 15)
)
ipDectClearAlarmTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectClearAlarmTrap.setStatus(
        "current"
    )

ipDectCriticalFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 16)
)
ipDectCriticalFaultTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectCriticalFaultTrap.setStatus(
        "current"
    )

ipDectMajorFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 17)
)
ipDectMajorFaultTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectMajorFaultTrap.setStatus(
        "current"
    )

ipDectMinorFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 18)
)
ipDectMinorFaultTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectMinorFaultTrap.setStatus(
        "current"
    )

ipDectIndeterminateFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27614, 0, 19)
)
ipDectIndeterminateFaultTrap.setObjects(
    ("ASCOM-IPDECT-MIB", "ipDectLastErrorCode")
)
if mibBuilder.loadTexts:
    ipDectIndeterminateFaultTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCOM-IPDECT-MIB",
    **{"ascom": ascom,
       "ascomTraps": ascomTraps,
       "ascomColdStart": ascomColdStart,
       "ascomWarmStart": ascomWarmStart,
       "ascomLinkDown": ascomLinkDown,
       "ascomLinkUp": ascomLinkUp,
       "ascomAuthenticationFailure": ascomAuthenticationFailure,
       "ipDectSetCriticalAlarmTrap": ipDectSetCriticalAlarmTrap,
       "ipDectSetMajorAlarmTrap": ipDectSetMajorAlarmTrap,
       "ipDectSetMinorAlarmTrap": ipDectSetMinorAlarmTrap,
       "ipDectSetIndeterminateAlarmTrap": ipDectSetIndeterminateAlarmTrap,
       "ipDectClearAlarmTrap": ipDectClearAlarmTrap,
       "ipDectCriticalFaultTrap": ipDectCriticalFaultTrap,
       "ipDectMajorFaultTrap": ipDectMajorFaultTrap,
       "ipDectMinorFaultTrap": ipDectMinorFaultTrap,
       "ipDectIndeterminateFaultTrap": ipDectIndeterminateFaultTrap,
       "ascomMibs": ascomMibs,
       "ascomIpdect": ascomIpdect,
       "ascomIpdectMIB": ascomIpdectMIB,
       "ipDectAttr": ipDectAttr,
       "ipDectFaultLogEntries": ipDectFaultLogEntries,
       "ipDectAlarmLogEntries": ipDectAlarmLogEntries,
       "ipDectLastErrorCode": ipDectLastErrorCode,
       "ipDectFaults": ipDectFaults,
       "ipDectFaultLogTable": ipDectFaultLogTable,
       "ipDectFaultLogEntry": ipDectFaultLogEntry,
       "ipDectFaultIndex": ipDectFaultIndex,
       "ipDectFaultDate": ipDectFaultDate,
       "ipDectFaultTime": ipDectFaultTime,
       "ipDectFaultActivity": ipDectFaultActivity,
       "ipDectFaultCode": ipDectFaultCode,
       "ipDectFaultSeverity": ipDectFaultSeverity,
       "ipDectFaultSource": ipDectFaultSource,
       "ipDectFaultIp": ipDectFaultIp,
       "ipDectFaultDescription": ipDectFaultDescription,
       "ipDectActiveAlarmsTable": ipDectActiveAlarmsTable,
       "ipDectActiveAlarmsEntry": ipDectActiveAlarmsEntry,
       "ipDectActiveAlarmsIndex": ipDectActiveAlarmsIndex,
       "ipDectAlarmDate": ipDectAlarmDate,
       "ipDectAlarmTime": ipDectAlarmTime,
       "ipDectAlarmCode": ipDectAlarmCode,
       "ipDectAlarmSeverity": ipDectAlarmSeverity,
       "ipDectAlarmSource": ipDectAlarmSource,
       "ipDectAlarmIp": ipDectAlarmIp,
       "ipDectAlarmDescription": ipDectAlarmDescription}
)
