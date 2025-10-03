# SNMP MIB module (TRELLIX-SENSOR-CONF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\trellix\TRELLIX-SENSOR-CONF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:48 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")

(TrellixCUGEType,
 TrellixFEType,
 TrellixGEType,
 TrellixIDSAction,
 TrellixIDSActionResult,
 TrellixIDSActionStatus,
 TrellixIDSCardType,
 TrellixIDSOperatingMode,
 TrellixIDSPortType,
 TrellixIDSResponseMode,
 TrellixPluggableModuleType,
 TrellixPortLinearIndex,
 TrellixPortSpeed,
 TrellixTFTPAction,
 TrellixTFTPFailedResult,
 TrellixTFTPFileType,
 TrellixTFTPInProgressResult,
 TrellixTFTPStatus) = mibBuilder.importSymbols(
    "TRELLIX-INTRUVERT-TC",
    "TrellixCUGEType",
    "TrellixFEType",
    "TrellixGEType",
    "TrellixIDSAction",
    "TrellixIDSActionResult",
    "TrellixIDSActionStatus",
    "TrellixIDSCardType",
    "TrellixIDSOperatingMode",
    "TrellixIDSPortType",
    "TrellixIDSResponseMode",
    "TrellixPluggableModuleType",
    "TrellixPortLinearIndex",
    "TrellixPortSpeed",
    "TrellixTFTPAction",
    "TrellixTFTPFailedResult",
    "TrellixTFTPFileType",
    "TrellixTFTPInProgressResult",
    "TrellixTFTPStatus")

(intfPhysicalPortIndex,
 intfPortIndex,
 intfVirtualPortIndex,
 intfVirtualSlotIndex,
 ivSensorConfiguration,
 ntpServerIndex,
 processorNumIndex,
 respPortIndex,
 slotIndex,
 sslProbeIpv4Index,
 sslProbeIpv6Index) = mibBuilder.importSymbols(
    "TRELLIX-SENSOR-SMI",
    "intfPhysicalPortIndex",
    "intfPortIndex",
    "intfVirtualPortIndex",
    "intfVirtualSlotIndex",
    "ivSensorConfiguration",
    "ntpServerIndex",
    "processorNumIndex",
    "respPortIndex",
    "slotIndex",
    "sslProbeIpv4Index",
    "sslProbeIpv6Index")


# MODULE-IDENTITY

ivSensorConfigurationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ivSensorConfigurationMIB.setRevisions(
        ("2007-06-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemGrp_ObjectIdentity = ObjectIdentity
systemGrp = _SystemGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1)
)


class _IvSysName_Type(DisplayString):
    """Custom type ivSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IvSysName_Type.__name__ = "DisplayString"
_IvSysName_Object = MibScalar
ivSysName = _IvSysName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 1),
    _IvSysName_Type()
)
ivSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysName.setStatus("current")


class _IvSysLocation_Type(DisplayString):
    """Custom type ivSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IvSysLocation_Type.__name__ = "DisplayString"
_IvSysLocation_Object = MibScalar
ivSysLocation = _IvSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 2),
    _IvSysLocation_Type()
)
ivSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysLocation.setStatus("current")


class _IvSysContact_Type(DisplayString):
    """Custom type ivSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IvSysContact_Type.__name__ = "DisplayString"
_IvSysContact_Object = MibScalar
ivSysContact = _IvSysContact_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 3),
    _IvSysContact_Type()
)
ivSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysContact.setStatus("current")


class _IvSysModel_Type(DisplayString):
    """Custom type ivSysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IvSysModel_Type.__name__ = "DisplayString"
_IvSysModel_Object = MibScalar
ivSysModel = _IvSysModel_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 4),
    _IvSysModel_Type()
)
ivSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysModel.setStatus("current")


class _IvSysSerialNumber_Type(DisplayString):
    """Custom type ivSysSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_IvSysSerialNumber_Type.__name__ = "DisplayString"
_IvSysSerialNumber_Object = MibScalar
ivSysSerialNumber = _IvSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 5),
    _IvSysSerialNumber_Type()
)
ivSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysSerialNumber.setStatus("current")


class _IvSysDescr_Type(DisplayString):
    """Custom type ivSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IvSysDescr_Type.__name__ = "DisplayString"
_IvSysDescr_Object = MibScalar
ivSysDescr = _IvSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 6),
    _IvSysDescr_Type()
)
ivSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysDescr.setStatus("current")
_IvSysObjectID_Type = ObjectIdentifier
_IvSysObjectID_Object = MibScalar
ivSysObjectID = _IvSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 7),
    _IvSysObjectID_Type()
)
ivSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysObjectID.setStatus("current")
_IvSysUpTime_Type = TimeTicks
_IvSysUpTime_Object = MibScalar
ivSysUpTime = _IvSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 8),
    _IvSysUpTime_Type()
)
ivSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysUpTime.setStatus("current")
_IvSysLastCfgTime_Type = DateAndTime
_IvSysLastCfgTime_Object = MibScalar
ivSysLastCfgTime = _IvSysLastCfgTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 9),
    _IvSysLastCfgTime_Type()
)
ivSysLastCfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysLastCfgTime.setStatus("current")
_IvSysDiskSpaceLeft_Type = Integer32
_IvSysDiskSpaceLeft_Object = MibScalar
ivSysDiskSpaceLeft = _IvSysDiskSpaceLeft_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 10),
    _IvSysDiskSpaceLeft_Type()
)
ivSysDiskSpaceLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysDiskSpaceLeft.setStatus("current")


class _IvSysAlertChannelStatus_Type(Integer32):
    """Custom type ivSysAlertChannelStatus based on Integer32"""
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
        *(("down", 0),
          ("up", 1),
          ("errorInGetTimeFromManager", 2),
          ("errorGeneratingCertificates", 3),
          ("errorPersistingCertificates", 4),
          ("errorConnectingToManager", 5),
          ("errorInUntrustedConnectionSetup", 6),
          ("errorInInstall", 7),
          ("errorPersistingManagerPublicCertificate", 8),
          ("errorInMutualTrustMatch", 9),
          ("errorInSnmpKeyExchange", 10),
          ("errorInInitialProtocolMessageExchange", 11),
          ("sensorInstallInProgress", 12),
          ("openingAlertChannelInProgress", 13),
          ("errorInLinkHenceReopening", 14),
          ("errorInChannelReopening", 15),
          ("closingChannelInProgress", 16),
          ("errorClosingChannel", 17),
          ("sendAlertWarning", 18),
          ("keepAliveWarning", 19),
          ("errorDeletingCerts", 20),
          ("errorCreatingSnmpUser", 21),
          ("errorChangingSnmpUserKeys", 22))
    )


_IvSysAlertChannelStatus_Type.__name__ = "Integer32"
_IvSysAlertChannelStatus_Object = MibScalar
ivSysAlertChannelStatus = _IvSysAlertChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 11),
    _IvSysAlertChannelStatus_Type()
)
ivSysAlertChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysAlertChannelStatus.setStatus("current")


class _IvSysPacketLogChannelStatus_Type(Integer32):
    """Custom type ivSysPacketLogChannelStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("errorInGetTimeFromManager", 2),
          ("errorGeneratingCertificates", 3),
          ("errorPersistingCertificates", 4),
          ("errorConnectingToManager", 5),
          ("errorInUntrustedConnectionSetup", 6),
          ("errorInInstall", 7),
          ("errorPersistingManagerPublicCertificate", 8),
          ("errorInMutualTrustMatch", 9),
          ("errorInSnmpKeyExchange", 10),
          ("errorInInitialProtocolMessageExchange", 11),
          ("packetLogInstallInProgress", 12),
          ("openingPacketLogInProgress", 13),
          ("errorInLinkHenceReopening", 14),
          ("errorInChannelReopening", 15),
          ("closingChannelInProgress", 16),
          ("errorClosingChannel", 17),
          ("sendLogWarning", 18),
          ("keepAliveWarning", 19))
    )


_IvSysPacketLogChannelStatus_Type.__name__ = "Integer32"
_IvSysPacketLogChannelStatus_Object = MibScalar
ivSysPacketLogChannelStatus = _IvSysPacketLogChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 12),
    _IvSysPacketLogChannelStatus_Type()
)
ivSysPacketLogChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysPacketLogChannelStatus.setStatus("current")


class _IvSysHealth_Type(Integer32):
    """Custom type ivSysHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 0),
          ("good", 1),
          ("uninitialized", 2))
    )


_IvSysHealth_Type.__name__ = "Integer32"
_IvSysHealth_Object = MibScalar
ivSysHealth = _IvSysHealth_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 13),
    _IvSysHealth_Type()
)
ivSysHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysHealth.setStatus("current")


class _IvSysResetPassword_Type(Integer32):
    """Custom type ivSysResetPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("resetPassword", 1))
    )


_IvSysResetPassword_Type.__name__ = "Integer32"
_IvSysResetPassword_Object = MibScalar
ivSysResetPassword = _IvSysResetPassword_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 14),
    _IvSysResetPassword_Type()
)
ivSysResetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysResetPassword.setStatus("current")


class _IvSysDeleteSignatures_Type(Integer32):
    """Custom type ivSysDeleteSignatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("deleteSignatures", 1))
    )


_IvSysDeleteSignatures_Type.__name__ = "Integer32"
_IvSysDeleteSignatures_Object = MibScalar
ivSysDeleteSignatures = _IvSysDeleteSignatures_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 15),
    _IvSysDeleteSignatures_Type()
)
ivSysDeleteSignatures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysDeleteSignatures.setStatus("current")


class _IvSysSlaveSerialNumber_Type(DisplayString):
    """Custom type ivSysSlaveSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_IvSysSlaveSerialNumber_Type.__name__ = "DisplayString"
_IvSysSlaveSerialNumber_Object = MibScalar
ivSysSlaveSerialNumber = _IvSysSlaveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 16),
    _IvSysSlaveSerialNumber_Type()
)
ivSysSlaveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysSlaveSerialNumber.setStatus("current")


class _IvSysUIDSeed_Type(Integer32):
    """Custom type ivSysUIDSeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IvSysUIDSeed_Type.__name__ = "Integer32"
_IvSysUIDSeed_Object = MibScalar
ivSysUIDSeed = _IvSysUIDSeed_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 17),
    _IvSysUIDSeed_Type()
)
ivSysUIDSeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysUIDSeed.setStatus("current")


class _IvSysFipsMode_Type(Integer32):
    """Custom type ivSysFipsMode based on Integer32"""
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


_IvSysFipsMode_Type.__name__ = "Integer32"
_IvSysFipsMode_Object = MibScalar
ivSysFipsMode = _IvSysFipsMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 18),
    _IvSysFipsMode_Type()
)
ivSysFipsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysFipsMode.setStatus("current")
_IvSysNumLbPorts_Type = Integer32
_IvSysNumLbPorts_Object = MibScalar
ivSysNumLbPorts = _IvSysNumLbPorts_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 19),
    _IvSysNumLbPorts_Type()
)
ivSysNumLbPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysNumLbPorts.setStatus("current")
_IvSysUpTimeNew_Type = Counter64
_IvSysUpTimeNew_Object = MibScalar
ivSysUpTimeNew = _IvSysUpTimeNew_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 20),
    _IvSysUpTimeNew_Type()
)
ivSysUpTimeNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysUpTimeNew.setStatus("current")
_IvSysCapacityMode_Type = Counter64
_IvSysCapacityMode_Object = MibScalar
ivSysCapacityMode = _IvSysCapacityMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 21),
    _IvSysCapacityMode_Type()
)
ivSysCapacityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysCapacityMode.setStatus("current")
_IvSysCurrentCapacityMode_Type = Counter64
_IvSysCurrentCapacityMode_Object = MibScalar
ivSysCurrentCapacityMode = _IvSysCurrentCapacityMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 22),
    _IvSysCurrentCapacityMode_Type()
)
ivSysCurrentCapacityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysCurrentCapacityMode.setStatus("current")
_IvSysDeviceMode_Type = Counter64
_IvSysDeviceMode_Object = MibScalar
ivSysDeviceMode = _IvSysDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 23),
    _IvSysDeviceMode_Type()
)
ivSysDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysDeviceMode.setStatus("current")
_IvSysConfDeviceMode_Type = Counter64
_IvSysConfDeviceMode_Object = MibScalar
ivSysConfDeviceMode = _IvSysConfDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 24),
    _IvSysConfDeviceMode_Type()
)
ivSysConfDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysConfDeviceMode.setStatus("current")
_IvSysRebootStatus_Type = Counter64
_IvSysRebootStatus_Object = MibScalar
ivSysRebootStatus = _IvSysRebootStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 25),
    _IvSysRebootStatus_Type()
)
ivSysRebootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysRebootStatus.setStatus("current")


class _IvSysRebootReason_Type(DisplayString):
    """Custom type ivSysRebootReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IvSysRebootReason_Type.__name__ = "DisplayString"
_IvSysRebootReason_Object = MibScalar
ivSysRebootReason = _IvSysRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 1, 26),
    _IvSysRebootReason_Type()
)
ivSysRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysRebootReason.setStatus("current")
_SystemIPCfgGrp_ObjectIdentity = ObjectIdentity
systemIPCfgGrp = _SystemIPCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2)
)
_IvSysIPAddress_Type = IpAddress
_IvSysIPAddress_Object = MibScalar
ivSysIPAddress = _IvSysIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 1),
    _IvSysIPAddress_Type()
)
ivSysIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysIPAddress.setStatus("current")
_IvSysMACAddress_Type = MacAddress
_IvSysMACAddress_Object = MibScalar
ivSysMACAddress = _IvSysMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 2),
    _IvSysMACAddress_Type()
)
ivSysMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysMACAddress.setStatus("current")
_IvSysSubnetMask_Type = IpAddress
_IvSysSubnetMask_Object = MibScalar
ivSysSubnetMask = _IvSysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 3),
    _IvSysSubnetMask_Type()
)
ivSysSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysSubnetMask.setStatus("current")
_IvSysGateway_Type = IpAddress
_IvSysGateway_Object = MibScalar
ivSysGateway = _IvSysGateway_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 4),
    _IvSysGateway_Type()
)
ivSysGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysGateway.setStatus("current")
_IvSysIPv6Address_Type = Ipv6Address
_IvSysIPv6Address_Object = MibScalar
ivSysIPv6Address = _IvSysIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 5),
    _IvSysIPv6Address_Type()
)
ivSysIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysIPv6Address.setStatus("current")


class _IvSysIpv6SubnetMask_Type(Integer32):
    """Custom type ivSysIpv6SubnetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IvSysIpv6SubnetMask_Type.__name__ = "Integer32"
_IvSysIpv6SubnetMask_Object = MibScalar
ivSysIpv6SubnetMask = _IvSysIpv6SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 6),
    _IvSysIpv6SubnetMask_Type()
)
ivSysIpv6SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysIpv6SubnetMask.setStatus("current")
_IvSysIpv6Gateway_Type = Ipv6Address
_IvSysIpv6Gateway_Object = MibScalar
ivSysIpv6Gateway = _IvSysIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 7),
    _IvSysIpv6Gateway_Type()
)
ivSysIpv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysIpv6Gateway.setStatus("current")
_IvSysVmHostIPAddress_Type = IpAddress
_IvSysVmHostIPAddress_Object = MibScalar
ivSysVmHostIPAddress = _IvSysVmHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 8),
    _IvSysVmHostIPAddress_Type()
)
ivSysVmHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysVmHostIPAddress.setStatus("current")
_IvSysVmHostIPv6Address_Type = Ipv6Address
_IvSysVmHostIPv6Address_Object = MibScalar
ivSysVmHostIPv6Address = _IvSysVmHostIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 9),
    _IvSysVmHostIPv6Address_Type()
)
ivSysVmHostIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysVmHostIPv6Address.setStatus("current")


class _IvSysVmHostName_Type(DisplayString):
    """Custom type ivSysVmHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IvSysVmHostName_Type.__name__ = "DisplayString"
_IvSysVmHostName_Object = MibScalar
ivSysVmHostName = _IvSysVmHostName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 10),
    _IvSysVmHostName_Type()
)
ivSysVmHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysVmHostName.setStatus("current")


class _IvSysVmMgmtAdditionalInfo_Type(DisplayString):
    """Custom type ivSysVmMgmtAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IvSysVmMgmtAdditionalInfo_Type.__name__ = "DisplayString"
_IvSysVmMgmtAdditionalInfo_Object = MibScalar
ivSysVmMgmtAdditionalInfo = _IvSysVmMgmtAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 2, 11),
    _IvSysVmMgmtAdditionalInfo_Type()
)
ivSysVmMgmtAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysVmMgmtAdditionalInfo.setStatus("current")
_SystemFailoverGrp_ObjectIdentity = ObjectIdentity
systemFailoverGrp = _SystemFailoverGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 3)
)


class _IvSysFailoverStatus_Type(Integer32):
    """Custom type ivSysFailoverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("peer-up", 1),
          ("peer-down", 2),
          ("peer-incompatible", 3))
    )


_IvSysFailoverStatus_Type.__name__ = "Integer32"
_IvSysFailoverStatus_Object = MibScalar
ivSysFailoverStatus = _IvSysFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 3, 1),
    _IvSysFailoverStatus_Type()
)
ivSysFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivSysFailoverStatus.setStatus("current")


class _IvSysFailoverAction_Type(Integer32):
    """Custom type ivSysFailoverAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_IvSysFailoverAction_Type.__name__ = "Integer32"
_IvSysFailoverAction_Object = MibScalar
ivSysFailoverAction = _IvSysFailoverAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 3, 2),
    _IvSysFailoverAction_Type()
)
ivSysFailoverAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysFailoverAction.setStatus("current")


class _IvSysFailoverMode_Type(Integer32):
    """Custom type ivSysFailoverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_IvSysFailoverMode_Type.__name__ = "Integer32"
_IvSysFailoverMode_Object = MibScalar
ivSysFailoverMode = _IvSysFailoverMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 3, 3),
    _IvSysFailoverMode_Type()
)
ivSysFailoverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysFailoverMode.setStatus("current")


class _IvSysFailopenAction_Type(Integer32):
    """Custom type ivSysFailopenAction based on Integer32"""
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


_IvSysFailopenAction_Type.__name__ = "Integer32"
_IvSysFailopenAction_Object = MibScalar
ivSysFailopenAction = _IvSysFailopenAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 3, 4),
    _IvSysFailopenAction_Type()
)
ivSysFailopenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysFailopenAction.setStatus("current")


class _IvSysSTPForwardConfig_Type(Integer32):
    """Custom type ivSysSTPForwardConfig based on Integer32"""
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


_IvSysSTPForwardConfig_Type.__name__ = "Integer32"
_IvSysSTPForwardConfig_Object = MibScalar
ivSysSTPForwardConfig = _IvSysSTPForwardConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 3, 5),
    _IvSysSTPForwardConfig_Type()
)
ivSysSTPForwardConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivSysSTPForwardConfig.setStatus("current")
_EmsGrp_ObjectIdentity = ObjectIdentity
emsGrp = _EmsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4)
)
_EmsTable_Object = MibTable
emsTable = _EmsTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    emsTable.setStatus("current")
_EmsEntry_Object = MibTableRow
emsEntry = _EmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1)
)
emsEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "emsIndex"),
)
if mibBuilder.loadTexts:
    emsEntry.setStatus("current")


class _EmsIndex_Type(Integer32):
    """Custom type emsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EmsIndex_Type.__name__ = "Integer32"
_EmsIndex_Object = MibTableColumn
emsIndex = _EmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 1),
    _EmsIndex_Type()
)
emsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emsIndex.setStatus("current")


class _EmsPriority_Type(Integer32):
    """Custom type emsPriority based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("standalone", 3),
          ("unknown", 4))
    )


_EmsPriority_Type.__name__ = "Integer32"
_EmsPriority_Object = MibTableColumn
emsPriority = _EmsPriority_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 2),
    _EmsPriority_Type()
)
emsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsPriority.setStatus("current")
_EmsIPAddress_Type = IpAddress
_EmsIPAddress_Object = MibTableColumn
emsIPAddress = _EmsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 3),
    _EmsIPAddress_Type()
)
emsIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsIPAddress.setStatus("current")


class _EmsHAMode_Type(Integer32):
    """Custom type emsHAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failover", 1),
          ("standalone", 2),
          ("unknown", 3))
    )


_EmsHAMode_Type.__name__ = "Integer32"
_EmsHAMode_Object = MibTableColumn
emsHAMode = _EmsHAMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 4),
    _EmsHAMode_Type()
)
emsHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsHAMode.setStatus("current")


class _EmsHAStatus_Type(Integer32):
    """Custom type emsHAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("standby", 3))
    )


_EmsHAStatus_Type.__name__ = "Integer32"
_EmsHAStatus_Object = MibTableColumn
emsHAStatus = _EmsHAStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 5),
    _EmsHAStatus_Type()
)
emsHAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsHAStatus.setStatus("current")


class _EmsAlertChannelStatus_Type(Integer32):
    """Custom type emsAlertChannelStatus based on Integer32"""
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
        *(("down", 0),
          ("up", 1),
          ("errorInGetTimeFromManager", 2),
          ("errorGeneratingCertificates", 3),
          ("errorPersistingCertificates", 4),
          ("errorConnectingToManager", 5),
          ("errorInUntrustedConnectionSetup", 6),
          ("errorInInstall", 7),
          ("errorPersistingManagerPublicCertificate", 8),
          ("errorInMutualTrustMatch", 9),
          ("errorInSnmpKeyExchange", 10),
          ("errorInInitialProtocolMessageExchange", 11),
          ("sensorInstallInProgress", 12),
          ("openingAlertChannelInProgress", 13),
          ("errorInLinkHenceReopening", 14),
          ("errorInChannelReopening", 15),
          ("closingChannelInProgress", 16),
          ("errorClosingChannel", 17),
          ("sendAlertWarning", 18),
          ("keepAliveWarning", 19),
          ("errorDeletingCerts", 20),
          ("errorCreatingSnmpUser", 21),
          ("errorChangingSnmpUserKeys", 22))
    )


_EmsAlertChannelStatus_Type.__name__ = "Integer32"
_EmsAlertChannelStatus_Object = MibTableColumn
emsAlertChannelStatus = _EmsAlertChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 6),
    _EmsAlertChannelStatus_Type()
)
emsAlertChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsAlertChannelStatus.setStatus("current")


class _EmsPacketLogChannelStatus_Type(Integer32):
    """Custom type emsPacketLogChannelStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("errorInGetTimeFromManager", 2),
          ("errorGeneratingCertificates", 3),
          ("errorPersistingCertificates", 4),
          ("errorConnectingToManager", 5),
          ("errorInUntrustedConnectionSetup", 6),
          ("errorInInstall", 7),
          ("errorPersistingManagerPublicCertificate", 8),
          ("errorInMutualTrustMatch", 9),
          ("errorInSnmpKeyExchange", 10),
          ("errorInInitialProtocolMessageExchange", 11),
          ("packetLogInstallInProgress", 12),
          ("openingPacketLogInProgress", 13),
          ("errorInLinkHenceReopening", 14),
          ("errorInChannelReopening", 15),
          ("closingChannelInProgress", 16),
          ("errorClosingChannel", 17),
          ("sendLogWarning", 18),
          ("keepAliveWarning", 19))
    )


_EmsPacketLogChannelStatus_Type.__name__ = "Integer32"
_EmsPacketLogChannelStatus_Object = MibTableColumn
emsPacketLogChannelStatus = _EmsPacketLogChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 7),
    _EmsPacketLogChannelStatus_Type()
)
emsPacketLogChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsPacketLogChannelStatus.setStatus("current")
_EmsIPv6Address_Type = Ipv6Address
_EmsIPv6Address_Object = MibTableColumn
emsIPv6Address = _EmsIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 8),
    _EmsIPv6Address_Type()
)
emsIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsIPv6Address.setStatus("current")


class _EmsIPAddressType_Type(Integer32):
    """Custom type emsIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_EmsIPAddressType_Type.__name__ = "Integer32"
_EmsIPAddressType_Object = MibTableColumn
emsIPAddressType = _EmsIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 9),
    _EmsIPAddressType_Type()
)
emsIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsIPAddressType.setStatus("current")


class _EmsAuthChannelStatus_Type(Integer32):
    """Custom type emsAuthChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_EmsAuthChannelStatus_Type.__name__ = "Integer32"
_EmsAuthChannelStatus_Object = MibTableColumn
emsAuthChannelStatus = _EmsAuthChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 1, 1, 10),
    _EmsAuthChannelStatus_Type()
)
emsAuthChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsAuthChannelStatus.setStatus("current")


class _EmsChangeAction_Type(Integer32):
    """Custom type emsChangeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("standalone-to-ha", 1),
          ("ha-to-standalone", 2),
          ("switchover", 3),
          ("add-ism-sec-ip", 4))
    )


_EmsChangeAction_Type.__name__ = "Integer32"
_EmsChangeAction_Object = MibScalar
emsChangeAction = _EmsChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 2),
    _EmsChangeAction_Type()
)
emsChangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsChangeAction.setStatus("current")
_EmsParamIpAddress_Type = IpAddress
_EmsParamIpAddress_Object = MibScalar
emsParamIpAddress = _EmsParamIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 3),
    _EmsParamIpAddress_Type()
)
emsParamIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsParamIpAddress.setStatus("current")


class _EmsParamPriority_Type(Integer32):
    """Custom type emsParamPriority based on Integer32"""
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
        *(("other", 0),
          ("primary", 1),
          ("secondary", 2),
          ("standalone", 3))
    )


_EmsParamPriority_Type.__name__ = "Integer32"
_EmsParamPriority_Object = MibScalar
emsParamPriority = _EmsParamPriority_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 4),
    _EmsParamPriority_Type()
)
emsParamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsParamPriority.setStatus("current")
_EmsParamAddIpAddress_Type = IpAddress
_EmsParamAddIpAddress_Object = MibScalar
emsParamAddIpAddress = _EmsParamAddIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 5),
    _EmsParamAddIpAddress_Type()
)
emsParamAddIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsParamAddIpAddress.setStatus("current")
_EmsParamIpv6Address_Type = Ipv6Address
_EmsParamIpv6Address_Object = MibScalar
emsParamIpv6Address = _EmsParamIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 6),
    _EmsParamIpv6Address_Type()
)
emsParamIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsParamIpv6Address.setStatus("current")
_EmsParamAddIpv6Address_Type = Ipv6Address
_EmsParamAddIpv6Address_Object = MibScalar
emsParamAddIpv6Address = _EmsParamAddIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 7),
    _EmsParamAddIpv6Address_Type()
)
emsParamAddIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsParamAddIpv6Address.setStatus("current")


class _EmsTenantId_Type(OctetString):
    """Custom type emsTenantId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_EmsTenantId_Type.__name__ = "OctetString"
_EmsTenantId_Object = MibScalar
emsTenantId = _EmsTenantId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 8),
    _EmsTenantId_Type()
)
emsTenantId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsTenantId.setStatus("current")


class _EmsPrimaryNSMGUID_Type(OctetString):
    """Custom type emsPrimaryNSMGUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_EmsPrimaryNSMGUID_Type.__name__ = "OctetString"
_EmsPrimaryNSMGUID_Object = MibScalar
emsPrimaryNSMGUID = _EmsPrimaryNSMGUID_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 9),
    _EmsPrimaryNSMGUID_Type()
)
emsPrimaryNSMGUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsPrimaryNSMGUID.setStatus("current")


class _EmsSecondaryNSMGUID_Type(OctetString):
    """Custom type emsSecondaryNSMGUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_EmsSecondaryNSMGUID_Type.__name__ = "OctetString"
_EmsSecondaryNSMGUID_Object = MibScalar
emsSecondaryNSMGUID = _EmsSecondaryNSMGUID_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 4, 10),
    _EmsSecondaryNSMGUID_Type()
)
emsSecondaryNSMGUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsSecondaryNSMGUID.setStatus("current")
_TftpGrp_ObjectIdentity = ObjectIdentity
tftpGrp = _TftpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5)
)


class _TftpKey_Type(OctetString):
    """Custom type tftpKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_TftpKey_Type.__name__ = "OctetString"
_TftpKey_Object = MibScalar
tftpKey = _TftpKey_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 1),
    _TftpKey_Type()
)
tftpKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpKey.setStatus("current")


class _TftpFileSize_Type(Integer32):
    """Custom type tftpFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 134217727),
    )


_TftpFileSize_Type.__name__ = "Integer32"
_TftpFileSize_Object = MibScalar
tftpFileSize = _TftpFileSize_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 2),
    _TftpFileSize_Type()
)
tftpFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileSize.setStatus("current")


class _TftpFileName_Type(DisplayString):
    """Custom type tftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TftpFileName_Type.__name__ = "DisplayString"
_TftpFileName_Object = MibScalar
tftpFileName = _TftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 3),
    _TftpFileName_Type()
)
tftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileName.setStatus("current")
_TftpServerAddress_Type = IpAddress
_TftpServerAddress_Object = MibScalar
tftpServerAddress = _TftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 4),
    _TftpServerAddress_Type()
)
tftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerAddress.setStatus("current")
_TftpAction_Type = TrellixTFTPAction
_TftpAction_Object = MibScalar
tftpAction = _TftpAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 5),
    _TftpAction_Type()
)
tftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpAction.setStatus("current")
_TftpActionStatus_Type = TrellixTFTPStatus
_TftpActionStatus_Object = MibScalar
tftpActionStatus = _TftpActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 6),
    _TftpActionStatus_Type()
)
tftpActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpActionStatus.setStatus("current")
_TftpActionInProgressResult_Type = TrellixTFTPInProgressResult
_TftpActionInProgressResult_Object = MibScalar
tftpActionInProgressResult = _TftpActionInProgressResult_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 7),
    _TftpActionInProgressResult_Type()
)
tftpActionInProgressResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpActionInProgressResult.setStatus("current")
_TftpActionFailedResult_Type = TrellixTFTPFailedResult
_TftpActionFailedResult_Object = MibScalar
tftpActionFailedResult = _TftpActionFailedResult_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 8),
    _TftpActionFailedResult_Type()
)
tftpActionFailedResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpActionFailedResult.setStatus("current")
_TftpActionTransactionId_Type = Integer32
_TftpActionTransactionId_Object = MibScalar
tftpActionTransactionId = _TftpActionTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 9),
    _TftpActionTransactionId_Type()
)
tftpActionTransactionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpActionTransactionId.setStatus("current")
_TftpServerIpv6Address_Type = Ipv6Address
_TftpServerIpv6Address_Object = MibScalar
tftpServerIpv6Address = _TftpServerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 10),
    _TftpServerIpv6Address_Type()
)
tftpServerIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIpv6Address.setStatus("current")


class _TftpIVKey_Type(OctetString):
    """Custom type tftpIVKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_TftpIVKey_Type.__name__ = "OctetString"
_TftpIVKey_Object = MibScalar
tftpIVKey = _TftpIVKey_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 5, 11),
    _TftpIVKey_Type()
)
tftpIVKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpIVKey.setStatus("current")
_ChassisGrp_ObjectIdentity = ObjectIdentity
chassisGrp = _ChassisGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7)
)


class _TemperatureStatus_Type(Integer32):
    """Custom type temperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("abnormal", 1))
    )


_TemperatureStatus_Type.__name__ = "Integer32"
_TemperatureStatus_Object = MibScalar
temperatureStatus = _TemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 1),
    _TemperatureStatus_Type()
)
temperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureStatus.setStatus("current")


class _FanStatus_Type(Integer32):
    """Custom type fanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("abnormal", 1),
          ("removed", 2))
    )


_FanStatus_Type.__name__ = "Integer32"
_FanStatus_Object = MibScalar
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 2),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("current")


class _PrimaryPowerSupplyStatus_Type(Integer32):
    """Custom type primaryPowerSupplyStatus based on Integer32"""
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
        *(("not-present", 0),
          ("present-operational", 1),
          ("present-nonoperational", 2),
          ("error", 3))
    )


_PrimaryPowerSupplyStatus_Type.__name__ = "Integer32"
_PrimaryPowerSupplyStatus_Object = MibScalar
primaryPowerSupplyStatus = _PrimaryPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 3),
    _PrimaryPowerSupplyStatus_Type()
)
primaryPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryPowerSupplyStatus.setStatus("current")


class _SecondaryPowerSupplyStatus_Type(Integer32):
    """Custom type secondaryPowerSupplyStatus based on Integer32"""
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
        *(("not-present", 0),
          ("present-operational", 1),
          ("present-nonoperational", 2),
          ("error", 3))
    )


_SecondaryPowerSupplyStatus_Type.__name__ = "Integer32"
_SecondaryPowerSupplyStatus_Object = MibScalar
secondaryPowerSupplyStatus = _SecondaryPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 4),
    _SecondaryPowerSupplyStatus_Type()
)
secondaryPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryPowerSupplyStatus.setStatus("current")


class _PciLegacyErrorStatus_Type(DisplayString):
    """Custom type pciLegacyErrorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PciLegacyErrorStatus_Type.__name__ = "DisplayString"
_PciLegacyErrorStatus_Object = MibScalar
pciLegacyErrorStatus = _PciLegacyErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 5),
    _PciLegacyErrorStatus_Type()
)
pciLegacyErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pciLegacyErrorStatus.setStatus("current")


class _PciFatalError1Status_Type(DisplayString):
    """Custom type pciFatalError1Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PciFatalError1Status_Type.__name__ = "DisplayString"
_PciFatalError1Status_Object = MibScalar
pciFatalError1Status = _PciFatalError1Status_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 6),
    _PciFatalError1Status_Type()
)
pciFatalError1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pciFatalError1Status.setStatus("current")


class _PciFatalError2Status_Type(DisplayString):
    """Custom type pciFatalError2Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PciFatalError2Status_Type.__name__ = "DisplayString"
_PciFatalError2Status_Object = MibScalar
pciFatalError2Status = _PciFatalError2Status_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 7),
    _PciFatalError2Status_Type()
)
pciFatalError2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pciFatalError2Status.setStatus("current")


class _SystemEventLogStatus_Type(DisplayString):
    """Custom type systemEventLogStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SystemEventLogStatus_Type.__name__ = "DisplayString"
_SystemEventLogStatus_Object = MibScalar
systemEventLogStatus = _SystemEventLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 8),
    _SystemEventLogStatus_Type()
)
systemEventLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEventLogStatus.setStatus("current")


class _BmcWatchdogStatus_Type(DisplayString):
    """Custom type bmcWatchdogStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_BmcWatchdogStatus_Type.__name__ = "DisplayString"
_BmcWatchdogStatus_Object = MibScalar
bmcWatchdogStatus = _BmcWatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 9),
    _BmcWatchdogStatus_Type()
)
bmcWatchdogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcWatchdogStatus.setStatus("current")
_ProcessorStatusTable_Object = MibTable
processorStatusTable = _ProcessorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 10)
)
if mibBuilder.loadTexts:
    processorStatusTable.setStatus("current")
_ProcessorStatusEntry_Object = MibTableRow
processorStatusEntry = _ProcessorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 10, 1)
)
processorStatusEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "processorNumIndex"),
)
if mibBuilder.loadTexts:
    processorStatusEntry.setStatus("current")


class _ProcessorStatus_Type(DisplayString):
    """Custom type processorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ProcessorStatus_Type.__name__ = "DisplayString"
_ProcessorStatus_Object = MibTableColumn
processorStatus = _ProcessorStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 10, 1, 1),
    _ProcessorStatus_Type()
)
processorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorStatus.setStatus("current")


class _MemoryECCStatus_Type(DisplayString):
    """Custom type memoryECCStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MemoryECCStatus_Type.__name__ = "DisplayString"
_MemoryECCStatus_Object = MibScalar
memoryECCStatus = _MemoryECCStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 11),
    _MemoryECCStatus_Type()
)
memoryECCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryECCStatus.setStatus("current")


class _PostSysEventStatus_Type(DisplayString):
    """Custom type postSysEventStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PostSysEventStatus_Type.__name__ = "DisplayString"
_PostSysEventStatus_Object = MibScalar
postSysEventStatus = _PostSysEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 12),
    _PostSysEventStatus_Type()
)
postSysEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postSysEventStatus.setStatus("current")


class _PostErrorStatus_Type(DisplayString):
    """Custom type postErrorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PostErrorStatus_Type.__name__ = "DisplayString"
_PostErrorStatus_Object = MibScalar
postErrorStatus = _PostErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 7, 13),
    _PostErrorStatus_Type()
)
postErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postErrorStatus.setStatus("current")
_ManagementCardGrp_ObjectIdentity = ObjectIdentity
managementCardGrp = _ManagementCardGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8)
)
_MgmtCardTable_Object = MibTable
mgmtCardTable = _MgmtCardTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mgmtCardTable.setStatus("current")
_MgmtCardEntry_Object = MibTableRow
mgmtCardEntry = _MgmtCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1, 1)
)
mgmtCardEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
)
if mibBuilder.loadTexts:
    mgmtCardEntry.setStatus("current")
_McAction_Type = TrellixIDSAction
_McAction_Object = MibTableColumn
mcAction = _McAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1, 1, 1),
    _McAction_Type()
)
mcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcAction.setStatus("current")
_McActionStatus_Type = TrellixIDSActionStatus
_McActionStatus_Object = MibTableColumn
mcActionStatus = _McActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1, 1, 2),
    _McActionStatus_Type()
)
mcActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcActionStatus.setStatus("current")
_McActionResult_Type = TrellixIDSActionResult
_McActionResult_Object = MibTableColumn
mcActionResult = _McActionResult_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1, 1, 3),
    _McActionResult_Type()
)
mcActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcActionResult.setStatus("current")


class _McHwVersion_Type(DisplayString):
    """Custom type mcHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_McHwVersion_Type.__name__ = "DisplayString"
_McHwVersion_Object = MibTableColumn
mcHwVersion = _McHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1, 1, 4),
    _McHwVersion_Type()
)
mcHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHwVersion.setStatus("current")


class _McCurrentSwVersion_Type(DisplayString):
    """Custom type mcCurrentSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_McCurrentSwVersion_Type.__name__ = "DisplayString"
_McCurrentSwVersion_Object = MibTableColumn
mcCurrentSwVersion = _McCurrentSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1, 1, 5),
    _McCurrentSwVersion_Type()
)
mcCurrentSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcCurrentSwVersion.setStatus("current")


class _McFutureSwFileName_Type(DisplayString):
    """Custom type mcFutureSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_McFutureSwFileName_Type.__name__ = "DisplayString"
_McFutureSwFileName_Object = MibTableColumn
mcFutureSwFileName = _McFutureSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1, 1, 6),
    _McFutureSwFileName_Type()
)
mcFutureSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcFutureSwFileName.setStatus("current")
_McDateAndTime_Type = DateAndTime
_McDateAndTime_Object = MibTableColumn
mcDateAndTime = _McDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 8, 1, 1, 7),
    _McDateAndTime_Type()
)
mcDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcDateAndTime.setStatus("current")
_Slave_ChassisGrp_ObjectIdentity = ObjectIdentity
slave_ChassisGrp = _Slave_ChassisGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 9)
)


class _SlaveTemperatureStatus_Type(Integer32):
    """Custom type slaveTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("abnormal", 1))
    )


_SlaveTemperatureStatus_Type.__name__ = "Integer32"
_SlaveTemperatureStatus_Object = MibScalar
slaveTemperatureStatus = _SlaveTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 9, 1),
    _SlaveTemperatureStatus_Type()
)
slaveTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveTemperatureStatus.setStatus("current")


class _SlaveFanStatus_Type(Integer32):
    """Custom type slaveFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("abnormal", 1))
    )


_SlaveFanStatus_Type.__name__ = "Integer32"
_SlaveFanStatus_Object = MibScalar
slaveFanStatus = _SlaveFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 9, 2),
    _SlaveFanStatus_Type()
)
slaveFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveFanStatus.setStatus("current")


class _SlavePrimaryPowerSupplyStatus_Type(Integer32):
    """Custom type slavePrimaryPowerSupplyStatus based on Integer32"""
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
        *(("not-present", 0),
          ("present-operational", 1),
          ("present-nonoperational", 2),
          ("error", 3))
    )


_SlavePrimaryPowerSupplyStatus_Type.__name__ = "Integer32"
_SlavePrimaryPowerSupplyStatus_Object = MibScalar
slavePrimaryPowerSupplyStatus = _SlavePrimaryPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 9, 3),
    _SlavePrimaryPowerSupplyStatus_Type()
)
slavePrimaryPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slavePrimaryPowerSupplyStatus.setStatus("current")


class _SlaveSecondaryPowerSupplyStatus_Type(Integer32):
    """Custom type slaveSecondaryPowerSupplyStatus based on Integer32"""
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
        *(("not-present", 0),
          ("present-operational", 1),
          ("present-nonoperational", 2),
          ("error", 3))
    )


_SlaveSecondaryPowerSupplyStatus_Type.__name__ = "Integer32"
_SlaveSecondaryPowerSupplyStatus_Object = MibScalar
slaveSecondaryPowerSupplyStatus = _SlaveSecondaryPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 9, 4),
    _SlaveSecondaryPowerSupplyStatus_Type()
)
slaveSecondaryPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveSecondaryPowerSupplyStatus.setStatus("current")
_SensorCardGrp_ObjectIdentity = ObjectIdentity
sensorCardGrp = _SensorCardGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10)
)
_SensorCardTable_Object = MibTable
sensorCardTable = _SensorCardTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    sensorCardTable.setStatus("current")
_SensorCardEntry_Object = MibTableRow
sensorCardEntry = _SensorCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1)
)
sensorCardEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
)
if mibBuilder.loadTexts:
    sensorCardEntry.setStatus("current")
_ScAction_Type = TrellixIDSAction
_ScAction_Object = MibTableColumn
scAction = _ScAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 1),
    _ScAction_Type()
)
scAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scAction.setStatus("current")
_ScSigUpdateResult_Type = TrellixIDSActionResult
_ScSigUpdateResult_Object = MibTableColumn
scSigUpdateResult = _ScSigUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 2),
    _ScSigUpdateResult_Type()
)
scSigUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scSigUpdateResult.setStatus("current")


class _ScHwVersion_Type(DisplayString):
    """Custom type scHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ScHwVersion_Type.__name__ = "DisplayString"
_ScHwVersion_Object = MibTableColumn
scHwVersion = _ScHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 3),
    _ScHwVersion_Type()
)
scHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHwVersion.setStatus("current")


class _ScCurrentSwVersion_Type(DisplayString):
    """Custom type scCurrentSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ScCurrentSwVersion_Type.__name__ = "DisplayString"
_ScCurrentSwVersion_Object = MibTableColumn
scCurrentSwVersion = _ScCurrentSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 4),
    _ScCurrentSwVersion_Type()
)
scCurrentSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCurrentSwVersion.setStatus("current")


class _ScFutureSwFileName_Type(DisplayString):
    """Custom type scFutureSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ScFutureSwFileName_Type.__name__ = "DisplayString"
_ScFutureSwFileName_Object = MibTableColumn
scFutureSwFileName = _ScFutureSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 5),
    _ScFutureSwFileName_Type()
)
scFutureSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scFutureSwFileName.setStatus("current")


class _ScCurrentSigVersion_Type(DisplayString):
    """Custom type scCurrentSigVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ScCurrentSigVersion_Type.__name__ = "DisplayString"
_ScCurrentSigVersion_Object = MibTableColumn
scCurrentSigVersion = _ScCurrentSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 6),
    _ScCurrentSigVersion_Type()
)
scCurrentSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCurrentSigVersion.setStatus("current")


class _ScFutureSigFileName_Type(DisplayString):
    """Custom type scFutureSigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ScFutureSigFileName_Type.__name__ = "DisplayString"
_ScFutureSigFileName_Object = MibTableColumn
scFutureSigFileName = _ScFutureSigFileName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 7),
    _ScFutureSigFileName_Type()
)
scFutureSigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scFutureSigFileName.setStatus("current")
_ScMACAddress_Type = MacAddress
_ScMACAddress_Object = MibTableColumn
scMACAddress = _ScMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 8),
    _ScMACAddress_Type()
)
scMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scMACAddress.setStatus("current")


class _ScCurrentBotDATVersion_Type(DisplayString):
    """Custom type scCurrentBotDATVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ScCurrentBotDATVersion_Type.__name__ = "DisplayString"
_ScCurrentBotDATVersion_Object = MibTableColumn
scCurrentBotDATVersion = _ScCurrentBotDATVersion_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 1, 1, 9),
    _ScCurrentBotDATVersion_Type()
)
scCurrentBotDATVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCurrentBotDATVersion.setStatus("current")
_IpTable_Object = MibTable
ipTable = _IpTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6)
)
if mibBuilder.loadTexts:
    ipTable.setStatus("current")
_IpEntry_Object = MibTableRow
ipEntry = _IpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1)
)
ipEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
)
if mibBuilder.loadTexts:
    ipEntry.setStatus("current")


class _IpFragmentTimer_Type(Integer32):
    """Custom type ipFragmentTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 180),
    )


_IpFragmentTimer_Type.__name__ = "Integer32"
_IpFragmentTimer_Object = MibTableColumn
ipFragmentTimer = _IpFragmentTimer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 1),
    _IpFragmentTimer_Type()
)
ipFragmentTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFragmentTimer.setStatus("current")


class _IpOverlapOption_Type(Integer32):
    """Custom type ipOverlapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oldData", 1),
          ("newData", 2))
    )


_IpOverlapOption_Type.__name__ = "Integer32"
_IpOverlapOption_Object = MibTableColumn
ipOverlapOption = _IpOverlapOption_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 2),
    _IpOverlapOption_Type()
)
ipOverlapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipOverlapOption.setStatus("current")


class _IpTTLConfigMode_Type(Integer32):
    """Custom type ipTTLConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTTLChecking", 1),
          ("checkThreshold", 2),
          ("resetTTL", 3))
    )


_IpTTLConfigMode_Type.__name__ = "Integer32"
_IpTTLConfigMode_Object = MibTableColumn
ipTTLConfigMode = _IpTTLConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 3),
    _IpTTLConfigMode_Type()
)
ipTTLConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTTLConfigMode.setStatus("current")


class _IpTTLThreshold_Type(Integer32):
    """Custom type ipTTLThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpTTLThreshold_Type.__name__ = "Integer32"
_IpTTLThreshold_Object = MibTableColumn
ipTTLThreshold = _IpTTLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 4),
    _IpTTLThreshold_Type()
)
ipTTLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTTLThreshold.setStatus("current")


class _IpTTLResetValue_Type(Integer32):
    """Custom type ipTTLResetValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpTTLResetValue_Type.__name__ = "Integer32"
_IpTTLResetValue_Object = MibTableColumn
ipTTLResetValue = _IpTTLResetValue_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 5),
    _IpTTLResetValue_Type()
)
ipTTLResetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTTLResetValue.setStatus("current")


class _IpSmallestFragmentSize_Type(Integer32):
    """Custom type ipSmallestFragmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1480),
    )


_IpSmallestFragmentSize_Type.__name__ = "Integer32"
_IpSmallestFragmentSize_Object = MibTableColumn
ipSmallestFragmentSize = _IpSmallestFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 6),
    _IpSmallestFragmentSize_Type()
)
ipSmallestFragmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSmallestFragmentSize.setStatus("current")


class _IpSmallFragmentThreshold_Type(Integer32):
    """Custom type ipSmallFragmentThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_IpSmallFragmentThreshold_Type.__name__ = "Integer32"
_IpSmallFragmentThreshold_Object = MibTableColumn
ipSmallFragmentThreshold = _IpSmallFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 7),
    _IpSmallFragmentThreshold_Type()
)
ipSmallFragmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSmallFragmentThreshold.setStatus("current")


class _IpFragmentReassemblyOption_Type(Integer32):
    """Custom type ipFragmentReassemblyOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_IpFragmentReassemblyOption_Type.__name__ = "Integer32"
_IpFragmentReassemblyOption_Object = MibTableColumn
ipFragmentReassemblyOption = _IpFragmentReassemblyOption_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 8),
    _IpFragmentReassemblyOption_Type()
)
ipFragmentReassemblyOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFragmentReassemblyOption.setStatus("current")


class _Ipv6OverlapOption_Type(Integer32):
    """Custom type ipv6OverlapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oldData", 1),
          ("newData", 2),
          ("drop", 3))
    )


_Ipv6OverlapOption_Type.__name__ = "Integer32"
_Ipv6OverlapOption_Object = MibTableColumn
ipv6OverlapOption = _Ipv6OverlapOption_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 9),
    _Ipv6OverlapOption_Type()
)
ipv6OverlapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6OverlapOption.setStatus("current")


class _Ipv6SmallestFragmentSize_Type(Integer32):
    """Custom type ipv6SmallestFragmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 1280),
    )


_Ipv6SmallestFragmentSize_Type.__name__ = "Integer32"
_Ipv6SmallestFragmentSize_Object = MibTableColumn
ipv6SmallestFragmentSize = _Ipv6SmallestFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 10),
    _Ipv6SmallestFragmentSize_Type()
)
ipv6SmallestFragmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6SmallestFragmentSize.setStatus("current")


class _Ipv6SmallFragmentThreshold_Type(Integer32):
    """Custom type ipv6SmallFragmentThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_Ipv6SmallFragmentThreshold_Type.__name__ = "Integer32"
_Ipv6SmallFragmentThreshold_Object = MibTableColumn
ipv6SmallFragmentThreshold = _Ipv6SmallFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 6, 1, 11),
    _Ipv6SmallFragmentThreshold_Type()
)
ipv6SmallFragmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6SmallFragmentThreshold.setStatus("current")
_TcpTable_Object = MibTable
tcpTable = _TcpTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7)
)
if mibBuilder.loadTexts:
    tcpTable.setStatus("current")
_TcpEntry_Object = MibTableRow
tcpEntry = _TcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1)
)
tcpEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
)
if mibBuilder.loadTexts:
    tcpEntry.setStatus("current")


class _SupportedUDPFlows_Type(Integer32):
    """Custom type supportedUDPFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_SupportedUDPFlows_Type.__name__ = "Integer32"
_SupportedUDPFlows_Object = MibTableColumn
supportedUDPFlows = _SupportedUDPFlows_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 1),
    _SupportedUDPFlows_Type()
)
supportedUDPFlows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supportedUDPFlows.setStatus("current")


class _TcbInactivityTimer_Type(Integer32):
    """Custom type tcbInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1200),
    )


_TcbInactivityTimer_Type.__name__ = "Integer32"
_TcbInactivityTimer_Object = MibTableColumn
tcbInactivityTimer = _TcbInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 2),
    _TcbInactivityTimer_Type()
)
tcbInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcbInactivityTimer.setStatus("current")


class _TcpSegmentTimer_Type(Integer32):
    """Custom type tcpSegmentTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_TcpSegmentTimer_Type.__name__ = "Integer32"
_TcpSegmentTimer_Object = MibTableColumn
tcpSegmentTimer = _TcpSegmentTimer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 3),
    _TcpSegmentTimer_Type()
)
tcpSegmentTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpSegmentTimer.setStatus("current")


class _Tcp2MSLTimer_Type(Integer32):
    """Custom type tcp2MSLTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 120),
    )


_Tcp2MSLTimer_Type.__name__ = "Integer32"
_Tcp2MSLTimer_Object = MibTableColumn
tcp2MSLTimer = _Tcp2MSLTimer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 4),
    _Tcp2MSLTimer_Type()
)
tcp2MSLTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcp2MSLTimer.setStatus("current")
_InactiveFlowsRSTEnabled_Type = TruthValue
_InactiveFlowsRSTEnabled_Object = MibTableColumn
inactiveFlowsRSTEnabled = _InactiveFlowsRSTEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 5),
    _InactiveFlowsRSTEnabled_Type()
)
inactiveFlowsRSTEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inactiveFlowsRSTEnabled.setStatus("current")
_DropReTxTCPEnabled_Type = TruthValue
_DropReTxTCPEnabled_Object = MibTableColumn
dropReTxTCPEnabled = _DropReTxTCPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 6),
    _DropReTxTCPEnabled_Type()
)
dropReTxTCPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dropReTxTCPEnabled.setStatus("current")


class _ColdStartTime_Type(Integer32):
    """Custom type coldStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_ColdStartTime_Type.__name__ = "Integer32"
_ColdStartTime_Object = MibTableColumn
coldStartTime = _ColdStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 7),
    _ColdStartTime_Type()
)
coldStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coldStartTime.setStatus("current")


class _ColdStartDropAction_Type(Integer32):
    """Custom type coldStartDropAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dropFlows", 1),
          ("forwardFlows", 2))
    )


_ColdStartDropAction_Type.__name__ = "Integer32"
_ColdStartDropAction_Object = MibTableColumn
coldStartDropAction = _ColdStartDropAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 8),
    _ColdStartDropAction_Type()
)
coldStartDropAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coldStartDropAction.setStatus("current")


class _NormalizationOnOffOption_Type(Integer32):
    """Custom type normalizationOnOffOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_NormalizationOnOffOption_Type.__name__ = "Integer32"
_NormalizationOnOffOption_Object = MibTableColumn
normalizationOnOffOption = _NormalizationOnOffOption_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 9),
    _NormalizationOnOffOption_Type()
)
normalizationOnOffOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    normalizationOnOffOption.setStatus("current")


class _TcpOverlapOption_Type(Integer32):
    """Custom type tcpOverlapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oldData", 1),
          ("newData", 2))
    )


_TcpOverlapOption_Type.__name__ = "Integer32"
_TcpOverlapOption_Object = MibTableColumn
tcpOverlapOption = _TcpOverlapOption_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 10),
    _TcpOverlapOption_Type()
)
tcpOverlapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOverlapOption.setStatus("current")


class _SAckPermittedOption_Type(Integer32):
    """Custom type sAckPermittedOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SAckPermittedOption_Type.__name__ = "Integer32"
_SAckPermittedOption_Object = MibTableColumn
sAckPermittedOption = _SAckPermittedOption_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 11),
    _SAckPermittedOption_Type()
)
sAckPermittedOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sAckPermittedOption.setStatus("current")
_TTCPOptionThreshold_Type = Integer32
_TTCPOptionThreshold_Object = MibTableColumn
tTCPOptionThreshold = _TTCPOptionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 12),
    _TTCPOptionThreshold_Type()
)
tTCPOptionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tTCPOptionThreshold.setStatus("current")


class _DropOnPAWSFail_Type(Integer32):
    """Custom type dropOnPAWSFail based on Integer32"""
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


_DropOnPAWSFail_Type.__name__ = "Integer32"
_DropOnPAWSFail_Object = MibTableColumn
dropOnPAWSFail = _DropOnPAWSFail_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 13),
    _DropOnPAWSFail_Type()
)
dropOnPAWSFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dropOnPAWSFail.setStatus("current")


class _TimestampEchoMatchFail_Type(Integer32):
    """Custom type timestampEchoMatchFail based on Integer32"""
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


_TimestampEchoMatchFail_Type.__name__ = "Integer32"
_TimestampEchoMatchFail_Object = MibTableColumn
timestampEchoMatchFail = _TimestampEchoMatchFail_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 14),
    _TimestampEchoMatchFail_Type()
)
timestampEchoMatchFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timestampEchoMatchFail.setStatus("current")


class _DropMD5Option_Type(Integer32):
    """Custom type dropMD5Option based on Integer32"""
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


_DropMD5Option_Type.__name__ = "Integer32"
_DropMD5Option_Object = MibTableColumn
dropMD5Option = _DropMD5Option_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 15),
    _DropMD5Option_Type()
)
dropMD5Option.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dropMD5Option.setStatus("current")


class _UnsolicitedUDPPacketsTimeout_Type(Integer32):
    """Custom type unsolicitedUDPPacketsTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_UnsolicitedUDPPacketsTimeout_Type.__name__ = "Integer32"
_UnsolicitedUDPPacketsTimeout_Object = MibTableColumn
unsolicitedUDPPacketsTimeout = _UnsolicitedUDPPacketsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 16),
    _UnsolicitedUDPPacketsTimeout_Type()
)
unsolicitedUDPPacketsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unsolicitedUDPPacketsTimeout.setStatus("current")


class _SynProxyEnable_Type(Integer32):
    """Custom type synProxyEnable based on Integer32"""
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


_SynProxyEnable_Type.__name__ = "Integer32"
_SynProxyEnable_Object = MibTableColumn
synProxyEnable = _SynProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 17),
    _SynProxyEnable_Type()
)
synProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synProxyEnable.setStatus("current")


class _AckScanDiscardTime_Type(Integer32):
    """Custom type ackScanDiscardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AckScanDiscardTime_Type.__name__ = "Integer32"
_AckScanDiscardTime_Object = MibTableColumn
ackScanDiscardTime = _AckScanDiscardTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 18),
    _AckScanDiscardTime_Type()
)
ackScanDiscardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ackScanDiscardTime.setStatus("current")


class _HalfOpenConnectionResetEnable_Type(Integer32):
    """Custom type halfOpenConnectionResetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("resetDisable", 1),
          ("resetAllUnfinished3WHConns", 2),
          ("resetDosUnfinished3WHConns", 3))
    )


_HalfOpenConnectionResetEnable_Type.__name__ = "Integer32"
_HalfOpenConnectionResetEnable_Object = MibTableColumn
halfOpenConnectionResetEnable = _HalfOpenConnectionResetEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 19),
    _HalfOpenConnectionResetEnable_Type()
)
halfOpenConnectionResetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    halfOpenConnectionResetEnable.setStatus("current")


class _OutOfContextTcpPktEnable_Type(Integer32):
    """Custom type outOfContextTcpPktEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("permit-out-of-order", 3),
          ("deny-no-tcb", 4),
          ("stateless-inspection", 5))
    )


_OutOfContextTcpPktEnable_Type.__name__ = "Integer32"
_OutOfContextTcpPktEnable_Object = MibTableColumn
outOfContextTcpPktEnable = _OutOfContextTcpPktEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 20),
    _OutOfContextTcpPktEnable_Type()
)
outOfContextTcpPktEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfContextTcpPktEnable.setStatus("current")


class _SynCookieConfig_Type(Integer32):
    """Custom type synCookieConfig based on Integer32"""
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
        *(("disable", 0),
          ("enable-inbound", 1),
          ("enable-outbound", 2),
          ("enable-in-out", 3))
    )


_SynCookieConfig_Type.__name__ = "Integer32"
_SynCookieConfig_Object = MibTableColumn
synCookieConfig = _SynCookieConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 21),
    _SynCookieConfig_Type()
)
synCookieConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synCookieConfig.setStatus("current")


class _SynCookieInboundThreshold_Type(Integer32):
    """Custom type synCookieInboundThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 420000),
    )


_SynCookieInboundThreshold_Type.__name__ = "Integer32"
_SynCookieInboundThreshold_Object = MibTableColumn
synCookieInboundThreshold = _SynCookieInboundThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 22),
    _SynCookieInboundThreshold_Type()
)
synCookieInboundThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synCookieInboundThreshold.setStatus("current")


class _SynCookieOutboundThreshold_Type(Integer32):
    """Custom type synCookieOutboundThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 420000),
    )


_SynCookieOutboundThreshold_Type.__name__ = "Integer32"
_SynCookieOutboundThreshold_Object = MibTableColumn
synCookieOutboundThreshold = _SynCookieOutboundThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 23),
    _SynCookieOutboundThreshold_Type()
)
synCookieOutboundThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synCookieOutboundThreshold.setStatus("current")


class _SynCookieMss_Type(Integer32):
    """Custom type synCookieMss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(536, 1460),
    )


_SynCookieMss_Type.__name__ = "Integer32"
_SynCookieMss_Object = MibTableColumn
synCookieMss = _SynCookieMss_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 24),
    _SynCookieMss_Type()
)
synCookieMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synCookieMss.setStatus("current")


class _SinkHoleTimeToLive_Type(Integer32):
    """Custom type sinkHoleTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 18),
    )


_SinkHoleTimeToLive_Type.__name__ = "Integer32"
_SinkHoleTimeToLive_Object = MibTableColumn
sinkHoleTimeToLive = _SinkHoleTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 25),
    _SinkHoleTimeToLive_Type()
)
sinkHoleTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sinkHoleTimeToLive.setStatus("current")
_SinkHoleIpAddress_Type = IpAddress
_SinkHoleIpAddress_Object = MibTableColumn
sinkHoleIpAddress = _SinkHoleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 7, 1, 26),
    _SinkHoleIpAddress_Type()
)
sinkHoleIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sinkHoleIpAddress.setStatus("current")
_SessionTable_Object = MibTable
sessionTable = _SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8)
)
if mibBuilder.loadTexts:
    sessionTable.setStatus("current")
_SessionEntry_Object = MibTableRow
sessionEntry = _SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1)
)
sessionEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionSrcIpAddress"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionDestIpAddress"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionSrcPortNo"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionDestPortNo"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionProtocol"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionVIDSIdentifier"),
)
if mibBuilder.loadTexts:
    sessionEntry.setStatus("current")
_SessionSrcIpAddress_Type = IpAddress
_SessionSrcIpAddress_Object = MibTableColumn
sessionSrcIpAddress = _SessionSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 1),
    _SessionSrcIpAddress_Type()
)
sessionSrcIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionSrcIpAddress.setStatus("current")
_SessionDestIpAddress_Type = IpAddress
_SessionDestIpAddress_Object = MibTableColumn
sessionDestIpAddress = _SessionDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 2),
    _SessionDestIpAddress_Type()
)
sessionDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionDestIpAddress.setStatus("current")
_SessionSrcPortNo_Type = Integer32
_SessionSrcPortNo_Object = MibTableColumn
sessionSrcPortNo = _SessionSrcPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 3),
    _SessionSrcPortNo_Type()
)
sessionSrcPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionSrcPortNo.setStatus("current")
_SessionDestPortNo_Type = Integer32
_SessionDestPortNo_Object = MibTableColumn
sessionDestPortNo = _SessionDestPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 4),
    _SessionDestPortNo_Type()
)
sessionDestPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionDestPortNo.setStatus("current")


class _SessionProtocol_Type(Integer32):
    """Custom type sessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_SessionProtocol_Type.__name__ = "Integer32"
_SessionProtocol_Object = MibTableColumn
sessionProtocol = _SessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 5),
    _SessionProtocol_Type()
)
sessionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionProtocol.setStatus("current")
_SessionVIDSIdentifier_Type = Integer32
_SessionVIDSIdentifier_Object = MibTableColumn
sessionVIDSIdentifier = _SessionVIDSIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 6),
    _SessionVIDSIdentifier_Type()
)
sessionVIDSIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionVIDSIdentifier.setStatus("current")


class _SessionConfigAction_Type(Integer32):
    """Custom type sessionConfigAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetSession", 1),
          ("logSession", 2))
    )


_SessionConfigAction_Type.__name__ = "Integer32"
_SessionConfigAction_Object = MibTableColumn
sessionConfigAction = _SessionConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 7),
    _SessionConfigAction_Type()
)
sessionConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionConfigAction.setStatus("current")
_SessionLogTime_Type = Integer32
_SessionLogTime_Object = MibTableColumn
sessionLogTime = _SessionLogTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 8),
    _SessionLogTime_Type()
)
sessionLogTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogTime.setStatus("current")
_SessionIntfPortNo_Type = TrellixPortLinearIndex
_SessionIntfPortNo_Object = MibTableColumn
sessionIntfPortNo = _SessionIntfPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 8, 1, 9),
    _SessionIntfPortNo_Type()
)
sessionIntfPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionIntfPortNo.setStatus("current")
_SessionV6Table_Object = MibTable
sessionV6Table = _SessionV6Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9)
)
if mibBuilder.loadTexts:
    sessionV6Table.setStatus("current")
_SessionV6Entry_Object = MibTableRow
sessionV6Entry = _SessionV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1)
)
sessionV6Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionSrcIpv6Address"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionDestIpv6Address"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionv6SrcPortNo"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionv6DestPortNo"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionv6Protocol"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "sessionv6VIDSIdentifier"),
)
if mibBuilder.loadTexts:
    sessionV6Entry.setStatus("current")
_SessionSrcIpv6Address_Type = Ipv6Address
_SessionSrcIpv6Address_Object = MibTableColumn
sessionSrcIpv6Address = _SessionSrcIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 1),
    _SessionSrcIpv6Address_Type()
)
sessionSrcIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionSrcIpv6Address.setStatus("current")
_SessionDestIpv6Address_Type = Ipv6Address
_SessionDestIpv6Address_Object = MibTableColumn
sessionDestIpv6Address = _SessionDestIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 2),
    _SessionDestIpv6Address_Type()
)
sessionDestIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionDestIpv6Address.setStatus("current")
_Sessionv6SrcPortNo_Type = Integer32
_Sessionv6SrcPortNo_Object = MibTableColumn
sessionv6SrcPortNo = _Sessionv6SrcPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 3),
    _Sessionv6SrcPortNo_Type()
)
sessionv6SrcPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionv6SrcPortNo.setStatus("current")
_Sessionv6DestPortNo_Type = Integer32
_Sessionv6DestPortNo_Object = MibTableColumn
sessionv6DestPortNo = _Sessionv6DestPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 4),
    _Sessionv6DestPortNo_Type()
)
sessionv6DestPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionv6DestPortNo.setStatus("current")


class _Sessionv6Protocol_Type(Integer32):
    """Custom type sessionv6Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_Sessionv6Protocol_Type.__name__ = "Integer32"
_Sessionv6Protocol_Object = MibTableColumn
sessionv6Protocol = _Sessionv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 5),
    _Sessionv6Protocol_Type()
)
sessionv6Protocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionv6Protocol.setStatus("current")
_Sessionv6VIDSIdentifier_Type = Integer32
_Sessionv6VIDSIdentifier_Object = MibTableColumn
sessionv6VIDSIdentifier = _Sessionv6VIDSIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 6),
    _Sessionv6VIDSIdentifier_Type()
)
sessionv6VIDSIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionv6VIDSIdentifier.setStatus("current")


class _Sessionv6ConfigAction_Type(Integer32):
    """Custom type sessionv6ConfigAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetSession", 1),
          ("logSession", 2))
    )


_Sessionv6ConfigAction_Type.__name__ = "Integer32"
_Sessionv6ConfigAction_Object = MibTableColumn
sessionv6ConfigAction = _Sessionv6ConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 7),
    _Sessionv6ConfigAction_Type()
)
sessionv6ConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionv6ConfigAction.setStatus("current")
_Sessionv6LogTime_Type = Integer32
_Sessionv6LogTime_Object = MibTableColumn
sessionv6LogTime = _Sessionv6LogTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 8),
    _Sessionv6LogTime_Type()
)
sessionv6LogTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionv6LogTime.setStatus("current")
_Sessionv6IntfPortNo_Type = TrellixPortLinearIndex
_Sessionv6IntfPortNo_Object = MibTableColumn
sessionv6IntfPortNo = _Sessionv6IntfPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 9, 1, 9),
    _Sessionv6IntfPortNo_Type()
)
sessionv6IntfPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionv6IntfPortNo.setStatus("current")
_PluggableModuleState_Type = Integer32
_PluggableModuleState_Object = MibScalar
pluggableModuleState = _PluggableModuleState_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 10, 10),
    _PluggableModuleState_Type()
)
pluggableModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableModuleState.setStatus("current")
_InterfacePortGrp_ObjectIdentity = ObjectIdentity
interfacePortGrp = _InterfacePortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11)
)
_IntfPortTable_Object = MibTable
intfPortTable = _IntfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    intfPortTable.setStatus("current")
_IntfPortEntry_Object = MibTableRow
intfPortEntry = _IntfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1)
)
intfPortEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
    (0, "TRELLIX-SENSOR-SMI", "intfPortIndex"),
)
if mibBuilder.loadTexts:
    intfPortEntry.setStatus("current")


class _IntfPortIfDescr_Type(DisplayString):
    """Custom type intfPortIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntfPortIfDescr_Type.__name__ = "DisplayString"
_IntfPortIfDescr_Object = MibTableColumn
intfPortIfDescr = _IntfPortIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 1),
    _IntfPortIfDescr_Type()
)
intfPortIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortIfDescr.setStatus("current")
_IntfPortIfType_Type = TrellixIDSPortType
_IntfPortIfType_Object = MibTableColumn
intfPortIfType = _IntfPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 2),
    _IntfPortIfType_Type()
)
intfPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortIfType.setStatus("current")


class _IntfPortIfAdminStatus_Type(Integer32):
    """Custom type intfPortIfAdminStatus based on Integer32"""
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


_IntfPortIfAdminStatus_Type.__name__ = "Integer32"
_IntfPortIfAdminStatus_Object = MibTableColumn
intfPortIfAdminStatus = _IntfPortIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 3),
    _IntfPortIfAdminStatus_Type()
)
intfPortIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortIfAdminStatus.setStatus("current")


class _IntfPortIfOperStatus_Type(Integer32):
    """Custom type intfPortIfOperStatus based on Integer32"""
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


_IntfPortIfOperStatus_Type.__name__ = "Integer32"
_IntfPortIfOperStatus_Object = MibTableColumn
intfPortIfOperStatus = _IntfPortIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 4),
    _IntfPortIfOperStatus_Type()
)
intfPortIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortIfOperStatus.setStatus("current")
_IntfPortOperatingMode_Type = TrellixIDSOperatingMode
_IntfPortOperatingMode_Object = MibTableColumn
intfPortOperatingMode = _IntfPortOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 5),
    _IntfPortOperatingMode_Type()
)
intfPortOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortOperatingMode.setStatus("current")
_IntfPortEnableFullDuplex_Type = TruthValue
_IntfPortEnableFullDuplex_Object = MibTableColumn
intfPortEnableFullDuplex = _IntfPortEnableFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 6),
    _IntfPortEnableFullDuplex_Type()
)
intfPortEnableFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortEnableFullDuplex.setStatus("current")


class _IntfPortFullDuplexPeer_Type(Integer32):
    """Custom type intfPortFullDuplexPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IntfPortFullDuplexPeer_Type.__name__ = "Integer32"
_IntfPortFullDuplexPeer_Object = MibTableColumn
intfPortFullDuplexPeer = _IntfPortFullDuplexPeer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 7),
    _IntfPortFullDuplexPeer_Type()
)
intfPortFullDuplexPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortFullDuplexPeer.setStatus("current")


class _IntfPortSpeed_Type(Integer32):
    """Custom type intfPortSpeed based on Integer32"""
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
        *(("other", 0),
          ("ten-Mbps", 1),
          ("hundred-Mbps", 2),
          ("one-Gbps", 3),
          ("ten-Gbps", 4),
          ("forty-Gbps", 5))
    )


_IntfPortSpeed_Type.__name__ = "Integer32"
_IntfPortSpeed_Object = MibTableColumn
intfPortSpeed = _IntfPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 8),
    _IntfPortSpeed_Type()
)
intfPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortSpeed.setStatus("current")
_IntfPortSpeedConfig_Type = TrellixPortSpeed
_IntfPortSpeedConfig_Object = MibTableColumn
intfPortSpeedConfig = _IntfPortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 9),
    _IntfPortSpeedConfig_Type()
)
intfPortSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortSpeedConfig.setStatus("current")
_IntfPortEnableInternalTap_Type = TruthValue
_IntfPortEnableInternalTap_Object = MibTableColumn
intfPortEnableInternalTap = _IntfPortEnableInternalTap_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 10),
    _IntfPortEnableInternalTap_Type()
)
intfPortEnableInternalTap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortEnableInternalTap.setStatus("current")


class _IntfPortInOutType_Type(Integer32):
    """Custom type intfPortInOutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inside", 1),
          ("outside", 2),
          ("not-specified", 3))
    )


_IntfPortInOutType_Type.__name__ = "Integer32"
_IntfPortInOutType_Object = MibTableColumn
intfPortInOutType = _IntfPortInOutType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 11),
    _IntfPortInOutType_Type()
)
intfPortInOutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortInOutType.setStatus("current")
_IntfGEPortSpeedConfig_Type = TrellixGEType
_IntfGEPortSpeedConfig_Object = MibTableColumn
intfGEPortSpeedConfig = _IntfGEPortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 12),
    _IntfGEPortSpeedConfig_Type()
)
intfGEPortSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfGEPortSpeedConfig.setStatus("current")


class _IntfFailOpenSwitchStatus_Type(Integer32):
    """Custom type intfFailOpenSwitchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 1),
          ("present", 2),
          ("not-present", 3))
    )


_IntfFailOpenSwitchStatus_Type.__name__ = "Integer32"
_IntfFailOpenSwitchStatus_Object = MibTableColumn
intfFailOpenSwitchStatus = _IntfFailOpenSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 13),
    _IntfFailOpenSwitchStatus_Type()
)
intfFailOpenSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfFailOpenSwitchStatus.setStatus("current")


class _IntfFailOpenPortStatus_Type(Integer32):
    """Custom type intfFailOpenPortStatus based on Integer32"""
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
        *(("not-applicable", 1),
          ("inline-fail-open", 2),
          ("bypass", 3),
          ("tap", 4),
          ("absent", 5),
          ("unknown", 6),
          ("layer2-bypass", 7))
    )


_IntfFailOpenPortStatus_Type.__name__ = "Integer32"
_IntfFailOpenPortStatus_Object = MibTableColumn
intfFailOpenPortStatus = _IntfFailOpenPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 14),
    _IntfFailOpenPortStatus_Type()
)
intfFailOpenPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfFailOpenPortStatus.setStatus("current")


class _IntfPortEnableAntiSpoofing_Type(Integer32):
    """Custom type intfPortEnableAntiSpoofing based on Integer32"""
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
        *(("disable-bothsides-spoof-detect", 1),
          ("enable-inside-spoof-detect", 2),
          ("enable-outside-spoof-detect", 3),
          ("enable-bothsides-spoof-detect", 4))
    )


_IntfPortEnableAntiSpoofing_Type.__name__ = "Integer32"
_IntfPortEnableAntiSpoofing_Object = MibTableColumn
intfPortEnableAntiSpoofing = _IntfPortEnableAntiSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 15),
    _IntfPortEnableAntiSpoofing_Type()
)
intfPortEnableAntiSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortEnableAntiSpoofing.setStatus("current")


class _IntfPortHostQRActionStatus_Type(Integer32):
    """Custom type intfPortHostQRActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("quarantine", 1),
          ("remediate", 2))
    )


_IntfPortHostQRActionStatus_Type.__name__ = "Integer32"
_IntfPortHostQRActionStatus_Object = MibTableColumn
intfPortHostQRActionStatus = _IntfPortHostQRActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 18),
    _IntfPortHostQRActionStatus_Type()
)
intfPortHostQRActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortHostQRActionStatus.setStatus("obsolete")


class _IntfPortMpeQRActionStatus_Type(Integer32):
    """Custom type intfPortMpeQRActionStatus based on Integer32"""
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
        *(("disabled", 0),
          ("mpeNotify", 1),
          ("mpeQuarantine", 2),
          ("mpeRemediate", 3))
    )


_IntfPortMpeQRActionStatus_Type.__name__ = "Integer32"
_IntfPortMpeQRActionStatus_Object = MibTableColumn
intfPortMpeQRActionStatus = _IntfPortMpeQRActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 19),
    _IntfPortMpeQRActionStatus_Type()
)
intfPortMpeQRActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortMpeQRActionStatus.setStatus("obsolete")


class _IntfPortAllowlistACLLookupStatus_Type(Integer32):
    """Custom type intfPortAllowlistACLLookupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IntfPortAllowlistACLLookupStatus_Type.__name__ = "Integer32"
_IntfPortAllowlistACLLookupStatus_Object = MibTableColumn
intfPortAllowlistACLLookupStatus = _IntfPortAllowlistACLLookupStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 20),
    _IntfPortAllowlistACLLookupStatus_Type()
)
intfPortAllowlistACLLookupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortAllowlistACLLookupStatus.setStatus("obsolete")


class _IntfPortPeerDeviceAdvtStatus_Type(Integer32):
    """Custom type intfPortPeerDeviceAdvtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("other", 0)
    )


_IntfPortPeerDeviceAdvtStatus_Type.__name__ = "Integer32"
_IntfPortPeerDeviceAdvtStatus_Object = MibTableColumn
intfPortPeerDeviceAdvtStatus = _IntfPortPeerDeviceAdvtStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 21),
    _IntfPortPeerDeviceAdvtStatus_Type()
)
intfPortPeerDeviceAdvtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortPeerDeviceAdvtStatus.setStatus("current")
_IntfPortIsMcafeeConnector_Type = TruthValue
_IntfPortIsMcafeeConnector_Object = MibTableColumn
intfPortIsMcafeeConnector = _IntfPortIsMcafeeConnector_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 22),
    _IntfPortIsMcafeeConnector_Type()
)
intfPortIsMcafeeConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortIsMcafeeConnector.setStatus("current")
_IntfPortAllowAnyConnector_Type = TruthValue
_IntfPortAllowAnyConnector_Object = MibTableColumn
intfPortAllowAnyConnector = _IntfPortAllowAnyConnector_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 23),
    _IntfPortAllowAnyConnector_Type()
)
intfPortAllowAnyConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortAllowAnyConnector.setStatus("current")


class _IntfPortCageType_Type(Integer32):
    """Custom type intfPortCageType based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("rJ-45", 1),
          ("rJ-11", 2),
          ("gBIC", 3),
          ("sFP", 4),
          ("xFP", 5),
          ("sFP-plus", 6),
          ("qSFP", 7),
          ("rJ-45-plus", 8),
          ("sFP-plus-BPFO", 9))
    )


_IntfPortCageType_Type.__name__ = "Integer32"
_IntfPortCageType_Object = MibTableColumn
intfPortCageType = _IntfPortCageType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 24),
    _IntfPortCageType_Type()
)
intfPortCageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortCageType.setStatus("current")


class _IntfPortGetMediaType_Type(Integer32):
    """Custom type intfPortGetMediaType based on Integer32"""
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
          ("optical", 1),
          ("electrical", 2))
    )


_IntfPortGetMediaType_Type.__name__ = "Integer32"
_IntfPortGetMediaType_Object = MibTableColumn
intfPortGetMediaType = _IntfPortGetMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 25),
    _IntfPortGetMediaType_Type()
)
intfPortGetMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortGetMediaType.setStatus("current")


class _IntfPortSetMediaType_Type(Integer32):
    """Custom type intfPortSetMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optical", 1),
          ("electrical", 2))
    )


_IntfPortSetMediaType_Type.__name__ = "Integer32"
_IntfPortSetMediaType_Object = MibTableColumn
intfPortSetMediaType = _IntfPortSetMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 26),
    _IntfPortSetMediaType_Type()
)
intfPortSetMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortSetMediaType.setStatus("current")


class _IntfPortAdditionalInfo_Type(DisplayString):
    """Custom type intfPortAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntfPortAdditionalInfo_Type.__name__ = "DisplayString"
_IntfPortAdditionalInfo_Object = MibTableColumn
intfPortAdditionalInfo = _IntfPortAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 27),
    _IntfPortAdditionalInfo_Type()
)
intfPortAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortAdditionalInfo.setStatus("current")
_IntfPortMonPortIpAddress_Type = IpAddress
_IntfPortMonPortIpAddress_Object = MibTableColumn
intfPortMonPortIpAddress = _IntfPortMonPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 28),
    _IntfPortMonPortIpAddress_Type()
)
intfPortMonPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortMonPortIpAddress.setStatus("current")
_IntfPortMonPortNetMask_Type = IpAddress
_IntfPortMonPortNetMask_Object = MibTableColumn
intfPortMonPortNetMask = _IntfPortMonPortNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 29),
    _IntfPortMonPortNetMask_Type()
)
intfPortMonPortNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortMonPortNetMask.setStatus("current")
_IntfPortGatewayIpAddress_Type = IpAddress
_IntfPortGatewayIpAddress_Object = MibTableColumn
intfPortGatewayIpAddress = _IntfPortGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 30),
    _IntfPortGatewayIpAddress_Type()
)
intfPortGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortGatewayIpAddress.setStatus("current")
_IntfPortNbadConfigStatus_Type = TruthValue
_IntfPortNbadConfigStatus_Object = MibTableColumn
intfPortNbadConfigStatus = _IntfPortNbadConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 31),
    _IntfPortNbadConfigStatus_Type()
)
intfPortNbadConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortNbadConfigStatus.setStatus("current")


class _IntfPortVlanId_Type(Integer32):
    """Custom type intfPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2164326399),
    )


_IntfPortVlanId_Type.__name__ = "Integer32"
_IntfPortVlanId_Object = MibTableColumn
intfPortVlanId = _IntfPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 32),
    _IntfPortVlanId_Type()
)
intfPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortVlanId.setStatus("current")
_IntfPortAppIdStatsConfigStatus_Type = TruthValue
_IntfPortAppIdStatsConfigStatus_Object = MibTableColumn
intfPortAppIdStatsConfigStatus = _IntfPortAppIdStatsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 33),
    _IntfPortAppIdStatsConfigStatus_Type()
)
intfPortAppIdStatsConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortAppIdStatsConfigStatus.setStatus("current")


class _IntfPortConnectorType_Type(Integer32):
    """Custom type intfPortConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("qSFP", 1),
          ("sFP-plus", 2),
          ("sFP-fiber", 3),
          ("sFP-copper", 4))
    )


_IntfPortConnectorType_Type.__name__ = "Integer32"
_IntfPortConnectorType_Object = MibTableColumn
intfPortConnectorType = _IntfPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 34),
    _IntfPortConnectorType_Type()
)
intfPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortConnectorType.setStatus("current")
_IntfPortLinearIndex_Type = TrellixPortLinearIndex
_IntfPortLinearIndex_Object = MibTableColumn
intfPortLinearIndex = _IntfPortLinearIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 35),
    _IntfPortLinearIndex_Type()
)
intfPortLinearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortLinearIndex.setStatus("current")
_IntfPortFecConfig_Type = Integer32
_IntfPortFecConfig_Object = MibTableColumn
intfPortFecConfig = _IntfPortFecConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 36),
    _IntfPortFecConfig_Type()
)
intfPortFecConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPortFecConfig.setStatus("current")


class _IntfPortTranceiverSerialNumber_Type(DisplayString):
    """Custom type intfPortTranceiverSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntfPortTranceiverSerialNumber_Type.__name__ = "DisplayString"
_IntfPortTranceiverSerialNumber_Object = MibTableColumn
intfPortTranceiverSerialNumber = _IntfPortTranceiverSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 1, 1, 37),
    _IntfPortTranceiverSerialNumber_Type()
)
intfPortTranceiverSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortTranceiverSerialNumber.setStatus("current")
_IntfPortGBICHotSwapTime_Type = DateAndTime
_IntfPortGBICHotSwapTime_Object = MibScalar
intfPortGBICHotSwapTime = _IntfPortGBICHotSwapTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 11, 2),
    _IntfPortGBICHotSwapTime_Type()
)
intfPortGBICHotSwapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortGBICHotSwapTime.setStatus("current")
_ResponsePortGrp_ObjectIdentity = ObjectIdentity
responsePortGrp = _ResponsePortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12)
)
_RespPortTable_Object = MibTable
respPortTable = _RespPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    respPortTable.setStatus("current")
_RespPortEntry_Object = MibTableRow
respPortEntry = _RespPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1)
)
respPortEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
    (0, "TRELLIX-SENSOR-SMI", "respPortIndex"),
)
if mibBuilder.loadTexts:
    respPortEntry.setStatus("current")
_RespPortDescr_Type = DisplayString
_RespPortDescr_Object = MibTableColumn
respPortDescr = _RespPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 1),
    _RespPortDescr_Type()
)
respPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respPortDescr.setStatus("current")
_RespPortType_Type = TrellixIDSPortType
_RespPortType_Object = MibTableColumn
respPortType = _RespPortType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 2),
    _RespPortType_Type()
)
respPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respPortType.setStatus("current")


class _RespPortAdminStatus_Type(Integer32):
    """Custom type respPortAdminStatus based on Integer32"""
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


_RespPortAdminStatus_Type.__name__ = "Integer32"
_RespPortAdminStatus_Object = MibTableColumn
respPortAdminStatus = _RespPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 3),
    _RespPortAdminStatus_Type()
)
respPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respPortAdminStatus.setStatus("current")


class _RespPortOperStatus_Type(Integer32):
    """Custom type respPortOperStatus based on Integer32"""
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


_RespPortOperStatus_Type.__name__ = "Integer32"
_RespPortOperStatus_Object = MibTableColumn
respPortOperStatus = _RespPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 4),
    _RespPortOperStatus_Type()
)
respPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respPortOperStatus.setStatus("current")
_RespPortEnableFullDuplex_Type = TruthValue
_RespPortEnableFullDuplex_Object = MibTableColumn
respPortEnableFullDuplex = _RespPortEnableFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 5),
    _RespPortEnableFullDuplex_Type()
)
respPortEnableFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respPortEnableFullDuplex.setStatus("current")
_RespPortSpeed_Type = TrellixPortSpeed
_RespPortSpeed_Object = MibTableColumn
respPortSpeed = _RespPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 6),
    _RespPortSpeed_Type()
)
respPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respPortSpeed.setStatus("current")


class _RespPortPktDestination_Type(Integer32):
    """Custom type respPortPktDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("router", 2))
    )


_RespPortPktDestination_Type.__name__ = "Integer32"
_RespPortPktDestination_Object = MibTableColumn
respPortPktDestination = _RespPortPktDestination_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 7),
    _RespPortPktDestination_Type()
)
respPortPktDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respPortPktDestination.setStatus("current")
_RespPortMacAddress_Type = MacAddress
_RespPortMacAddress_Object = MibTableColumn
respPortMacAddress = _RespPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 8),
    _RespPortMacAddress_Type()
)
respPortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respPortMacAddress.setStatus("current")
_RespCUGEPortSpeed_Type = TrellixCUGEType
_RespCUGEPortSpeed_Object = MibTableColumn
respCUGEPortSpeed = _RespCUGEPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 9),
    _RespCUGEPortSpeed_Type()
)
respCUGEPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respCUGEPortSpeed.setStatus("current")


class _RespAdditionalInfo_Type(DisplayString):
    """Custom type respAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RespAdditionalInfo_Type.__name__ = "DisplayString"
_RespAdditionalInfo_Object = MibTableColumn
respAdditionalInfo = _RespAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 1, 1, 11),
    _RespAdditionalInfo_Type()
)
respAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respAdditionalInfo.setStatus("current")
_IntfRespTable_Object = MibTable
intfRespTable = _IntfRespTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    intfRespTable.setStatus("current")
_IntfRespEntry_Object = MibTableRow
intfRespEntry = _IntfRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 2, 1)
)
intfRespEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
    (0, "TRELLIX-SENSOR-SMI", "intfPortIndex"),
)
if mibBuilder.loadTexts:
    intfRespEntry.setStatus("current")


class _IntfRespType_Type(Integer32):
    """Custom type intfRespType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("responsePort", 1),
          ("inline", 2))
    )


_IntfRespType_Type.__name__ = "Integer32"
_IntfRespType_Object = MibTableColumn
intfRespType = _IntfRespType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 2, 1, 1),
    _IntfRespType_Type()
)
intfRespType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfRespType.setStatus("current")
_IntfRespPortNo_Type = Integer32
_IntfRespPortNo_Object = MibTableColumn
intfRespPortNo = _IntfRespPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 12, 2, 1, 2),
    _IntfRespPortNo_Type()
)
intfRespPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfRespPortNo.setStatus("current")
_DosConfigGrp_ObjectIdentity = ObjectIdentity
dosConfigGrp = _DosConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14)
)


class _DosLearningModeAction_Type(Integer32):
    """Custom type dosLearningModeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceDetection", 1),
          ("learning", 2),
          ("reloadProfile", 3))
    )


_DosLearningModeAction_Type.__name__ = "Integer32"
_DosLearningModeAction_Object = MibScalar
dosLearningModeAction = _DosLearningModeAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 1),
    _DosLearningModeAction_Type()
)
dosLearningModeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosLearningModeAction.setStatus("current")
_DosProfileTable_Object = MibTable
dosProfileTable = _DosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 2)
)
if mibBuilder.loadTexts:
    dosProfileTable.setStatus("current")
_DosProfileEntry_Object = MibTableRow
dosProfileEntry = _DosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 2, 1)
)
dosProfileEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "dosProfileVidsId"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "dosProfileId"),
)
if mibBuilder.loadTexts:
    dosProfileEntry.setStatus("current")
_DosProfileVidsId_Type = Unsigned32
_DosProfileVidsId_Object = MibTableColumn
dosProfileVidsId = _DosProfileVidsId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 2, 1, 1),
    _DosProfileVidsId_Type()
)
dosProfileVidsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dosProfileVidsId.setStatus("current")
_DosProfileId_Type = Unsigned32
_DosProfileId_Object = MibTableColumn
dosProfileId = _DosProfileId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 2, 1, 2),
    _DosProfileId_Type()
)
dosProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dosProfileId.setStatus("current")


class _DosProfileStatus_Type(Integer32):
    """Custom type dosProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learning", 1),
          ("detection", 2))
    )


_DosProfileStatus_Type.__name__ = "Integer32"
_DosProfileStatus_Object = MibTableColumn
dosProfileStatus = _DosProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 2, 1, 3),
    _DosProfileStatus_Type()
)
dosProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileStatus.setStatus("current")
_DosProfileLearningTime_Type = Unsigned32
_DosProfileLearningTime_Object = MibTableColumn
dosProfileLearningTime = _DosProfileLearningTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 2, 1, 4),
    _DosProfileLearningTime_Type()
)
dosProfileLearningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileLearningTime.setStatus("current")
_DosProfileBulkTable_Object = MibTable
dosProfileBulkTable = _DosProfileBulkTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 3)
)
if mibBuilder.loadTexts:
    dosProfileBulkTable.setStatus("current")
_DosProfileBulkEntry_Object = MibTableRow
dosProfileBulkEntry = _DosProfileBulkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 3, 1)
)
dosProfileBulkEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "dosProfileBulkIndex"),
)
if mibBuilder.loadTexts:
    dosProfileBulkEntry.setStatus("current")
_DosProfileBulkIndex_Type = Integer32
_DosProfileBulkIndex_Object = MibTableColumn
dosProfileBulkIndex = _DosProfileBulkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 3, 1, 1),
    _DosProfileBulkIndex_Type()
)
dosProfileBulkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dosProfileBulkIndex.setStatus("current")
_DosProfileBulkVidsId_Type = Unsigned32
_DosProfileBulkVidsId_Object = MibTableColumn
dosProfileBulkVidsId = _DosProfileBulkVidsId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 3, 1, 2),
    _DosProfileBulkVidsId_Type()
)
dosProfileBulkVidsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileBulkVidsId.setStatus("current")
_DosProfileBulkId_Type = Unsigned32
_DosProfileBulkId_Object = MibTableColumn
dosProfileBulkId = _DosProfileBulkId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 3, 1, 3),
    _DosProfileBulkId_Type()
)
dosProfileBulkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileBulkId.setStatus("current")


class _DosProfileBulkStatus_Type(Integer32):
    """Custom type dosProfileBulkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learning", 1),
          ("detection", 2))
    )


_DosProfileBulkStatus_Type.__name__ = "Integer32"
_DosProfileBulkStatus_Object = MibTableColumn
dosProfileBulkStatus = _DosProfileBulkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 3, 1, 4),
    _DosProfileBulkStatus_Type()
)
dosProfileBulkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileBulkStatus.setStatus("current")
_DosProfileBulkLearningTime_Type = Unsigned32
_DosProfileBulkLearningTime_Object = MibTableColumn
dosProfileBulkLearningTime = _DosProfileBulkLearningTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 3, 1, 5),
    _DosProfileBulkLearningTime_Type()
)
dosProfileBulkLearningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileBulkLearningTime.setStatus("current")
_DosProfileShortAndLongTermTable_Object = MibTable
dosProfileShortAndLongTermTable = _DosProfileShortAndLongTermTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 4)
)
if mibBuilder.loadTexts:
    dosProfileShortAndLongTermTable.setStatus("current")
_DosProfileShortAndLongTermEntry_Object = MibTableRow
dosProfileShortAndLongTermEntry = _DosProfileShortAndLongTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 4, 1)
)
dosProfileShortAndLongTermEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "dosProfileShortAndLongTermVIDSIndex"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "dosProfileShortAndLongTermNIIndex"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "dosProfileShortAndLongTermMeasureIndex"),
)
if mibBuilder.loadTexts:
    dosProfileShortAndLongTermEntry.setStatus("current")
_DosProfileShortAndLongTermVIDSIndex_Type = Unsigned32
_DosProfileShortAndLongTermVIDSIndex_Object = MibTableColumn
dosProfileShortAndLongTermVIDSIndex = _DosProfileShortAndLongTermVIDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 4, 1, 1),
    _DosProfileShortAndLongTermVIDSIndex_Type()
)
dosProfileShortAndLongTermVIDSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dosProfileShortAndLongTermVIDSIndex.setStatus("current")
_DosProfileShortAndLongTermNIIndex_Type = Unsigned32
_DosProfileShortAndLongTermNIIndex_Object = MibTableColumn
dosProfileShortAndLongTermNIIndex = _DosProfileShortAndLongTermNIIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 4, 1, 2),
    _DosProfileShortAndLongTermNIIndex_Type()
)
dosProfileShortAndLongTermNIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dosProfileShortAndLongTermNIIndex.setStatus("current")


class _DosProfileShortAndLongTermMeasureIndex_Type(Integer32):
    """Custom type dosProfileShortAndLongTermMeasureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DosProfileShortAndLongTermMeasureIndex_Type.__name__ = "Integer32"
_DosProfileShortAndLongTermMeasureIndex_Object = MibTableColumn
dosProfileShortAndLongTermMeasureIndex = _DosProfileShortAndLongTermMeasureIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 4, 1, 3),
    _DosProfileShortAndLongTermMeasureIndex_Type()
)
dosProfileShortAndLongTermMeasureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dosProfileShortAndLongTermMeasureIndex.setStatus("current")


class _DosProfileShortAndLongTermBinCount_Type(Integer32):
    """Custom type dosProfileShortAndLongTermBinCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DosProfileShortAndLongTermBinCount_Type.__name__ = "Integer32"
_DosProfileShortAndLongTermBinCount_Object = MibTableColumn
dosProfileShortAndLongTermBinCount = _DosProfileShortAndLongTermBinCount_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 4, 1, 4),
    _DosProfileShortAndLongTermBinCount_Type()
)
dosProfileShortAndLongTermBinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileShortAndLongTermBinCount.setStatus("current")


class _DosProfileShortTermContent_Type(OctetString):
    """Custom type dosProfileShortTermContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_DosProfileShortTermContent_Type.__name__ = "OctetString"
_DosProfileShortTermContent_Object = MibTableColumn
dosProfileShortTermContent = _DosProfileShortTermContent_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 4, 1, 5),
    _DosProfileShortTermContent_Type()
)
dosProfileShortTermContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileShortTermContent.setStatus("current")


class _DosProfileLongTermContent_Type(OctetString):
    """Custom type dosProfileLongTermContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_DosProfileLongTermContent_Type.__name__ = "OctetString"
_DosProfileLongTermContent_Object = MibTableColumn
dosProfileLongTermContent = _DosProfileLongTermContent_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 4, 1, 6),
    _DosProfileLongTermContent_Type()
)
dosProfileLongTermContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosProfileLongTermContent.setStatus("current")


class _EnableDosPktLogging_Type(Integer32):
    """Custom type enableDosPktLogging based on Integer32"""
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


_EnableDosPktLogging_Type.__name__ = "Integer32"
_EnableDosPktLogging_Object = MibScalar
enableDosPktLogging = _EnableDosPktLogging_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 6),
    _EnableDosPktLogging_Type()
)
enableDosPktLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDosPktLogging.setStatus("current")
_TimedDosPktDropTable_Object = MibTable
timedDosPktDropTable = _TimedDosPktDropTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 7)
)
if mibBuilder.loadTexts:
    timedDosPktDropTable.setStatus("current")
_TimedDosPktDropEntry_Object = MibTableRow
timedDosPktDropEntry = _TimedDosPktDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 7, 1)
)
timedDosPktDropEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "timedDosPktDropVidsIdIndex"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "timedDosPktDropNiIdIndex"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "timedDosPktDropMsrIdIndex"),
)
if mibBuilder.loadTexts:
    timedDosPktDropEntry.setStatus("current")
_TimedDosPktDropVidsIdIndex_Type = Unsigned32
_TimedDosPktDropVidsIdIndex_Object = MibTableColumn
timedDosPktDropVidsIdIndex = _TimedDosPktDropVidsIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 7, 1, 1),
    _TimedDosPktDropVidsIdIndex_Type()
)
timedDosPktDropVidsIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timedDosPktDropVidsIdIndex.setStatus("current")
_TimedDosPktDropNiIdIndex_Type = Unsigned32
_TimedDosPktDropNiIdIndex_Object = MibTableColumn
timedDosPktDropNiIdIndex = _TimedDosPktDropNiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 7, 1, 2),
    _TimedDosPktDropNiIdIndex_Type()
)
timedDosPktDropNiIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timedDosPktDropNiIdIndex.setStatus("current")
_TimedDosPktDropMsrIdIndex_Type = Integer32
_TimedDosPktDropMsrIdIndex_Object = MibTableColumn
timedDosPktDropMsrIdIndex = _TimedDosPktDropMsrIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 7, 1, 3),
    _TimedDosPktDropMsrIdIndex_Type()
)
timedDosPktDropMsrIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timedDosPktDropMsrIdIndex.setStatus("current")


class _TimedDosPktDropAction_Type(Integer32):
    """Custom type timedDosPktDropAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("extend", 3))
    )


_TimedDosPktDropAction_Type.__name__ = "Integer32"
_TimedDosPktDropAction_Object = MibTableColumn
timedDosPktDropAction = _TimedDosPktDropAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 7, 1, 4),
    _TimedDosPktDropAction_Type()
)
timedDosPktDropAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timedDosPktDropAction.setStatus("current")
_TimedDosPktDropDuration_Type = Unsigned32
_TimedDosPktDropDuration_Object = MibTableColumn
timedDosPktDropDuration = _TimedDosPktDropDuration_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 7, 1, 5),
    _TimedDosPktDropDuration_Type()
)
timedDosPktDropDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timedDosPktDropDuration.setStatus("current")
_TimedDosPktDropEndTime_Type = Unsigned32
_TimedDosPktDropEndTime_Object = MibTableColumn
timedDosPktDropEndTime = _TimedDosPktDropEndTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 7, 1, 6),
    _TimedDosPktDropEndTime_Type()
)
timedDosPktDropEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timedDosPktDropEndTime.setStatus("current")
_BulkTimedDosPktDropTable_Object = MibTable
bulkTimedDosPktDropTable = _BulkTimedDosPktDropTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 8)
)
if mibBuilder.loadTexts:
    bulkTimedDosPktDropTable.setStatus("current")
_BulkTimedDosPktDropEntry_Object = MibTableRow
bulkTimedDosPktDropEntry = _BulkTimedDosPktDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 8, 1)
)
bulkTimedDosPktDropEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "bulkTimedDosPktDropIndex"),
)
if mibBuilder.loadTexts:
    bulkTimedDosPktDropEntry.setStatus("current")
_BulkTimedDosPktDropIndex_Type = Integer32
_BulkTimedDosPktDropIndex_Object = MibTableColumn
bulkTimedDosPktDropIndex = _BulkTimedDosPktDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 8, 1, 1),
    _BulkTimedDosPktDropIndex_Type()
)
bulkTimedDosPktDropIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bulkTimedDosPktDropIndex.setStatus("current")
_BulkTimedDosPktDropVidsId_Type = Unsigned32
_BulkTimedDosPktDropVidsId_Object = MibTableColumn
bulkTimedDosPktDropVidsId = _BulkTimedDosPktDropVidsId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 8, 1, 2),
    _BulkTimedDosPktDropVidsId_Type()
)
bulkTimedDosPktDropVidsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bulkTimedDosPktDropVidsId.setStatus("current")
_BulkTimedDosPktDropNiId_Type = Unsigned32
_BulkTimedDosPktDropNiId_Object = MibTableColumn
bulkTimedDosPktDropNiId = _BulkTimedDosPktDropNiId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 8, 1, 3),
    _BulkTimedDosPktDropNiId_Type()
)
bulkTimedDosPktDropNiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bulkTimedDosPktDropNiId.setStatus("current")
_BulkTimedDosPktDropMsrId_Type = Integer32
_BulkTimedDosPktDropMsrId_Object = MibTableColumn
bulkTimedDosPktDropMsrId = _BulkTimedDosPktDropMsrId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 8, 1, 4),
    _BulkTimedDosPktDropMsrId_Type()
)
bulkTimedDosPktDropMsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bulkTimedDosPktDropMsrId.setStatus("current")
_BulkTimedDosPktDropEndTime_Type = Unsigned32
_BulkTimedDosPktDropEndTime_Object = MibTableColumn
bulkTimedDosPktDropEndTime = _BulkTimedDosPktDropEndTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 8, 1, 5),
    _BulkTimedDosPktDropEndTime_Type()
)
bulkTimedDosPktDropEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bulkTimedDosPktDropEndTime.setStatus("current")


class _InternalVLANId_Type(Integer32):
    """Custom type internalVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_InternalVLANId_Type.__name__ = "Integer32"
_InternalVLANId_Object = MibScalar
internalVLANId = _InternalVLANId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 14, 9),
    _InternalVLANId_Type()
)
internalVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalVLANId.setStatus("current")
_PktLogGrp_ObjectIdentity = ObjectIdentity
pktLogGrp = _PktLogGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 15)
)
_PktLogServerIPAddress_Type = IpAddress
_PktLogServerIPAddress_Object = MibScalar
pktLogServerIPAddress = _PktLogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 15, 1),
    _PktLogServerIPAddress_Type()
)
pktLogServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktLogServerIPAddress.setStatus("current")


class _PktLogServerPort_Type(Integer32):
    """Custom type pktLogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PktLogServerPort_Type.__name__ = "Integer32"
_PktLogServerPort_Object = MibScalar
pktLogServerPort = _PktLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 15, 2),
    _PktLogServerPort_Type()
)
pktLogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktLogServerPort.setStatus("current")


class _PktLogMaxPacketsPerFlow_Type(Integer32):
    """Custom type pktLogMaxPacketsPerFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_PktLogMaxPacketsPerFlow_Type.__name__ = "Integer32"
_PktLogMaxPacketsPerFlow_Object = MibScalar
pktLogMaxPacketsPerFlow = _PktLogMaxPacketsPerFlow_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 15, 3),
    _PktLogMaxPacketsPerFlow_Type()
)
pktLogMaxPacketsPerFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktLogMaxPacketsPerFlow.setStatus("current")


class _PktLogEncryptionEnable_Type(Integer32):
    """Custom type pktLogEncryptionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_PktLogEncryptionEnable_Type.__name__ = "Integer32"
_PktLogEncryptionEnable_Object = MibScalar
pktLogEncryptionEnable = _PktLogEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 15, 4),
    _PktLogEncryptionEnable_Type()
)
pktLogEncryptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktLogEncryptionEnable.setStatus("current")
_PktLogServerIPv6Address_Type = Ipv6Address
_PktLogServerIPv6Address_Object = MibScalar
pktLogServerIPv6Address = _PktLogServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 15, 5),
    _PktLogServerIPv6Address_Type()
)
pktLogServerIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktLogServerIPv6Address.setStatus("current")
_PktAlertThrottleGrp_ObjectIdentity = ObjectIdentity
pktAlertThrottleGrp = _PktAlertThrottleGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 16)
)


class _PktAlertThrottleGlobalThreshold_Type(Integer32):
    """Custom type pktAlertThrottleGlobalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PktAlertThrottleGlobalThreshold_Type.__name__ = "Integer32"
_PktAlertThrottleGlobalThreshold_Object = MibScalar
pktAlertThrottleGlobalThreshold = _PktAlertThrottleGlobalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 16, 1),
    _PktAlertThrottleGlobalThreshold_Type()
)
pktAlertThrottleGlobalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktAlertThrottleGlobalThreshold.setStatus("current")


class _PktAlertThrottleInterval_Type(Integer32):
    """Custom type pktAlertThrottleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PktAlertThrottleInterval_Type.__name__ = "Integer32"
_PktAlertThrottleInterval_Object = MibScalar
pktAlertThrottleInterval = _PktAlertThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 16, 2),
    _PktAlertThrottleInterval_Type()
)
pktAlertThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktAlertThrottleInterval.setStatus("current")


class _PktAlertThrottleAction_Type(Integer32):
    """Custom type pktAlertThrottleAction based on Integer32"""
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


_PktAlertThrottleAction_Type.__name__ = "Integer32"
_PktAlertThrottleAction_Object = MibScalar
pktAlertThrottleAction = _PktAlertThrottleAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 16, 3),
    _PktAlertThrottleAction_Type()
)
pktAlertThrottleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktAlertThrottleAction.setStatus("current")


class _PktAlertThrottleThreshold_Type(Integer32):
    """Custom type pktAlertThrottleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_PktAlertThrottleThreshold_Type.__name__ = "Integer32"
_PktAlertThrottleThreshold_Object = MibScalar
pktAlertThrottleThreshold = _PktAlertThrottleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 16, 4),
    _PktAlertThrottleThreshold_Type()
)
pktAlertThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktAlertThrottleThreshold.setStatus("current")


class _PktAlertCorrelationTime_Type(Integer32):
    """Custom type pktAlertCorrelationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PktAlertCorrelationTime_Type.__name__ = "Integer32"
_PktAlertCorrelationTime_Object = MibScalar
pktAlertCorrelationTime = _PktAlertCorrelationTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 16, 5),
    _PktAlertCorrelationTime_Type()
)
pktAlertCorrelationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktAlertCorrelationTime.setStatus("current")
_SslConfigGrp_ObjectIdentity = ObjectIdentity
sslConfigGrp = _SslConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17)
)


class _SslSessionCacheLifetime_Type(Integer32):
    """Custom type sslSessionCacheLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967296),
    )


_SslSessionCacheLifetime_Type.__name__ = "Integer32"
_SslSessionCacheLifetime_Object = MibScalar
sslSessionCacheLifetime = _SslSessionCacheLifetime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 1),
    _SslSessionCacheLifetime_Type()
)
sslSessionCacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSessionCacheLifetime.setStatus("current")


class _SslSupportAction_Type(Integer32):
    """Custom type sslSupportAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SslSupportAction_Type.__name__ = "Integer32"
_SslSupportAction_Object = MibScalar
sslSupportAction = _SslSupportAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 2),
    _SslSupportAction_Type()
)
sslSupportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSupportAction.setStatus("current")


class _SslSupportStatus_Type(Integer32):
    """Custom type sslSupportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SslSupportStatus_Type.__name__ = "Integer32"
_SslSupportStatus_Object = MibScalar
sslSupportStatus = _SslSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 3),
    _SslSupportStatus_Type()
)
sslSupportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSupportStatus.setStatus("current")


class _SslSessionRemoveCerts_Type(Integer32):
    """Custom type sslSessionRemoveCerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_SslSessionRemoveCerts_Type.__name__ = "Integer32"
_SslSessionRemoveCerts_Object = MibScalar
sslSessionRemoveCerts = _SslSessionRemoveCerts_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 4),
    _SslSessionRemoveCerts_Type()
)
sslSessionRemoveCerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSessionRemoveCerts.setStatus("current")


class _SslPktLoggingEnable_Type(Integer32):
    """Custom type sslPktLoggingEnable based on Integer32"""
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


_SslPktLoggingEnable_Type.__name__ = "Integer32"
_SslPktLoggingEnable_Object = MibScalar
sslPktLoggingEnable = _SslPktLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 5),
    _SslPktLoggingEnable_Type()
)
sslPktLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslPktLoggingEnable.setStatus("current")


class _SslModesofOperation_Type(Integer32):
    """Custom type sslModesofOperation based on Integer32"""
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
        *(("disable", 0),
          ("inbound-known-key-only", 1),
          ("outbound-proxy-only", 2),
          ("inbound-proxy-only", 3),
          ("inbound-and-outbound-proxy", 4),
          ("inbound-known-key-and-outbound-proxy", 5))
    )


_SslModesofOperation_Type.__name__ = "Integer32"
_SslModesofOperation_Object = MibScalar
sslModesofOperation = _SslModesofOperation_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 6),
    _SslModesofOperation_Type()
)
sslModesofOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslModesofOperation.setStatus("current")


class _SslSessionCacheLifetimeOutbound_Type(Integer32):
    """Custom type sslSessionCacheLifetimeOutbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967296),
    )


_SslSessionCacheLifetimeOutbound_Type.__name__ = "Integer32"
_SslSessionCacheLifetimeOutbound_Object = MibScalar
sslSessionCacheLifetimeOutbound = _SslSessionCacheLifetimeOutbound_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 7),
    _SslSessionCacheLifetimeOutbound_Type()
)
sslSessionCacheLifetimeOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSessionCacheLifetimeOutbound.setStatus("current")


class _SslPktLoggingOutboundEnable_Type(Integer32):
    """Custom type sslPktLoggingOutboundEnable based on Integer32"""
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


_SslPktLoggingOutboundEnable_Type.__name__ = "Integer32"
_SslPktLoggingOutboundEnable_Object = MibScalar
sslPktLoggingOutboundEnable = _SslPktLoggingOutboundEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 8),
    _SslPktLoggingOutboundEnable_Type()
)
sslPktLoggingOutboundEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslPktLoggingOutboundEnable.setStatus("current")


class _SslProxyOutboundUnknownServerCertificate_Type(Integer32):
    """Custom type sslProxyOutboundUnknownServerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("block", 2),
          ("decrypt", 3))
    )


_SslProxyOutboundUnknownServerCertificate_Type.__name__ = "Integer32"
_SslProxyOutboundUnknownServerCertificate_Object = MibScalar
sslProxyOutboundUnknownServerCertificate = _SslProxyOutboundUnknownServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 9),
    _SslProxyOutboundUnknownServerCertificate_Type()
)
sslProxyOutboundUnknownServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProxyOutboundUnknownServerCertificate.setStatus("current")


class _SslProxyOutboundUntrustedServerCertficate_Type(Integer32):
    """Custom type sslProxyOutboundUntrustedServerCertficate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("block", 2),
          ("decrypt", 3))
    )


_SslProxyOutboundUntrustedServerCertficate_Type.__name__ = "Integer32"
_SslProxyOutboundUntrustedServerCertficate_Object = MibScalar
sslProxyOutboundUntrustedServerCertficate = _SslProxyOutboundUntrustedServerCertficate_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 10),
    _SslProxyOutboundUntrustedServerCertficate_Type()
)
sslProxyOutboundUntrustedServerCertficate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProxyOutboundUntrustedServerCertficate.setStatus("current")


class _SslProxyOutboundUnsupportedCipherSuite_Type(Integer32):
    """Custom type sslProxyOutboundUnsupportedCipherSuite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("block", 2))
    )


_SslProxyOutboundUnsupportedCipherSuite_Type.__name__ = "Integer32"
_SslProxyOutboundUnsupportedCipherSuite_Object = MibScalar
sslProxyOutboundUnsupportedCipherSuite = _SslProxyOutboundUnsupportedCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 11),
    _SslProxyOutboundUnsupportedCipherSuite_Type()
)
sslProxyOutboundUnsupportedCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProxyOutboundUnsupportedCipherSuite.setStatus("current")


class _SslProxyInboundUnsupportedCipherSuite_Type(Integer32):
    """Custom type sslProxyInboundUnsupportedCipherSuite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("block", 2))
    )


_SslProxyInboundUnsupportedCipherSuite_Type.__name__ = "Integer32"
_SslProxyInboundUnsupportedCipherSuite_Object = MibScalar
sslProxyInboundUnsupportedCipherSuite = _SslProxyInboundUnsupportedCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 12),
    _SslProxyInboundUnsupportedCipherSuite_Type()
)
sslProxyInboundUnsupportedCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProxyInboundUnsupportedCipherSuite.setStatus("current")


class _SslProxyOutboundUnsupportedServerCertificate_Type(Integer32):
    """Custom type sslProxyOutboundUnsupportedServerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("block", 2))
    )


_SslProxyOutboundUnsupportedServerCertificate_Type.__name__ = "Integer32"
_SslProxyOutboundUnsupportedServerCertificate_Object = MibScalar
sslProxyOutboundUnsupportedServerCertificate = _SslProxyOutboundUnsupportedServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 13),
    _SslProxyOutboundUnsupportedServerCertificate_Type()
)
sslProxyOutboundUnsupportedServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProxyOutboundUnsupportedServerCertificate.setStatus("current")


class _SslProxyInboundUnsupportedServerCertificate_Type(Integer32):
    """Custom type sslProxyInboundUnsupportedServerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("block", 2))
    )


_SslProxyInboundUnsupportedServerCertificate_Type.__name__ = "Integer32"
_SslProxyInboundUnsupportedServerCertificate_Object = MibScalar
sslProxyInboundUnsupportedServerCertificate = _SslProxyInboundUnsupportedServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 14),
    _SslProxyInboundUnsupportedServerCertificate_Type()
)
sslProxyInboundUnsupportedServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProxyInboundUnsupportedServerCertificate.setStatus("current")


class _MaxSslFlowSupportedInSslDisableMode_Type(Integer32):
    """Custom type maxSslFlowSupportedInSslDisableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MaxSslFlowSupportedInSslDisableMode_Type.__name__ = "Integer32"
_MaxSslFlowSupportedInSslDisableMode_Object = MibScalar
maxSslFlowSupportedInSslDisableMode = _MaxSslFlowSupportedInSslDisableMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 15),
    _MaxSslFlowSupportedInSslDisableMode_Type()
)
maxSslFlowSupportedInSslDisableMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSslFlowSupportedInSslDisableMode.setStatus("current")


class _MaxFlowSupportedInSslDisableMode_Type(Integer32):
    """Custom type maxFlowSupportedInSslDisableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MaxFlowSupportedInSslDisableMode_Type.__name__ = "Integer32"
_MaxFlowSupportedInSslDisableMode_Object = MibScalar
maxFlowSupportedInSslDisableMode = _MaxFlowSupportedInSslDisableMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 16),
    _MaxFlowSupportedInSslDisableMode_Type()
)
maxFlowSupportedInSslDisableMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFlowSupportedInSslDisableMode.setStatus("current")


class _MaxSslFlowSupportedInSslInboundLegacyMode_Type(Integer32):
    """Custom type maxSslFlowSupportedInSslInboundLegacyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MaxSslFlowSupportedInSslInboundLegacyMode_Type.__name__ = "Integer32"
_MaxSslFlowSupportedInSslInboundLegacyMode_Object = MibScalar
maxSslFlowSupportedInSslInboundLegacyMode = _MaxSslFlowSupportedInSslInboundLegacyMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 17),
    _MaxSslFlowSupportedInSslInboundLegacyMode_Type()
)
maxSslFlowSupportedInSslInboundLegacyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSslFlowSupportedInSslInboundLegacyMode.setStatus("current")


class _MaxFlowSupportedInSslInboundLegacyMode_Type(Integer32):
    """Custom type maxFlowSupportedInSslInboundLegacyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MaxFlowSupportedInSslInboundLegacyMode_Type.__name__ = "Integer32"
_MaxFlowSupportedInSslInboundLegacyMode_Object = MibScalar
maxFlowSupportedInSslInboundLegacyMode = _MaxFlowSupportedInSslInboundLegacyMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 18),
    _MaxFlowSupportedInSslInboundLegacyMode_Type()
)
maxFlowSupportedInSslInboundLegacyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFlowSupportedInSslInboundLegacyMode.setStatus("current")


class _MaxSslFlowSupportedInSslOutboundMode_Type(Integer32):
    """Custom type maxSslFlowSupportedInSslOutboundMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MaxSslFlowSupportedInSslOutboundMode_Type.__name__ = "Integer32"
_MaxSslFlowSupportedInSslOutboundMode_Object = MibScalar
maxSslFlowSupportedInSslOutboundMode = _MaxSslFlowSupportedInSslOutboundMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 19),
    _MaxSslFlowSupportedInSslOutboundMode_Type()
)
maxSslFlowSupportedInSslOutboundMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSslFlowSupportedInSslOutboundMode.setStatus("current")


class _MaxFlowSupportedInSslOutboundMode_Type(Integer32):
    """Custom type maxFlowSupportedInSslOutboundMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MaxFlowSupportedInSslOutboundMode_Type.__name__ = "Integer32"
_MaxFlowSupportedInSslOutboundMode_Object = MibScalar
maxFlowSupportedInSslOutboundMode = _MaxFlowSupportedInSslOutboundMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 20),
    _MaxFlowSupportedInSslOutboundMode_Type()
)
maxFlowSupportedInSslOutboundMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFlowSupportedInSslOutboundMode.setStatus("current")


class _SslModesofOperationStatus_Type(Integer32):
    """Custom type sslModesofOperationStatus based on Integer32"""
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
        *(("disable", 0),
          ("inbound-known-key-only", 1),
          ("outbound-proxy-only", 2),
          ("inbound-proxy-only", 3),
          ("inbound-and-outbound-proxy", 4),
          ("inbound-known-key-and-outbound-proxy", 5))
    )


_SslModesofOperationStatus_Type.__name__ = "Integer32"
_SslModesofOperationStatus_Object = MibScalar
sslModesofOperationStatus = _SslModesofOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 21),
    _SslModesofOperationStatus_Type()
)
sslModesofOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslModesofOperationStatus.setStatus("current")


class _SslProxyOutboundUnknownURLCategory_Type(Integer32):
    """Custom type sslProxyOutboundUnknownURLCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("decrypt", 3))
    )


_SslProxyOutboundUnknownURLCategory_Type.__name__ = "Integer32"
_SslProxyOutboundUnknownURLCategory_Object = MibScalar
sslProxyOutboundUnknownURLCategory = _SslProxyOutboundUnknownURLCategory_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 22),
    _SslProxyOutboundUnknownURLCategory_Type()
)
sslProxyOutboundUnknownURLCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProxyOutboundUnknownURLCategory.setStatus("current")


class _SslShKeyDecryptEnable_Type(Integer32):
    """Custom type sslShKeyDecryptEnable based on Integer32"""
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


_SslShKeyDecryptEnable_Type.__name__ = "Integer32"
_SslShKeyDecryptEnable_Object = MibScalar
sslShKeyDecryptEnable = _SslShKeyDecryptEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 17, 23),
    _SslShKeyDecryptEnable_Type()
)
sslShKeyDecryptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslShKeyDecryptEnable.setStatus("current")
_L2ConfigGrp_ObjectIdentity = ObjectIdentity
l2ConfigGrp = _L2ConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 18)
)


class _L2ModeEnable_Type(Integer32):
    """Custom type l2ModeEnable based on Integer32"""
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


_L2ModeEnable_Type.__name__ = "Integer32"
_L2ModeEnable_Object = MibScalar
l2ModeEnable = _L2ModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 18, 1),
    _L2ModeEnable_Type()
)
l2ModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ModeEnable.setStatus("current")


class _L2ModeStatus_Type(Integer32):
    """Custom type l2ModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2Mode", 1),
          ("ipsMode", 2))
    )


_L2ModeStatus_Type.__name__ = "Integer32"
_L2ModeStatus_Object = MibScalar
l2ModeStatus = _L2ModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 18, 2),
    _L2ModeStatus_Type()
)
l2ModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ModeStatus.setStatus("current")


class _L2ModeCfgDuration_Type(Integer32):
    """Custom type l2ModeCfgDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_L2ModeCfgDuration_Type.__name__ = "Integer32"
_L2ModeCfgDuration_Object = MibScalar
l2ModeCfgDuration = _L2ModeCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 18, 3),
    _L2ModeCfgDuration_Type()
)
l2ModeCfgDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ModeCfgDuration.setStatus("current")


class _L2ModeCfgThreshold_Type(Integer32):
    """Custom type l2ModeCfgThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_L2ModeCfgThreshold_Type.__name__ = "Integer32"
_L2ModeCfgThreshold_Object = MibScalar
l2ModeCfgThreshold = _L2ModeCfgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 18, 4),
    _L2ModeCfgThreshold_Type()
)
l2ModeCfgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ModeCfgThreshold.setStatus("current")


class _L2ModeOccCount_Type(Integer32):
    """Custom type l2ModeOccCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_L2ModeOccCount_Type.__name__ = "Integer32"
_L2ModeOccCount_Object = MibScalar
l2ModeOccCount = _L2ModeOccCount_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 18, 5),
    _L2ModeOccCount_Type()
)
l2ModeOccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ModeOccCount.setStatus("current")


class _L2ModeReason_Type(DisplayString):
    """Custom type l2ModeReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_L2ModeReason_Type.__name__ = "DisplayString"
_L2ModeReason_Object = MibScalar
l2ModeReason = _L2ModeReason_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 18, 6),
    _L2ModeReason_Type()
)
l2ModeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ModeReason.setStatus("current")
_AclLogAlertGrp_ObjectIdentity = ObjectIdentity
aclLogAlertGrp = _AclLogAlertGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 19)
)


class _AclAlertLogging_Type(Integer32):
    """Custom type aclAlertLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g-enable-dropped", 1),
          ("g-enable-allowed", 2),
          ("g-enable-all", 3),
          ("enable-per-acl", 4),
          ("disable", 5))
    )


_AclAlertLogging_Type.__name__ = "Integer32"
_AclAlertLogging_Object = MibScalar
aclAlertLogging = _AclAlertLogging_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 19, 1),
    _AclAlertLogging_Type()
)
aclAlertLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAlertLogging.setStatus("current")


class _AclAlertThrottleMaxIpPair_Type(Integer32):
    """Custom type aclAlertThrottleMaxIpPair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclAlertThrottleMaxIpPair_Type.__name__ = "Integer32"
_AclAlertThrottleMaxIpPair_Object = MibScalar
aclAlertThrottleMaxIpPair = _AclAlertThrottleMaxIpPair_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 19, 2),
    _AclAlertThrottleMaxIpPair_Type()
)
aclAlertThrottleMaxIpPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAlertThrottleMaxIpPair.setStatus("current")


class _AclAlertThrottleInterval_Type(Integer32):
    """Custom type aclAlertThrottleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AclAlertThrottleInterval_Type.__name__ = "Integer32"
_AclAlertThrottleInterval_Object = MibScalar
aclAlertThrottleInterval = _AclAlertThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 19, 3),
    _AclAlertThrottleInterval_Type()
)
aclAlertThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAlertThrottleInterval.setStatus("current")


class _AclAlertThrottleAction_Type(Integer32):
    """Custom type aclAlertThrottleAction based on Integer32"""
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


_AclAlertThrottleAction_Type.__name__ = "Integer32"
_AclAlertThrottleAction_Object = MibScalar
aclAlertThrottleAction = _AclAlertThrottleAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 19, 4),
    _AclAlertThrottleAction_Type()
)
aclAlertThrottleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAlertThrottleAction.setStatus("current")


class _AclAlertThrottleThreshold_Type(Integer32):
    """Custom type aclAlertThrottleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_AclAlertThrottleThreshold_Type.__name__ = "Integer32"
_AclAlertThrottleThreshold_Object = MibScalar
aclAlertThrottleThreshold = _AclAlertThrottleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 19, 5),
    _AclAlertThrottleThreshold_Type()
)
aclAlertThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAlertThrottleThreshold.setStatus("current")


class _AclAlertDirectToSyslog_Type(Integer32):
    """Custom type aclAlertDirectToSyslog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendViaNSM", 1),
          ("sendDirect", 2))
    )


_AclAlertDirectToSyslog_Type.__name__ = "Integer32"
_AclAlertDirectToSyslog_Object = MibScalar
aclAlertDirectToSyslog = _AclAlertDirectToSyslog_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 19, 6),
    _AclAlertDirectToSyslog_Type()
)
aclAlertDirectToSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAlertDirectToSyslog.setStatus("current")
_TacacsPlusAuthGrp_ObjectIdentity = ObjectIdentity
tacacsPlusAuthGrp = _TacacsPlusAuthGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20)
)


class _EnableTacacsPlusAuth_Type(Integer32):
    """Custom type enableTacacsPlusAuth based on Integer32"""
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


_EnableTacacsPlusAuth_Type.__name__ = "Integer32"
_EnableTacacsPlusAuth_Object = MibScalar
enableTacacsPlusAuth = _EnableTacacsPlusAuth_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20, 1),
    _EnableTacacsPlusAuth_Type()
)
enableTacacsPlusAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTacacsPlusAuth.setStatus("current")


class _EnableTacacsPlusTrafficEncr_Type(Integer32):
    """Custom type enableTacacsPlusTrafficEncr based on Integer32"""
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


_EnableTacacsPlusTrafficEncr_Type.__name__ = "Integer32"
_EnableTacacsPlusTrafficEncr_Object = MibScalar
enableTacacsPlusTrafficEncr = _EnableTacacsPlusTrafficEncr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20, 2),
    _EnableTacacsPlusTrafficEncr_Type()
)
enableTacacsPlusTrafficEncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTacacsPlusTrafficEncr.setStatus("current")


class _TacacsPlusEncrSecret_Type(DisplayString):
    """Custom type tacacsPlusEncrSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TacacsPlusEncrSecret_Type.__name__ = "DisplayString"
_TacacsPlusEncrSecret_Object = MibScalar
tacacsPlusEncrSecret = _TacacsPlusEncrSecret_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20, 3),
    _TacacsPlusEncrSecret_Type()
)
tacacsPlusEncrSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusEncrSecret.setStatus("current")
_TacacsPlusServerIPTable_Object = MibTable
tacacsPlusServerIPTable = _TacacsPlusServerIPTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20, 4)
)
if mibBuilder.loadTexts:
    tacacsPlusServerIPTable.setStatus("current")
_TacacsPlusServerIPEntry_Object = MibTableRow
tacacsPlusServerIPEntry = _TacacsPlusServerIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20, 4, 1)
)
tacacsPlusServerIPEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "tacIndex"),
)
if mibBuilder.loadTexts:
    tacacsPlusServerIPEntry.setStatus("current")
_TacIndex_Type = Integer32
_TacIndex_Object = MibTableColumn
tacIndex = _TacIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20, 4, 1, 1),
    _TacIndex_Type()
)
tacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacIndex.setStatus("current")
_TacacsPlusServerIPAddr_Type = IpAddress
_TacacsPlusServerIPAddr_Object = MibTableColumn
tacacsPlusServerIPAddr = _TacacsPlusServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20, 4, 1, 2),
    _TacacsPlusServerIPAddr_Type()
)
tacacsPlusServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerIPAddr.setStatus("current")
_EnableTacacsPlusAuthorization_Type = Integer32
_EnableTacacsPlusAuthorization_Object = MibScalar
enableTacacsPlusAuthorization = _EnableTacacsPlusAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 20, 5),
    _EnableTacacsPlusAuthorization_Type()
)
enableTacacsPlusAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTacacsPlusAuthorization.setStatus("current")
_IpV6ConfigGrp_ObjectIdentity = ObjectIdentity
ipV6ConfigGrp = _IpV6ConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 21)
)


class _IpV6TrafficHandling_Type(Integer32):
    """Custom type ipV6TrafficHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont-parse-block-inline", 1),
          ("dont-parse-allow-inline", 2),
          ("parse-and-detect-attacks", 3))
    )


_IpV6TrafficHandling_Type.__name__ = "Integer32"
_IpV6TrafficHandling_Object = MibScalar
ipV6TrafficHandling = _IpV6TrafficHandling_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 21, 2),
    _IpV6TrafficHandling_Type()
)
ipV6TrafficHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipV6TrafficHandling.setStatus("current")
_HostQGrp_ObjectIdentity = ObjectIdentity
hostQGrp = _HostQGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22)
)
_HostQConfigGrp_ObjectIdentity = ObjectIdentity
hostQConfigGrp = _HostQConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 1)
)


class _HostQFilterTimeOut_Type(Integer32):
    """Custom type hostQFilterTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_HostQFilterTimeOut_Type.__name__ = "Integer32"
_HostQFilterTimeOut_Object = MibScalar
hostQFilterTimeOut = _HostQFilterTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 1, 1),
    _HostQFilterTimeOut_Type()
)
hostQFilterTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostQFilterTimeOut.setStatus("obsolete")


class _HostQDeleteAllFilters_Type(Integer32):
    """Custom type hostQDeleteAllFilters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("true", 1))
    )


_HostQDeleteAllFilters_Type.__name__ = "Integer32"
_HostQDeleteAllFilters_Object = MibScalar
hostQDeleteAllFilters = _HostQDeleteAllFilters_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 1, 2),
    _HostQDeleteAllFilters_Type()
)
hostQDeleteAllFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostQDeleteAllFilters.setStatus("current")
_HostQBulkFilterV4Table_Object = MibTable
hostQBulkFilterV4Table = _HostQBulkFilterV4Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2)
)
if mibBuilder.loadTexts:
    hostQBulkFilterV4Table.setStatus("current")
_HostQBulkFilterV4Entry_Object = MibTableRow
hostQBulkFilterV4Entry = _HostQBulkFilterV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1)
)
hostQBulkFilterV4Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQBulkFilterIndexV4"),
)
if mibBuilder.loadTexts:
    hostQBulkFilterV4Entry.setStatus("current")
_HostQBulkFilterIndexV4_Type = Integer32
_HostQBulkFilterIndexV4_Object = MibTableColumn
hostQBulkFilterIndexV4 = _HostQBulkFilterIndexV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 1),
    _HostQBulkFilterIndexV4_Type()
)
hostQBulkFilterIndexV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterIndexV4.setStatus("current")
_HostQBulkFilterSrcIPAddrV4_Type = IpAddress
_HostQBulkFilterSrcIPAddrV4_Object = MibTableColumn
hostQBulkFilterSrcIPAddrV4 = _HostQBulkFilterSrcIPAddrV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 2),
    _HostQBulkFilterSrcIPAddrV4_Type()
)
hostQBulkFilterSrcIPAddrV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterSrcIPAddrV4.setStatus("current")
_HostQBulkFilterVidsIdV4_Type = Integer32
_HostQBulkFilterVidsIdV4_Object = MibTableColumn
hostQBulkFilterVidsIdV4 = _HostQBulkFilterVidsIdV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 3),
    _HostQBulkFilterVidsIdV4_Type()
)
hostQBulkFilterVidsIdV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterVidsIdV4.setStatus("current")
_HostQBulkFilterAttackIdV4_Type = Integer32
_HostQBulkFilterAttackIdV4_Object = MibTableColumn
hostQBulkFilterAttackIdV4 = _HostQBulkFilterAttackIdV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 4),
    _HostQBulkFilterAttackIdV4_Type()
)
hostQBulkFilterAttackIdV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterAttackIdV4.setStatus("current")
_HostQBulkFilterEndTimeV4_Type = Unsigned32
_HostQBulkFilterEndTimeV4_Object = MibTableColumn
hostQBulkFilterEndTimeV4 = _HostQBulkFilterEndTimeV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 5),
    _HostQBulkFilterEndTimeV4_Type()
)
hostQBulkFilterEndTimeV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterEndTimeV4.setStatus("current")


class _HostQBulkFilterQRStatusV4_Type(Integer32):
    """Custom type hostQBulkFilterQRStatusV4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hostQuarantined-local", 1),
          ("hostUnderRemediation-local", 2),
          ("hostQuarantined-mpe", 4),
          ("hostQuarantined-both", 5),
          ("hostUnderRemediation-local-hostQuarantined-mpe", 6),
          ("hostUnderRemediation-mpe", 8),
          ("hostQuarantined-local-hostUnderRemediation-mpe", 9),
          ("hostUnderRemediation-both", 10))
    )


_HostQBulkFilterQRStatusV4_Type.__name__ = "Integer32"
_HostQBulkFilterQRStatusV4_Object = MibTableColumn
hostQBulkFilterQRStatusV4 = _HostQBulkFilterQRStatusV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 6),
    _HostQBulkFilterQRStatusV4_Type()
)
hostQBulkFilterQRStatusV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterQRStatusV4.setStatus("current")


class _HostQBulkFilterMPEReplyMsgV4_Type(Integer32):
    """Custom type hostQBulkFilterMPEReplyMsgV4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("managedHost", 1),
          ("unmanagedHost", 2))
    )


_HostQBulkFilterMPEReplyMsgV4_Type.__name__ = "Integer32"
_HostQBulkFilterMPEReplyMsgV4_Object = MibTableColumn
hostQBulkFilterMPEReplyMsgV4 = _HostQBulkFilterMPEReplyMsgV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 7),
    _HostQBulkFilterMPEReplyMsgV4_Type()
)
hostQBulkFilterMPEReplyMsgV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterMPEReplyMsgV4.setStatus("current")
_HostQBulkFilterMonPortIdV4_Type = TrellixPortLinearIndex
_HostQBulkFilterMonPortIdV4_Object = MibTableColumn
hostQBulkFilterMonPortIdV4 = _HostQBulkFilterMonPortIdV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 8),
    _HostQBulkFilterMonPortIdV4_Type()
)
hostQBulkFilterMonPortIdV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterMonPortIdV4.setStatus("current")
_HostQBulkFilterEZIdV4_Type = Integer32
_HostQBulkFilterEZIdV4_Object = MibTableColumn
hostQBulkFilterEZIdV4 = _HostQBulkFilterEZIdV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 2, 1, 9),
    _HostQBulkFilterEZIdV4_Type()
)
hostQBulkFilterEZIdV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterEZIdV4.setStatus("current")
_HostQBulkFilterV6Table_Object = MibTable
hostQBulkFilterV6Table = _HostQBulkFilterV6Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3)
)
if mibBuilder.loadTexts:
    hostQBulkFilterV6Table.setStatus("current")
_HostQBulkFilterV6Entry_Object = MibTableRow
hostQBulkFilterV6Entry = _HostQBulkFilterV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1)
)
hostQBulkFilterV6Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQBulkFilterIndexV6"),
)
if mibBuilder.loadTexts:
    hostQBulkFilterV6Entry.setStatus("current")
_HostQBulkFilterIndexV6_Type = Integer32
_HostQBulkFilterIndexV6_Object = MibTableColumn
hostQBulkFilterIndexV6 = _HostQBulkFilterIndexV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1, 1),
    _HostQBulkFilterIndexV6_Type()
)
hostQBulkFilterIndexV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterIndexV6.setStatus("current")
_HostQBulkFilterSrcIPAddrV6_Type = Ipv6Address
_HostQBulkFilterSrcIPAddrV6_Object = MibTableColumn
hostQBulkFilterSrcIPAddrV6 = _HostQBulkFilterSrcIPAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1, 2),
    _HostQBulkFilterSrcIPAddrV6_Type()
)
hostQBulkFilterSrcIPAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterSrcIPAddrV6.setStatus("current")
_HostQBulkFilterVidsIdV6_Type = Integer32
_HostQBulkFilterVidsIdV6_Object = MibTableColumn
hostQBulkFilterVidsIdV6 = _HostQBulkFilterVidsIdV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1, 3),
    _HostQBulkFilterVidsIdV6_Type()
)
hostQBulkFilterVidsIdV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterVidsIdV6.setStatus("current")
_HostQBulkFilterAttackIdV6_Type = Integer32
_HostQBulkFilterAttackIdV6_Object = MibTableColumn
hostQBulkFilterAttackIdV6 = _HostQBulkFilterAttackIdV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1, 4),
    _HostQBulkFilterAttackIdV6_Type()
)
hostQBulkFilterAttackIdV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterAttackIdV6.setStatus("current")
_HostQBulkFilterEndTimeV6_Type = Unsigned32
_HostQBulkFilterEndTimeV6_Object = MibTableColumn
hostQBulkFilterEndTimeV6 = _HostQBulkFilterEndTimeV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1, 5),
    _HostQBulkFilterEndTimeV6_Type()
)
hostQBulkFilterEndTimeV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterEndTimeV6.setStatus("current")


class _HostQBulkFilterQRStatusV6_Type(Integer32):
    """Custom type hostQBulkFilterQRStatusV6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hostQuarantined-local", 1),
          ("hostUnderRemediation-local", 2),
          ("hostQuarantined-mpe", 4),
          ("hostQuarantined-both", 5),
          ("hostUnderRemediation-local-hostQuarantined-mpe", 6),
          ("hostUnderRemediation-mpe", 8),
          ("hostQuarantined-local-hostUnderRemediation-mpe", 9),
          ("hostUnderRemediation-both", 10))
    )


_HostQBulkFilterQRStatusV6_Type.__name__ = "Integer32"
_HostQBulkFilterQRStatusV6_Object = MibTableColumn
hostQBulkFilterQRStatusV6 = _HostQBulkFilterQRStatusV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1, 6),
    _HostQBulkFilterQRStatusV6_Type()
)
hostQBulkFilterQRStatusV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterQRStatusV6.setStatus("current")


class _HostQBulkFilterMPEReplyMsgV6_Type(Integer32):
    """Custom type hostQBulkFilterMPEReplyMsgV6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("managedHost", 1),
          ("unmanagedHost", 2))
    )


_HostQBulkFilterMPEReplyMsgV6_Type.__name__ = "Integer32"
_HostQBulkFilterMPEReplyMsgV6_Object = MibTableColumn
hostQBulkFilterMPEReplyMsgV6 = _HostQBulkFilterMPEReplyMsgV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1, 7),
    _HostQBulkFilterMPEReplyMsgV6_Type()
)
hostQBulkFilterMPEReplyMsgV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterMPEReplyMsgV6.setStatus("current")
_HostQBulkFilterMonPortIdV6_Type = TrellixPortLinearIndex
_HostQBulkFilterMonPortIdV6_Object = MibTableColumn
hostQBulkFilterMonPortIdV6 = _HostQBulkFilterMonPortIdV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 3, 1, 8),
    _HostQBulkFilterMonPortIdV6_Type()
)
hostQBulkFilterMonPortIdV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQBulkFilterMonPortIdV6.setStatus("current")
_HostQNeverDenyV4Table_Object = MibTable
hostQNeverDenyV4Table = _HostQNeverDenyV4Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 4)
)
if mibBuilder.loadTexts:
    hostQNeverDenyV4Table.setStatus("obsolete")
_HostQNeverDenyV4Entry_Object = MibTableRow
hostQNeverDenyV4Entry = _HostQNeverDenyV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 4, 1)
)
hostQNeverDenyV4Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQNeverDenyIpAddressV4"),
)
if mibBuilder.loadTexts:
    hostQNeverDenyV4Entry.setStatus("obsolete")
_HostQNeverDenyIpAddressV4_Type = IpAddress
_HostQNeverDenyIpAddressV4_Object = MibTableColumn
hostQNeverDenyIpAddressV4 = _HostQNeverDenyIpAddressV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 4, 1, 1),
    _HostQNeverDenyIpAddressV4_Type()
)
hostQNeverDenyIpAddressV4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostQNeverDenyIpAddressV4.setStatus("obsolete")
_HostQNeverDenyActionV4_Type = RowStatus
_HostQNeverDenyActionV4_Object = MibTableColumn
hostQNeverDenyActionV4 = _HostQNeverDenyActionV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 4, 1, 2),
    _HostQNeverDenyActionV4_Type()
)
hostQNeverDenyActionV4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostQNeverDenyActionV4.setStatus("obsolete")
_HostQNeverDenyV6Table_Object = MibTable
hostQNeverDenyV6Table = _HostQNeverDenyV6Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 5)
)
if mibBuilder.loadTexts:
    hostQNeverDenyV6Table.setStatus("obsolete")
_HostQNeverDenyV6Entry_Object = MibTableRow
hostQNeverDenyV6Entry = _HostQNeverDenyV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 5, 1)
)
hostQNeverDenyV6Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQNeverDenyIpAddressV6"),
)
if mibBuilder.loadTexts:
    hostQNeverDenyV6Entry.setStatus("obsolete")
_HostQNeverDenyIpAddressV6_Type = Ipv6Address
_HostQNeverDenyIpAddressV6_Object = MibTableColumn
hostQNeverDenyIpAddressV6 = _HostQNeverDenyIpAddressV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 5, 1, 1),
    _HostQNeverDenyIpAddressV6_Type()
)
hostQNeverDenyIpAddressV6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostQNeverDenyIpAddressV6.setStatus("obsolete")
_HostQNeverDenyActionV6_Type = RowStatus
_HostQNeverDenyActionV6_Object = MibTableColumn
hostQNeverDenyActionV6 = _HostQNeverDenyActionV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 5, 1, 2),
    _HostQNeverDenyActionV6_Type()
)
hostQNeverDenyActionV6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostQNeverDenyActionV6.setStatus("obsolete")
_HostQUserDefFilterV4Table_Object = MibTable
hostQUserDefFilterV4Table = _HostQUserDefFilterV4Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 6)
)
if mibBuilder.loadTexts:
    hostQUserDefFilterV4Table.setStatus("current")
_HostQUserDefFilterV4Entry_Object = MibTableRow
hostQUserDefFilterV4Entry = _HostQUserDefFilterV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 6, 1)
)
hostQUserDefFilterV4Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQUserDefFilterSrcIpV4"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQUserDefFilterVidsIdV4"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQUserDefFilterAttackIdV4"),
)
if mibBuilder.loadTexts:
    hostQUserDefFilterV4Entry.setStatus("current")
_HostQUserDefFilterSrcIpV4_Type = IpAddress
_HostQUserDefFilterSrcIpV4_Object = MibTableColumn
hostQUserDefFilterSrcIpV4 = _HostQUserDefFilterSrcIpV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 6, 1, 1),
    _HostQUserDefFilterSrcIpV4_Type()
)
hostQUserDefFilterSrcIpV4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostQUserDefFilterSrcIpV4.setStatus("current")
_HostQUserDefFilterVidsIdV4_Type = Integer32
_HostQUserDefFilterVidsIdV4_Object = MibTableColumn
hostQUserDefFilterVidsIdV4 = _HostQUserDefFilterVidsIdV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 6, 1, 2),
    _HostQUserDefFilterVidsIdV4_Type()
)
hostQUserDefFilterVidsIdV4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostQUserDefFilterVidsIdV4.setStatus("current")
_HostQUserDefFilterAttackIdV4_Type = Integer32
_HostQUserDefFilterAttackIdV4_Object = MibTableColumn
hostQUserDefFilterAttackIdV4 = _HostQUserDefFilterAttackIdV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 6, 1, 3),
    _HostQUserDefFilterAttackIdV4_Type()
)
hostQUserDefFilterAttackIdV4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostQUserDefFilterAttackIdV4.setStatus("current")
_HostQUserDefFilterDurationV4_Type = Unsigned32
_HostQUserDefFilterDurationV4_Object = MibTableColumn
hostQUserDefFilterDurationV4 = _HostQUserDefFilterDurationV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 6, 1, 4),
    _HostQUserDefFilterDurationV4_Type()
)
hostQUserDefFilterDurationV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostQUserDefFilterDurationV4.setStatus("current")


class _HostQUserDefFilterActionV4_Type(Integer32):
    """Custom type hostQUserDefFilterActionV4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("add", 1),
          ("delete", 2))
    )


_HostQUserDefFilterActionV4_Type.__name__ = "Integer32"
_HostQUserDefFilterActionV4_Object = MibTableColumn
hostQUserDefFilterActionV4 = _HostQUserDefFilterActionV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 6, 1, 5),
    _HostQUserDefFilterActionV4_Type()
)
hostQUserDefFilterActionV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostQUserDefFilterActionV4.setStatus("current")
_HostQUserDefFilterRemediationV4_Type = TruthValue
_HostQUserDefFilterRemediationV4_Object = MibTableColumn
hostQUserDefFilterRemediationV4 = _HostQUserDefFilterRemediationV4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 6, 1, 6),
    _HostQUserDefFilterRemediationV4_Type()
)
hostQUserDefFilterRemediationV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostQUserDefFilterRemediationV4.setStatus("current")
_HostQUserDefFilterV6Table_Object = MibTable
hostQUserDefFilterV6Table = _HostQUserDefFilterV6Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 7)
)
if mibBuilder.loadTexts:
    hostQUserDefFilterV6Table.setStatus("current")
_HostQUserDefFilterV6Entry_Object = MibTableRow
hostQUserDefFilterV6Entry = _HostQUserDefFilterV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 7, 1)
)
hostQUserDefFilterV6Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQUserDefFilterSrcIpV6"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQUserDefFilterVidsIdV6"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostQUserDefFilterAttackIdV6"),
)
if mibBuilder.loadTexts:
    hostQUserDefFilterV6Entry.setStatus("current")
_HostQUserDefFilterSrcIpV6_Type = Ipv6Address
_HostQUserDefFilterSrcIpV6_Object = MibTableColumn
hostQUserDefFilterSrcIpV6 = _HostQUserDefFilterSrcIpV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 7, 1, 1),
    _HostQUserDefFilterSrcIpV6_Type()
)
hostQUserDefFilterSrcIpV6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostQUserDefFilterSrcIpV6.setStatus("current")
_HostQUserDefFilterVidsIdV6_Type = Integer32
_HostQUserDefFilterVidsIdV6_Object = MibTableColumn
hostQUserDefFilterVidsIdV6 = _HostQUserDefFilterVidsIdV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 7, 1, 2),
    _HostQUserDefFilterVidsIdV6_Type()
)
hostQUserDefFilterVidsIdV6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostQUserDefFilterVidsIdV6.setStatus("current")
_HostQUserDefFilterAttackIdV6_Type = Integer32
_HostQUserDefFilterAttackIdV6_Object = MibTableColumn
hostQUserDefFilterAttackIdV6 = _HostQUserDefFilterAttackIdV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 7, 1, 3),
    _HostQUserDefFilterAttackIdV6_Type()
)
hostQUserDefFilterAttackIdV6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostQUserDefFilterAttackIdV6.setStatus("current")
_HostQUserDefFilterDurationV6_Type = Unsigned32
_HostQUserDefFilterDurationV6_Object = MibTableColumn
hostQUserDefFilterDurationV6 = _HostQUserDefFilterDurationV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 7, 1, 4),
    _HostQUserDefFilterDurationV6_Type()
)
hostQUserDefFilterDurationV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostQUserDefFilterDurationV6.setStatus("current")


class _HostQUserDefFilterActionV6_Type(Integer32):
    """Custom type hostQUserDefFilterActionV6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("add", 1),
          ("delete", 2))
    )


_HostQUserDefFilterActionV6_Type.__name__ = "Integer32"
_HostQUserDefFilterActionV6_Object = MibTableColumn
hostQUserDefFilterActionV6 = _HostQUserDefFilterActionV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 22, 7, 1, 5),
    _HostQUserDefFilterActionV6_Type()
)
hostQUserDefFilterActionV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostQUserDefFilterActionV6.setStatus("current")
_NmsGrp_ObjectIdentity = ObjectIdentity
nmsGrp = _NmsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23)
)
_NmsUserGrp_ObjectIdentity = ObjectIdentity
nmsUserGrp = _NmsUserGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1)
)
_NmsUserTable_Object = MibTable
nmsUserTable = _NmsUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    nmsUserTable.setStatus("current")
_NmsUserEntry_Object = MibTableRow
nmsUserEntry = _NmsUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1, 1, 1)
)
nmsUserEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "nmsUserName"),
)
if mibBuilder.loadTexts:
    nmsUserEntry.setStatus("current")


class _NmsUserName_Type(DisplayString):
    """Custom type nmsUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 31),
    )


_NmsUserName_Type.__name__ = "DisplayString"
_NmsUserName_Object = MibTableColumn
nmsUserName = _NmsUserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1, 1, 1, 1),
    _NmsUserName_Type()
)
nmsUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmsUserName.setStatus("current")


class _NmsAuthKey_Type(DisplayString):
    """Custom type nmsAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 15),
    )


_NmsAuthKey_Type.__name__ = "DisplayString"
_NmsAuthKey_Object = MibTableColumn
nmsAuthKey = _NmsAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1, 1, 1, 2),
    _NmsAuthKey_Type()
)
nmsAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsAuthKey.setStatus("current")


class _NmsEncrKey_Type(DisplayString):
    """Custom type nmsEncrKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 15),
    )


_NmsEncrKey_Type.__name__ = "DisplayString"
_NmsEncrKey_Object = MibTableColumn
nmsEncrKey = _NmsEncrKey_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1, 1, 1, 3),
    _NmsEncrKey_Type()
)
nmsEncrKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEncrKey.setStatus("current")
_NmsUserChangeAction_Type = RowStatus
_NmsUserChangeAction_Object = MibTableColumn
nmsUserChangeAction = _NmsUserChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1, 1, 1, 4),
    _NmsUserChangeAction_Type()
)
nmsUserChangeAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsUserChangeAction.setStatus("current")


class _NmsDeleteAllUsers_Type(Integer32):
    """Custom type nmsDeleteAllUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_NmsDeleteAllUsers_Type.__name__ = "Integer32"
_NmsDeleteAllUsers_Object = MibScalar
nmsDeleteAllUsers = _NmsDeleteAllUsers_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1, 2),
    _NmsDeleteAllUsers_Type()
)
nmsDeleteAllUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsDeleteAllUsers.setStatus("current")


class _NmsCommitUserEntryChanges_Type(Integer32):
    """Custom type nmsCommitUserEntryChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_NmsCommitUserEntryChanges_Type.__name__ = "Integer32"
_NmsCommitUserEntryChanges_Object = MibScalar
nmsCommitUserEntryChanges = _NmsCommitUserEntryChanges_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 1, 3),
    _NmsCommitUserEntryChanges_Type()
)
nmsCommitUserEntryChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsCommitUserEntryChanges.setStatus("current")
_NmsIpGrp_ObjectIdentity = ObjectIdentity
nmsIpGrp = _NmsIpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2)
)
_NmsIpTable_Object = MibTable
nmsIpTable = _NmsIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    nmsIpTable.setStatus("current")
_NmsIpEntry_Object = MibTableRow
nmsIpEntry = _NmsIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2, 1, 1)
)
nmsIpEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "nmsIpAddress"),
)
if mibBuilder.loadTexts:
    nmsIpEntry.setStatus("current")
_NmsIpAddress_Type = IpAddress
_NmsIpAddress_Object = MibTableColumn
nmsIpAddress = _NmsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2, 1, 1, 1),
    _NmsIpAddress_Type()
)
nmsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmsIpAddress.setStatus("current")
_NmsIpChangeAction_Type = RowStatus
_NmsIpChangeAction_Object = MibTableColumn
nmsIpChangeAction = _NmsIpChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2, 1, 1, 2),
    _NmsIpChangeAction_Type()
)
nmsIpChangeAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsIpChangeAction.setStatus("current")
_NmsIpv6Table_Object = MibTable
nmsIpv6Table = _NmsIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2, 2)
)
if mibBuilder.loadTexts:
    nmsIpv6Table.setStatus("current")
_NmsIpv6Entry_Object = MibTableRow
nmsIpv6Entry = _NmsIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2, 2, 1)
)
nmsIpv6Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "nmsIpv6Address"),
)
if mibBuilder.loadTexts:
    nmsIpv6Entry.setStatus("current")
_NmsIpv6Address_Type = Ipv6Address
_NmsIpv6Address_Object = MibTableColumn
nmsIpv6Address = _NmsIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2, 2, 1, 1),
    _NmsIpv6Address_Type()
)
nmsIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmsIpv6Address.setStatus("current")
_NmsIpv6ChangeAction_Type = RowStatus
_NmsIpv6ChangeAction_Object = MibTableColumn
nmsIpv6ChangeAction = _NmsIpv6ChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 23, 2, 2, 1, 2),
    _NmsIpv6ChangeAction_Type()
)
nmsIpv6ChangeAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsIpv6ChangeAction.setStatus("current")
_MpeGrp_ObjectIdentity = ObjectIdentity
mpeGrp = _MpeGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24)
)
_MpeConfigGrp_ObjectIdentity = ObjectIdentity
mpeConfigGrp = _MpeConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1)
)


class _MpeQRScope_Type(Integer32):
    """Custom type mpeQRScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unmanaged-hosts", 1),
          ("all-hosts", 2))
    )


_MpeQRScope_Type.__name__ = "Integer32"
_MpeQRScope_Object = MibScalar
mpeQRScope = _MpeQRScope_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 1),
    _MpeQRScope_Type()
)
mpeQRScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeQRScope.setStatus("obsolete")


class _MpeThrottleTimeout_Type(Integer32):
    """Custom type mpeThrottleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_MpeThrottleTimeout_Type.__name__ = "Integer32"
_MpeThrottleTimeout_Object = MibScalar
mpeThrottleTimeout = _MpeThrottleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 2),
    _MpeThrottleTimeout_Type()
)
mpeThrottleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeThrottleTimeout.setStatus("obsolete")
_MpeInstallConfigGrp_ObjectIdentity = ObjectIdentity
mpeInstallConfigGrp = _MpeInstallConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3)
)
_MpeIpAddress_Type = IpAddress
_MpeIpAddress_Object = MibScalar
mpeIpAddress = _MpeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3, 1),
    _MpeIpAddress_Type()
)
mpeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeIpAddress.setStatus("current")


class _MpeAnonymousPort_Type(Integer32):
    """Custom type mpeAnonymousPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpeAnonymousPort_Type.__name__ = "Integer32"
_MpeAnonymousPort_Object = MibScalar
mpeAnonymousPort = _MpeAnonymousPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3, 2),
    _MpeAnonymousPort_Type()
)
mpeAnonymousPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeAnonymousPort.setStatus("current")


class _MpeTrustedSSLPort_Type(Integer32):
    """Custom type mpeTrustedSSLPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpeTrustedSSLPort_Type.__name__ = "Integer32"
_MpeTrustedSSLPort_Object = MibScalar
mpeTrustedSSLPort = _MpeTrustedSSLPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3, 3),
    _MpeTrustedSSLPort_Type()
)
mpeTrustedSSLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeTrustedSSLPort.setStatus("current")


class _MpeePOCred_Type(DisplayString):
    """Custom type mpeePOCred based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 100),
    )


_MpeePOCred_Type.__name__ = "DisplayString"
_MpeePOCred_Object = MibScalar
mpeePOCred = _MpeePOCred_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3, 4),
    _MpeePOCred_Type()
)
mpeePOCred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeePOCred.setStatus("current")


class _MpeAnonymousURI_Type(DisplayString):
    """Custom type mpeAnonymousURI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 255),
    )


_MpeAnonymousURI_Type.__name__ = "DisplayString"
_MpeAnonymousURI_Object = MibScalar
mpeAnonymousURI = _MpeAnonymousURI_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3, 5),
    _MpeAnonymousURI_Type()
)
mpeAnonymousURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeAnonymousURI.setStatus("current")


class _MpeTrustedURI_Type(DisplayString):
    """Custom type mpeTrustedURI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 255),
    )


_MpeTrustedURI_Type.__name__ = "DisplayString"
_MpeTrustedURI_Object = MibScalar
mpeTrustedURI = _MpeTrustedURI_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3, 6),
    _MpeTrustedURI_Type()
)
mpeTrustedURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeTrustedURI.setStatus("current")


class _MpeInstallConfigAction_Type(Integer32):
    """Custom type mpeInstallConfigAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("install", 1),
          ("deinstall", 2))
    )


_MpeInstallConfigAction_Type.__name__ = "Integer32"
_MpeInstallConfigAction_Object = MibScalar
mpeInstallConfigAction = _MpeInstallConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3, 7),
    _MpeInstallConfigAction_Type()
)
mpeInstallConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeInstallConfigAction.setStatus("current")


class _MpeInstallConfigStatus_Type(Integer32):
    """Custom type mpeInstallConfigStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("installInProgress", 1),
          ("installed", 2),
          ("deinstallInProgress", 3),
          ("deinstalled", 4),
          ("certReqFailure", 5),
          ("sSLError", 6),
          ("httpRespError", 7),
          ("mpeURIError", 8),
          ("ePOCredError", 9),
          ("mpeServerError", 10),
          ("mpeTimeoutError", 11))
    )


_MpeInstallConfigStatus_Type.__name__ = "Integer32"
_MpeInstallConfigStatus_Object = MibScalar
mpeInstallConfigStatus = _MpeInstallConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 3, 8),
    _MpeInstallConfigStatus_Type()
)
mpeInstallConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeInstallConfigStatus.setStatus("current")


class _MpeRootCertStatus_Type(Integer32):
    """Custom type mpeRootCertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-found", 0),
          ("found", 1))
    )


_MpeRootCertStatus_Type.__name__ = "Integer32"
_MpeRootCertStatus_Object = MibScalar
mpeRootCertStatus = _MpeRootCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 4),
    _MpeRootCertStatus_Type()
)
mpeRootCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeRootCertStatus.setStatus("current")


class _MpeDeleteRootCert_Type(Integer32):
    """Custom type mpeDeleteRootCert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_MpeDeleteRootCert_Type.__name__ = "Integer32"
_MpeDeleteRootCert_Object = MibScalar
mpeDeleteRootCert = _MpeDeleteRootCert_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 5),
    _MpeDeleteRootCert_Type()
)
mpeDeleteRootCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeDeleteRootCert.setStatus("current")


class _MnacHealthLevelListenPort_Type(Integer32):
    """Custom type mnacHealthLevelListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MnacHealthLevelListenPort_Type.__name__ = "Integer32"
_MnacHealthLevelListenPort_Object = MibScalar
mnacHealthLevelListenPort = _MnacHealthLevelListenPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 6),
    _MnacHealthLevelListenPort_Type()
)
mnacHealthLevelListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnacHealthLevelListenPort.setStatus("current")


class _MnacConnectivityFailureTimeout_Type(Integer32):
    """Custom type mnacConnectivityFailureTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_MnacConnectivityFailureTimeout_Type.__name__ = "Integer32"
_MnacConnectivityFailureTimeout_Object = MibScalar
mnacConnectivityFailureTimeout = _MnacConnectivityFailureTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 7),
    _MnacConnectivityFailureTimeout_Type()
)
mnacConnectivityFailureTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnacConnectivityFailureTimeout.setStatus("current")
_MnacAgentGUIDPort_Type = Integer32
_MnacAgentGUIDPort_Object = MibScalar
mnacAgentGUIDPort = _MnacAgentGUIDPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 1, 8),
    _MnacAgentGUIDPort_Type()
)
mnacAgentGUIDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnacAgentGUIDPort.setStatus("current")
_MpeExcludedMacTable_Object = MibTable
mpeExcludedMacTable = _MpeExcludedMacTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 2)
)
if mibBuilder.loadTexts:
    mpeExcludedMacTable.setStatus("obsolete")
_MpeExcludedMacEntry_Object = MibTableRow
mpeExcludedMacEntry = _MpeExcludedMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 2, 1)
)
mpeExcludedMacEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "mpeMacAddress"),
)
if mibBuilder.loadTexts:
    mpeExcludedMacEntry.setStatus("obsolete")
_MpeMacAddress_Type = MacAddress
_MpeMacAddress_Object = MibTableColumn
mpeMacAddress = _MpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 2, 1, 1),
    _MpeMacAddress_Type()
)
mpeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpeMacAddress.setStatus("obsolete")
_MpeMacChangeAction_Type = RowStatus
_MpeMacChangeAction_Object = MibTableColumn
mpeMacChangeAction = _MpeMacChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 24, 2, 1, 2),
    _MpeMacChangeAction_Type()
)
mpeMacChangeAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeMacChangeAction.setStatus("obsolete")
_RemediationGrp_ObjectIdentity = ObjectIdentity
remediationGrp = _RemediationGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 25)
)
_RemediationConfigGrp_ObjectIdentity = ObjectIdentity
remediationConfigGrp = _RemediationConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 25, 1)
)


class _RemediationTimeout_Type(Integer32):
    """Custom type remediationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_RemediationTimeout_Type.__name__ = "Integer32"
_RemediationTimeout_Object = MibScalar
remediationTimeout = _RemediationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 25, 1, 2),
    _RemediationTimeout_Type()
)
remediationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remediationTimeout.setStatus("obsolete")
_EzLogAlertGrp_ObjectIdentity = ObjectIdentity
ezLogAlertGrp = _EzLogAlertGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 26)
)


class _EzAlertLogging_Type(Integer32):
    """Custom type ezAlertLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g-enable-dropped", 1),
          ("g-enable-allowed", 2),
          ("g-enable-all", 3),
          ("enable-per-acl", 4),
          ("disable", 5))
    )


_EzAlertLogging_Type.__name__ = "Integer32"
_EzAlertLogging_Object = MibScalar
ezAlertLogging = _EzAlertLogging_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 26, 1),
    _EzAlertLogging_Type()
)
ezAlertLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ezAlertLogging.setStatus("current")


class _EzAlertThrottleMaxIpPair_Type(Integer32):
    """Custom type ezAlertThrottleMaxIpPair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_EzAlertThrottleMaxIpPair_Type.__name__ = "Integer32"
_EzAlertThrottleMaxIpPair_Object = MibScalar
ezAlertThrottleMaxIpPair = _EzAlertThrottleMaxIpPair_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 26, 2),
    _EzAlertThrottleMaxIpPair_Type()
)
ezAlertThrottleMaxIpPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ezAlertThrottleMaxIpPair.setStatus("current")


class _EzAlertThrottleInterval_Type(Integer32):
    """Custom type ezAlertThrottleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_EzAlertThrottleInterval_Type.__name__ = "Integer32"
_EzAlertThrottleInterval_Object = MibScalar
ezAlertThrottleInterval = _EzAlertThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 26, 3),
    _EzAlertThrottleInterval_Type()
)
ezAlertThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ezAlertThrottleInterval.setStatus("current")


class _EzAlertThrottleAction_Type(Integer32):
    """Custom type ezAlertThrottleAction based on Integer32"""
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


_EzAlertThrottleAction_Type.__name__ = "Integer32"
_EzAlertThrottleAction_Object = MibScalar
ezAlertThrottleAction = _EzAlertThrottleAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 26, 4),
    _EzAlertThrottleAction_Type()
)
ezAlertThrottleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ezAlertThrottleAction.setStatus("current")


class _EzAlertThrottleThreshold_Type(Integer32):
    """Custom type ezAlertThrottleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_EzAlertThrottleThreshold_Type.__name__ = "Integer32"
_EzAlertThrottleThreshold_Object = MibScalar
ezAlertThrottleThreshold = _EzAlertThrottleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 26, 5),
    _EzAlertThrottleThreshold_Type()
)
ezAlertThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ezAlertThrottleThreshold.setStatus("current")


class _EzAlertDirectToSyslog_Type(Integer32):
    """Custom type ezAlertDirectToSyslog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendViaNSM", 1),
          ("sendDirect", 2))
    )


_EzAlertDirectToSyslog_Type.__name__ = "Integer32"
_EzAlertDirectToSyslog_Object = MibScalar
ezAlertDirectToSyslog = _EzAlertDirectToSyslog_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 26, 6),
    _EzAlertDirectToSyslog_Type()
)
ezAlertDirectToSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ezAlertDirectToSyslog.setStatus("current")
_NbadGrp_ObjectIdentity = ObjectIdentity
nbadGrp = _NbadGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27)
)
_NbadConfigGrp_ObjectIdentity = ObjectIdentity
nbadConfigGrp = _NbadConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1)
)
_NbadSensorIpAddress_Type = IpAddress
_NbadSensorIpAddress_Object = MibScalar
nbadSensorIpAddress = _NbadSensorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 1),
    _NbadSensorIpAddress_Type()
)
nbadSensorIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadSensorIpAddress.setStatus("current")


class _NbadSensorPort_Type(Integer32):
    """Custom type nbadSensorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_NbadSensorPort_Type.__name__ = "Integer32"
_NbadSensorPort_Object = MibScalar
nbadSensorPort = _NbadSensorPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 2),
    _NbadSensorPort_Type()
)
nbadSensorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadSensorPort.setStatus("current")
_NbadIPSPriMonPortId_Type = TrellixPortLinearIndex
_NbadIPSPriMonPortId_Object = MibScalar
nbadIPSPriMonPortId = _NbadIPSPriMonPortId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 3),
    _NbadIPSPriMonPortId_Type()
)
nbadIPSPriMonPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadIPSPriMonPortId.setStatus("current")
_NbadIPSSecMonPortId_Type = TrellixPortLinearIndex
_NbadIPSSecMonPortId_Object = MibScalar
nbadIPSSecMonPortId = _NbadIPSSecMonPortId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 4),
    _NbadIPSSecMonPortId_Type()
)
nbadIPSSecMonPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadIPSSecMonPortId.setStatus("current")
_NbadAppFingerPrintingEnabled_Type = TruthValue
_NbadAppFingerPrintingEnabled_Object = MibScalar
nbadAppFingerPrintingEnabled = _NbadAppFingerPrintingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 5),
    _NbadAppFingerPrintingEnabled_Type()
)
nbadAppFingerPrintingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadAppFingerPrintingEnabled.setStatus("current")
_NbadOSFingerPrintingEnabled_Type = TruthValue
_NbadOSFingerPrintingEnabled_Object = MibScalar
nbadOSFingerPrintingEnabled = _NbadOSFingerPrintingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 6),
    _NbadOSFingerPrintingEnabled_Type()
)
nbadOSFingerPrintingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadOSFingerPrintingEnabled.setStatus("current")
_NbadSslFlowDataCaptureEnabled_Type = TruthValue
_NbadSslFlowDataCaptureEnabled_Object = MibScalar
nbadSslFlowDataCaptureEnabled = _NbadSslFlowDataCaptureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 7),
    _NbadSslFlowDataCaptureEnabled_Type()
)
nbadSslFlowDataCaptureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadSslFlowDataCaptureEnabled.setStatus("current")


class _NbadFlowProtocolId_Type(Integer32):
    """Custom type nbadFlowProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("netflow", 1)
    )


_NbadFlowProtocolId_Type.__name__ = "Integer32"
_NbadFlowProtocolId_Object = MibScalar
nbadFlowProtocolId = _NbadFlowProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 8),
    _NbadFlowProtocolId_Type()
)
nbadFlowProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadFlowProtocolId.setStatus("current")


class _NbadFlowProtocolVersion_Type(Integer32):
    """Custom type nbadFlowProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("netFlowVersion9", 1)
    )


_NbadFlowProtocolVersion_Type.__name__ = "Integer32"
_NbadFlowProtocolVersion_Object = MibScalar
nbadFlowProtocolVersion = _NbadFlowProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 9),
    _NbadFlowProtocolVersion_Type()
)
nbadFlowProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadFlowProtocolVersion.setStatus("current")


class _NbadCaptureTCP_Type(Integer32):
    """Custom type nbadCaptureTCP based on Integer32"""
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


_NbadCaptureTCP_Type.__name__ = "Integer32"
_NbadCaptureTCP_Object = MibScalar
nbadCaptureTCP = _NbadCaptureTCP_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 10),
    _NbadCaptureTCP_Type()
)
nbadCaptureTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadCaptureTCP.setStatus("current")


class _NbadCaptureUDP_Type(Integer32):
    """Custom type nbadCaptureUDP based on Integer32"""
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


_NbadCaptureUDP_Type.__name__ = "Integer32"
_NbadCaptureUDP_Object = MibScalar
nbadCaptureUDP = _NbadCaptureUDP_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 11),
    _NbadCaptureUDP_Type()
)
nbadCaptureUDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadCaptureUDP.setStatus("current")


class _NbadCaptureICMP_Type(Integer32):
    """Custom type nbadCaptureICMP based on Integer32"""
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


_NbadCaptureICMP_Type.__name__ = "Integer32"
_NbadCaptureICMP_Object = MibScalar
nbadCaptureICMP = _NbadCaptureICMP_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 27, 1, 12),
    _NbadCaptureICMP_Type()
)
nbadCaptureICMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbadCaptureICMP.setStatus("current")
_HostDataGrp_ObjectIdentity = ObjectIdentity
hostDataGrp = _HostDataGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28)
)
_HostDataTable_Object = MibTable
hostDataTable = _HostDataTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1)
)
if mibBuilder.loadTexts:
    hostDataTable.setStatus("current")
_HostDataEntry_Object = MibTableRow
hostDataEntry = _HostDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1)
)
hostDataEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "hostDataIndex"),
)
if mibBuilder.loadTexts:
    hostDataEntry.setStatus("current")
_HostDataIndex_Type = Integer32
_HostDataIndex_Object = MibTableColumn
hostDataIndex = _HostDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 1),
    _HostDataIndex_Type()
)
hostDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDataIndex.setStatus("current")
_HostIPAddress_Type = IpAddress
_HostIPAddress_Object = MibTableColumn
hostIPAddress = _HostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 2),
    _HostIPAddress_Type()
)
hostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIPAddress.setStatus("current")
_HostMacAddress_Type = MacAddress
_HostMacAddress_Object = MibTableColumn
hostMacAddress = _HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 3),
    _HostMacAddress_Type()
)
hostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMacAddress.setStatus("current")
_HostDetectedDHCPMonPortId_Type = TrellixPortLinearIndex
_HostDetectedDHCPMonPortId_Object = MibTableColumn
hostDetectedDHCPMonPortId = _HostDetectedDHCPMonPortId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 4),
    _HostDetectedDHCPMonPortId_Type()
)
hostDetectedDHCPMonPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDetectedDHCPMonPortId.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 5),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")


class _HostUpdatedTimeStamp_Type(Integer32):
    """Custom type hostUpdatedTimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HostUpdatedTimeStamp_Type.__name__ = "Integer32"
_HostUpdatedTimeStamp_Object = MibTableColumn
hostUpdatedTimeStamp = _HostUpdatedTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 6),
    _HostUpdatedTimeStamp_Type()
)
hostUpdatedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostUpdatedTimeStamp.setStatus("current")


class _HostAgentGuid_Type(DisplayString):
    """Custom type hostAgentGuid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HostAgentGuid_Type.__name__ = "DisplayString"
_HostAgentGuid_Object = MibTableColumn
hostAgentGuid = _HostAgentGuid_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 7),
    _HostAgentGuid_Type()
)
hostAgentGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostAgentGuid.setStatus("current")


class _HostNACStatus_Type(Integer32):
    """Custom type hostNACStatus based on Integer32"""
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
        *(("managed", 1),
          ("unmanaged", 2),
          ("unmanageable", 3),
          ("unknown", 4))
    )


_HostNACStatus_Type.__name__ = "Integer32"
_HostNACStatus_Object = MibTableColumn
hostNACStatus = _HostNACStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 8),
    _HostNACStatus_Type()
)
hostNACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostNACStatus.setStatus("current")


class _HostState_Type(Integer32):
    """Custom type hostState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("preadmit-new", 1),
          ("preadmit-sgap", 2),
          ("preadmit-user-detect", 3),
          ("preadmit-host-detect", 4),
          ("preadmit-remediate", 5),
          ("postadmit", 6),
          ("postadmit-remediate", 7),
          ("post-boot", 8),
          ("ib-host-detect", 9),
          ("ib-auth-wait", 10),
          ("ib-host-sgap", 11),
          ("ib-user-detect", 12),
          ("ib-host-remediate", 13),
          ("ib-host-admit", 14),
          ("oob-host-admit", 15),
          ("ib-host-offline", 16))
    )


_HostState_Type.__name__ = "Integer32"
_HostState_Object = MibTableColumn
hostState = _HostState_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 9),
    _HostState_Type()
)
hostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostState.setStatus("current")


class _HostDeploymentMode_Type(Integer32):
    """Custom type hostDeploymentMode based on Integer32"""
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
        *(("dhcp", 1),
          ("standard", 2),
          ("hybrid", 3),
          ("oob", 4))
    )


_HostDeploymentMode_Type.__name__ = "Integer32"
_HostDeploymentMode_Object = MibTableColumn
hostDeploymentMode = _HostDeploymentMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 10),
    _HostDeploymentMode_Type()
)
hostDeploymentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDeploymentMode.setStatus("current")


class _HostHealthLevel_Type(Integer32):
    """Custom type hostHealthLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_HostHealthLevel_Type.__name__ = "Integer32"
_HostHealthLevel_Object = MibTableColumn
hostHealthLevel = _HostHealthLevel_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 11),
    _HostHealthLevel_Type()
)
hostHealthLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHealthLevel.setStatus("current")
_HostEZId_Type = Integer32
_HostEZId_Object = MibTableColumn
hostEZId = _HostEZId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 12),
    _HostEZId_Type()
)
hostEZId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostEZId.setStatus("current")


class _HostUserName_Type(DisplayString):
    """Custom type hostUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HostUserName_Type.__name__ = "DisplayString"
_HostUserName_Object = MibTableColumn
hostUserName = _HostUserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 13),
    _HostUserName_Type()
)
hostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostUserName.setStatus("current")
_HostPolicyId_Type = Integer32
_HostPolicyId_Object = MibTableColumn
hostPolicyId = _HostPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 14),
    _HostPolicyId_Type()
)
hostPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostPolicyId.setStatus("current")


class _HostDetectedTimeStamp_Type(Integer32):
    """Custom type hostDetectedTimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HostDetectedTimeStamp_Type.__name__ = "Integer32"
_HostDetectedTimeStamp_Object = MibTableColumn
hostDetectedTimeStamp = _HostDetectedTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 15),
    _HostDetectedTimeStamp_Type()
)
hostDetectedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDetectedTimeStamp.setStatus("current")
_HostOSInfo_Type = DisplayString
_HostOSInfo_Object = MibTableColumn
hostOSInfo = _HostOSInfo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 16),
    _HostOSInfo_Type()
)
hostOSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOSInfo.setStatus("current")


class _HostMNACAgentOSInfo_Type(DisplayString):
    """Custom type hostMNACAgentOSInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HostMNACAgentOSInfo_Type.__name__ = "DisplayString"
_HostMNACAgentOSInfo_Object = MibTableColumn
hostMNACAgentOSInfo = _HostMNACAgentOSInfo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 17),
    _HostMNACAgentOSInfo_Type()
)
hostMNACAgentOSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMNACAgentOSInfo.setStatus("current")
_HostActive_Type = TruthValue
_HostActive_Object = MibTableColumn
hostActive = _HostActive_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 18),
    _HostActive_Type()
)
hostActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostActive.setStatus("current")
_HostDetectedStdMonPortId_Type = TrellixPortLinearIndex
_HostDetectedStdMonPortId_Object = MibTableColumn
hostDetectedStdMonPortId = _HostDetectedStdMonPortId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 19),
    _HostDetectedStdMonPortId_Type()
)
hostDetectedStdMonPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDetectedStdMonPortId.setStatus("current")


class _HostDetectionType_Type(Integer32):
    """Custom type hostDetectionType based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("l2", 1),
          ("l3", 2),
          ("vpn", 3),
          ("snmp", 4),
          ("radiusMac", 5),
          ("radius8021x", 6),
          ("l3-snmp", 7),
          ("l3-radiusMac", 8),
          ("l3-radius8021x", 9))
    )


_HostDetectionType_Type.__name__ = "Integer32"
_HostDetectionType_Object = MibTableColumn
hostDetectionType = _HostDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 20),
    _HostDetectionType_Type()
)
hostDetectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDetectionType.setStatus("current")


class _HostUserAuthProtocol_Type(Integer32):
    """Custom type hostUserAuthProtocol based on Integer32"""
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
        *(("authGuest", 0),
          ("authRadius", 1),
          ("authAD", 2),
          ("authSelfReg", 3),
          ("authADSGAP", 4),
          ("auth8021xRadius", 5))
    )


_HostUserAuthProtocol_Type.__name__ = "Integer32"
_HostUserAuthProtocol_Object = MibTableColumn
hostUserAuthProtocol = _HostUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 21),
    _HostUserAuthProtocol_Type()
)
hostUserAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostUserAuthProtocol.setStatus("current")
_HostSwitchId_Type = Integer32
_HostSwitchId_Object = MibTableColumn
hostSwitchId = _HostSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 22),
    _HostSwitchId_Type()
)
hostSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSwitchId.setStatus("current")
_HostSwitchPortId_Type = Integer32
_HostSwitchPortId_Object = MibTableColumn
hostSwitchPortId = _HostSwitchPortId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 23),
    _HostSwitchPortId_Type()
)
hostSwitchPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSwitchPortId.setStatus("current")
_HostSwitchPortGroupId_Type = Integer32
_HostSwitchPortGroupId_Object = MibTableColumn
hostSwitchPortGroupId = _HostSwitchPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 24),
    _HostSwitchPortGroupId_Type()
)
hostSwitchPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSwitchPortGroupId.setStatus("current")
_HostQuarantineVlanId_Type = Integer32
_HostQuarantineVlanId_Object = MibTableColumn
hostQuarantineVlanId = _HostQuarantineVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 25),
    _HostQuarantineVlanId_Type()
)
hostQuarantineVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostQuarantineVlanId.setStatus("current")
_HostProductionVlanId_Type = Integer32
_HostProductionVlanId_Object = MibTableColumn
hostProductionVlanId = _HostProductionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 26),
    _HostProductionVlanId_Type()
)
hostProductionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostProductionVlanId.setStatus("current")
_NasIpAddress_Type = IpAddress
_NasIpAddress_Object = MibTableColumn
nasIpAddress = _NasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 27),
    _NasIpAddress_Type()
)
nasIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasIpAddress.setStatus("current")
_NasGroupObjectId_Type = Integer32
_NasGroupObjectId_Object = MibTableColumn
nasGroupObjectId = _NasGroupObjectId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 28),
    _NasGroupObjectId_Type()
)
nasGroupObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasGroupObjectId.setStatus("current")
_UserGroupObjectId_Type = Integer32
_UserGroupObjectId_Object = MibTableColumn
userGroupObjectId = _UserGroupObjectId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 29),
    _UserGroupObjectId_Type()
)
userGroupObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupObjectId.setStatus("current")


class _DeviceProfileString_Type(DisplayString):
    """Custom type deviceProfileString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DeviceProfileString_Type.__name__ = "DisplayString"
_DeviceProfileString_Object = MibTableColumn
deviceProfileString = _DeviceProfileString_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 30),
    _DeviceProfileString_Type()
)
deviceProfileString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceProfileString.setStatus("current")


class _HostOperationalMode_Type(Integer32):
    """Custom type hostOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enforcement", 1),
          ("audit", 2),
          ("simulation", 3))
    )


_HostOperationalMode_Type.__name__ = "Integer32"
_HostOperationalMode_Object = MibTableColumn
hostOperationalMode = _HostOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 31),
    _HostOperationalMode_Type()
)
hostOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOperationalMode.setStatus("current")


class _HostEnforcementAction_Type(Integer32):
    """Custom type hostEnforcementAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("allow", 2),
          ("custom-enforce", 3))
    )


_HostEnforcementAction_Type.__name__ = "Integer32"
_HostEnforcementAction_Object = MibTableColumn
hostEnforcementAction = _HostEnforcementAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 32),
    _HostEnforcementAction_Type()
)
hostEnforcementAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostEnforcementAction.setStatus("current")
_FlexiblePolicyRuleId_Type = Integer32
_FlexiblePolicyRuleId_Object = MibTableColumn
flexiblePolicyRuleId = _FlexiblePolicyRuleId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 1, 1, 33),
    _FlexiblePolicyRuleId_Type()
)
flexiblePolicyRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiblePolicyRuleId.setStatus("current")
_HostConfigGrp_ObjectIdentity = ObjectIdentity
hostConfigGrp = _HostConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 2)
)


class _HostEntryAttribute_Type(Integer32):
    """Custom type hostEntryAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_HostEntryAttribute_Type.__name__ = "Integer32"
_HostEntryAttribute_Object = MibScalar
hostEntryAttribute = _HostEntryAttribute_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 2, 1),
    _HostEntryAttribute_Type()
)
hostEntryAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEntryAttribute.setStatus("current")
_HostEntryIpAddress_Type = IpAddress
_HostEntryIpAddress_Object = MibScalar
hostEntryIpAddress = _HostEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 2, 2),
    _HostEntryIpAddress_Type()
)
hostEntryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEntryIpAddress.setStatus("current")
_HostEntryMac_Type = MacAddress
_HostEntryMac_Object = MibScalar
hostEntryMac = _HostEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 2, 3),
    _HostEntryMac_Type()
)
hostEntryMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEntryMac.setStatus("current")


class _HostEntryConfig_Type(Integer32):
    """Custom type hostEntryConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("delete-host", 1),
          ("modify-naz", 2),
          ("revert-naz", 3),
          ("host-oob-to-inline", 4),
          ("host-inline-to-oob", 5))
    )


_HostEntryConfig_Type.__name__ = "Integer32"
_HostEntryConfig_Object = MibScalar
hostEntryConfig = _HostEntryConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 2, 4),
    _HostEntryConfig_Type()
)
hostEntryConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEntryConfig.setStatus("current")
_HostEntryEZId_Type = Integer32
_HostEntryEZId_Object = MibScalar
hostEntryEZId = _HostEntryEZId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 2, 5),
    _HostEntryEZId_Type()
)
hostEntryEZId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEntryEZId.setStatus("current")
_HostDataAvailabilityStatus_Type = TruthValue
_HostDataAvailabilityStatus_Object = MibScalar
hostDataAvailabilityStatus = _HostDataAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 28, 3),
    _HostDataAvailabilityStatus_Type()
)
hostDataAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDataAvailabilityStatus.setStatus("current")
_SgapGrp_ObjectIdentity = ObjectIdentity
sgapGrp = _SgapGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29)
)
_SgapConfigGrp_ObjectIdentity = ObjectIdentity
sgapConfigGrp = _SgapConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1)
)


class _SgapAuthTimeout_Type(Integer32):
    """Custom type sgapAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_SgapAuthTimeout_Type.__name__ = "Integer32"
_SgapAuthTimeout_Object = MibScalar
sgapAuthTimeout = _SgapAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 1),
    _SgapAuthTimeout_Type()
)
sgapAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgapAuthTimeout.setStatus("current")
_SgapCSRConfigGrp_ObjectIdentity = ObjectIdentity
sgapCSRConfigGrp = _SgapCSRConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2)
)


class _SgapCSRCountryName_Type(DisplayString):
    """Custom type sgapCSRCountryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SgapCSRCountryName_Type.__name__ = "DisplayString"
_SgapCSRCountryName_Object = MibScalar
sgapCSRCountryName = _SgapCSRCountryName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2, 1),
    _SgapCSRCountryName_Type()
)
sgapCSRCountryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgapCSRCountryName.setStatus("current")


class _SgapCSRStateProvince_Type(DisplayString):
    """Custom type sgapCSRStateProvince based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SgapCSRStateProvince_Type.__name__ = "DisplayString"
_SgapCSRStateProvince_Object = MibScalar
sgapCSRStateProvince = _SgapCSRStateProvince_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2, 2),
    _SgapCSRStateProvince_Type()
)
sgapCSRStateProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgapCSRStateProvince.setStatus("current")


class _SgapCSRLocality_Type(DisplayString):
    """Custom type sgapCSRLocality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SgapCSRLocality_Type.__name__ = "DisplayString"
_SgapCSRLocality_Object = MibScalar
sgapCSRLocality = _SgapCSRLocality_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2, 3),
    _SgapCSRLocality_Type()
)
sgapCSRLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgapCSRLocality.setStatus("current")


class _SgapCSRCompany_Type(DisplayString):
    """Custom type sgapCSRCompany based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SgapCSRCompany_Type.__name__ = "DisplayString"
_SgapCSRCompany_Object = MibScalar
sgapCSRCompany = _SgapCSRCompany_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2, 4),
    _SgapCSRCompany_Type()
)
sgapCSRCompany.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgapCSRCompany.setStatus("current")


class _SgapCSROrganizationalUnit_Type(DisplayString):
    """Custom type sgapCSROrganizationalUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SgapCSROrganizationalUnit_Type.__name__ = "DisplayString"
_SgapCSROrganizationalUnit_Object = MibScalar
sgapCSROrganizationalUnit = _SgapCSROrganizationalUnit_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2, 5),
    _SgapCSROrganizationalUnit_Type()
)
sgapCSROrganizationalUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgapCSROrganizationalUnit.setStatus("current")


class _SgapCSRCommonName_Type(DisplayString):
    """Custom type sgapCSRCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SgapCSRCommonName_Type.__name__ = "DisplayString"
_SgapCSRCommonName_Object = MibScalar
sgapCSRCommonName = _SgapCSRCommonName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2, 6),
    _SgapCSRCommonName_Type()
)
sgapCSRCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgapCSRCommonName.setStatus("current")


class _SgapCSRGenerateAction_Type(Integer32):
    """Custom type sgapCSRGenerateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("generateCSR", 1),
          ("generateSelfSigned", 2))
    )


_SgapCSRGenerateAction_Type.__name__ = "Integer32"
_SgapCSRGenerateAction_Object = MibScalar
sgapCSRGenerateAction = _SgapCSRGenerateAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2, 7),
    _SgapCSRGenerateAction_Type()
)
sgapCSRGenerateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgapCSRGenerateAction.setStatus("current")


class _SgapCSRGenerateStatus_Type(Integer32):
    """Custom type sgapCSRGenerateStatus based on Integer32"""
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
        *(("other", 0),
          ("generationInProgress", 1),
          ("generationComplete", 2),
          ("generationFailed", 3))
    )


_SgapCSRGenerateStatus_Type.__name__ = "Integer32"
_SgapCSRGenerateStatus_Object = MibScalar
sgapCSRGenerateStatus = _SgapCSRGenerateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 2, 8),
    _SgapCSRGenerateStatus_Type()
)
sgapCSRGenerateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgapCSRGenerateStatus.setStatus("current")


class _SgapCertStatus_Type(Integer32):
    """Custom type sgapCertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("certAbsent", 1),
          ("defaultCert", 2),
          ("selfsignedCert", 3),
          ("casignedCert", 4))
    )


_SgapCertStatus_Type.__name__ = "Integer32"
_SgapCertStatus_Object = MibScalar
sgapCertStatus = _SgapCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 29, 1, 3),
    _SgapCertStatus_Type()
)
sgapCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgapCertStatus.setStatus("current")
_AlarmAndTrendsGrp_ObjectIdentity = ObjectIdentity
alarmAndTrendsGrp = _AlarmAndTrendsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30)
)
_SensorPerfAlertGrp_ObjectIdentity = ObjectIdentity
sensorPerfAlertGrp = _SensorPerfAlertGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 1)
)
_SensorPerfAlertEnable_Type = TruthValue
_SensorPerfAlertEnable_Object = MibScalar
sensorPerfAlertEnable = _SensorPerfAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 1, 1),
    _SensorPerfAlertEnable_Type()
)
sensorPerfAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorPerfAlertEnable.setStatus("current")


class _SensorPerfAlertDuration_Type(Integer32):
    """Custom type sensorPerfAlertDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SensorPerfAlertDuration_Type.__name__ = "Integer32"
_SensorPerfAlertDuration_Object = MibScalar
sensorPerfAlertDuration = _SensorPerfAlertDuration_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 1, 2),
    _SensorPerfAlertDuration_Type()
)
sensorPerfAlertDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorPerfAlertDuration.setStatus("current")
_SensorPerfAlertParameters_Type = OctetString
_SensorPerfAlertParameters_Object = MibScalar
sensorPerfAlertParameters = _SensorPerfAlertParameters_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 1, 3),
    _SensorPerfAlertParameters_Type()
)
sensorPerfAlertParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorPerfAlertParameters.setStatus("current")
_AlarmConfigGrp_ObjectIdentity = ObjectIdentity
alarmConfigGrp = _AlarmConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2)
)
_AlarmStatus_Type = TruthValue
_AlarmStatus_Object = MibScalar
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 1),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("current")


class _AlarmDeleteAllEntries_Type(Integer32):
    """Custom type alarmDeleteAllEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_AlarmDeleteAllEntries_Type.__name__ = "Integer32"
_AlarmDeleteAllEntries_Object = MibScalar
alarmDeleteAllEntries = _AlarmDeleteAllEntries_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 2),
    _AlarmDeleteAllEntries_Type()
)
alarmDeleteAllEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmDeleteAllEntries.setStatus("current")


class _AlarmDuration_Type(Integer32):
    """Custom type alarmDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlarmDuration_Type.__name__ = "Integer32"
_AlarmDuration_Object = MibScalar
alarmDuration = _AlarmDuration_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 3),
    _AlarmDuration_Type()
)
alarmDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmDuration.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1)
)
alarmEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
_AlarmIndex_Type = Integer32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")


class _AlarmSampleType_Type(Integer32):
    """Custom type alarmSampleType based on Integer32"""
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
        *(("cpu-utilization-abs", 0),
          ("tcpudp-flows", 1),
          ("sensor-throughput-delta", 2),
          ("mon-port-throughput-delta", 3),
          ("sensor-l2-error-drop-delta", 4),
          ("sensor-l3-l4-error-drop-delta", 5),
          ("system-memory", 6),
          ("packet-buffers", 7),
          ("decrypted-ssl-flows", 8))
    )


_AlarmSampleType_Type.__name__ = "Integer32"
_AlarmSampleType_Object = MibTableColumn
alarmSampleType = _AlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1, 2),
    _AlarmSampleType_Type()
)
alarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSampleType.setStatus("current")


class _AlarmSampleTypeIndexBitmap_Type(OctetString):
    """Custom type alarmSampleTypeIndexBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlarmSampleTypeIndexBitmap_Type.__name__ = "OctetString"
_AlarmSampleTypeIndexBitmap_Object = MibTableColumn
alarmSampleTypeIndexBitmap = _AlarmSampleTypeIndexBitmap_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1, 3),
    _AlarmSampleTypeIndexBitmap_Type()
)
alarmSampleTypeIndexBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSampleTypeIndexBitmap.setStatus("current")


class _AlarmSampleTypeDesc_Type(DisplayString):
    """Custom type alarmSampleTypeDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlarmSampleTypeDesc_Type.__name__ = "DisplayString"
_AlarmSampleTypeDesc_Object = MibTableColumn
alarmSampleTypeDesc = _AlarmSampleTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1, 4),
    _AlarmSampleTypeDesc_Type()
)
alarmSampleTypeDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSampleTypeDesc.setStatus("current")
_AlarmRaisingThreshold_Type = Unsigned32
_AlarmRaisingThreshold_Object = MibTableColumn
alarmRaisingThreshold = _AlarmRaisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1, 5),
    _AlarmRaisingThreshold_Type()
)
alarmRaisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRaisingThreshold.setStatus("current")
_AlarmFallingThreshold_Type = Unsigned32
_AlarmFallingThreshold_Object = MibTableColumn
alarmFallingThreshold = _AlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1, 6),
    _AlarmFallingThreshold_Type()
)
alarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFallingThreshold.setStatus("current")


class _AlarmStartupType_Type(Integer32):
    """Custom type alarmStartupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("raising", 1),
          ("falling", 2),
          ("both", 3))
    )


_AlarmStartupType_Type.__name__ = "Integer32"
_AlarmStartupType_Object = MibTableColumn
alarmStartupType = _AlarmStartupType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1, 7),
    _AlarmStartupType_Type()
)
alarmStartupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmStartupType.setStatus("current")
_AlarmEntryStatus_Type = RowStatus
_AlarmEntryStatus_Object = MibTableColumn
alarmEntryStatus = _AlarmEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 4, 1, 8),
    _AlarmEntryStatus_Type()
)
alarmEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmEntryStatus.setStatus("current")
_BwSavingStatus_Type = TruthValue
_BwSavingStatus_Object = MibScalar
bwSavingStatus = _BwSavingStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 30, 2, 5),
    _BwSavingStatus_Type()
)
bwSavingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSavingStatus.setStatus("current")
_OobnacGrp_ObjectIdentity = ObjectIdentity
oobnacGrp = _OobnacGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31)
)
_OobnacSwDiscoveryGrp_ObjectIdentity = ObjectIdentity
oobnacSwDiscoveryGrp = _OobnacSwDiscoveryGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1)
)
_SwInstanceTable_Object = MibTable
swInstanceTable = _SwInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1)
)
if mibBuilder.loadTexts:
    swInstanceTable.setStatus("current")
_SwInstanceEntry_Object = MibTableRow
swInstanceEntry = _SwInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1)
)
swInstanceEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "swIdIndex"),
)
if mibBuilder.loadTexts:
    swInstanceEntry.setStatus("current")
_SwIdIndex_Type = Integer32
_SwIdIndex_Object = MibTableColumn
swIdIndex = _SwIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 1),
    _SwIdIndex_Type()
)
swIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIdIndex.setStatus("current")


class _SwDetDesc_Type(DisplayString):
    """Custom type swDetDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SwDetDesc_Type.__name__ = "DisplayString"
_SwDetDesc_Object = MibTableColumn
swDetDesc = _SwDetDesc_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 2),
    _SwDetDesc_Type()
)
swDetDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDetDesc.setStatus("current")
_SwProfileId_Type = Integer32
_SwProfileId_Object = MibTableColumn
swProfileId = _SwProfileId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 3),
    _SwProfileId_Type()
)
swProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swProfileId.setStatus("current")
_SwIPAddress_Type = IpAddress
_SwIPAddress_Object = MibTableColumn
swIPAddress = _SwIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 4),
    _SwIPAddress_Type()
)
swIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIPAddress.setStatus("current")
_SwIPV6Address_Type = Ipv6Address
_SwIPV6Address_Object = MibTableColumn
swIPV6Address = _SwIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 5),
    _SwIPV6Address_Type()
)
swIPV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIPV6Address.setStatus("current")


class _SwName_Type(DisplayString):
    """Custom type swName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SwName_Type.__name__ = "DisplayString"
_SwName_Object = MibTableColumn
swName = _SwName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 6),
    _SwName_Type()
)
swName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swName.setStatus("current")


class _SwDesc_Type(DisplayString):
    """Custom type swDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SwDesc_Type.__name__ = "DisplayString"
_SwDesc_Object = MibTableColumn
swDesc = _SwDesc_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 7),
    _SwDesc_Type()
)
swDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDesc.setStatus("current")
_SwEnable_Type = TruthValue
_SwEnable_Object = MibTableColumn
swEnable = _SwEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 8),
    _SwEnable_Type()
)
swEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEnable.setStatus("current")
_SwSNMPsupport_Type = TruthValue
_SwSNMPsupport_Object = MibTableColumn
swSNMPsupport = _SwSNMPsupport_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 9),
    _SwSNMPsupport_Type()
)
swSNMPsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNMPsupport.setStatus("current")


class _SwSnmpVerSupport_Type(Integer32):
    """Custom type swSnmpVerSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2", 2),
          ("snmpv3", 3))
    )


_SwSnmpVerSupport_Type.__name__ = "Integer32"
_SwSnmpVerSupport_Object = MibTableColumn
swSnmpVerSupport = _SwSnmpVerSupport_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 10),
    _SwSnmpVerSupport_Type()
)
swSnmpVerSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSnmpVerSupport.setStatus("current")


class _SwREADCommunityStr_Type(DisplayString):
    """Custom type swREADCommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwREADCommunityStr_Type.__name__ = "DisplayString"
_SwREADCommunityStr_Object = MibTableColumn
swREADCommunityStr = _SwREADCommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 11),
    _SwREADCommunityStr_Type()
)
swREADCommunityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swREADCommunityStr.setStatus("current")


class _SwWRITECommunityStr_Type(DisplayString):
    """Custom type swWRITECommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwWRITECommunityStr_Type.__name__ = "DisplayString"
_SwWRITECommunityStr_Object = MibTableColumn
swWRITECommunityStr = _SwWRITECommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 12),
    _SwWRITECommunityStr_Type()
)
swWRITECommunityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWRITECommunityStr.setStatus("current")


class _SwTRAPCommunityStr_Type(DisplayString):
    """Custom type swTRAPCommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwTRAPCommunityStr_Type.__name__ = "DisplayString"
_SwTRAPCommunityStr_Object = MibTableColumn
swTRAPCommunityStr = _SwTRAPCommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 13),
    _SwTRAPCommunityStr_Type()
)
swTRAPCommunityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTRAPCommunityStr.setStatus("current")
_SwSNMPPort_Type = Integer32
_SwSNMPPort_Object = MibTableColumn
swSNMPPort = _SwSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 14),
    _SwSNMPPort_Type()
)
swSNMPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNMPPort.setStatus("current")


class _SwV3UserName_Type(DisplayString):
    """Custom type swV3UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwV3UserName_Type.__name__ = "DisplayString"
_SwV3UserName_Object = MibTableColumn
swV3UserName = _SwV3UserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 15),
    _SwV3UserName_Type()
)
swV3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swV3UserName.setStatus("current")


class _SwV3SecurityLevel_Type(Integer32):
    """Custom type swV3SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_SwV3SecurityLevel_Type.__name__ = "Integer32"
_SwV3SecurityLevel_Object = MibTableColumn
swV3SecurityLevel = _SwV3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 16),
    _SwV3SecurityLevel_Type()
)
swV3SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swV3SecurityLevel.setStatus("current")


class _SwV3AuthProtocol_Type(Integer32):
    """Custom type swV3AuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mD5", 1),
          ("sHA", 2))
    )


_SwV3AuthProtocol_Type.__name__ = "Integer32"
_SwV3AuthProtocol_Object = MibTableColumn
swV3AuthProtocol = _SwV3AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 17),
    _SwV3AuthProtocol_Type()
)
swV3AuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swV3AuthProtocol.setStatus("current")


class _SwV3AuthKey_Type(DisplayString):
    """Custom type swV3AuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwV3AuthKey_Type.__name__ = "DisplayString"
_SwV3AuthKey_Object = MibTableColumn
swV3AuthKey = _SwV3AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 18),
    _SwV3AuthKey_Type()
)
swV3AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swV3AuthKey.setStatus("current")


class _SwV3EncrProtocol_Type(Integer32):
    """Custom type swV3EncrProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dES", 1),
          ("aES", 2))
    )


_SwV3EncrProtocol_Type.__name__ = "Integer32"
_SwV3EncrProtocol_Object = MibTableColumn
swV3EncrProtocol = _SwV3EncrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 19),
    _SwV3EncrProtocol_Type()
)
swV3EncrProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swV3EncrProtocol.setStatus("current")


class _SwV3EncrKey_Type(DisplayString):
    """Custom type swV3EncrKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwV3EncrKey_Type.__name__ = "DisplayString"
_SwV3EncrKey_Object = MibTableColumn
swV3EncrKey = _SwV3EncrKey_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 20),
    _SwV3EncrKey_Type()
)
swV3EncrKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swV3EncrKey.setStatus("current")
_SwCLIsupport_Type = TruthValue
_SwCLIsupport_Object = MibTableColumn
swCLIsupport = _SwCLIsupport_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 21),
    _SwCLIsupport_Type()
)
swCLIsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCLIsupport.setStatus("current")


class _SwCLINwProtocol_Type(Integer32):
    """Custom type swCLINwProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2))
    )


_SwCLINwProtocol_Type.__name__ = "Integer32"
_SwCLINwProtocol_Object = MibTableColumn
swCLINwProtocol = _SwCLINwProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 22),
    _SwCLINwProtocol_Type()
)
swCLINwProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCLINwProtocol.setStatus("current")


class _SwCLIUserName_Type(DisplayString):
    """Custom type swCLIUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwCLIUserName_Type.__name__ = "DisplayString"
_SwCLIUserName_Object = MibTableColumn
swCLIUserName = _SwCLIUserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 23),
    _SwCLIUserName_Type()
)
swCLIUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCLIUserName.setStatus("current")


class _SwCLIPwd_Type(DisplayString):
    """Custom type swCLIPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwCLIPwd_Type.__name__ = "DisplayString"
_SwCLIPwd_Object = MibTableColumn
swCLIPwd = _SwCLIPwd_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 24),
    _SwCLIPwd_Type()
)
swCLIPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCLIPwd.setStatus("current")


class _SwCLIEnablePwd_Type(DisplayString):
    """Custom type swCLIEnablePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwCLIEnablePwd_Type.__name__ = "DisplayString"
_SwCLIEnablePwd_Object = MibTableColumn
swCLIEnablePwd = _SwCLIEnablePwd_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 25),
    _SwCLIEnablePwd_Type()
)
swCLIEnablePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCLIEnablePwd.setStatus("current")
_SwCLIAutoSaveConfig_Type = TruthValue
_SwCLIAutoSaveConfig_Object = MibTableColumn
swCLIAutoSaveConfig = _SwCLIAutoSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 26),
    _SwCLIAutoSaveConfig_Type()
)
swCLIAutoSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCLIAutoSaveConfig.setStatus("current")
_SwRadiusSupport_Type = TruthValue
_SwRadiusSupport_Object = MibTableColumn
swRadiusSupport = _SwRadiusSupport_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 27),
    _SwRadiusSupport_Type()
)
swRadiusSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusSupport.setStatus("current")


class _SwRadiusSharedSecret_Type(DisplayString):
    """Custom type swRadiusSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwRadiusSharedSecret_Type.__name__ = "DisplayString"
_SwRadiusSharedSecret_Object = MibTableColumn
swRadiusSharedSecret = _SwRadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 28),
    _SwRadiusSharedSecret_Type()
)
swRadiusSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusSharedSecret.setStatus("current")


class _SwPlaceHolderVlan_Type(DisplayString):
    """Custom type swPlaceHolderVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwPlaceHolderVlan_Type.__name__ = "DisplayString"
_SwPlaceHolderVlan_Object = MibTableColumn
swPlaceHolderVlan = _SwPlaceHolderVlan_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 29),
    _SwPlaceHolderVlan_Type()
)
swPlaceHolderVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPlaceHolderVlan.setStatus("current")
_SwUseDefaultQVlanPool_Type = TruthValue
_SwUseDefaultQVlanPool_Object = MibTableColumn
swUseDefaultQVlanPool = _SwUseDefaultQVlanPool_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 30),
    _SwUseDefaultQVlanPool_Type()
)
swUseDefaultQVlanPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUseDefaultQVlanPool.setStatus("current")


class _SwQVlanPoolRange_Type(DisplayString):
    """Custom type swQVlanPoolRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SwQVlanPoolRange_Type.__name__ = "DisplayString"
_SwQVlanPoolRange_Object = MibTableColumn
swQVlanPoolRange = _SwQVlanPoolRange_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 31),
    _SwQVlanPoolRange_Type()
)
swQVlanPoolRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQVlanPoolRange.setStatus("current")
_SwDiscoverAction_Type = RowStatus
_SwDiscoverAction_Object = MibTableColumn
swDiscoverAction = _SwDiscoverAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 32),
    _SwDiscoverAction_Type()
)
swDiscoverAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDiscoverAction.setStatus("current")


class _SwCLILoginType_Type(Integer32):
    """Custom type swCLILoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userPwd", 1),
          ("pwdEnable", 2),
          ("userPwdEnable", 3))
    )


_SwCLILoginType_Type.__name__ = "Integer32"
_SwCLILoginType_Object = MibTableColumn
swCLILoginType = _SwCLILoginType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 33),
    _SwCLILoginType_Type()
)
swCLILoginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCLILoginType.setStatus("current")
_SwAuthMacAddRadSrvOption_Type = TruthValue
_SwAuthMacAddRadSrvOption_Object = MibTableColumn
swAuthMacAddRadSrvOption = _SwAuthMacAddRadSrvOption_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 34),
    _SwAuthMacAddRadSrvOption_Type()
)
swAuthMacAddRadSrvOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthMacAddRadSrvOption.setStatus("current")


class _SwActionStatus_Type(Integer32):
    """Custom type swActionStatus based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("in-deletion-mode", 3),
          ("in-addition-mode", 4))
    )


_SwActionStatus_Type.__name__ = "Integer32"
_SwActionStatus_Object = MibTableColumn
swActionStatus = _SwActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 35),
    _SwActionStatus_Type()
)
swActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActionStatus.setStatus("current")
_SwPortDefaultVlan_Type = Integer32
_SwPortDefaultVlan_Object = MibTableColumn
swPortDefaultVlan = _SwPortDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 36),
    _SwPortDefaultVlan_Type()
)
swPortDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortDefaultVlan.setStatus("current")


class _SwActionStatusTime_Type(Integer32):
    """Custom type swActionStatusTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SwActionStatusTime_Type.__name__ = "Integer32"
_SwActionStatusTime_Object = MibTableColumn
swActionStatusTime = _SwActionStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 1, 1, 37),
    _SwActionStatusTime_Type()
)
swActionStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActionStatusTime.setStatus("current")
_SwIpAddress_Type = IpAddress
_SwIpAddress_Object = MibScalar
swIpAddress = _SwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 2),
    _SwIpAddress_Type()
)
swIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpAddress.setStatus("current")
_SwIpV6Address_Type = Ipv6Address
_SwIpV6Address_Object = MibScalar
swIpV6Address = _SwIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 3),
    _SwIpV6Address_Type()
)
swIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpV6Address.setStatus("current")


class _ReadCommunityString_Type(DisplayString):
    """Custom type readCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ReadCommunityString_Type.__name__ = "DisplayString"
_ReadCommunityString_Object = MibScalar
readCommunityString = _ReadCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 4),
    _ReadCommunityString_Type()
)
readCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readCommunityString.setStatus("current")
_SnmpPort_Type = Integer32
_SnmpPort_Object = MibScalar
snmpPort = _SnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 5),
    _SnmpPort_Type()
)
snmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPort.setStatus("current")


class _SnmpVerSupport_Type(Integer32):
    """Custom type snmpVerSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2", 2),
          ("snmpv3", 3))
    )


_SnmpVerSupport_Type.__name__ = "Integer32"
_SnmpVerSupport_Object = MibScalar
snmpVerSupport = _SnmpVerSupport_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 6),
    _SnmpVerSupport_Type()
)
snmpVerSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpVerSupport.setStatus("current")


class _WriteCommunityStr_Type(DisplayString):
    """Custom type writeCommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_WriteCommunityStr_Type.__name__ = "DisplayString"
_WriteCommunityStr_Object = MibScalar
writeCommunityStr = _WriteCommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 7),
    _WriteCommunityStr_Type()
)
writeCommunityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writeCommunityStr.setStatus("current")


class _TrapCommunityStr_Type(DisplayString):
    """Custom type trapCommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TrapCommunityStr_Type.__name__ = "DisplayString"
_TrapCommunityStr_Object = MibScalar
trapCommunityStr = _TrapCommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 8),
    _TrapCommunityStr_Type()
)
trapCommunityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunityStr.setStatus("current")


class _V3UserName_Type(DisplayString):
    """Custom type v3UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_V3UserName_Type.__name__ = "DisplayString"
_V3UserName_Object = MibScalar
v3UserName = _V3UserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 9),
    _V3UserName_Type()
)
v3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3UserName.setStatus("current")


class _V3SecurityLevel_Type(Integer32):
    """Custom type v3SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_V3SecurityLevel_Type.__name__ = "Integer32"
_V3SecurityLevel_Object = MibScalar
v3SecurityLevel = _V3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 10),
    _V3SecurityLevel_Type()
)
v3SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3SecurityLevel.setStatus("current")


class _V3AuthProtocol_Type(Integer32):
    """Custom type v3AuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mD5", 1),
          ("sHA", 2))
    )


_V3AuthProtocol_Type.__name__ = "Integer32"
_V3AuthProtocol_Object = MibScalar
v3AuthProtocol = _V3AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 11),
    _V3AuthProtocol_Type()
)
v3AuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3AuthProtocol.setStatus("current")


class _V3AuthKey_Type(DisplayString):
    """Custom type v3AuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_V3AuthKey_Type.__name__ = "DisplayString"
_V3AuthKey_Object = MibScalar
v3AuthKey = _V3AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 12),
    _V3AuthKey_Type()
)
v3AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3AuthKey.setStatus("current")


class _V3EncrProtocol_Type(Integer32):
    """Custom type v3EncrProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dES", 1),
          ("aES", 2))
    )


_V3EncrProtocol_Type.__name__ = "Integer32"
_V3EncrProtocol_Object = MibScalar
v3EncrProtocol = _V3EncrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 13),
    _V3EncrProtocol_Type()
)
v3EncrProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3EncrProtocol.setStatus("current")


class _V3EncrKey_Type(DisplayString):
    """Custom type v3EncrKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_V3EncrKey_Type.__name__ = "DisplayString"
_V3EncrKey_Object = MibScalar
v3EncrKey = _V3EncrKey_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 14),
    _V3EncrKey_Type()
)
v3EncrKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3EncrKey.setStatus("current")


class _CliNwProtocol_Type(Integer32):
    """Custom type cliNwProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2))
    )


_CliNwProtocol_Type.__name__ = "Integer32"
_CliNwProtocol_Object = MibScalar
cliNwProtocol = _CliNwProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 15),
    _CliNwProtocol_Type()
)
cliNwProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliNwProtocol.setStatus("current")


class _CliUserName_Type(DisplayString):
    """Custom type cliUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CliUserName_Type.__name__ = "DisplayString"
_CliUserName_Object = MibScalar
cliUserName = _CliUserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 16),
    _CliUserName_Type()
)
cliUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliUserName.setStatus("current")


class _CliPwd_Type(DisplayString):
    """Custom type cliPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CliPwd_Type.__name__ = "DisplayString"
_CliPwd_Object = MibScalar
cliPwd = _CliPwd_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 17),
    _CliPwd_Type()
)
cliPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliPwd.setStatus("current")


class _CliEnablePwd_Type(DisplayString):
    """Custom type cliEnablePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CliEnablePwd_Type.__name__ = "DisplayString"
_CliEnablePwd_Object = MibScalar
cliEnablePwd = _CliEnablePwd_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 18),
    _CliEnablePwd_Type()
)
cliEnablePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliEnablePwd.setStatus("current")


class _SwQueryAction_Type(Integer32):
    """Custom type swQueryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("initialQuery", 1),
          ("testSnmp", 2),
          ("testCli", 3),
          ("deleteAllSwEntries", 4),
          ("reLearnSwitch", 5))
    )


_SwQueryAction_Type.__name__ = "Integer32"
_SwQueryAction_Object = MibScalar
swQueryAction = _SwQueryAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 19),
    _SwQueryAction_Type()
)
swQueryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQueryAction.setStatus("current")


class _CliLoginType_Type(Integer32):
    """Custom type cliLoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userPwd", 1),
          ("pwdEnable", 2),
          ("userPwdEnable", 3))
    )


_CliLoginType_Type.__name__ = "Integer32"
_CliLoginType_Object = MibScalar
cliLoginType = _CliLoginType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 20),
    _CliLoginType_Type()
)
cliLoginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliLoginType.setStatus("current")
_ProfileId_Type = Integer32
_ProfileId_Object = MibScalar
profileId = _ProfileId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 21),
    _ProfileId_Type()
)
profileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileId.setStatus("current")
_SwitchId_Type = Integer32
_SwitchId_Object = MibScalar
switchId = _SwitchId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 1, 22),
    _SwitchId_Type()
)
switchId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchId.setStatus("current")
_OobnacAllSwitchesGrp_ObjectIdentity = ObjectIdentity
oobnacAllSwitchesGrp = _OobnacAllSwitchesGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 2)
)


class _OobnDefaultQvlanPool_Type(DisplayString):
    """Custom type oobnDefaultQvlanPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OobnDefaultQvlanPool_Type.__name__ = "DisplayString"
_OobnDefaultQvlanPool_Object = MibScalar
oobnDefaultQvlanPool = _OobnDefaultQvlanPool_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 2, 1),
    _OobnDefaultQvlanPool_Type()
)
oobnDefaultQvlanPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnDefaultQvlanPool.setStatus("current")
_OobnacRadNumRetries_Type = Integer32
_OobnacRadNumRetries_Object = MibScalar
oobnacRadNumRetries = _OobnacRadNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 2, 2),
    _OobnacRadNumRetries_Type()
)
oobnacRadNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacRadNumRetries.setStatus("current")
_OobnacRadRespTimeOut_Type = Integer32
_OobnacRadRespTimeOut_Object = MibScalar
oobnacRadRespTimeOut = _OobnacRadRespTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 2, 3),
    _OobnacRadRespTimeOut_Type()
)
oobnacRadRespTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacRadRespTimeOut.setStatus("current")
_OobnacFailoverGrp_ObjectIdentity = ObjectIdentity
oobnacFailoverGrp = _OobnacFailoverGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3)
)
_OobnacFloatingIpAddress_Type = IpAddress
_OobnacFloatingIpAddress_Object = MibScalar
oobnacFloatingIpAddress = _OobnacFloatingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 1),
    _OobnacFloatingIpAddress_Type()
)
oobnacFloatingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacFloatingIpAddress.setStatus("current")
_OobnacFloatingIpv6Address_Type = Ipv6Address
_OobnacFloatingIpv6Address_Object = MibScalar
oobnacFloatingIpv6Address = _OobnacFloatingIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 2),
    _OobnacFloatingIpv6Address_Type()
)
oobnacFloatingIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacFloatingIpv6Address.setStatus("current")
_OobnacFloatingNetMask_Type = Integer32
_OobnacFloatingNetMask_Object = MibScalar
oobnacFloatingNetMask = _OobnacFloatingNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 3),
    _OobnacFloatingNetMask_Type()
)
oobnacFloatingNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacFloatingNetMask.setStatus("current")
_OobnacFloatingv6NetMask_Type = Integer32
_OobnacFloatingv6NetMask_Object = MibScalar
oobnacFloatingv6NetMask = _OobnacFloatingv6NetMask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 4),
    _OobnacFloatingv6NetMask_Type()
)
oobnacFloatingv6NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacFloatingv6NetMask.setStatus("current")
_OobnacFloatingGatewayIpAddress_Type = IpAddress
_OobnacFloatingGatewayIpAddress_Object = MibScalar
oobnacFloatingGatewayIpAddress = _OobnacFloatingGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 5),
    _OobnacFloatingGatewayIpAddress_Type()
)
oobnacFloatingGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacFloatingGatewayIpAddress.setStatus("current")
_OobnacFloatingGatewayIpv6Address_Type = Ipv6Address
_OobnacFloatingGatewayIpv6Address_Object = MibScalar
oobnacFloatingGatewayIpv6Address = _OobnacFloatingGatewayIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 6),
    _OobnacFloatingGatewayIpv6Address_Type()
)
oobnacFloatingGatewayIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacFloatingGatewayIpv6Address.setStatus("current")
_OobnacPeerIpAddress_Type = IpAddress
_OobnacPeerIpAddress_Object = MibScalar
oobnacPeerIpAddress = _OobnacPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 7),
    _OobnacPeerIpAddress_Type()
)
oobnacPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacPeerIpAddress.setStatus("current")
_OobnacPeerIpv6Address_Type = Ipv6Address
_OobnacPeerIpv6Address_Object = MibScalar
oobnacPeerIpv6Address = _OobnacPeerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 8),
    _OobnacPeerIpv6Address_Type()
)
oobnacPeerIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oobnacPeerIpv6Address.setStatus("current")


class _OobnacFailoverSensorStatus_Type(Integer32):
    """Custom type oobnacFailoverSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 0),
          ("standby", 1),
          ("active", 2))
    )


_OobnacFailoverSensorStatus_Type.__name__ = "Integer32"
_OobnacFailoverSensorStatus_Object = MibScalar
oobnacFailoverSensorStatus = _OobnacFailoverSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 31, 3, 9),
    _OobnacFailoverSensorStatus_Type()
)
oobnacFailoverSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oobnacFailoverSensorStatus.setStatus("current")
_MalwareGrp_ObjectIdentity = ObjectIdentity
malwareGrp = _MalwareGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32)
)
_MalwarePriDNSServerIp_Type = IpAddress
_MalwarePriDNSServerIp_Object = MibScalar
malwarePriDNSServerIp = _MalwarePriDNSServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 1),
    _MalwarePriDNSServerIp_Type()
)
malwarePriDNSServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    malwarePriDNSServerIp.setStatus("obsolete")
_MalwareSecDNSServerIp_Type = IpAddress
_MalwareSecDNSServerIp_Object = MibScalar
malwareSecDNSServerIp = _MalwareSecDNSServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 2),
    _MalwareSecDNSServerIp_Type()
)
malwareSecDNSServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    malwareSecDNSServerIp.setStatus("obsolete")
_MalwarePriDNSServerIpV6_Type = Ipv6Address
_MalwarePriDNSServerIpV6_Object = MibScalar
malwarePriDNSServerIpV6 = _MalwarePriDNSServerIpV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 3),
    _MalwarePriDNSServerIpV6_Type()
)
malwarePriDNSServerIpV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    malwarePriDNSServerIpV6.setStatus("obsolete")
_MalwareSecDNSServerIpV6_Type = Ipv6Address
_MalwareSecDNSServerIpV6_Object = MibScalar
malwareSecDNSServerIpV6 = _MalwareSecDNSServerIpV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 4),
    _MalwareSecDNSServerIpV6_Type()
)
malwareSecDNSServerIpV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    malwareSecDNSServerIpV6.setStatus("obsolete")


class _MalwareRiskLevel_Type(Integer32):
    """Custom type malwareRiskLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("veryLow", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4),
          ("veryHigh", 5))
    )


_MalwareRiskLevel_Type.__name__ = "Integer32"
_MalwareRiskLevel_Object = MibScalar
malwareRiskLevel = _MalwareRiskLevel_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 5),
    _MalwareRiskLevel_Type()
)
malwareRiskLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    malwareRiskLevel.setStatus("current")


class _MalwareArtemisDetectionMode_Type(Integer32):
    """Custom type malwareArtemisDetectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alertOnly", 1),
          ("alertAndBlock", 2),
          ("alertBlockAndTCP-Reset", 3))
    )


_MalwareArtemisDetectionMode_Type.__name__ = "Integer32"
_MalwareArtemisDetectionMode_Object = MibScalar
malwareArtemisDetectionMode = _MalwareArtemisDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 6),
    _MalwareArtemisDetectionMode_Type()
)
malwareArtemisDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    malwareArtemisDetectionMode.setStatus("current")


class _MalwareUDFDetectionMode_Type(Integer32):
    """Custom type malwareUDFDetectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alertOnly", 1),
          ("alertAndBlock", 2),
          ("alertBlockAndTCP-Reset", 3))
    )


_MalwareUDFDetectionMode_Type.__name__ = "Integer32"
_MalwareUDFDetectionMode_Object = MibScalar
malwareUDFDetectionMode = _MalwareUDFDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 7),
    _MalwareUDFDetectionMode_Type()
)
malwareUDFDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    malwareUDFDetectionMode.setStatus("current")
_GamEngSensorCfgGrp_ObjectIdentity = ObjectIdentity
gamEngSensorCfgGrp = _GamEngSensorCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8)
)
_GamEngSensorAutoUpdateConfig_Type = TruthValue
_GamEngSensorAutoUpdateConfig_Object = MibScalar
gamEngSensorAutoUpdateConfig = _GamEngSensorAutoUpdateConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8, 1),
    _GamEngSensorAutoUpdateConfig_Type()
)
gamEngSensorAutoUpdateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamEngSensorAutoUpdateConfig.setStatus("current")


class _GamEngSensorAutoUpdateInterval_Type(Integer32):
    """Custom type gamEngSensorAutoUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 1440),
    )


_GamEngSensorAutoUpdateInterval_Type.__name__ = "Integer32"
_GamEngSensorAutoUpdateInterval_Object = MibScalar
gamEngSensorAutoUpdateInterval = _GamEngSensorAutoUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8, 2),
    _GamEngSensorAutoUpdateInterval_Type()
)
gamEngSensorAutoUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamEngSensorAutoUpdateInterval.setStatus("current")


class _GamEngVer_Type(DisplayString):
    """Custom type gamEngVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_GamEngVer_Type.__name__ = "DisplayString"
_GamEngVer_Object = MibScalar
gamEngVer = _GamEngVer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8, 3),
    _GamEngVer_Type()
)
gamEngVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamEngVer.setStatus("current")


class _GamDatVer_Type(DisplayString):
    """Custom type gamDatVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_GamDatVer_Type.__name__ = "DisplayString"
_GamDatVer_Object = MibScalar
gamDatVer = _GamDatVer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8, 4),
    _GamDatVer_Type()
)
gamDatVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamDatVer.setStatus("current")


class _AvEngVer_Type(DisplayString):
    """Custom type avEngVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_AvEngVer_Type.__name__ = "DisplayString"
_AvEngVer_Object = MibScalar
avEngVer = _AvEngVer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8, 5),
    _AvEngVer_Type()
)
avEngVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEngVer.setStatus("current")


class _AvDatVer_Type(DisplayString):
    """Custom type avDatVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_AvDatVer_Type.__name__ = "DisplayString"
_AvDatVer_Object = MibScalar
avDatVer = _AvDatVer_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8, 6),
    _AvDatVer_Type()
)
avDatVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avDatVer.setStatus("current")
_GamEngUpdatedTime_Type = Unsigned32
_GamEngUpdatedTime_Object = MibScalar
gamEngUpdatedTime = _GamEngUpdatedTime_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8, 7),
    _GamEngUpdatedTime_Type()
)
gamEngUpdatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamEngUpdatedTime.setStatus("current")


class _GamManualFullUpdateFileUploadStatus_Type(Integer32):
    """Custom type gamManualFullUpdateFileUploadStatus based on Integer32"""
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
        *(("readyForGAMUpdate", 1),
          ("gAMUpdateTransferInProgress", 2),
          ("gAMUpdateTransferError", 3),
          ("gAMUpdateQueued", 4),
          ("applyingGAMUpdate", 5),
          ("gAMUpdateCompleted", 6),
          ("gAMUpdateError", 7))
    )


_GamManualFullUpdateFileUploadStatus_Type.__name__ = "Integer32"
_GamManualFullUpdateFileUploadStatus_Object = MibScalar
gamManualFullUpdateFileUploadStatus = _GamManualFullUpdateFileUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 32, 8, 8),
    _GamManualFullUpdateFileUploadStatus_Type()
)
gamManualFullUpdateFileUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamManualFullUpdateFileUploadStatus.setStatus("current")
_MiscCfgGrp_ObjectIdentity = ObjectIdentity
miscCfgGrp = _MiscCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33)
)


class _JumboframeParsingConfig_Type(Integer32):
    """Custom type jumboframeParsingConfig based on Integer32"""
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


_JumboframeParsingConfig_Type.__name__ = "Integer32"
_JumboframeParsingConfig_Object = MibScalar
jumboframeParsingConfig = _JumboframeParsingConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 1),
    _JumboframeParsingConfig_Type()
)
jumboframeParsingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jumboframeParsingConfig.setStatus("current")
_CurrentJumboframeParsingStatus_Type = Integer32
_CurrentJumboframeParsingStatus_Object = MibScalar
currentJumboframeParsingStatus = _CurrentJumboframeParsingStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 2),
    _CurrentJumboframeParsingStatus_Type()
)
currentJumboframeParsingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentJumboframeParsingStatus.setStatus("current")
_AppIdStatsConfigStatus_Type = TruthValue
_AppIdStatsConfigStatus_Object = MibScalar
appIdStatsConfigStatus = _AppIdStatsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 3),
    _AppIdStatsConfigStatus_Type()
)
appIdStatsConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appIdStatsConfigStatus.setStatus("current")


class _HitlessRebootStatus_Type(Integer32):
    """Custom type hitlessRebootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notavailable", 2))
    )


_HitlessRebootStatus_Type.__name__ = "Integer32"
_HitlessRebootStatus_Object = MibScalar
hitlessRebootStatus = _HitlessRebootStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 4),
    _HitlessRebootStatus_Type()
)
hitlessRebootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hitlessRebootStatus.setStatus("current")


class _ExistingGeoDBFilename_Type(OctetString):
    """Custom type existingGeoDBFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExistingGeoDBFilename_Type.__name__ = "OctetString"
_ExistingGeoDBFilename_Object = MibScalar
existingGeoDBFilename = _ExistingGeoDBFilename_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 5),
    _ExistingGeoDBFilename_Type()
)
existingGeoDBFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    existingGeoDBFilename.setStatus("current")


class _NsmTrackUserLoggingStatus_Type(Integer32):
    """Custom type nsmTrackUserLoggingStatus based on Integer32"""
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


_NsmTrackUserLoggingStatus_Type.__name__ = "Integer32"
_NsmTrackUserLoggingStatus_Object = MibScalar
nsmTrackUserLoggingStatus = _NsmTrackUserLoggingStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 6),
    _NsmTrackUserLoggingStatus_Type()
)
nsmTrackUserLoggingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsmTrackUserLoggingStatus.setStatus("current")
_AccelerateFTPInboundConfig_Type = TruthValue
_AccelerateFTPInboundConfig_Object = MibScalar
accelerateFTPInboundConfig = _AccelerateFTPInboundConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 7),
    _AccelerateFTPInboundConfig_Type()
)
accelerateFTPInboundConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accelerateFTPInboundConfig.setStatus("current")
_AccelerateFTPOutboundConfig_Type = TruthValue
_AccelerateFTPOutboundConfig_Object = MibScalar
accelerateFTPOutboundConfig = _AccelerateFTPOutboundConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 8),
    _AccelerateFTPOutboundConfig_Type()
)
accelerateFTPOutboundConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accelerateFTPOutboundConfig.setStatus("current")
_ParseTunnellingConfig_Type = TruthValue
_ParseTunnellingConfig_Object = MibScalar
parseTunnellingConfig = _ParseTunnellingConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 9),
    _ParseTunnellingConfig_Type()
)
parseTunnellingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parseTunnellingConfig.setStatus("current")
_Prev256ByteLoggingConfig_Type = TruthValue
_Prev256ByteLoggingConfig_Object = MibScalar
prev256ByteLoggingConfig = _Prev256ByteLoggingConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 10),
    _Prev256ByteLoggingConfig_Type()
)
prev256ByteLoggingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prev256ByteLoggingConfig.setStatus("current")
_CliAuditLoggingConfig_Type = TruthValue
_CliAuditLoggingConfig_Object = MibScalar
cliAuditLoggingConfig = _CliAuditLoggingConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 11),
    _CliAuditLoggingConfig_Type()
)
cliAuditLoggingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliAuditLoggingConfig.setStatus("current")


class _SnortRuleEngineConfig_Type(Integer32):
    """Custom type snortRuleEngineConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("traditional", 1),
          ("nextGeneration", 2))
    )


_SnortRuleEngineConfig_Type.__name__ = "Integer32"
_SnortRuleEngineConfig_Object = MibScalar
snortRuleEngineConfig = _SnortRuleEngineConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 12),
    _SnortRuleEngineConfig_Type()
)
snortRuleEngineConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snortRuleEngineConfig.setStatus("current")
_CurrentSnortRuleEngineStatus_Type = Integer32
_CurrentSnortRuleEngineStatus_Object = MibScalar
currentSnortRuleEngineStatus = _CurrentSnortRuleEngineStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 13),
    _CurrentSnortRuleEngineStatus_Type()
)
currentSnortRuleEngineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSnortRuleEngineStatus.setStatus("current")
_InsightsTelemetryConfig_Type = TruthValue
_InsightsTelemetryConfig_Object = MibScalar
insightsTelemetryConfig = _InsightsTelemetryConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 33, 14),
    _InsightsTelemetryConfig_Type()
)
insightsTelemetryConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insightsTelemetryConfig.setStatus("current")
_Layer2FwdGrp_ObjectIdentity = ObjectIdentity
layer2FwdGrp = _Layer2FwdGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34)
)
_Layer2FwdCfgGrp_ObjectIdentity = ObjectIdentity
layer2FwdCfgGrp = _Layer2FwdCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 1)
)


class _Layer2FwdType_Type(Integer32):
    """Custom type layer2FwdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("vlan", 3),
          ("all", 4),
          ("ip", 5))
    )


_Layer2FwdType_Type.__name__ = "Integer32"
_Layer2FwdType_Object = MibScalar
layer2FwdType = _Layer2FwdType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 1, 1),
    _Layer2FwdType_Type()
)
layer2FwdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer2FwdType.setStatus("current")
_Layer2IntfPort_Type = TrellixPortLinearIndex
_Layer2IntfPort_Object = MibScalar
layer2IntfPort = _Layer2IntfPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 1, 2),
    _Layer2IntfPort_Type()
)
layer2IntfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer2IntfPort.setStatus("current")


class _Layer2FwdAction_Type(Integer32):
    """Custom type layer2FwdAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("clearAll", 3))
    )


_Layer2FwdAction_Type.__name__ = "Integer32"
_Layer2FwdAction_Object = MibScalar
layer2FwdAction = _Layer2FwdAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 1, 3),
    _Layer2FwdAction_Type()
)
layer2FwdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer2FwdAction.setStatus("current")
_Layer2FwdBeginId_Type = Integer32
_Layer2FwdBeginId_Object = MibScalar
layer2FwdBeginId = _Layer2FwdBeginId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 1, 4),
    _Layer2FwdBeginId_Type()
)
layer2FwdBeginId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer2FwdBeginId.setStatus("current")
_Layer2FwdEndId_Type = Integer32
_Layer2FwdEndId_Object = MibScalar
layer2FwdEndId = _Layer2FwdEndId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 1, 5),
    _Layer2FwdEndId_Type()
)
layer2FwdEndId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer2FwdEndId.setStatus("current")


class _Layer2FwdConfig_Type(Integer32):
    """Custom type layer2FwdConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Layer2FwdConfig_Type.__name__ = "Integer32"
_Layer2FwdConfig_Object = MibScalar
layer2FwdConfig = _Layer2FwdConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 1, 6),
    _Layer2FwdConfig_Type()
)
layer2FwdConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer2FwdConfig.setStatus("current")
_Layer2FwdTCPTable_Object = MibTable
layer2FwdTCPTable = _Layer2FwdTCPTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 2)
)
if mibBuilder.loadTexts:
    layer2FwdTCPTable.setStatus("current")
_Layer2FwdTCPEntry_Object = MibTableRow
layer2FwdTCPEntry = _Layer2FwdTCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 2, 1)
)
layer2FwdTCPEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "tcpIntfPortIndex"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "tcpEntryIndex"),
)
if mibBuilder.loadTexts:
    layer2FwdTCPEntry.setStatus("current")
_TcpIntfPortIndex_Type = TrellixPortLinearIndex
_TcpIntfPortIndex_Object = MibTableColumn
tcpIntfPortIndex = _TcpIntfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 2, 1, 1),
    _TcpIntfPortIndex_Type()
)
tcpIntfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpIntfPortIndex.setStatus("current")
_TcpEntryIndex_Type = Integer32
_TcpEntryIndex_Object = MibTableColumn
tcpEntryIndex = _TcpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 2, 1, 2),
    _TcpEntryIndex_Type()
)
tcpEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpEntryIndex.setStatus("current")


class _TcpPortRange_Type(DisplayString):
    """Custom type tcpPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TcpPortRange_Type.__name__ = "DisplayString"
_TcpPortRange_Object = MibTableColumn
tcpPortRange = _TcpPortRange_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 2, 1, 3),
    _TcpPortRange_Type()
)
tcpPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpPortRange.setStatus("current")
_Layer2FwdUDPTable_Object = MibTable
layer2FwdUDPTable = _Layer2FwdUDPTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 3)
)
if mibBuilder.loadTexts:
    layer2FwdUDPTable.setStatus("current")
_Layer2FwdUDPEntry_Object = MibTableRow
layer2FwdUDPEntry = _Layer2FwdUDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 3, 1)
)
layer2FwdUDPEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "udpIntfPortIndex"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "udpEntryIndex"),
)
if mibBuilder.loadTexts:
    layer2FwdUDPEntry.setStatus("current")
_UdpIntfPortIndex_Type = TrellixPortLinearIndex
_UdpIntfPortIndex_Object = MibTableColumn
udpIntfPortIndex = _UdpIntfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 3, 1, 1),
    _UdpIntfPortIndex_Type()
)
udpIntfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpIntfPortIndex.setStatus("current")
_UdpEntryIndex_Type = Integer32
_UdpEntryIndex_Object = MibTableColumn
udpEntryIndex = _UdpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 3, 1, 2),
    _UdpEntryIndex_Type()
)
udpEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpEntryIndex.setStatus("current")


class _UdpPortRange_Type(DisplayString):
    """Custom type udpPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UdpPortRange_Type.__name__ = "DisplayString"
_UdpPortRange_Object = MibTableColumn
udpPortRange = _UdpPortRange_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 3, 1, 3),
    _UdpPortRange_Type()
)
udpPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpPortRange.setStatus("current")
_Layer2FwdVLANTable_Object = MibTable
layer2FwdVLANTable = _Layer2FwdVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 4)
)
if mibBuilder.loadTexts:
    layer2FwdVLANTable.setStatus("current")
_Layer2FwdVLANEntry_Object = MibTableRow
layer2FwdVLANEntry = _Layer2FwdVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 4, 1)
)
layer2FwdVLANEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "vlanIntfPortIndex"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "vlanEntryIndex"),
)
if mibBuilder.loadTexts:
    layer2FwdVLANEntry.setStatus("current")
_VlanIntfPortIndex_Type = TrellixPortLinearIndex
_VlanIntfPortIndex_Object = MibTableColumn
vlanIntfPortIndex = _VlanIntfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 4, 1, 1),
    _VlanIntfPortIndex_Type()
)
vlanIntfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanIntfPortIndex.setStatus("current")
_VlanEntryIndex_Type = Integer32
_VlanEntryIndex_Object = MibTableColumn
vlanEntryIndex = _VlanEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 4, 1, 2),
    _VlanEntryIndex_Type()
)
vlanEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanEntryIndex.setStatus("current")


class _VlanPortRange_Type(DisplayString):
    """Custom type vlanPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VlanPortRange_Type.__name__ = "DisplayString"
_VlanPortRange_Object = MibTableColumn
vlanPortRange = _VlanPortRange_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 4, 1, 3),
    _VlanPortRange_Type()
)
vlanPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortRange.setStatus("current")
_Layer2FwdIPTable_Object = MibTable
layer2FwdIPTable = _Layer2FwdIPTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 5)
)
if mibBuilder.loadTexts:
    layer2FwdIPTable.setStatus("current")
_Layer2FwdIPEntry_Object = MibTableRow
layer2FwdIPEntry = _Layer2FwdIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 5, 1)
)
layer2FwdIPEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "ipIntfPortIndex"),
    (0, "TRELLIX-SENSOR-CONF-MIB", "ipEntryIndex"),
)
if mibBuilder.loadTexts:
    layer2FwdIPEntry.setStatus("current")
_IpIntfPortIndex_Type = TrellixPortLinearIndex
_IpIntfPortIndex_Object = MibTableColumn
ipIntfPortIndex = _IpIntfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 5, 1, 1),
    _IpIntfPortIndex_Type()
)
ipIntfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipIntfPortIndex.setStatus("current")
_IpEntryIndex_Type = Integer32
_IpEntryIndex_Object = MibTableColumn
ipEntryIndex = _IpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 5, 1, 2),
    _IpEntryIndex_Type()
)
ipEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipEntryIndex.setStatus("current")


class _IpPortRange_Type(DisplayString):
    """Custom type ipPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpPortRange_Type.__name__ = "DisplayString"
_IpPortRange_Object = MibTableColumn
ipPortRange = _IpPortRange_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 34, 5, 1, 3),
    _IpPortRange_Type()
)
ipPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPortRange.setStatus("current")
_PktCapCfgGrp_ObjectIdentity = ObjectIdentity
pktCapCfgGrp = _PktCapCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35)
)


class _PktCapMode_Type(Integer32):
    """Custom type pktCapMode based on Integer32"""
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
          ("portModeEnable", 2),
          ("fileModeEnable", 3))
    )


_PktCapMode_Type.__name__ = "Integer32"
_PktCapMode_Object = MibScalar
pktCapMode = _PktCapMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 1),
    _PktCapMode_Type()
)
pktCapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapMode.setStatus("current")


class _PktCapDuration_Type(Integer32):
    """Custom type pktCapDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 315360000),
    )


_PktCapDuration_Type.__name__ = "Integer32"
_PktCapDuration_Object = MibScalar
pktCapDuration = _PktCapDuration_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 2),
    _PktCapDuration_Type()
)
pktCapDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapDuration.setStatus("current")
_PktCapPmSpanPortForCapture_Type = TrellixPortLinearIndex
_PktCapPmSpanPortForCapture_Object = MibScalar
pktCapPmSpanPortForCapture = _PktCapPmSpanPortForCapture_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 3),
    _PktCapPmSpanPortForCapture_Type()
)
pktCapPmSpanPortForCapture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapPmSpanPortForCapture.setStatus("current")


class _PktCapFmLocation_Type(Integer32):
    """Custom type pktCapFmLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manager", 1),
          ("tftpServer", 2),
          ("scpServer", 3))
    )


_PktCapFmLocation_Type.__name__ = "Integer32"
_PktCapFmLocation_Object = MibScalar
pktCapFmLocation = _PktCapFmLocation_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 4),
    _PktCapFmLocation_Type()
)
pktCapFmLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapFmLocation.setStatus("current")


class _PktCapFmMaxSize_Type(Integer32):
    """Custom type pktCapFmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PktCapFmMaxSize_Type.__name__ = "Integer32"
_PktCapFmMaxSize_Object = MibScalar
pktCapFmMaxSize = _PktCapFmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 5),
    _PktCapFmMaxSize_Type()
)
pktCapFmMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapFmMaxSize.setStatus("current")


class _PktCapFmFUServerAddress_Type(OctetString):
    """Custom type pktCapFmFUServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_PktCapFmFUServerAddress_Type.__name__ = "OctetString"
_PktCapFmFUServerAddress_Object = MibScalar
pktCapFmFUServerAddress = _PktCapFmFUServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 6),
    _PktCapFmFUServerAddress_Type()
)
pktCapFmFUServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapFmFUServerAddress.setStatus("current")


class _PktCapFmFUFileName_Type(DisplayString):
    """Custom type pktCapFmFUFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PktCapFmFUFileName_Type.__name__ = "DisplayString"
_PktCapFmFUFileName_Object = MibScalar
pktCapFmFUFileName = _PktCapFmFUFileName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 7),
    _PktCapFmFUFileName_Type()
)
pktCapFmFUFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapFmFUFileName.setStatus("current")


class _PktCapFmFUSetting_Type(Integer32):
    """Custom type pktCapFmFUSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_PktCapFmFUSetting_Type.__name__ = "Integer32"
_PktCapFmFUSetting_Object = MibScalar
pktCapFmFUSetting = _PktCapFmFUSetting_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 8),
    _PktCapFmFUSetting_Type()
)
pktCapFmFUSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapFmFUSetting.setStatus("current")


class _PktCapFilterFileName_Type(DisplayString):
    """Custom type pktCapFilterFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PktCapFilterFileName_Type.__name__ = "DisplayString"
_PktCapFilterFileName_Object = MibScalar
pktCapFilterFileName = _PktCapFilterFileName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 9),
    _PktCapFilterFileName_Type()
)
pktCapFilterFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktCapFilterFileName.setStatus("current")


class _PktCapFilterFileTimeStamp_Type(Integer32):
    """Custom type pktCapFilterFileTimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PktCapFilterFileTimeStamp_Type.__name__ = "Integer32"
_PktCapFilterFileTimeStamp_Object = MibScalar
pktCapFilterFileTimeStamp = _PktCapFilterFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 10),
    _PktCapFilterFileTimeStamp_Type()
)
pktCapFilterFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktCapFilterFileTimeStamp.setStatus("current")
_PktCapCommandGrp_ObjectIdentity = ObjectIdentity
pktCapCommandGrp = _PktCapCommandGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 11)
)


class _PktCapCmd_Type(Integer32):
    """Custom type pktCapCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("delete-filter-file", 3),
          ("cancel", 4),
          ("delete-pcap-file", 5))
    )


_PktCapCmd_Type.__name__ = "Integer32"
_PktCapCmd_Object = MibScalar
pktCapCmd = _PktCapCmd_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 11, 1),
    _PktCapCmd_Type()
)
pktCapCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapCmd.setStatus("current")


class _PktCapStatus_Type(Integer32):
    """Custom type pktCapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("not-running", 2))
    )


_PktCapStatus_Type.__name__ = "Integer32"
_PktCapStatus_Object = MibScalar
pktCapStatus = _PktCapStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 11, 2),
    _PktCapStatus_Type()
)
pktCapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktCapStatus.setStatus("current")


class _PacketCaptureFmFUControl_Type(Integer32):
    """Custom type packetCaptureFmFUControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("upload-to-NSM", 3))
    )


_PacketCaptureFmFUControl_Type.__name__ = "Integer32"
_PacketCaptureFmFUControl_Object = MibScalar
packetCaptureFmFUControl = _PacketCaptureFmFUControl_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 11, 3),
    _PacketCaptureFmFUControl_Type()
)
packetCaptureFmFUControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    packetCaptureFmFUControl.setStatus("current")


class _PacketCaptureFmFileStatus_Type(Integer32):
    """Custom type packetCaptureFmFileStatus based on Integer32"""
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
        *(("fileUploadInProgress", 1),
          ("fileExistNotUploaded", 2),
          ("fileNotExist", 3),
          ("fileUploadFailed", 4),
          ("fileUploadDone", 5),
          ("fileUploadNotStarted", 6))
    )


_PacketCaptureFmFileStatus_Type.__name__ = "Integer32"
_PacketCaptureFmFileStatus_Object = MibScalar
packetCaptureFmFileStatus = _PacketCaptureFmFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 11, 4),
    _PacketCaptureFmFileStatus_Type()
)
packetCaptureFmFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetCaptureFmFileStatus.setStatus("current")


class _PacketCaptureFmTest_Type(Integer32):
    """Custom type packetCaptureFmTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_PacketCaptureFmTest_Type.__name__ = "Integer32"
_PacketCaptureFmTest_Object = MibScalar
packetCaptureFmTest = _PacketCaptureFmTest_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 11, 5),
    _PacketCaptureFmTest_Type()
)
packetCaptureFmTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    packetCaptureFmTest.setStatus("current")


class _PacketCaptureFmTestStatus_Type(Integer32):
    """Custom type packetCaptureFmTestStatus based on Integer32"""
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
        *(("success", 1),
          ("failure", 2),
          ("resultNotValid", 3),
          ("fileUploadServerConnectFailure", 4),
          ("fileUploadServerConnectTimeout", 5),
          ("fileUploadServerAuthenticationFailure", 6),
          ("fileUploadInProgress", 7))
    )


_PacketCaptureFmTestStatus_Type.__name__ = "Integer32"
_PacketCaptureFmTestStatus_Object = MibScalar
packetCaptureFmTestStatus = _PacketCaptureFmTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 11, 6),
    _PacketCaptureFmTestStatus_Type()
)
packetCaptureFmTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetCaptureFmTestStatus.setStatus("current")


class _PktCapFmSCPUserName_Type(DisplayString):
    """Custom type pktCapFmSCPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PktCapFmSCPUserName_Type.__name__ = "DisplayString"
_PktCapFmSCPUserName_Object = MibScalar
pktCapFmSCPUserName = _PktCapFmSCPUserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 12),
    _PktCapFmSCPUserName_Type()
)
pktCapFmSCPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapFmSCPUserName.setStatus("current")


class _PktCapFmSCPPassword_Type(DisplayString):
    """Custom type pktCapFmSCPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PktCapFmSCPPassword_Type.__name__ = "DisplayString"
_PktCapFmSCPPassword_Object = MibScalar
pktCapFmSCPPassword = _PktCapFmSCPPassword_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 35, 13),
    _PktCapFmSCPPassword_Type()
)
pktCapFmSCPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktCapFmSCPPassword.setStatus("current")
_DnsCfgGrp_ObjectIdentity = ObjectIdentity
dnsCfgGrp = _DnsCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 36)
)
_PriDNSServerIp_Type = IpAddress
_PriDNSServerIp_Object = MibScalar
priDNSServerIp = _PriDNSServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 36, 1),
    _PriDNSServerIp_Type()
)
priDNSServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priDNSServerIp.setStatus("current")
_SecDNSServerIp_Type = IpAddress
_SecDNSServerIp_Object = MibScalar
secDNSServerIp = _SecDNSServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 36, 2),
    _SecDNSServerIp_Type()
)
secDNSServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secDNSServerIp.setStatus("current")
_PriDNSServerIpV6_Type = Ipv6Address
_PriDNSServerIpV6_Object = MibScalar
priDNSServerIpV6 = _PriDNSServerIpV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 36, 3),
    _PriDNSServerIpV6_Type()
)
priDNSServerIpV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priDNSServerIpV6.setStatus("current")
_SecDNSServerIpV6_Type = Ipv6Address
_SecDNSServerIpV6_Object = MibScalar
secDNSServerIpV6 = _SecDNSServerIpV6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 36, 4),
    _SecDNSServerIpV6_Type()
)
secDNSServerIpV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secDNSServerIpV6.setStatus("current")


class _DnsSearchList_Type(OctetString):
    """Custom type dnsSearchList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DnsSearchList_Type.__name__ = "OctetString"
_DnsSearchList_Object = MibScalar
dnsSearchList = _DnsSearchList_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 36, 5),
    _DnsSearchList_Type()
)
dnsSearchList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsSearchList.setStatus("current")
_Layer7DCapConfigGrp_ObjectIdentity = ObjectIdentity
layer7DCapConfigGrp = _Layer7DCapConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 37)
)


class _Layer7DCapPercentageOfFlows_Type(Integer32):
    """Custom type layer7DCapPercentageOfFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Layer7DCapPercentageOfFlows_Type.__name__ = "Integer32"
_Layer7DCapPercentageOfFlows_Object = MibScalar
layer7DCapPercentageOfFlows = _Layer7DCapPercentageOfFlows_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 37, 1),
    _Layer7DCapPercentageOfFlows_Type()
)
layer7DCapPercentageOfFlows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7DCapPercentageOfFlows.setStatus("current")


class _Layer7DCapBuffSize_Type(Integer32):
    """Custom type layer7DCapBuffSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1500),
    )


_Layer7DCapBuffSize_Type.__name__ = "Integer32"
_Layer7DCapBuffSize_Object = MibScalar
layer7DCapBuffSize = _Layer7DCapBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 37, 2),
    _Layer7DCapBuffSize_Type()
)
layer7DCapBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7DCapBuffSize.setStatus("current")


class _Layer7DCapMaxSupportedFlows_Type(Integer32):
    """Custom type layer7DCapMaxSupportedFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Layer7DCapMaxSupportedFlows_Type.__name__ = "Integer32"
_Layer7DCapMaxSupportedFlows_Object = MibScalar
layer7DCapMaxSupportedFlows = _Layer7DCapMaxSupportedFlows_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 37, 3),
    _Layer7DCapMaxSupportedFlows_Type()
)
layer7DCapMaxSupportedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7DCapMaxSupportedFlows.setStatus("current")
_InterfacePhysicalPortGrp_ObjectIdentity = ObjectIdentity
interfacePhysicalPortGrp = _InterfacePhysicalPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38)
)
_IntfPhysicalPortTable_Object = MibTable
intfPhysicalPortTable = _IntfPhysicalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1)
)
if mibBuilder.loadTexts:
    intfPhysicalPortTable.setStatus("current")
_IntfPhysicalPortEntry_Object = MibTableRow
intfPhysicalPortEntry = _IntfPhysicalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1)
)
intfPhysicalPortEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
    (0, "TRELLIX-SENSOR-SMI", "intfPhysicalPortIndex"),
)
if mibBuilder.loadTexts:
    intfPhysicalPortEntry.setStatus("current")


class _IntfPhysicalPortIfDescr_Type(DisplayString):
    """Custom type intfPhysicalPortIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntfPhysicalPortIfDescr_Type.__name__ = "DisplayString"
_IntfPhysicalPortIfDescr_Object = MibTableColumn
intfPhysicalPortIfDescr = _IntfPhysicalPortIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 1),
    _IntfPhysicalPortIfDescr_Type()
)
intfPhysicalPortIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortIfDescr.setStatus("current")
_IntfPhysicalPortIfType_Type = TrellixIDSPortType
_IntfPhysicalPortIfType_Object = MibTableColumn
intfPhysicalPortIfType = _IntfPhysicalPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 2),
    _IntfPhysicalPortIfType_Type()
)
intfPhysicalPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortIfType.setStatus("current")


class _IntfPhysicalPortIfAdminStatus_Type(Integer32):
    """Custom type intfPhysicalPortIfAdminStatus based on Integer32"""
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


_IntfPhysicalPortIfAdminStatus_Type.__name__ = "Integer32"
_IntfPhysicalPortIfAdminStatus_Object = MibTableColumn
intfPhysicalPortIfAdminStatus = _IntfPhysicalPortIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 3),
    _IntfPhysicalPortIfAdminStatus_Type()
)
intfPhysicalPortIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortIfAdminStatus.setStatus("current")


class _IntfPhysicalPortIfOperStatus_Type(Integer32):
    """Custom type intfPhysicalPortIfOperStatus based on Integer32"""
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


_IntfPhysicalPortIfOperStatus_Type.__name__ = "Integer32"
_IntfPhysicalPortIfOperStatus_Object = MibTableColumn
intfPhysicalPortIfOperStatus = _IntfPhysicalPortIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 4),
    _IntfPhysicalPortIfOperStatus_Type()
)
intfPhysicalPortIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortIfOperStatus.setStatus("current")
_IntfPhysicalPortEnableFullDuplex_Type = TruthValue
_IntfPhysicalPortEnableFullDuplex_Object = MibTableColumn
intfPhysicalPortEnableFullDuplex = _IntfPhysicalPortEnableFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 5),
    _IntfPhysicalPortEnableFullDuplex_Type()
)
intfPhysicalPortEnableFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortEnableFullDuplex.setStatus("current")


class _IntfPhysicalPortSpeed_Type(Integer32):
    """Custom type intfPhysicalPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ten-Mbps", 1),
          ("hundred-Mbps", 2),
          ("one-Gbps", 3),
          ("ten-Gbps", 4))
    )


_IntfPhysicalPortSpeed_Type.__name__ = "Integer32"
_IntfPhysicalPortSpeed_Object = MibTableColumn
intfPhysicalPortSpeed = _IntfPhysicalPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 6),
    _IntfPhysicalPortSpeed_Type()
)
intfPhysicalPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortSpeed.setStatus("current")
_IntfPhysicalPortSpeedConfig_Type = TrellixPortSpeed
_IntfPhysicalPortSpeedConfig_Object = MibTableColumn
intfPhysicalPortSpeedConfig = _IntfPhysicalPortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 7),
    _IntfPhysicalPortSpeedConfig_Type()
)
intfPhysicalPortSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortSpeedConfig.setStatus("current")
_IntfPhysicalPortIsMcafeeConnector_Type = TruthValue
_IntfPhysicalPortIsMcafeeConnector_Object = MibTableColumn
intfPhysicalPortIsMcafeeConnector = _IntfPhysicalPortIsMcafeeConnector_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 8),
    _IntfPhysicalPortIsMcafeeConnector_Type()
)
intfPhysicalPortIsMcafeeConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortIsMcafeeConnector.setStatus("current")
_IntfPhysicalPortAllowAnyConnector_Type = TruthValue
_IntfPhysicalPortAllowAnyConnector_Object = MibTableColumn
intfPhysicalPortAllowAnyConnector = _IntfPhysicalPortAllowAnyConnector_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 9),
    _IntfPhysicalPortAllowAnyConnector_Type()
)
intfPhysicalPortAllowAnyConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortAllowAnyConnector.setStatus("current")


class _IntfPhysicalPortCageType_Type(Integer32):
    """Custom type intfPhysicalPortCageType based on Integer32"""
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
        *(("other", 0),
          ("rJ-45", 1),
          ("rJ-11", 2),
          ("gBIC", 3),
          ("sFP", 4),
          ("xFP", 5))
    )


_IntfPhysicalPortCageType_Type.__name__ = "Integer32"
_IntfPhysicalPortCageType_Object = MibTableColumn
intfPhysicalPortCageType = _IntfPhysicalPortCageType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 10),
    _IntfPhysicalPortCageType_Type()
)
intfPhysicalPortCageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortCageType.setStatus("current")


class _IntfPhysicalPortGetMediaType_Type(Integer32):
    """Custom type intfPhysicalPortGetMediaType based on Integer32"""
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
          ("optical", 1),
          ("electrical", 2))
    )


_IntfPhysicalPortGetMediaType_Type.__name__ = "Integer32"
_IntfPhysicalPortGetMediaType_Object = MibTableColumn
intfPhysicalPortGetMediaType = _IntfPhysicalPortGetMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 11),
    _IntfPhysicalPortGetMediaType_Type()
)
intfPhysicalPortGetMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortGetMediaType.setStatus("current")


class _IntfPhysicalPortSetMediaType_Type(Integer32):
    """Custom type intfPhysicalPortSetMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optical", 1),
          ("electrical", 2))
    )


_IntfPhysicalPortSetMediaType_Type.__name__ = "Integer32"
_IntfPhysicalPortSetMediaType_Object = MibTableColumn
intfPhysicalPortSetMediaType = _IntfPhysicalPortSetMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 12),
    _IntfPhysicalPortSetMediaType_Type()
)
intfPhysicalPortSetMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortSetMediaType.setStatus("current")
_IntfPhysicalPortMonPortIpAddress_Type = IpAddress
_IntfPhysicalPortMonPortIpAddress_Object = MibTableColumn
intfPhysicalPortMonPortIpAddress = _IntfPhysicalPortMonPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 13),
    _IntfPhysicalPortMonPortIpAddress_Type()
)
intfPhysicalPortMonPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortMonPortIpAddress.setStatus("current")
_IntfPhysicalPortMonPortNetMask_Type = IpAddress
_IntfPhysicalPortMonPortNetMask_Object = MibTableColumn
intfPhysicalPortMonPortNetMask = _IntfPhysicalPortMonPortNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 14),
    _IntfPhysicalPortMonPortNetMask_Type()
)
intfPhysicalPortMonPortNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortMonPortNetMask.setStatus("current")
_IntfPhysicalPortGatewayIpAddress_Type = IpAddress
_IntfPhysicalPortGatewayIpAddress_Object = MibTableColumn
intfPhysicalPortGatewayIpAddress = _IntfPhysicalPortGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 15),
    _IntfPhysicalPortGatewayIpAddress_Type()
)
intfPhysicalPortGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortGatewayIpAddress.setStatus("current")
_IntfPhysicalPortNbadConfigStatus_Type = TruthValue
_IntfPhysicalPortNbadConfigStatus_Object = MibTableColumn
intfPhysicalPortNbadConfigStatus = _IntfPhysicalPortNbadConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 16),
    _IntfPhysicalPortNbadConfigStatus_Type()
)
intfPhysicalPortNbadConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortNbadConfigStatus.setStatus("current")


class _IntfPhysicalPortVlanId_Type(Integer32):
    """Custom type intfPhysicalPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2164326399),
    )


_IntfPhysicalPortVlanId_Type.__name__ = "Integer32"
_IntfPhysicalPortVlanId_Object = MibTableColumn
intfPhysicalPortVlanId = _IntfPhysicalPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 17),
    _IntfPhysicalPortVlanId_Type()
)
intfPhysicalPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfPhysicalPortVlanId.setStatus("current")


class _IntfPhysicalPortLBSerialNumber_Type(DisplayString):
    """Custom type intfPhysicalPortLBSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_IntfPhysicalPortLBSerialNumber_Type.__name__ = "DisplayString"
_IntfPhysicalPortLBSerialNumber_Object = MibTableColumn
intfPhysicalPortLBSerialNumber = _IntfPhysicalPortLBSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 18),
    _IntfPhysicalPortLBSerialNumber_Type()
)
intfPhysicalPortLBSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortLBSerialNumber.setStatus("current")


class _IntfPhysicalPortLBPortNumber_Type(Integer32):
    """Custom type intfPhysicalPortLBPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IntfPhysicalPortLBPortNumber_Type.__name__ = "Integer32"
_IntfPhysicalPortLBPortNumber_Object = MibTableColumn
intfPhysicalPortLBPortNumber = _IntfPhysicalPortLBPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 19),
    _IntfPhysicalPortLBPortNumber_Type()
)
intfPhysicalPortLBPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortLBPortNumber.setStatus("current")


class _IntfPhysicalPortConnectorType_Type(Integer32):
    """Custom type intfPhysicalPortConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("qSFP", 1),
          ("sFP-plus", 2),
          ("sFP-fiber", 3),
          ("sFP-copper", 4))
    )


_IntfPhysicalPortConnectorType_Type.__name__ = "Integer32"
_IntfPhysicalPortConnectorType_Object = MibTableColumn
intfPhysicalPortConnectorType = _IntfPhysicalPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 20),
    _IntfPhysicalPortConnectorType_Type()
)
intfPhysicalPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortConnectorType.setStatus("current")
_IntfPhysicalPortLinearIndex_Type = TrellixPortLinearIndex
_IntfPhysicalPortLinearIndex_Object = MibTableColumn
intfPhysicalPortLinearIndex = _IntfPhysicalPortLinearIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 38, 1, 1, 21),
    _IntfPhysicalPortLinearIndex_Type()
)
intfPhysicalPortLinearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortLinearIndex.setStatus("current")
_GtiConfigGrp_ObjectIdentity = ObjectIdentity
gtiConfigGrp = _GtiConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39)
)


class _GtiProxyServerName_Type(DisplayString):
    """Custom type gtiProxyServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_GtiProxyServerName_Type.__name__ = "DisplayString"
_GtiProxyServerName_Object = MibScalar
gtiProxyServerName = _GtiProxyServerName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 1),
    _GtiProxyServerName_Type()
)
gtiProxyServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiProxyServerName.setStatus("current")


class _GtiProxyPort_Type(Integer32):
    """Custom type gtiProxyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_GtiProxyPort_Type.__name__ = "Integer32"
_GtiProxyPort_Object = MibScalar
gtiProxyPort = _GtiProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 2),
    _GtiProxyPort_Type()
)
gtiProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiProxyPort.setStatus("current")


class _GtiProxyUsername_Type(DisplayString):
    """Custom type gtiProxyUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GtiProxyUsername_Type.__name__ = "DisplayString"
_GtiProxyUsername_Object = MibScalar
gtiProxyUsername = _GtiProxyUsername_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 3),
    _GtiProxyUsername_Type()
)
gtiProxyUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiProxyUsername.setStatus("current")


class _GtiProxyPassword_Type(DisplayString):
    """Custom type gtiProxyPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GtiProxyPassword_Type.__name__ = "DisplayString"
_GtiProxyPassword_Object = MibScalar
gtiProxyPassword = _GtiProxyPassword_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 4),
    _GtiProxyPassword_Type()
)
gtiProxyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiProxyPassword.setStatus("current")
_GtiConfigPrivateCloudGrp_ObjectIdentity = ObjectIdentity
gtiConfigPrivateCloudGrp = _GtiConfigPrivateCloudGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 5)
)


class _GtiPrivateCloudServerIPAddressType_Type(Integer32):
    """Custom type gtiPrivateCloudServerIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_GtiPrivateCloudServerIPAddressType_Type.__name__ = "Integer32"
_GtiPrivateCloudServerIPAddressType_Object = MibScalar
gtiPrivateCloudServerIPAddressType = _GtiPrivateCloudServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 5, 1),
    _GtiPrivateCloudServerIPAddressType_Type()
)
gtiPrivateCloudServerIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiPrivateCloudServerIPAddressType.setStatus("current")
_GtiPrivateCloudServerIPv4Address_Type = IpAddress
_GtiPrivateCloudServerIPv4Address_Object = MibScalar
gtiPrivateCloudServerIPv4Address = _GtiPrivateCloudServerIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 5, 2),
    _GtiPrivateCloudServerIPv4Address_Type()
)
gtiPrivateCloudServerIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiPrivateCloudServerIPv4Address.setStatus("current")
_GtiPrivateCloudServerIPv6Address_Type = Ipv6Address
_GtiPrivateCloudServerIPv6Address_Object = MibScalar
gtiPrivateCloudServerIPv6Address = _GtiPrivateCloudServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 5, 3),
    _GtiPrivateCloudServerIPv6Address_Type()
)
gtiPrivateCloudServerIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiPrivateCloudServerIPv6Address.setStatus("current")


class _GtiPrivateCloudServerConnectionConfig_Type(Integer32):
    """Custom type gtiPrivateCloudServerConnectionConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("reconnect", 3))
    )


_GtiPrivateCloudServerConnectionConfig_Type.__name__ = "Integer32"
_GtiPrivateCloudServerConnectionConfig_Object = MibScalar
gtiPrivateCloudServerConnectionConfig = _GtiPrivateCloudServerConnectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 5, 4),
    _GtiPrivateCloudServerConnectionConfig_Type()
)
gtiPrivateCloudServerConnectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiPrivateCloudServerConnectionConfig.setStatus("current")


class _GtiPrivateCloudServerDeleteCertificate_Type(Integer32):
    """Custom type gtiPrivateCloudServerDeleteCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("dont-delete", 2))
    )


_GtiPrivateCloudServerDeleteCertificate_Type.__name__ = "Integer32"
_GtiPrivateCloudServerDeleteCertificate_Object = MibScalar
gtiPrivateCloudServerDeleteCertificate = _GtiPrivateCloudServerDeleteCertificate_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 5, 5),
    _GtiPrivateCloudServerDeleteCertificate_Type()
)
gtiPrivateCloudServerDeleteCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiPrivateCloudServerDeleteCertificate.setStatus("current")


class _GtiPrivateCloudServerCertificateStatus_Type(Integer32):
    """Custom type gtiPrivateCloudServerCertificateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("not-Present", 2))
    )


_GtiPrivateCloudServerCertificateStatus_Type.__name__ = "Integer32"
_GtiPrivateCloudServerCertificateStatus_Object = MibScalar
gtiPrivateCloudServerCertificateStatus = _GtiPrivateCloudServerCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 5, 6),
    _GtiPrivateCloudServerCertificateStatus_Type()
)
gtiPrivateCloudServerCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtiPrivateCloudServerCertificateStatus.setStatus("current")


class _GtiPrivateCloudChannelStatus_Type(Integer32):
    """Custom type gtiPrivateCloudChannelStatus based on Integer32"""
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
        *(("gtiPrivateCloud-TrustedSource-Channel-Down", 0),
          ("gtiPrivateCloud-TrustedSource-Channel-InProgress", 1),
          ("gtiPrivateCloud-TrustedSource-Channel-Established", 2),
          ("gtiPrivateCloud-TrustedSource-Channel-Status-Unknown", 3),
          ("gtiPrivateCloud-TrustedSource-Channel-Down-Error-In-Cert-ret", 4),
          ("gtiPrivateCloud-Network-Issue", 5))
    )


_GtiPrivateCloudChannelStatus_Type.__name__ = "Integer32"
_GtiPrivateCloudChannelStatus_Object = MibScalar
gtiPrivateCloudChannelStatus = _GtiPrivateCloudChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 5, 7),
    _GtiPrivateCloudChannelStatus_Type()
)
gtiPrivateCloudChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtiPrivateCloudChannelStatus.setStatus("current")
_GtiUnifiedConfigGrp_ObjectIdentity = ObjectIdentity
gtiUnifiedConfigGrp = _GtiUnifiedConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6)
)


class _GtiFileRESTGTIType_Type(Integer32):
    """Custom type gtiFileRESTGTIType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private-gti-server", 1),
          ("public-gti-server", 2))
    )


_GtiFileRESTGTIType_Type.__name__ = "Integer32"
_GtiFileRESTGTIType_Object = MibScalar
gtiFileRESTGTIType = _GtiFileRESTGTIType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6, 1),
    _GtiFileRESTGTIType_Type()
)
gtiFileRESTGTIType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiFileRESTGTIType.setStatus("current")


class _GtiFileRESTPublicGTIFQDN_Type(DisplayString):
    """Custom type gtiFileRESTPublicGTIFQDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_GtiFileRESTPublicGTIFQDN_Type.__name__ = "DisplayString"
_GtiFileRESTPublicGTIFQDN_Object = MibScalar
gtiFileRESTPublicGTIFQDN = _GtiFileRESTPublicGTIFQDN_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6, 2),
    _GtiFileRESTPublicGTIFQDN_Type()
)
gtiFileRESTPublicGTIFQDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiFileRESTPublicGTIFQDN.setStatus("current")


class _GtiFileRESTUsername_Type(DisplayString):
    """Custom type gtiFileRESTUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_GtiFileRESTUsername_Type.__name__ = "DisplayString"
_GtiFileRESTUsername_Object = MibScalar
gtiFileRESTUsername = _GtiFileRESTUsername_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6, 3),
    _GtiFileRESTUsername_Type()
)
gtiFileRESTUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiFileRESTUsername.setStatus("current")


class _GtiFileRESTPassword_Type(DisplayString):
    """Custom type gtiFileRESTPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_GtiFileRESTPassword_Type.__name__ = "DisplayString"
_GtiFileRESTPassword_Object = MibScalar
gtiFileRESTPassword = _GtiFileRESTPassword_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6, 4),
    _GtiFileRESTPassword_Type()
)
gtiFileRESTPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiFileRESTPassword.setStatus("current")


class _GtiFileRESTConnectionConfig_Type(Integer32):
    """Custom type gtiFileRESTConnectionConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect-private-gti-server", 1),
          ("connect-public-gti-server", 2),
          ("reconnect-private-gti-server", 3))
    )


_GtiFileRESTConnectionConfig_Type.__name__ = "Integer32"
_GtiFileRESTConnectionConfig_Object = MibScalar
gtiFileRESTConnectionConfig = _GtiFileRESTConnectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6, 5),
    _GtiFileRESTConnectionConfig_Type()
)
gtiFileRESTConnectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiFileRESTConnectionConfig.setStatus("current")


class _GtiFileRESTPvtGTIIPType_Type(Integer32):
    """Custom type gtiFileRESTPvtGTIIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fqdn", 1),
          ("ipv4", 4),
          ("ipv6", 6))
    )


_GtiFileRESTPvtGTIIPType_Type.__name__ = "Integer32"
_GtiFileRESTPvtGTIIPType_Object = MibScalar
gtiFileRESTPvtGTIIPType = _GtiFileRESTPvtGTIIPType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6, 6),
    _GtiFileRESTPvtGTIIPType_Type()
)
gtiFileRESTPvtGTIIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiFileRESTPvtGTIIPType.setStatus("current")
_GtiFileRESTPvtGTIIPv4Address_Type = IpAddress
_GtiFileRESTPvtGTIIPv4Address_Object = MibScalar
gtiFileRESTPvtGTIIPv4Address = _GtiFileRESTPvtGTIIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6, 7),
    _GtiFileRESTPvtGTIIPv4Address_Type()
)
gtiFileRESTPvtGTIIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiFileRESTPvtGTIIPv4Address.setStatus("current")
_GtiFileRESTPvtGTIIPV6Address_Type = Ipv6Address
_GtiFileRESTPvtGTIIPV6Address_Object = MibScalar
gtiFileRESTPvtGTIIPV6Address = _GtiFileRESTPvtGTIIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 39, 6, 8),
    _GtiFileRESTPvtGTIIPV6Address_Type()
)
gtiFileRESTPvtGTIIPV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtiFileRESTPvtGTIIPV6Address.setStatus("current")
_NtpConfigGrp_ObjectIdentity = ObjectIdentity
ntpConfigGrp = _NtpConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40)
)
_NtpConfigTable_Object = MibTable
ntpConfigTable = _NtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1)
)
if mibBuilder.loadTexts:
    ntpConfigTable.setStatus("current")
_NtpConfigEntry_Object = MibTableRow
ntpConfigEntry = _NtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1, 1)
)
ntpConfigEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "ntpServerIndex"),
)
if mibBuilder.loadTexts:
    ntpConfigEntry.setStatus("current")
_NtpConfigServerIPv4_Type = IpAddress
_NtpConfigServerIPv4_Object = MibTableColumn
ntpConfigServerIPv4 = _NtpConfigServerIPv4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1, 1, 1),
    _NtpConfigServerIPv4_Type()
)
ntpConfigServerIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpConfigServerIPv4.setStatus("current")
_NtpConfigServerIPv6_Type = Ipv6Address
_NtpConfigServerIPv6_Object = MibTableColumn
ntpConfigServerIPv6 = _NtpConfigServerIPv6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1, 1, 2),
    _NtpConfigServerIPv6_Type()
)
ntpConfigServerIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpConfigServerIPv6.setStatus("current")


class _NtpConfigPollInterval_Type(Integer32):
    """Custom type ntpConfigPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 17),
    )


_NtpConfigPollInterval_Type.__name__ = "Integer32"
_NtpConfigPollInterval_Object = MibTableColumn
ntpConfigPollInterval = _NtpConfigPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1, 1, 3),
    _NtpConfigPollInterval_Type()
)
ntpConfigPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpConfigPollInterval.setStatus("current")
_NtpConfigAuthenticationEnable_Type = TruthValue
_NtpConfigAuthenticationEnable_Object = MibTableColumn
ntpConfigAuthenticationEnable = _NtpConfigAuthenticationEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1, 1, 4),
    _NtpConfigAuthenticationEnable_Type()
)
ntpConfigAuthenticationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpConfigAuthenticationEnable.setStatus("current")


class _NtpConfigKeyId_Type(Integer32):
    """Custom type ntpConfigKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_NtpConfigKeyId_Type.__name__ = "Integer32"
_NtpConfigKeyId_Object = MibTableColumn
ntpConfigKeyId = _NtpConfigKeyId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1, 1, 5),
    _NtpConfigKeyId_Type()
)
ntpConfigKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpConfigKeyId.setStatus("current")


class _NtpConfigKeyType_Type(Integer32):
    """Custom type ntpConfigKeyType based on Integer32"""
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
        *(("md5", 1),
          ("sha", 2),
          ("sha1", 3),
          ("not-supported", 4))
    )


_NtpConfigKeyType_Type.__name__ = "Integer32"
_NtpConfigKeyType_Object = MibTableColumn
ntpConfigKeyType = _NtpConfigKeyType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1, 1, 6),
    _NtpConfigKeyType_Type()
)
ntpConfigKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpConfigKeyType.setStatus("current")


class _NtpConfigKeyValue_Type(OctetString):
    """Custom type ntpConfigKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NtpConfigKeyValue_Type.__name__ = "OctetString"
_NtpConfigKeyValue_Object = MibTableColumn
ntpConfigKeyValue = _NtpConfigKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 1, 1, 7),
    _NtpConfigKeyValue_Type()
)
ntpConfigKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpConfigKeyValue.setStatus("current")


class _NtpConfigFileCreate_Type(Integer32):
    """Custom type ntpConfigFileCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stop-ntpd", 0),
          ("start-ntpd", 1))
    )


_NtpConfigFileCreate_Type.__name__ = "Integer32"
_NtpConfigFileCreate_Object = MibScalar
ntpConfigFileCreate = _NtpConfigFileCreate_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 40, 2),
    _NtpConfigFileCreate_Type()
)
ntpConfigFileCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpConfigFileCreate.setStatus("current")
_PluggableModuleGrp_ObjectIdentity = ObjectIdentity
pluggableModuleGrp = _PluggableModuleGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 41)
)
_PluggableModuleTable_Object = MibTable
pluggableModuleTable = _PluggableModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 41, 1)
)
if mibBuilder.loadTexts:
    pluggableModuleTable.setStatus("current")
_PluggableModuleEntry_Object = MibTableRow
pluggableModuleEntry = _PluggableModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 41, 1, 1)
)
pluggableModuleEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
)
if mibBuilder.loadTexts:
    pluggableModuleEntry.setStatus("current")


class _ModuleSerialNumber_Type(DisplayString):
    """Custom type moduleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModuleSerialNumber_Type.__name__ = "DisplayString"
_ModuleSerialNumber_Object = MibTableColumn
moduleSerialNumber = _ModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 41, 1, 1, 1),
    _ModuleSerialNumber_Type()
)
moduleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSerialNumber.setStatus("current")
_ModuleSysType_Type = TrellixPluggableModuleType
_ModuleSysType_Object = MibTableColumn
moduleSysType = _ModuleSysType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 41, 1, 1, 2),
    _ModuleSysType_Type()
)
moduleSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSysType.setStatus("current")
_ModulePresent_Type = TruthValue
_ModulePresent_Object = MibTableColumn
modulePresent = _ModulePresent_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 41, 1, 1, 3),
    _ModulePresent_Type()
)
modulePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePresent.setStatus("current")


class _ModuleNumPorts_Type(Integer32):
    """Custom type moduleNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ModuleNumPorts_Type.__name__ = "Integer32"
_ModuleNumPorts_Object = MibTableColumn
moduleNumPorts = _ModuleNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 41, 1, 1, 4),
    _ModuleNumPorts_Type()
)
moduleNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumPorts.setStatus("current")
_ModuleRebootRequired_Type = TruthValue
_ModuleRebootRequired_Object = MibTableColumn
moduleRebootRequired = _ModuleRebootRequired_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 41, 1, 1, 5),
    _ModuleRebootRequired_Type()
)
moduleRebootRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleRebootRequired.setStatus("current")
_InsightixNetworkGrp_ObjectIdentity = ObjectIdentity
insightixNetworkGrp = _InsightixNetworkGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42)
)
_InsightixCfgGrp_ObjectIdentity = ObjectIdentity
insightixCfgGrp = _InsightixCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1)
)


class _LdapServerIPAddressType_Type(Integer32):
    """Custom type ldapServerIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_LdapServerIPAddressType_Type.__name__ = "Integer32"
_LdapServerIPAddressType_Object = MibScalar
ldapServerIPAddressType = _LdapServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 1),
    _LdapServerIPAddressType_Type()
)
ldapServerIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServerIPAddressType.setStatus("current")
_LdapServerIPv4Address_Type = IpAddress
_LdapServerIPv4Address_Object = MibScalar
ldapServerIPv4Address = _LdapServerIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 2),
    _LdapServerIPv4Address_Type()
)
ldapServerIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerIPv4Address.setStatus("current")
_LdapServerIPv6Address_Type = Ipv6Address
_LdapServerIPv6Address_Object = MibScalar
ldapServerIPv6Address = _LdapServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 3),
    _LdapServerIPv6Address_Type()
)
ldapServerIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerIPv6Address.setStatus("current")


class _LdapServerPort_Type(Integer32):
    """Custom type ldapServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LdapServerPort_Type.__name__ = "Integer32"
_LdapServerPort_Object = MibScalar
ldapServerPort = _LdapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 4),
    _LdapServerPort_Type()
)
ldapServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerPort.setStatus("current")


class _LdapServerSSLConfig_Type(Integer32):
    """Custom type ldapServerSSLConfig based on Integer32"""
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


_LdapServerSSLConfig_Type.__name__ = "Integer32"
_LdapServerSSLConfig_Object = MibScalar
ldapServerSSLConfig = _LdapServerSSLConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 5),
    _LdapServerSSLConfig_Type()
)
ldapServerSSLConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerSSLConfig.setStatus("current")


class _LdapServerBaseDN_Type(DisplayString):
    """Custom type ldapServerBaseDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_LdapServerBaseDN_Type.__name__ = "DisplayString"
_LdapServerBaseDN_Object = MibScalar
ldapServerBaseDN = _LdapServerBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 6),
    _LdapServerBaseDN_Type()
)
ldapServerBaseDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerBaseDN.setStatus("current")


class _LdapServerUserName_Type(DisplayString):
    """Custom type ldapServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_LdapServerUserName_Type.__name__ = "DisplayString"
_LdapServerUserName_Object = MibScalar
ldapServerUserName = _LdapServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 7),
    _LdapServerUserName_Type()
)
ldapServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerUserName.setStatus("current")


class _LdapServerPassword_Type(DisplayString):
    """Custom type ldapServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_LdapServerPassword_Type.__name__ = "DisplayString"
_LdapServerPassword_Object = MibScalar
ldapServerPassword = _LdapServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 8),
    _LdapServerPassword_Type()
)
ldapServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerPassword.setStatus("current")


class _LdapServerConfigAction_Type(Integer32):
    """Custom type ldapServerConfigAction based on Integer32"""
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


_LdapServerConfigAction_Type.__name__ = "Integer32"
_LdapServerConfigAction_Object = MibScalar
ldapServerConfigAction = _LdapServerConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 9),
    _LdapServerConfigAction_Type()
)
ldapServerConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerConfigAction.setStatus("current")


class _LdapServerConfigStatus_Type(Integer32):
    """Custom type ldapServerConfigStatus based on Integer32"""
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
        *(("disConnected", 1),
          ("inProgress", 2),
          ("connected", 3),
          ("sslError", 4),
          ("baseDNError", 5),
          ("credError", 6),
          ("ldapServerError", 7),
          ("ldapServerTimeoutError", 8),
          ("ldapServerConnectionError", 9))
    )


_LdapServerConfigStatus_Type.__name__ = "Integer32"
_LdapServerConfigStatus_Object = MibScalar
ldapServerConfigStatus = _LdapServerConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 42, 1, 10),
    _LdapServerConfigStatus_Type()
)
ldapServerConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServerConfigStatus.setStatus("current")
_NtbaChannelCfgGrp_ObjectIdentity = ObjectIdentity
ntbaChannelCfgGrp = _NtbaChannelCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43)
)


class _NtbaServerIPAddressType_Type(Integer32):
    """Custom type ntbaServerIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_NtbaServerIPAddressType_Type.__name__ = "Integer32"
_NtbaServerIPAddressType_Object = MibScalar
ntbaServerIPAddressType = _NtbaServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 1),
    _NtbaServerIPAddressType_Type()
)
ntbaServerIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntbaServerIPAddressType.setStatus("current")
_NtbaServerIPv4Address_Type = IpAddress
_NtbaServerIPv4Address_Object = MibScalar
ntbaServerIPv4Address = _NtbaServerIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 2),
    _NtbaServerIPv4Address_Type()
)
ntbaServerIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntbaServerIPv4Address.setStatus("current")
_NtbaServerIPv6Address_Type = Ipv6Address
_NtbaServerIPv6Address_Object = MibScalar
ntbaServerIPv6Address = _NtbaServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 3),
    _NtbaServerIPv6Address_Type()
)
ntbaServerIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntbaServerIPv6Address.setStatus("current")


class _NtbaServerPort_Type(Integer32):
    """Custom type ntbaServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtbaServerPort_Type.__name__ = "Integer32"
_NtbaServerPort_Object = MibScalar
ntbaServerPort = _NtbaServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 4),
    _NtbaServerPort_Type()
)
ntbaServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntbaServerPort.setStatus("current")


class _NtbaServerConnectionConfig_Type(Integer32):
    """Custom type ntbaServerConnectionConfig based on Integer32"""
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


_NtbaServerConnectionConfig_Type.__name__ = "Integer32"
_NtbaServerConnectionConfig_Object = MibScalar
ntbaServerConnectionConfig = _NtbaServerConnectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 5),
    _NtbaServerConnectionConfig_Type()
)
ntbaServerConnectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntbaServerConnectionConfig.setStatus("current")


class _NtbaServerDeleteCertificate_Type(Integer32):
    """Custom type ntbaServerDeleteCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("dont-delete", 2))
    )


_NtbaServerDeleteCertificate_Type.__name__ = "Integer32"
_NtbaServerDeleteCertificate_Object = MibScalar
ntbaServerDeleteCertificate = _NtbaServerDeleteCertificate_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 6),
    _NtbaServerDeleteCertificate_Type()
)
ntbaServerDeleteCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntbaServerDeleteCertificate.setStatus("current")


class _NtbaServerCertificateStatus_Type(Integer32):
    """Custom type ntbaServerCertificateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("not-present", 2))
    )


_NtbaServerCertificateStatus_Type.__name__ = "Integer32"
_NtbaServerCertificateStatus_Object = MibScalar
ntbaServerCertificateStatus = _NtbaServerCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 7),
    _NtbaServerCertificateStatus_Type()
)
ntbaServerCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntbaServerCertificateStatus.setStatus("current")


class _NtbaShdKeySHAValue_Type(OctetString):
    """Custom type ntbaShdKeySHAValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_NtbaShdKeySHAValue_Type.__name__ = "OctetString"
_NtbaShdKeySHAValue_Object = MibScalar
ntbaShdKeySHAValue = _NtbaShdKeySHAValue_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 8),
    _NtbaShdKeySHAValue_Type()
)
ntbaShdKeySHAValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntbaShdKeySHAValue.setStatus("current")


class _NtbaChannelStatus_Type(Integer32):
    """Custom type ntbaChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ntba-Channel-Down", 0),
          ("ntba-Channel-InProgress", 1),
          ("ntba-Channel-Established", 2),
          ("ntba-Channel-Status-Unknown", 3),
          ("ntba-Cert-Mismatch", 4),
          ("ntba-Hash-Mismatch", 5),
          ("ntba-Network-Issue", 6))
    )


_NtbaChannelStatus_Type.__name__ = "Integer32"
_NtbaChannelStatus_Object = MibScalar
ntbaChannelStatus = _NtbaChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 43, 9),
    _NtbaChannelStatus_Type()
)
ntbaChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntbaChannelStatus.setStatus("current")
_ValidEdgeChannelCfgGrp_ObjectIdentity = ObjectIdentity
validEdgeChannelCfgGrp = _ValidEdgeChannelCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44)
)


class _ValidEdgeServerIPAddressType_Type(Integer32):
    """Custom type validEdgeServerIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_ValidEdgeServerIPAddressType_Type.__name__ = "Integer32"
_ValidEdgeServerIPAddressType_Object = MibScalar
validEdgeServerIPAddressType = _ValidEdgeServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 1),
    _ValidEdgeServerIPAddressType_Type()
)
validEdgeServerIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeServerIPAddressType.setStatus("current")
_ValidEdgeServerIPv4Address_Type = IpAddress
_ValidEdgeServerIPv4Address_Object = MibScalar
validEdgeServerIPv4Address = _ValidEdgeServerIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 2),
    _ValidEdgeServerIPv4Address_Type()
)
validEdgeServerIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeServerIPv4Address.setStatus("current")
_ValidEdgeServerIPv6Address_Type = Ipv6Address
_ValidEdgeServerIPv6Address_Object = MibScalar
validEdgeServerIPv6Address = _ValidEdgeServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 3),
    _ValidEdgeServerIPv6Address_Type()
)
validEdgeServerIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeServerIPv6Address.setStatus("current")


class _ValidEdgeServerPort_Type(Integer32):
    """Custom type validEdgeServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ValidEdgeServerPort_Type.__name__ = "Integer32"
_ValidEdgeServerPort_Object = MibScalar
validEdgeServerPort = _ValidEdgeServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 4),
    _ValidEdgeServerPort_Type()
)
validEdgeServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeServerPort.setStatus("current")


class _ValidEdgeServerConnectionConfig_Type(Integer32):
    """Custom type validEdgeServerConnectionConfig based on Integer32"""
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


_ValidEdgeServerConnectionConfig_Type.__name__ = "Integer32"
_ValidEdgeServerConnectionConfig_Object = MibScalar
validEdgeServerConnectionConfig = _ValidEdgeServerConnectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 5),
    _ValidEdgeServerConnectionConfig_Type()
)
validEdgeServerConnectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeServerConnectionConfig.setStatus("current")


class _ValidEdgeServerDeleteCertificate_Type(Integer32):
    """Custom type validEdgeServerDeleteCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("dont-delete", 2))
    )


_ValidEdgeServerDeleteCertificate_Type.__name__ = "Integer32"
_ValidEdgeServerDeleteCertificate_Object = MibScalar
validEdgeServerDeleteCertificate = _ValidEdgeServerDeleteCertificate_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 6),
    _ValidEdgeServerDeleteCertificate_Type()
)
validEdgeServerDeleteCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeServerDeleteCertificate.setStatus("current")


class _ValidEdgeServerCertificateStatus_Type(Integer32):
    """Custom type validEdgeServerCertificateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("not-present", 2))
    )


_ValidEdgeServerCertificateStatus_Type.__name__ = "Integer32"
_ValidEdgeServerCertificateStatus_Object = MibScalar
validEdgeServerCertificateStatus = _ValidEdgeServerCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 7),
    _ValidEdgeServerCertificateStatus_Type()
)
validEdgeServerCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    validEdgeServerCertificateStatus.setStatus("current")


class _ValidEdgeShdKeySHAValue_Type(OctetString):
    """Custom type validEdgeShdKeySHAValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_ValidEdgeShdKeySHAValue_Type.__name__ = "OctetString"
_ValidEdgeShdKeySHAValue_Object = MibScalar
validEdgeShdKeySHAValue = _ValidEdgeShdKeySHAValue_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 8),
    _ValidEdgeShdKeySHAValue_Type()
)
validEdgeShdKeySHAValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeShdKeySHAValue.setStatus("current")


class _ValidEdgeChannelStatus_Type(Integer32):
    """Custom type validEdgeChannelStatus based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("validEdge-Channel-Down", 0),
          ("validEdge-Channel-InProgress", 1),
          ("validEdge-Channel-Established", 2),
          ("validEdge-Channel-Status-Unknown", 3),
          ("validEdge-Cert-Mismatch", 4),
          ("validEdge-Hash-Mismatch", 5),
          ("validEdge-Network-Issue", 6),
          ("validEdge-Channel-Down-Error-In-Cert-ret", 7),
          ("validEdge-Channel-Down-No-Config", 8),
          ("validEdge-Channel-Down-Wrong-Config", 9),
          ("validEdge-Channel-Down-Cert-Absent", 10),
          ("validEdge-Channel-SSL-HandShake-Fail", 11),
          ("validEdge-Channel-Down-Reason-Unknown", 12),
          ("validEdge-Channel-Down-Config-Disable", 13),
          ("validEdge-Channel-Down-Closed-By-NTBA", 14),
          ("validEdge-Channel-Down-Large-Pkt-From-NTBA", 15),
          ("validEdge-Channel-Down-Missed-KeepAlives", 16),
          ("validEdge-Channel-Up-No-Reason", 17))
    )


_ValidEdgeChannelStatus_Type.__name__ = "Integer32"
_ValidEdgeChannelStatus_Object = MibScalar
validEdgeChannelStatus = _ValidEdgeChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 9),
    _ValidEdgeChannelStatus_Type()
)
validEdgeChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    validEdgeChannelStatus.setStatus("current")
_ValidEdgeChannelGlobalUserId_Type = Integer32
_ValidEdgeChannelGlobalUserId_Object = MibScalar
validEdgeChannelGlobalUserId = _ValidEdgeChannelGlobalUserId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 10),
    _ValidEdgeChannelGlobalUserId_Type()
)
validEdgeChannelGlobalUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeChannelGlobalUserId.setStatus("current")


class _ValidEdgeChannelGlobalUserName_Type(OctetString):
    """Custom type validEdgeChannelGlobalUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_ValidEdgeChannelGlobalUserName_Type.__name__ = "OctetString"
_ValidEdgeChannelGlobalUserName_Object = MibScalar
validEdgeChannelGlobalUserName = _ValidEdgeChannelGlobalUserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 44, 11),
    _ValidEdgeChannelGlobalUserName_Type()
)
validEdgeChannelGlobalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validEdgeChannelGlobalUserName.setStatus("current")
_DxlCfgGrp_ObjectIdentity = ObjectIdentity
dxlCfgGrp = _DxlCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 45)
)
_DxlConfig_Type = TruthValue
_DxlConfig_Object = MibScalar
dxlConfig = _DxlConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 45, 1),
    _DxlConfig_Type()
)
dxlConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxlConfig.setStatus("current")
_EpoCfgGrp_ObjectIdentity = ObjectIdentity
epoCfgGrp = _EpoCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 46)
)


class _EpoIPAddressType_Type(Integer32):
    """Custom type epoIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_EpoIPAddressType_Type.__name__ = "Integer32"
_EpoIPAddressType_Object = MibScalar
epoIPAddressType = _EpoIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 46, 1),
    _EpoIPAddressType_Type()
)
epoIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epoIPAddressType.setStatus("current")
_EpoIpAddress_Type = IpAddress
_EpoIpAddress_Object = MibScalar
epoIpAddress = _EpoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 46, 2),
    _EpoIpAddress_Type()
)
epoIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epoIpAddress.setStatus("current")
_EpoIPv6Address_Type = Ipv6Address
_EpoIPv6Address_Object = MibScalar
epoIPv6Address = _EpoIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 46, 3),
    _EpoIPv6Address_Type()
)
epoIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epoIPv6Address.setStatus("current")


class _EpoPort_Type(Integer32):
    """Custom type epoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EpoPort_Type.__name__ = "Integer32"
_EpoPort_Object = MibScalar
epoPort = _EpoPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 46, 4),
    _EpoPort_Type()
)
epoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epoPort.setStatus("current")


class _EpoCredUsername_Type(DisplayString):
    """Custom type epoCredUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 100),
    )


_EpoCredUsername_Type.__name__ = "DisplayString"
_EpoCredUsername_Object = MibScalar
epoCredUsername = _EpoCredUsername_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 46, 5),
    _EpoCredUsername_Type()
)
epoCredUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epoCredUsername.setStatus("current")


class _EpoCredPasswd_Type(DisplayString):
    """Custom type epoCredPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 100),
    )


_EpoCredPasswd_Type.__name__ = "DisplayString"
_EpoCredPasswd_Object = MibScalar
epoCredPasswd = _EpoCredPasswd_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 46, 6),
    _EpoCredPasswd_Type()
)
epoCredPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epoCredPasswd.setStatus("current")


class _EpoAction_Type(Integer32):
    """Custom type epoAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("disconnect", 2),
          ("reconnect", 3))
    )


_EpoAction_Type.__name__ = "Integer32"
_EpoAction_Object = MibScalar
epoAction = _EpoAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 46, 7),
    _EpoAction_Type()
)
epoAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epoAction.setStatus("current")
_RadiusAuthGrp_ObjectIdentity = ObjectIdentity
radiusAuthGrp = _RadiusAuthGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47)
)


class _RadiusAuthConfig_Type(Integer32):
    """Custom type radiusAuthConfig based on Integer32"""
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


_RadiusAuthConfig_Type.__name__ = "Integer32"
_RadiusAuthConfig_Object = MibScalar
radiusAuthConfig = _RadiusAuthConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 1),
    _RadiusAuthConfig_Type()
)
radiusAuthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthConfig.setStatus("current")


class _RadiusPrimaryServerIPAddrType_Type(Integer32):
    """Custom type radiusPrimaryServerIPAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_RadiusPrimaryServerIPAddrType_Type.__name__ = "Integer32"
_RadiusPrimaryServerIPAddrType_Object = MibScalar
radiusPrimaryServerIPAddrType = _RadiusPrimaryServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 2),
    _RadiusPrimaryServerIPAddrType_Type()
)
radiusPrimaryServerIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimaryServerIPAddrType.setStatus("current")
_RadiusPrimaryServerIPAddr_Type = IpAddress
_RadiusPrimaryServerIPAddr_Object = MibScalar
radiusPrimaryServerIPAddr = _RadiusPrimaryServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 3),
    _RadiusPrimaryServerIPAddr_Type()
)
radiusPrimaryServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimaryServerIPAddr.setStatus("current")
_RadiusPrimaryServerIPv6Addr_Type = Ipv6Address
_RadiusPrimaryServerIPv6Addr_Object = MibScalar
radiusPrimaryServerIPv6Addr = _RadiusPrimaryServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 4),
    _RadiusPrimaryServerIPv6Addr_Type()
)
radiusPrimaryServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimaryServerIPv6Addr.setStatus("current")


class _RadiusPrimaryServerEncrSecret_Type(DisplayString):
    """Custom type radiusPrimaryServerEncrSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RadiusPrimaryServerEncrSecret_Type.__name__ = "DisplayString"
_RadiusPrimaryServerEncrSecret_Object = MibScalar
radiusPrimaryServerEncrSecret = _RadiusPrimaryServerEncrSecret_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 5),
    _RadiusPrimaryServerEncrSecret_Type()
)
radiusPrimaryServerEncrSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimaryServerEncrSecret.setStatus("current")


class _RadiusPriServerAuthPort_Type(Integer32):
    """Custom type radiusPriServerAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusPriServerAuthPort_Type.__name__ = "Integer32"
_RadiusPriServerAuthPort_Object = MibScalar
radiusPriServerAuthPort = _RadiusPriServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 6),
    _RadiusPriServerAuthPort_Type()
)
radiusPriServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPriServerAuthPort.setStatus("current")
_RadiusPriServerAccConfig_Type = TruthValue
_RadiusPriServerAccConfig_Object = MibScalar
radiusPriServerAccConfig = _RadiusPriServerAccConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 7),
    _RadiusPriServerAccConfig_Type()
)
radiusPriServerAccConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPriServerAccConfig.setStatus("current")


class _RadiusPriServerAccPort_Type(Integer32):
    """Custom type radiusPriServerAccPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusPriServerAccPort_Type.__name__ = "Integer32"
_RadiusPriServerAccPort_Object = MibScalar
radiusPriServerAccPort = _RadiusPriServerAccPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 8),
    _RadiusPriServerAccPort_Type()
)
radiusPriServerAccPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPriServerAccPort.setStatus("current")


class _RadiusPriServerConnTimeOut_Type(Integer32):
    """Custom type radiusPriServerConnTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RadiusPriServerConnTimeOut_Type.__name__ = "Integer32"
_RadiusPriServerConnTimeOut_Object = MibScalar
radiusPriServerConnTimeOut = _RadiusPriServerConnTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 9),
    _RadiusPriServerConnTimeOut_Type()
)
radiusPriServerConnTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPriServerConnTimeOut.setStatus("current")


class _RadiusBackupServerIPAddrType_Type(Integer32):
    """Custom type radiusBackupServerIPAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_RadiusBackupServerIPAddrType_Type.__name__ = "Integer32"
_RadiusBackupServerIPAddrType_Object = MibScalar
radiusBackupServerIPAddrType = _RadiusBackupServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 10),
    _RadiusBackupServerIPAddrType_Type()
)
radiusBackupServerIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusBackupServerIPAddrType.setStatus("current")
_RadiusBackupServerIPAddr_Type = IpAddress
_RadiusBackupServerIPAddr_Object = MibScalar
radiusBackupServerIPAddr = _RadiusBackupServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 11),
    _RadiusBackupServerIPAddr_Type()
)
radiusBackupServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusBackupServerIPAddr.setStatus("current")
_RadiusBackupServerIPv6Addr_Type = Ipv6Address
_RadiusBackupServerIPv6Addr_Object = MibScalar
radiusBackupServerIPv6Addr = _RadiusBackupServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 12),
    _RadiusBackupServerIPv6Addr_Type()
)
radiusBackupServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusBackupServerIPv6Addr.setStatus("current")


class _RadiusBackupServerEncrSecret_Type(DisplayString):
    """Custom type radiusBackupServerEncrSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RadiusBackupServerEncrSecret_Type.__name__ = "DisplayString"
_RadiusBackupServerEncrSecret_Object = MibScalar
radiusBackupServerEncrSecret = _RadiusBackupServerEncrSecret_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 13),
    _RadiusBackupServerEncrSecret_Type()
)
radiusBackupServerEncrSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusBackupServerEncrSecret.setStatus("current")


class _RadiusBackupServerAuthPort_Type(Integer32):
    """Custom type radiusBackupServerAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusBackupServerAuthPort_Type.__name__ = "Integer32"
_RadiusBackupServerAuthPort_Object = MibScalar
radiusBackupServerAuthPort = _RadiusBackupServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 14),
    _RadiusBackupServerAuthPort_Type()
)
radiusBackupServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusBackupServerAuthPort.setStatus("current")
_RadiusBackupServerAccConfig_Type = TruthValue
_RadiusBackupServerAccConfig_Object = MibScalar
radiusBackupServerAccConfig = _RadiusBackupServerAccConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 15),
    _RadiusBackupServerAccConfig_Type()
)
radiusBackupServerAccConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusBackupServerAccConfig.setStatus("current")


class _RadiusBackupServerAccPort_Type(Integer32):
    """Custom type radiusBackupServerAccPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusBackupServerAccPort_Type.__name__ = "Integer32"
_RadiusBackupServerAccPort_Object = MibScalar
radiusBackupServerAccPort = _RadiusBackupServerAccPort_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 16),
    _RadiusBackupServerAccPort_Type()
)
radiusBackupServerAccPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusBackupServerAccPort.setStatus("current")


class _RadiusBackupServerConnTimeOut_Type(Integer32):
    """Custom type radiusBackupServerConnTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RadiusBackupServerConnTimeOut_Type.__name__ = "Integer32"
_RadiusBackupServerConnTimeOut_Object = MibScalar
radiusBackupServerConnTimeOut = _RadiusBackupServerConnTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 47, 17),
    _RadiusBackupServerConnTimeOut_Type()
)
radiusBackupServerConnTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusBackupServerConnTimeOut.setStatus("current")
_SshAccessGrp_ObjectIdentity = ObjectIdentity
sshAccessGrp = _SshAccessGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48)
)
_SshAccessCfgGrp_ObjectIdentity = ObjectIdentity
sshAccessCfgGrp = _SshAccessCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 1)
)
_SshAccessControlStatus_Type = TruthValue
_SshAccessControlStatus_Object = MibScalar
sshAccessControlStatus = _SshAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 1, 1),
    _SshAccessControlStatus_Type()
)
sshAccessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAccessControlStatus.setStatus("current")
_SshAccessControlResetIpv4_Type = TruthValue
_SshAccessControlResetIpv4_Object = MibScalar
sshAccessControlResetIpv4 = _SshAccessControlResetIpv4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 1, 2),
    _SshAccessControlResetIpv4_Type()
)
sshAccessControlResetIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAccessControlResetIpv4.setStatus("current")
_SshAccessLogSupport_Type = TruthValue
_SshAccessLogSupport_Object = MibScalar
sshAccessLogSupport = _SshAccessLogSupport_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 1, 3),
    _SshAccessLogSupport_Type()
)
sshAccessLogSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAccessLogSupport.setStatus("current")
_SshAccessControlResetIpv6_Type = TruthValue
_SshAccessControlResetIpv6_Object = MibScalar
sshAccessControlResetIpv6 = _SshAccessControlResetIpv6_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 1, 4),
    _SshAccessControlResetIpv6_Type()
)
sshAccessControlResetIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAccessControlResetIpv6.setStatus("current")


class _SshAccessNumIpv4Entries_Type(Integer32):
    """Custom type sshAccessNumIpv4Entries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SshAccessNumIpv4Entries_Type.__name__ = "Integer32"
_SshAccessNumIpv4Entries_Object = MibScalar
sshAccessNumIpv4Entries = _SshAccessNumIpv4Entries_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 2),
    _SshAccessNumIpv4Entries_Type()
)
sshAccessNumIpv4Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshAccessNumIpv4Entries.setStatus("current")
_SshAccessIpTable_Object = MibTable
sshAccessIpTable = _SshAccessIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 3)
)
if mibBuilder.loadTexts:
    sshAccessIpTable.setStatus("current")
_SshAccessIpEntry_Object = MibTableRow
sshAccessIpEntry = _SshAccessIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 3, 1)
)
sshAccessIpEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "sshIpv4Index"),
)
if mibBuilder.loadTexts:
    sshAccessIpEntry.setStatus("current")
_SshIpv4Index_Type = Integer32
_SshIpv4Index_Object = MibTableColumn
sshIpv4Index = _SshIpv4Index_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 3, 1, 1),
    _SshIpv4Index_Type()
)
sshIpv4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshIpv4Index.setStatus("current")
_SshIpAddress_Type = IpAddress
_SshIpAddress_Object = MibTableColumn
sshIpAddress = _SshIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 3, 1, 2),
    _SshIpAddress_Type()
)
sshIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshIpAddress.setStatus("current")


class _SshMaskIpv4_Type(Integer32):
    """Custom type sshMaskIpv4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SshMaskIpv4_Type.__name__ = "Integer32"
_SshMaskIpv4_Object = MibTableColumn
sshMaskIpv4 = _SshMaskIpv4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 3, 1, 3),
    _SshMaskIpv4_Type()
)
sshMaskIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshMaskIpv4.setStatus("current")
_SshAccessIpConfig_Type = RowStatus
_SshAccessIpConfig_Object = MibTableColumn
sshAccessIpConfig = _SshAccessIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 3, 1, 4),
    _SshAccessIpConfig_Type()
)
sshAccessIpConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sshAccessIpConfig.setStatus("current")


class _SshAccessNumIpv6Entries_Type(Integer32):
    """Custom type sshAccessNumIpv6Entries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SshAccessNumIpv6Entries_Type.__name__ = "Integer32"
_SshAccessNumIpv6Entries_Object = MibScalar
sshAccessNumIpv6Entries = _SshAccessNumIpv6Entries_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 4),
    _SshAccessNumIpv6Entries_Type()
)
sshAccessNumIpv6Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshAccessNumIpv6Entries.setStatus("current")
_SshAccessIpv6Table_Object = MibTable
sshAccessIpv6Table = _SshAccessIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 5)
)
if mibBuilder.loadTexts:
    sshAccessIpv6Table.setStatus("current")
_SshAccessIpv6Entry_Object = MibTableRow
sshAccessIpv6Entry = _SshAccessIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 5, 1)
)
sshAccessIpv6Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-CONF-MIB", "sshIpv6Index"),
)
if mibBuilder.loadTexts:
    sshAccessIpv6Entry.setStatus("current")
_SshIpv6Index_Type = Integer32
_SshIpv6Index_Object = MibTableColumn
sshIpv6Index = _SshIpv6Index_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 5, 1, 1),
    _SshIpv6Index_Type()
)
sshIpv6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshIpv6Index.setStatus("current")
_SshAccessIpv6Address_Type = Ipv6Address
_SshAccessIpv6Address_Object = MibTableColumn
sshAccessIpv6Address = _SshAccessIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 5, 1, 2),
    _SshAccessIpv6Address_Type()
)
sshAccessIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAccessIpv6Address.setStatus("current")


class _SshAccessIpv6Mask_Type(Integer32):
    """Custom type sshAccessIpv6Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SshAccessIpv6Mask_Type.__name__ = "Integer32"
_SshAccessIpv6Mask_Object = MibTableColumn
sshAccessIpv6Mask = _SshAccessIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 5, 1, 3),
    _SshAccessIpv6Mask_Type()
)
sshAccessIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAccessIpv6Mask.setStatus("current")
_SshAccessIpv6Config_Type = RowStatus
_SshAccessIpv6Config_Object = MibTableColumn
sshAccessIpv6Config = _SshAccessIpv6Config_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 48, 5, 1, 4),
    _SshAccessIpv6Config_Type()
)
sshAccessIpv6Config.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sshAccessIpv6Config.setStatus("current")
_VirtualPluggableModuleGrp_ObjectIdentity = ObjectIdentity
virtualPluggableModuleGrp = _VirtualPluggableModuleGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 49)
)


class _ModuleOneNumPorts_Type(Integer32):
    """Custom type moduleOneNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ModuleOneNumPorts_Type.__name__ = "Integer32"
_ModuleOneNumPorts_Object = MibScalar
moduleOneNumPorts = _ModuleOneNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 49, 1),
    _ModuleOneNumPorts_Type()
)
moduleOneNumPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleOneNumPorts.setStatus("current")


class _ModuleTwoNumPorts_Type(Integer32):
    """Custom type moduleTwoNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ModuleTwoNumPorts_Type.__name__ = "Integer32"
_ModuleTwoNumPorts_Object = MibScalar
moduleTwoNumPorts = _ModuleTwoNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 49, 2),
    _ModuleTwoNumPorts_Type()
)
moduleTwoNumPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleTwoNumPorts.setStatus("current")
_SslProbeAccessGrp_ObjectIdentity = ObjectIdentity
sslProbeAccessGrp = _SslProbeAccessGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51)
)
_SslProbeAccessCfgGrp_ObjectIdentity = ObjectIdentity
sslProbeAccessCfgGrp = _SslProbeAccessCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 1)
)


class _SslProbeAccessMaxAgentConn_Type(Integer32):
    """Custom type sslProbeAccessMaxAgentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SslProbeAccessMaxAgentConn_Type.__name__ = "Integer32"
_SslProbeAccessMaxAgentConn_Object = MibScalar
sslProbeAccessMaxAgentConn = _SslProbeAccessMaxAgentConn_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 1, 1),
    _SslProbeAccessMaxAgentConn_Type()
)
sslProbeAccessMaxAgentConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProbeAccessMaxAgentConn.setStatus("current")


class _SslProbeAccessNumIpv4Entries_Type(Integer32):
    """Custom type sslProbeAccessNumIpv4Entries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SslProbeAccessNumIpv4Entries_Type.__name__ = "Integer32"
_SslProbeAccessNumIpv4Entries_Object = MibScalar
sslProbeAccessNumIpv4Entries = _SslProbeAccessNumIpv4Entries_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 2),
    _SslProbeAccessNumIpv4Entries_Type()
)
sslProbeAccessNumIpv4Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProbeAccessNumIpv4Entries.setStatus("current")
_SslProbeAccessIpTable_Object = MibTable
sslProbeAccessIpTable = _SslProbeAccessIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 3)
)
if mibBuilder.loadTexts:
    sslProbeAccessIpTable.setStatus("current")
_SslProbeAccessIpEntry_Object = MibTableRow
sslProbeAccessIpEntry = _SslProbeAccessIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 3, 1)
)
sslProbeAccessIpEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "sslProbeIpv4Index"),
)
if mibBuilder.loadTexts:
    sslProbeAccessIpEntry.setStatus("current")
_SslProbeIpAddress_Type = IpAddress
_SslProbeIpAddress_Object = MibTableColumn
sslProbeIpAddress = _SslProbeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 3, 1, 1),
    _SslProbeIpAddress_Type()
)
sslProbeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProbeIpAddress.setStatus("current")


class _SslProbeMaskIpv4_Type(Integer32):
    """Custom type sslProbeMaskIpv4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SslProbeMaskIpv4_Type.__name__ = "Integer32"
_SslProbeMaskIpv4_Object = MibTableColumn
sslProbeMaskIpv4 = _SslProbeMaskIpv4_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 3, 1, 2),
    _SslProbeMaskIpv4_Type()
)
sslProbeMaskIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProbeMaskIpv4.setStatus("current")
_SslProbeAccessIpConfig_Type = RowStatus
_SslProbeAccessIpConfig_Object = MibTableColumn
sslProbeAccessIpConfig = _SslProbeAccessIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 3, 1, 3),
    _SslProbeAccessIpConfig_Type()
)
sslProbeAccessIpConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sslProbeAccessIpConfig.setStatus("current")


class _SslProbeAccessNumIpv6Entries_Type(Integer32):
    """Custom type sslProbeAccessNumIpv6Entries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SslProbeAccessNumIpv6Entries_Type.__name__ = "Integer32"
_SslProbeAccessNumIpv6Entries_Object = MibScalar
sslProbeAccessNumIpv6Entries = _SslProbeAccessNumIpv6Entries_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 4),
    _SslProbeAccessNumIpv6Entries_Type()
)
sslProbeAccessNumIpv6Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProbeAccessNumIpv6Entries.setStatus("current")
_SslProbeAccessIpv6Table_Object = MibTable
sslProbeAccessIpv6Table = _SslProbeAccessIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 5)
)
if mibBuilder.loadTexts:
    sslProbeAccessIpv6Table.setStatus("current")
_SslProbeAccessIpv6Entry_Object = MibTableRow
sslProbeAccessIpv6Entry = _SslProbeAccessIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 5, 1)
)
sslProbeAccessIpv6Entry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "sslProbeIpv6Index"),
)
if mibBuilder.loadTexts:
    sslProbeAccessIpv6Entry.setStatus("current")
_SslProbeAccessIpv6Address_Type = Ipv6Address
_SslProbeAccessIpv6Address_Object = MibTableColumn
sslProbeAccessIpv6Address = _SslProbeAccessIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 5, 1, 1),
    _SslProbeAccessIpv6Address_Type()
)
sslProbeAccessIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProbeAccessIpv6Address.setStatus("current")


class _SslProbeAccessIpv6Mask_Type(Integer32):
    """Custom type sslProbeAccessIpv6Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SslProbeAccessIpv6Mask_Type.__name__ = "Integer32"
_SslProbeAccessIpv6Mask_Object = MibTableColumn
sslProbeAccessIpv6Mask = _SslProbeAccessIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 5, 1, 2),
    _SslProbeAccessIpv6Mask_Type()
)
sslProbeAccessIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslProbeAccessIpv6Mask.setStatus("current")
_SslProbeAccessIpv6Config_Type = RowStatus
_SslProbeAccessIpv6Config_Object = MibTableColumn
sslProbeAccessIpv6Config = _SslProbeAccessIpv6Config_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 51, 5, 1, 3),
    _SslProbeAccessIpv6Config_Type()
)
sslProbeAccessIpv6Config.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sslProbeAccessIpv6Config.setStatus("current")
_SensorCertificateGroup_ObjectIdentity = ObjectIdentity
sensorCertificateGroup = _SensorCertificateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52)
)
_SensorCertificateConfigGrp_ObjectIdentity = ObjectIdentity
sensorCertificateConfigGrp = _SensorCertificateConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1)
)
_SensorCertificateCSRConfigGrp_ObjectIdentity = ObjectIdentity
sensorCertificateCSRConfigGrp = _SensorCertificateCSRConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1)
)


class _SensorCertificateCSRCountryName_Type(DisplayString):
    """Custom type sensorCertificateCSRCountryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SensorCertificateCSRCountryName_Type.__name__ = "DisplayString"
_SensorCertificateCSRCountryName_Object = MibScalar
sensorCertificateCSRCountryName = _SensorCertificateCSRCountryName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 1),
    _SensorCertificateCSRCountryName_Type()
)
sensorCertificateCSRCountryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertificateCSRCountryName.setStatus("current")


class _SensorCertificateCSRStateProvince_Type(DisplayString):
    """Custom type sensorCertificateCSRStateProvince based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SensorCertificateCSRStateProvince_Type.__name__ = "DisplayString"
_SensorCertificateCSRStateProvince_Object = MibScalar
sensorCertificateCSRStateProvince = _SensorCertificateCSRStateProvince_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 2),
    _SensorCertificateCSRStateProvince_Type()
)
sensorCertificateCSRStateProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertificateCSRStateProvince.setStatus("current")


class _SensorCertificateCSRLocality_Type(DisplayString):
    """Custom type sensorCertificateCSRLocality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SensorCertificateCSRLocality_Type.__name__ = "DisplayString"
_SensorCertificateCSRLocality_Object = MibScalar
sensorCertificateCSRLocality = _SensorCertificateCSRLocality_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 3),
    _SensorCertificateCSRLocality_Type()
)
sensorCertificateCSRLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertificateCSRLocality.setStatus("current")


class _SensorCertificateCSRCompany_Type(DisplayString):
    """Custom type sensorCertificateCSRCompany based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SensorCertificateCSRCompany_Type.__name__ = "DisplayString"
_SensorCertificateCSRCompany_Object = MibScalar
sensorCertificateCSRCompany = _SensorCertificateCSRCompany_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 4),
    _SensorCertificateCSRCompany_Type()
)
sensorCertificateCSRCompany.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertificateCSRCompany.setStatus("current")


class _SensorCertificateCSROrganizationalUnit_Type(DisplayString):
    """Custom type sensorCertificateCSROrganizationalUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SensorCertificateCSROrganizationalUnit_Type.__name__ = "DisplayString"
_SensorCertificateCSROrganizationalUnit_Object = MibScalar
sensorCertificateCSROrganizationalUnit = _SensorCertificateCSROrganizationalUnit_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 5),
    _SensorCertificateCSROrganizationalUnit_Type()
)
sensorCertificateCSROrganizationalUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertificateCSROrganizationalUnit.setStatus("current")


class _SensorCertificateCSRCommonName_Type(DisplayString):
    """Custom type sensorCertificateCSRCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SensorCertificateCSRCommonName_Type.__name__ = "DisplayString"
_SensorCertificateCSRCommonName_Object = MibScalar
sensorCertificateCSRCommonName = _SensorCertificateCSRCommonName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 6),
    _SensorCertificateCSRCommonName_Type()
)
sensorCertificateCSRCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertificateCSRCommonName.setStatus("current")


class _SensorCertificateCSRGenerateAction_Type(Integer32):
    """Custom type sensorCertificateCSRGenerateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("generateCSR", 1),
          ("generateSelfSigned", 2))
    )


_SensorCertificateCSRGenerateAction_Type.__name__ = "Integer32"
_SensorCertificateCSRGenerateAction_Object = MibScalar
sensorCertificateCSRGenerateAction = _SensorCertificateCSRGenerateAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 7),
    _SensorCertificateCSRGenerateAction_Type()
)
sensorCertificateCSRGenerateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertificateCSRGenerateAction.setStatus("current")


class _SensorCertificateCSRGenerateStatus_Type(Integer32):
    """Custom type sensorCertificateCSRGenerateStatus based on Integer32"""
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
        *(("other", 0),
          ("generationInProgress", 1),
          ("generationComplete", 2),
          ("generationFailed", 3))
    )


_SensorCertificateCSRGenerateStatus_Type.__name__ = "Integer32"
_SensorCertificateCSRGenerateStatus_Object = MibScalar
sensorCertificateCSRGenerateStatus = _SensorCertificateCSRGenerateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 8),
    _SensorCertificateCSRGenerateStatus_Type()
)
sensorCertificateCSRGenerateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCertificateCSRGenerateStatus.setStatus("current")
_SensorCertSubAltName_Type = Integer32
_SensorCertSubAltName_Object = MibScalar
sensorCertSubAltName = _SensorCertSubAltName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 1, 9),
    _SensorCertSubAltName_Type()
)
sensorCertSubAltName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertSubAltName.setStatus("current")


class _SensorCertificateStatus_Type(Integer32):
    """Custom type sensorCertificateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("certAbsent", 1),
          ("defaultCert", 2),
          ("selfsignedCert", 3),
          ("casignedCert", 4))
    )


_SensorCertificateStatus_Type.__name__ = "Integer32"
_SensorCertificateStatus_Object = MibScalar
sensorCertificateStatus = _SensorCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 2),
    _SensorCertificateStatus_Type()
)
sensorCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCertificateStatus.setStatus("current")
_SensorCertMigrateAction_Type = Integer32
_SensorCertMigrateAction_Object = MibScalar
sensorCertMigrateAction = _SensorCertMigrateAction_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 52, 1, 3),
    _SensorCertMigrateAction_Type()
)
sensorCertMigrateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorCertMigrateAction.setStatus("current")
_SensorStackGrp_ObjectIdentity = ObjectIdentity
sensorStackGrp = _SensorStackGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 53)
)


class _StackName_Type(DisplayString):
    """Custom type stackName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_StackName_Type.__name__ = "DisplayString"
_StackName_Object = MibScalar
stackName = _StackName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 53, 1),
    _StackName_Type()
)
stackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackName.setStatus("current")


class _StackNodeId_Type(Integer32):
    """Custom type stackNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_StackNodeId_Type.__name__ = "Integer32"
_StackNodeId_Object = MibScalar
stackNodeId = _StackNodeId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 53, 2),
    _StackNodeId_Type()
)
stackNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackNodeId.setStatus("current")


class _StackNodeLeftNeighbour_Type(Integer32):
    """Custom type stackNodeLeftNeighbour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_StackNodeLeftNeighbour_Type.__name__ = "Integer32"
_StackNodeLeftNeighbour_Object = MibScalar
stackNodeLeftNeighbour = _StackNodeLeftNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 53, 3),
    _StackNodeLeftNeighbour_Type()
)
stackNodeLeftNeighbour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackNodeLeftNeighbour.setStatus("current")


class _StackNodeRightNeighbour_Type(Integer32):
    """Custom type stackNodeRightNeighbour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_StackNodeRightNeighbour_Type.__name__ = "Integer32"
_StackNodeRightNeighbour_Object = MibScalar
stackNodeRightNeighbour = _StackNodeRightNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 53, 4),
    _StackNodeRightNeighbour_Type()
)
stackNodeRightNeighbour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackNodeRightNeighbour.setStatus("current")
_InterfaceVirtualPortGrp_ObjectIdentity = ObjectIdentity
interfaceVirtualPortGrp = _InterfaceVirtualPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54)
)
_IntfVirtualPortTable_Object = MibTable
intfVirtualPortTable = _IntfVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1)
)
if mibBuilder.loadTexts:
    intfVirtualPortTable.setStatus("current")
_IntfVirtualPortEntry_Object = MibTableRow
intfVirtualPortEntry = _IntfVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1)
)
intfVirtualPortEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "intfVirtualSlotIndex"),
    (0, "TRELLIX-SENSOR-SMI", "intfVirtualPortIndex"),
)
if mibBuilder.loadTexts:
    intfVirtualPortEntry.setStatus("current")


class _IntfVirtualPortIfDescr_Type(DisplayString):
    """Custom type intfVirtualPortIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IntfVirtualPortIfDescr_Type.__name__ = "DisplayString"
_IntfVirtualPortIfDescr_Object = MibTableColumn
intfVirtualPortIfDescr = _IntfVirtualPortIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 1),
    _IntfVirtualPortIfDescr_Type()
)
intfVirtualPortIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfVirtualPortIfDescr.setStatus("current")
_IntfVirtualPortIfType_Type = TrellixIDSPortType
_IntfVirtualPortIfType_Object = MibTableColumn
intfVirtualPortIfType = _IntfVirtualPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 2),
    _IntfVirtualPortIfType_Type()
)
intfVirtualPortIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortIfType.setStatus("current")


class _IntfVirtualPortIfAdminStatus_Type(Integer32):
    """Custom type intfVirtualPortIfAdminStatus based on Integer32"""
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


_IntfVirtualPortIfAdminStatus_Type.__name__ = "Integer32"
_IntfVirtualPortIfAdminStatus_Object = MibTableColumn
intfVirtualPortIfAdminStatus = _IntfVirtualPortIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 3),
    _IntfVirtualPortIfAdminStatus_Type()
)
intfVirtualPortIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortIfAdminStatus.setStatus("current")
_IntfVirtualPortOperatingMode_Type = TrellixIDSOperatingMode
_IntfVirtualPortOperatingMode_Object = MibTableColumn
intfVirtualPortOperatingMode = _IntfVirtualPortOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 4),
    _IntfVirtualPortOperatingMode_Type()
)
intfVirtualPortOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortOperatingMode.setStatus("current")
_IntfVirtualPortEnableFullDuplex_Type = TruthValue
_IntfVirtualPortEnableFullDuplex_Object = MibTableColumn
intfVirtualPortEnableFullDuplex = _IntfVirtualPortEnableFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 5),
    _IntfVirtualPortEnableFullDuplex_Type()
)
intfVirtualPortEnableFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortEnableFullDuplex.setStatus("current")
_IntfVirtualPortSpeedConfig_Type = TrellixPortSpeed
_IntfVirtualPortSpeedConfig_Object = MibTableColumn
intfVirtualPortSpeedConfig = _IntfVirtualPortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 6),
    _IntfVirtualPortSpeedConfig_Type()
)
intfVirtualPortSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortSpeedConfig.setStatus("current")
_IntfVirtualPortEnableInternalTap_Type = TruthValue
_IntfVirtualPortEnableInternalTap_Object = MibTableColumn
intfVirtualPortEnableInternalTap = _IntfVirtualPortEnableInternalTap_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 7),
    _IntfVirtualPortEnableInternalTap_Type()
)
intfVirtualPortEnableInternalTap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortEnableInternalTap.setStatus("current")


class _IntfVirtualPortInOutType_Type(Integer32):
    """Custom type intfVirtualPortInOutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inside", 1),
          ("outside", 2),
          ("not-specified", 3))
    )


_IntfVirtualPortInOutType_Type.__name__ = "Integer32"
_IntfVirtualPortInOutType_Object = MibTableColumn
intfVirtualPortInOutType = _IntfVirtualPortInOutType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 8),
    _IntfVirtualPortInOutType_Type()
)
intfVirtualPortInOutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortInOutType.setStatus("current")


class _IntfVirtualFailOpenSwitchStatus_Type(Integer32):
    """Custom type intfVirtualFailOpenSwitchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 1),
          ("present", 2),
          ("not-present", 3))
    )


_IntfVirtualFailOpenSwitchStatus_Type.__name__ = "Integer32"
_IntfVirtualFailOpenSwitchStatus_Object = MibTableColumn
intfVirtualFailOpenSwitchStatus = _IntfVirtualFailOpenSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 9),
    _IntfVirtualFailOpenSwitchStatus_Type()
)
intfVirtualFailOpenSwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualFailOpenSwitchStatus.setStatus("current")


class _IntfVirtualFailOpenPortStatus_Type(Integer32):
    """Custom type intfVirtualFailOpenPortStatus based on Integer32"""
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
        *(("not-applicable", 1),
          ("inline-fail-open", 2),
          ("bypass", 3),
          ("tap", 4),
          ("absent", 5),
          ("unknown", 6),
          ("layer2-bypass", 7))
    )


_IntfVirtualFailOpenPortStatus_Type.__name__ = "Integer32"
_IntfVirtualFailOpenPortStatus_Object = MibTableColumn
intfVirtualFailOpenPortStatus = _IntfVirtualFailOpenPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 10),
    _IntfVirtualFailOpenPortStatus_Type()
)
intfVirtualFailOpenPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualFailOpenPortStatus.setStatus("current")


class _IntfVirtualPortEnableAntiSpoofing_Type(Integer32):
    """Custom type intfVirtualPortEnableAntiSpoofing based on Integer32"""
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
        *(("disable-bothsides-spoof-detect", 1),
          ("enable-inside-spoof-detect", 2),
          ("enable-outside-spoof-detect", 3),
          ("enable-bothsides-spoof-detect", 4))
    )


_IntfVirtualPortEnableAntiSpoofing_Type.__name__ = "Integer32"
_IntfVirtualPortEnableAntiSpoofing_Object = MibTableColumn
intfVirtualPortEnableAntiSpoofing = _IntfVirtualPortEnableAntiSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 11),
    _IntfVirtualPortEnableAntiSpoofing_Type()
)
intfVirtualPortEnableAntiSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortEnableAntiSpoofing.setStatus("current")
_IntfVirtualPortAllowAnyConnector_Type = TruthValue
_IntfVirtualPortAllowAnyConnector_Object = MibTableColumn
intfVirtualPortAllowAnyConnector = _IntfVirtualPortAllowAnyConnector_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 12),
    _IntfVirtualPortAllowAnyConnector_Type()
)
intfVirtualPortAllowAnyConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortAllowAnyConnector.setStatus("current")


class _IntfVirtualPortCageType_Type(Integer32):
    """Custom type intfVirtualPortCageType based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("rJ-45", 1),
          ("rJ-11", 2),
          ("gBIC", 3),
          ("sFP", 4),
          ("xFP", 5),
          ("sFP-plus", 6),
          ("qSFP", 7),
          ("rJ-45-plus", 8),
          ("sFP-plus-BPFO", 9))
    )


_IntfVirtualPortCageType_Type.__name__ = "Integer32"
_IntfVirtualPortCageType_Object = MibTableColumn
intfVirtualPortCageType = _IntfVirtualPortCageType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 13),
    _IntfVirtualPortCageType_Type()
)
intfVirtualPortCageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortCageType.setStatus("current")


class _IntfVirtualPortSetMediaType_Type(Integer32):
    """Custom type intfVirtualPortSetMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optical", 1),
          ("electrical", 2))
    )


_IntfVirtualPortSetMediaType_Type.__name__ = "Integer32"
_IntfVirtualPortSetMediaType_Object = MibTableColumn
intfVirtualPortSetMediaType = _IntfVirtualPortSetMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 14),
    _IntfVirtualPortSetMediaType_Type()
)
intfVirtualPortSetMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortSetMediaType.setStatus("current")
_IntfVirtualPortMonPortIpAddress_Type = IpAddress
_IntfVirtualPortMonPortIpAddress_Object = MibTableColumn
intfVirtualPortMonPortIpAddress = _IntfVirtualPortMonPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 15),
    _IntfVirtualPortMonPortIpAddress_Type()
)
intfVirtualPortMonPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortMonPortIpAddress.setStatus("current")
_IntfVirtualPortMonPortNetMask_Type = IpAddress
_IntfVirtualPortMonPortNetMask_Object = MibTableColumn
intfVirtualPortMonPortNetMask = _IntfVirtualPortMonPortNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 16),
    _IntfVirtualPortMonPortNetMask_Type()
)
intfVirtualPortMonPortNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortMonPortNetMask.setStatus("current")
_IntfVirtualPortGatewayIpAddress_Type = IpAddress
_IntfVirtualPortGatewayIpAddress_Object = MibTableColumn
intfVirtualPortGatewayIpAddress = _IntfVirtualPortGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 17),
    _IntfVirtualPortGatewayIpAddress_Type()
)
intfVirtualPortGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortGatewayIpAddress.setStatus("current")
_IntfVirtualPortNbadConfigStatus_Type = TruthValue
_IntfVirtualPortNbadConfigStatus_Object = MibTableColumn
intfVirtualPortNbadConfigStatus = _IntfVirtualPortNbadConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 18),
    _IntfVirtualPortNbadConfigStatus_Type()
)
intfVirtualPortNbadConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortNbadConfigStatus.setStatus("current")


class _IntfVirtualPortVlanId_Type(Integer32):
    """Custom type intfVirtualPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2164326399),
    )


_IntfVirtualPortVlanId_Type.__name__ = "Integer32"
_IntfVirtualPortVlanId_Object = MibTableColumn
intfVirtualPortVlanId = _IntfVirtualPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 19),
    _IntfVirtualPortVlanId_Type()
)
intfVirtualPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortVlanId.setStatus("current")
_IntfVirtualPortAppIdStatsConfigStatus_Type = TruthValue
_IntfVirtualPortAppIdStatsConfigStatus_Object = MibTableColumn
intfVirtualPortAppIdStatsConfigStatus = _IntfVirtualPortAppIdStatsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 20),
    _IntfVirtualPortAppIdStatsConfigStatus_Type()
)
intfVirtualPortAppIdStatsConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortAppIdStatsConfigStatus.setStatus("current")
_IntfVirtualPortLinearIndex_Type = TrellixPortLinearIndex
_IntfVirtualPortLinearIndex_Object = MibTableColumn
intfVirtualPortLinearIndex = _IntfVirtualPortLinearIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 21),
    _IntfVirtualPortLinearIndex_Type()
)
intfVirtualPortLinearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfVirtualPortLinearIndex.setStatus("current")
_IntfVirtualPortFECConfig_Type = TruthValue
_IntfVirtualPortFECConfig_Object = MibTableColumn
intfVirtualPortFECConfig = _IntfVirtualPortFECConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 54, 1, 1, 22),
    _IntfVirtualPortFECConfig_Type()
)
intfVirtualPortFECConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualPortFECConfig.setStatus("current")
_ResponseVirtualPortGrp_ObjectIdentity = ObjectIdentity
responseVirtualPortGrp = _ResponseVirtualPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55)
)
_RespVirtualPortTable_Object = MibTable
respVirtualPortTable = _RespVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1)
)
if mibBuilder.loadTexts:
    respVirtualPortTable.setStatus("current")
_RespVirtualPortEntry_Object = MibTableRow
respVirtualPortEntry = _RespVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1)
)
respVirtualPortEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
    (0, "TRELLIX-SENSOR-SMI", "respPortIndex"),
)
if mibBuilder.loadTexts:
    respVirtualPortEntry.setStatus("current")
_RespVirtualPortDescr_Type = DisplayString
_RespVirtualPortDescr_Object = MibTableColumn
respVirtualPortDescr = _RespVirtualPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 1),
    _RespVirtualPortDescr_Type()
)
respVirtualPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respVirtualPortDescr.setStatus("current")
_RespVirtualPortType_Type = TrellixIDSPortType
_RespVirtualPortType_Object = MibTableColumn
respVirtualPortType = _RespVirtualPortType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 2),
    _RespVirtualPortType_Type()
)
respVirtualPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respVirtualPortType.setStatus("current")


class _RespVirtualPortAdminStatus_Type(Integer32):
    """Custom type respVirtualPortAdminStatus based on Integer32"""
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


_RespVirtualPortAdminStatus_Type.__name__ = "Integer32"
_RespVirtualPortAdminStatus_Object = MibTableColumn
respVirtualPortAdminStatus = _RespVirtualPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 3),
    _RespVirtualPortAdminStatus_Type()
)
respVirtualPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respVirtualPortAdminStatus.setStatus("current")


class _RespVirtualPortOperStatus_Type(Integer32):
    """Custom type respVirtualPortOperStatus based on Integer32"""
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


_RespVirtualPortOperStatus_Type.__name__ = "Integer32"
_RespVirtualPortOperStatus_Object = MibTableColumn
respVirtualPortOperStatus = _RespVirtualPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 4),
    _RespVirtualPortOperStatus_Type()
)
respVirtualPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respVirtualPortOperStatus.setStatus("current")
_RespVirtualPortEnableFullDuplex_Type = TruthValue
_RespVirtualPortEnableFullDuplex_Object = MibTableColumn
respVirtualPortEnableFullDuplex = _RespVirtualPortEnableFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 5),
    _RespVirtualPortEnableFullDuplex_Type()
)
respVirtualPortEnableFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respVirtualPortEnableFullDuplex.setStatus("current")
_RespVirtualPortSpeed_Type = TrellixPortSpeed
_RespVirtualPortSpeed_Object = MibTableColumn
respVirtualPortSpeed = _RespVirtualPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 6),
    _RespVirtualPortSpeed_Type()
)
respVirtualPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respVirtualPortSpeed.setStatus("current")


class _RespVirtualPortPktDestination_Type(Integer32):
    """Custom type respVirtualPortPktDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("router", 2))
    )


_RespVirtualPortPktDestination_Type.__name__ = "Integer32"
_RespVirtualPortPktDestination_Object = MibTableColumn
respVirtualPortPktDestination = _RespVirtualPortPktDestination_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 7),
    _RespVirtualPortPktDestination_Type()
)
respVirtualPortPktDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respVirtualPortPktDestination.setStatus("current")
_RespVirtualPortMacAddress_Type = MacAddress
_RespVirtualPortMacAddress_Object = MibTableColumn
respVirtualPortMacAddress = _RespVirtualPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 8),
    _RespVirtualPortMacAddress_Type()
)
respVirtualPortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respVirtualPortMacAddress.setStatus("current")
_RespVirtualCUGEPortSpeed_Type = TrellixCUGEType
_RespVirtualCUGEPortSpeed_Object = MibTableColumn
respVirtualCUGEPortSpeed = _RespVirtualCUGEPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 9),
    _RespVirtualCUGEPortSpeed_Type()
)
respVirtualCUGEPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    respVirtualCUGEPortSpeed.setStatus("current")


class _RespVirtualAdditionalInfo_Type(DisplayString):
    """Custom type respVirtualAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RespVirtualAdditionalInfo_Type.__name__ = "DisplayString"
_RespVirtualAdditionalInfo_Object = MibTableColumn
respVirtualAdditionalInfo = _RespVirtualAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 1, 1, 11),
    _RespVirtualAdditionalInfo_Type()
)
respVirtualAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respVirtualAdditionalInfo.setStatus("current")
_IntfVirtualRespTable_Object = MibTable
intfVirtualRespTable = _IntfVirtualRespTable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 2)
)
if mibBuilder.loadTexts:
    intfVirtualRespTable.setStatus("current")
_IntfVirtualRespEntry_Object = MibTableRow
intfVirtualRespEntry = _IntfVirtualRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 2, 1)
)
intfVirtualRespEntry.setIndexNames(
    (0, "TRELLIX-SENSOR-SMI", "slotIndex"),
    (0, "TRELLIX-SENSOR-SMI", "intfPortIndex"),
)
if mibBuilder.loadTexts:
    intfVirtualRespEntry.setStatus("current")


class _IntfVirtualRespType_Type(Integer32):
    """Custom type intfVirtualRespType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("responsePort", 1),
          ("inline", 2))
    )


_IntfVirtualRespType_Type.__name__ = "Integer32"
_IntfVirtualRespType_Object = MibTableColumn
intfVirtualRespType = _IntfVirtualRespType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 2, 1, 1),
    _IntfVirtualRespType_Type()
)
intfVirtualRespType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualRespType.setStatus("current")
_IntfVirtualRespPortNo_Type = Integer32
_IntfVirtualRespPortNo_Object = MibTableColumn
intfVirtualRespPortNo = _IntfVirtualRespPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 55, 2, 1, 2),
    _IntfVirtualRespPortNo_Type()
)
intfVirtualRespPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intfVirtualRespPortNo.setStatus("current")
_MvxCfgGrp_ObjectIdentity = ObjectIdentity
mvxCfgGrp = _MvxCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56)
)


class _MvxConnectionConfig_Type(Integer32):
    """Custom type mvxConnectionConfig based on Integer32"""
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


_MvxConnectionConfig_Type.__name__ = "Integer32"
_MvxConnectionConfig_Object = MibScalar
mvxConnectionConfig = _MvxConnectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 1),
    _MvxConnectionConfig_Type()
)
mvxConnectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvxConnectionConfig.setStatus("current")


class _MvxIPAddressType_Type(Integer32):
    """Custom type mvxIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-v4", 4),
          ("ip-v6", 6))
    )


_MvxIPAddressType_Type.__name__ = "Integer32"
_MvxIPAddressType_Object = MibScalar
mvxIPAddressType = _MvxIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 2),
    _MvxIPAddressType_Type()
)
mvxIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvxIPAddressType.setStatus("current")
_MvxBrokerIPv4Address_Type = IpAddress
_MvxBrokerIPv4Address_Object = MibScalar
mvxBrokerIPv4Address = _MvxBrokerIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 3),
    _MvxBrokerIPv4Address_Type()
)
mvxBrokerIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvxBrokerIPv4Address.setStatus("current")
_MvxBrokerIPv6Address_Type = Ipv6Address
_MvxBrokerIPv6Address_Object = MibScalar
mvxBrokerIPv6Address = _MvxBrokerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 4),
    _MvxBrokerIPv6Address_Type()
)
mvxBrokerIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvxBrokerIPv6Address.setStatus("current")


class _MvxUserName_Type(DisplayString):
    """Custom type mvxUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MvxUserName_Type.__name__ = "DisplayString"
_MvxUserName_Object = MibScalar
mvxUserName = _MvxUserName_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 5),
    _MvxUserName_Type()
)
mvxUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvxUserName.setStatus("current")


class _MvxPassword_Type(DisplayString):
    """Custom type mvxPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MvxPassword_Type.__name__ = "DisplayString"
_MvxPassword_Object = MibScalar
mvxPassword = _MvxPassword_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 6),
    _MvxPassword_Type()
)
mvxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvxPassword.setStatus("current")


class _MvxCertificateValidation_Type(Integer32):
    """Custom type mvxCertificateValidation based on Integer32"""
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


_MvxCertificateValidation_Type.__name__ = "Integer32"
_MvxCertificateValidation_Object = MibScalar
mvxCertificateValidation = _MvxCertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 7),
    _MvxCertificateValidation_Type()
)
mvxCertificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvxCertificateValidation.setStatus("current")


class _MvxAuthStatus_Type(Integer32):
    """Custom type mvxAuthStatus based on Integer32"""
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


_MvxAuthStatus_Type.__name__ = "Integer32"
_MvxAuthStatus_Object = MibScalar
mvxAuthStatus = _MvxAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 8),
    _MvxAuthStatus_Type()
)
mvxAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvxAuthStatus.setStatus("current")


class _MvxUseProxy_Type(Integer32):
    """Custom type mvxUseProxy based on Integer32"""
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


_MvxUseProxy_Type.__name__ = "Integer32"
_MvxUseProxy_Object = MibScalar
mvxUseProxy = _MvxUseProxy_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 56, 9),
    _MvxUseProxy_Type()
)
mvxUseProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvxUseProxy.setStatus("current")
_ArpCfgGrp_ObjectIdentity = ObjectIdentity
arpCfgGrp = _ArpCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 103)
)


class _ArpSDEnable_Type(Integer32):
    """Custom type arpSDEnable based on Integer32"""
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


_ArpSDEnable_Type.__name__ = "Integer32"
_ArpSDEnable_Object = MibScalar
arpSDEnable = _ArpSDEnable_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2, 1, 103, 1),
    _ArpSDEnable_Type()
)
arpSDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpSDEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRELLIX-SENSOR-CONF-MIB",
    **{"ivSensorConfigurationMIB": ivSensorConfigurationMIB,
       "systemGrp": systemGrp,
       "ivSysName": ivSysName,
       "ivSysLocation": ivSysLocation,
       "ivSysContact": ivSysContact,
       "ivSysModel": ivSysModel,
       "ivSysSerialNumber": ivSysSerialNumber,
       "ivSysDescr": ivSysDescr,
       "ivSysObjectID": ivSysObjectID,
       "ivSysUpTime": ivSysUpTime,
       "ivSysLastCfgTime": ivSysLastCfgTime,
       "ivSysDiskSpaceLeft": ivSysDiskSpaceLeft,
       "ivSysAlertChannelStatus": ivSysAlertChannelStatus,
       "ivSysPacketLogChannelStatus": ivSysPacketLogChannelStatus,
       "ivSysHealth": ivSysHealth,
       "ivSysResetPassword": ivSysResetPassword,
       "ivSysDeleteSignatures": ivSysDeleteSignatures,
       "ivSysSlaveSerialNumber": ivSysSlaveSerialNumber,
       "ivSysUIDSeed": ivSysUIDSeed,
       "ivSysFipsMode": ivSysFipsMode,
       "ivSysNumLbPorts": ivSysNumLbPorts,
       "ivSysUpTimeNew": ivSysUpTimeNew,
       "ivSysCapacityMode": ivSysCapacityMode,
       "ivSysCurrentCapacityMode": ivSysCurrentCapacityMode,
       "ivSysDeviceMode": ivSysDeviceMode,
       "ivSysConfDeviceMode": ivSysConfDeviceMode,
       "ivSysRebootStatus": ivSysRebootStatus,
       "ivSysRebootReason": ivSysRebootReason,
       "systemIPCfgGrp": systemIPCfgGrp,
       "ivSysIPAddress": ivSysIPAddress,
       "ivSysMACAddress": ivSysMACAddress,
       "ivSysSubnetMask": ivSysSubnetMask,
       "ivSysGateway": ivSysGateway,
       "ivSysIPv6Address": ivSysIPv6Address,
       "ivSysIpv6SubnetMask": ivSysIpv6SubnetMask,
       "ivSysIpv6Gateway": ivSysIpv6Gateway,
       "ivSysVmHostIPAddress": ivSysVmHostIPAddress,
       "ivSysVmHostIPv6Address": ivSysVmHostIPv6Address,
       "ivSysVmHostName": ivSysVmHostName,
       "ivSysVmMgmtAdditionalInfo": ivSysVmMgmtAdditionalInfo,
       "systemFailoverGrp": systemFailoverGrp,
       "ivSysFailoverStatus": ivSysFailoverStatus,
       "ivSysFailoverAction": ivSysFailoverAction,
       "ivSysFailoverMode": ivSysFailoverMode,
       "ivSysFailopenAction": ivSysFailopenAction,
       "ivSysSTPForwardConfig": ivSysSTPForwardConfig,
       "emsGrp": emsGrp,
       "emsTable": emsTable,
       "emsEntry": emsEntry,
       "emsIndex": emsIndex,
       "emsPriority": emsPriority,
       "emsIPAddress": emsIPAddress,
       "emsHAMode": emsHAMode,
       "emsHAStatus": emsHAStatus,
       "emsAlertChannelStatus": emsAlertChannelStatus,
       "emsPacketLogChannelStatus": emsPacketLogChannelStatus,
       "emsIPv6Address": emsIPv6Address,
       "emsIPAddressType": emsIPAddressType,
       "emsAuthChannelStatus": emsAuthChannelStatus,
       "emsChangeAction": emsChangeAction,
       "emsParamIpAddress": emsParamIpAddress,
       "emsParamPriority": emsParamPriority,
       "emsParamAddIpAddress": emsParamAddIpAddress,
       "emsParamIpv6Address": emsParamIpv6Address,
       "emsParamAddIpv6Address": emsParamAddIpv6Address,
       "emsTenantId": emsTenantId,
       "emsPrimaryNSMGUID": emsPrimaryNSMGUID,
       "emsSecondaryNSMGUID": emsSecondaryNSMGUID,
       "tftpGrp": tftpGrp,
       "tftpKey": tftpKey,
       "tftpFileSize": tftpFileSize,
       "tftpFileName": tftpFileName,
       "tftpServerAddress": tftpServerAddress,
       "tftpAction": tftpAction,
       "tftpActionStatus": tftpActionStatus,
       "tftpActionInProgressResult": tftpActionInProgressResult,
       "tftpActionFailedResult": tftpActionFailedResult,
       "tftpActionTransactionId": tftpActionTransactionId,
       "tftpServerIpv6Address": tftpServerIpv6Address,
       "tftpIVKey": tftpIVKey,
       "chassisGrp": chassisGrp,
       "temperatureStatus": temperatureStatus,
       "fanStatus": fanStatus,
       "primaryPowerSupplyStatus": primaryPowerSupplyStatus,
       "secondaryPowerSupplyStatus": secondaryPowerSupplyStatus,
       "pciLegacyErrorStatus": pciLegacyErrorStatus,
       "pciFatalError1Status": pciFatalError1Status,
       "pciFatalError2Status": pciFatalError2Status,
       "systemEventLogStatus": systemEventLogStatus,
       "bmcWatchdogStatus": bmcWatchdogStatus,
       "processorStatusTable": processorStatusTable,
       "processorStatusEntry": processorStatusEntry,
       "processorStatus": processorStatus,
       "memoryECCStatus": memoryECCStatus,
       "postSysEventStatus": postSysEventStatus,
       "postErrorStatus": postErrorStatus,
       "managementCardGrp": managementCardGrp,
       "mgmtCardTable": mgmtCardTable,
       "mgmtCardEntry": mgmtCardEntry,
       "mcAction": mcAction,
       "mcActionStatus": mcActionStatus,
       "mcActionResult": mcActionResult,
       "mcHwVersion": mcHwVersion,
       "mcCurrentSwVersion": mcCurrentSwVersion,
       "mcFutureSwFileName": mcFutureSwFileName,
       "mcDateAndTime": mcDateAndTime,
       "slave-ChassisGrp": slave_ChassisGrp,
       "slaveTemperatureStatus": slaveTemperatureStatus,
       "slaveFanStatus": slaveFanStatus,
       "slavePrimaryPowerSupplyStatus": slavePrimaryPowerSupplyStatus,
       "slaveSecondaryPowerSupplyStatus": slaveSecondaryPowerSupplyStatus,
       "sensorCardGrp": sensorCardGrp,
       "sensorCardTable": sensorCardTable,
       "sensorCardEntry": sensorCardEntry,
       "scAction": scAction,
       "scSigUpdateResult": scSigUpdateResult,
       "scHwVersion": scHwVersion,
       "scCurrentSwVersion": scCurrentSwVersion,
       "scFutureSwFileName": scFutureSwFileName,
       "scCurrentSigVersion": scCurrentSigVersion,
       "scFutureSigFileName": scFutureSigFileName,
       "scMACAddress": scMACAddress,
       "scCurrentBotDATVersion": scCurrentBotDATVersion,
       "ipTable": ipTable,
       "ipEntry": ipEntry,
       "ipFragmentTimer": ipFragmentTimer,
       "ipOverlapOption": ipOverlapOption,
       "ipTTLConfigMode": ipTTLConfigMode,
       "ipTTLThreshold": ipTTLThreshold,
       "ipTTLResetValue": ipTTLResetValue,
       "ipSmallestFragmentSize": ipSmallestFragmentSize,
       "ipSmallFragmentThreshold": ipSmallFragmentThreshold,
       "ipFragmentReassemblyOption": ipFragmentReassemblyOption,
       "ipv6OverlapOption": ipv6OverlapOption,
       "ipv6SmallestFragmentSize": ipv6SmallestFragmentSize,
       "ipv6SmallFragmentThreshold": ipv6SmallFragmentThreshold,
       "tcpTable": tcpTable,
       "tcpEntry": tcpEntry,
       "supportedUDPFlows": supportedUDPFlows,
       "tcbInactivityTimer": tcbInactivityTimer,
       "tcpSegmentTimer": tcpSegmentTimer,
       "tcp2MSLTimer": tcp2MSLTimer,
       "inactiveFlowsRSTEnabled": inactiveFlowsRSTEnabled,
       "dropReTxTCPEnabled": dropReTxTCPEnabled,
       "coldStartTime": coldStartTime,
       "coldStartDropAction": coldStartDropAction,
       "normalizationOnOffOption": normalizationOnOffOption,
       "tcpOverlapOption": tcpOverlapOption,
       "sAckPermittedOption": sAckPermittedOption,
       "tTCPOptionThreshold": tTCPOptionThreshold,
       "dropOnPAWSFail": dropOnPAWSFail,
       "timestampEchoMatchFail": timestampEchoMatchFail,
       "dropMD5Option": dropMD5Option,
       "unsolicitedUDPPacketsTimeout": unsolicitedUDPPacketsTimeout,
       "synProxyEnable": synProxyEnable,
       "ackScanDiscardTime": ackScanDiscardTime,
       "halfOpenConnectionResetEnable": halfOpenConnectionResetEnable,
       "outOfContextTcpPktEnable": outOfContextTcpPktEnable,
       "synCookieConfig": synCookieConfig,
       "synCookieInboundThreshold": synCookieInboundThreshold,
       "synCookieOutboundThreshold": synCookieOutboundThreshold,
       "synCookieMss": synCookieMss,
       "sinkHoleTimeToLive": sinkHoleTimeToLive,
       "sinkHoleIpAddress": sinkHoleIpAddress,
       "sessionTable": sessionTable,
       "sessionEntry": sessionEntry,
       "sessionSrcIpAddress": sessionSrcIpAddress,
       "sessionDestIpAddress": sessionDestIpAddress,
       "sessionSrcPortNo": sessionSrcPortNo,
       "sessionDestPortNo": sessionDestPortNo,
       "sessionProtocol": sessionProtocol,
       "sessionVIDSIdentifier": sessionVIDSIdentifier,
       "sessionConfigAction": sessionConfigAction,
       "sessionLogTime": sessionLogTime,
       "sessionIntfPortNo": sessionIntfPortNo,
       "sessionV6Table": sessionV6Table,
       "sessionV6Entry": sessionV6Entry,
       "sessionSrcIpv6Address": sessionSrcIpv6Address,
       "sessionDestIpv6Address": sessionDestIpv6Address,
       "sessionv6SrcPortNo": sessionv6SrcPortNo,
       "sessionv6DestPortNo": sessionv6DestPortNo,
       "sessionv6Protocol": sessionv6Protocol,
       "sessionv6VIDSIdentifier": sessionv6VIDSIdentifier,
       "sessionv6ConfigAction": sessionv6ConfigAction,
       "sessionv6LogTime": sessionv6LogTime,
       "sessionv6IntfPortNo": sessionv6IntfPortNo,
       "pluggableModuleState": pluggableModuleState,
       "interfacePortGrp": interfacePortGrp,
       "intfPortTable": intfPortTable,
       "intfPortEntry": intfPortEntry,
       "intfPortIfDescr": intfPortIfDescr,
       "intfPortIfType": intfPortIfType,
       "intfPortIfAdminStatus": intfPortIfAdminStatus,
       "intfPortIfOperStatus": intfPortIfOperStatus,
       "intfPortOperatingMode": intfPortOperatingMode,
       "intfPortEnableFullDuplex": intfPortEnableFullDuplex,
       "intfPortFullDuplexPeer": intfPortFullDuplexPeer,
       "intfPortSpeed": intfPortSpeed,
       "intfPortSpeedConfig": intfPortSpeedConfig,
       "intfPortEnableInternalTap": intfPortEnableInternalTap,
       "intfPortInOutType": intfPortInOutType,
       "intfGEPortSpeedConfig": intfGEPortSpeedConfig,
       "intfFailOpenSwitchStatus": intfFailOpenSwitchStatus,
       "intfFailOpenPortStatus": intfFailOpenPortStatus,
       "intfPortEnableAntiSpoofing": intfPortEnableAntiSpoofing,
       "intfPortHostQRActionStatus": intfPortHostQRActionStatus,
       "intfPortMpeQRActionStatus": intfPortMpeQRActionStatus,
       "intfPortAllowlistACLLookupStatus": intfPortAllowlistACLLookupStatus,
       "intfPortPeerDeviceAdvtStatus": intfPortPeerDeviceAdvtStatus,
       "intfPortIsMcafeeConnector": intfPortIsMcafeeConnector,
       "intfPortAllowAnyConnector": intfPortAllowAnyConnector,
       "intfPortCageType": intfPortCageType,
       "intfPortGetMediaType": intfPortGetMediaType,
       "intfPortSetMediaType": intfPortSetMediaType,
       "intfPortAdditionalInfo": intfPortAdditionalInfo,
       "intfPortMonPortIpAddress": intfPortMonPortIpAddress,
       "intfPortMonPortNetMask": intfPortMonPortNetMask,
       "intfPortGatewayIpAddress": intfPortGatewayIpAddress,
       "intfPortNbadConfigStatus": intfPortNbadConfigStatus,
       "intfPortVlanId": intfPortVlanId,
       "intfPortAppIdStatsConfigStatus": intfPortAppIdStatsConfigStatus,
       "intfPortConnectorType": intfPortConnectorType,
       "intfPortLinearIndex": intfPortLinearIndex,
       "intfPortFecConfig": intfPortFecConfig,
       "intfPortTranceiverSerialNumber": intfPortTranceiverSerialNumber,
       "intfPortGBICHotSwapTime": intfPortGBICHotSwapTime,
       "responsePortGrp": responsePortGrp,
       "respPortTable": respPortTable,
       "respPortEntry": respPortEntry,
       "respPortDescr": respPortDescr,
       "respPortType": respPortType,
       "respPortAdminStatus": respPortAdminStatus,
       "respPortOperStatus": respPortOperStatus,
       "respPortEnableFullDuplex": respPortEnableFullDuplex,
       "respPortSpeed": respPortSpeed,
       "respPortPktDestination": respPortPktDestination,
       "respPortMacAddress": respPortMacAddress,
       "respCUGEPortSpeed": respCUGEPortSpeed,
       "respAdditionalInfo": respAdditionalInfo,
       "intfRespTable": intfRespTable,
       "intfRespEntry": intfRespEntry,
       "intfRespType": intfRespType,
       "intfRespPortNo": intfRespPortNo,
       "dosConfigGrp": dosConfigGrp,
       "dosLearningModeAction": dosLearningModeAction,
       "dosProfileTable": dosProfileTable,
       "dosProfileEntry": dosProfileEntry,
       "dosProfileVidsId": dosProfileVidsId,
       "dosProfileId": dosProfileId,
       "dosProfileStatus": dosProfileStatus,
       "dosProfileLearningTime": dosProfileLearningTime,
       "dosProfileBulkTable": dosProfileBulkTable,
       "dosProfileBulkEntry": dosProfileBulkEntry,
       "dosProfileBulkIndex": dosProfileBulkIndex,
       "dosProfileBulkVidsId": dosProfileBulkVidsId,
       "dosProfileBulkId": dosProfileBulkId,
       "dosProfileBulkStatus": dosProfileBulkStatus,
       "dosProfileBulkLearningTime": dosProfileBulkLearningTime,
       "dosProfileShortAndLongTermTable": dosProfileShortAndLongTermTable,
       "dosProfileShortAndLongTermEntry": dosProfileShortAndLongTermEntry,
       "dosProfileShortAndLongTermVIDSIndex": dosProfileShortAndLongTermVIDSIndex,
       "dosProfileShortAndLongTermNIIndex": dosProfileShortAndLongTermNIIndex,
       "dosProfileShortAndLongTermMeasureIndex": dosProfileShortAndLongTermMeasureIndex,
       "dosProfileShortAndLongTermBinCount": dosProfileShortAndLongTermBinCount,
       "dosProfileShortTermContent": dosProfileShortTermContent,
       "dosProfileLongTermContent": dosProfileLongTermContent,
       "enableDosPktLogging": enableDosPktLogging,
       "timedDosPktDropTable": timedDosPktDropTable,
       "timedDosPktDropEntry": timedDosPktDropEntry,
       "timedDosPktDropVidsIdIndex": timedDosPktDropVidsIdIndex,
       "timedDosPktDropNiIdIndex": timedDosPktDropNiIdIndex,
       "timedDosPktDropMsrIdIndex": timedDosPktDropMsrIdIndex,
       "timedDosPktDropAction": timedDosPktDropAction,
       "timedDosPktDropDuration": timedDosPktDropDuration,
       "timedDosPktDropEndTime": timedDosPktDropEndTime,
       "bulkTimedDosPktDropTable": bulkTimedDosPktDropTable,
       "bulkTimedDosPktDropEntry": bulkTimedDosPktDropEntry,
       "bulkTimedDosPktDropIndex": bulkTimedDosPktDropIndex,
       "bulkTimedDosPktDropVidsId": bulkTimedDosPktDropVidsId,
       "bulkTimedDosPktDropNiId": bulkTimedDosPktDropNiId,
       "bulkTimedDosPktDropMsrId": bulkTimedDosPktDropMsrId,
       "bulkTimedDosPktDropEndTime": bulkTimedDosPktDropEndTime,
       "internalVLANId": internalVLANId,
       "pktLogGrp": pktLogGrp,
       "pktLogServerIPAddress": pktLogServerIPAddress,
       "pktLogServerPort": pktLogServerPort,
       "pktLogMaxPacketsPerFlow": pktLogMaxPacketsPerFlow,
       "pktLogEncryptionEnable": pktLogEncryptionEnable,
       "pktLogServerIPv6Address": pktLogServerIPv6Address,
       "pktAlertThrottleGrp": pktAlertThrottleGrp,
       "pktAlertThrottleGlobalThreshold": pktAlertThrottleGlobalThreshold,
       "pktAlertThrottleInterval": pktAlertThrottleInterval,
       "pktAlertThrottleAction": pktAlertThrottleAction,
       "pktAlertThrottleThreshold": pktAlertThrottleThreshold,
       "pktAlertCorrelationTime": pktAlertCorrelationTime,
       "sslConfigGrp": sslConfigGrp,
       "sslSessionCacheLifetime": sslSessionCacheLifetime,
       "sslSupportAction": sslSupportAction,
       "sslSupportStatus": sslSupportStatus,
       "sslSessionRemoveCerts": sslSessionRemoveCerts,
       "sslPktLoggingEnable": sslPktLoggingEnable,
       "sslModesofOperation": sslModesofOperation,
       "sslSessionCacheLifetimeOutbound": sslSessionCacheLifetimeOutbound,
       "sslPktLoggingOutboundEnable": sslPktLoggingOutboundEnable,
       "sslProxyOutboundUnknownServerCertificate": sslProxyOutboundUnknownServerCertificate,
       "sslProxyOutboundUntrustedServerCertficate": sslProxyOutboundUntrustedServerCertficate,
       "sslProxyOutboundUnsupportedCipherSuite": sslProxyOutboundUnsupportedCipherSuite,
       "sslProxyInboundUnsupportedCipherSuite": sslProxyInboundUnsupportedCipherSuite,
       "sslProxyOutboundUnsupportedServerCertificate": sslProxyOutboundUnsupportedServerCertificate,
       "sslProxyInboundUnsupportedServerCertificate": sslProxyInboundUnsupportedServerCertificate,
       "maxSslFlowSupportedInSslDisableMode": maxSslFlowSupportedInSslDisableMode,
       "maxFlowSupportedInSslDisableMode": maxFlowSupportedInSslDisableMode,
       "maxSslFlowSupportedInSslInboundLegacyMode": maxSslFlowSupportedInSslInboundLegacyMode,
       "maxFlowSupportedInSslInboundLegacyMode": maxFlowSupportedInSslInboundLegacyMode,
       "maxSslFlowSupportedInSslOutboundMode": maxSslFlowSupportedInSslOutboundMode,
       "maxFlowSupportedInSslOutboundMode": maxFlowSupportedInSslOutboundMode,
       "sslModesofOperationStatus": sslModesofOperationStatus,
       "sslProxyOutboundUnknownURLCategory": sslProxyOutboundUnknownURLCategory,
       "sslShKeyDecryptEnable": sslShKeyDecryptEnable,
       "l2ConfigGrp": l2ConfigGrp,
       "l2ModeEnable": l2ModeEnable,
       "l2ModeStatus": l2ModeStatus,
       "l2ModeCfgDuration": l2ModeCfgDuration,
       "l2ModeCfgThreshold": l2ModeCfgThreshold,
       "l2ModeOccCount": l2ModeOccCount,
       "l2ModeReason": l2ModeReason,
       "aclLogAlertGrp": aclLogAlertGrp,
       "aclAlertLogging": aclAlertLogging,
       "aclAlertThrottleMaxIpPair": aclAlertThrottleMaxIpPair,
       "aclAlertThrottleInterval": aclAlertThrottleInterval,
       "aclAlertThrottleAction": aclAlertThrottleAction,
       "aclAlertThrottleThreshold": aclAlertThrottleThreshold,
       "aclAlertDirectToSyslog": aclAlertDirectToSyslog,
       "tacacsPlusAuthGrp": tacacsPlusAuthGrp,
       "enableTacacsPlusAuth": enableTacacsPlusAuth,
       "enableTacacsPlusTrafficEncr": enableTacacsPlusTrafficEncr,
       "tacacsPlusEncrSecret": tacacsPlusEncrSecret,
       "tacacsPlusServerIPTable": tacacsPlusServerIPTable,
       "tacacsPlusServerIPEntry": tacacsPlusServerIPEntry,
       "tacIndex": tacIndex,
       "tacacsPlusServerIPAddr": tacacsPlusServerIPAddr,
       "enableTacacsPlusAuthorization": enableTacacsPlusAuthorization,
       "ipV6ConfigGrp": ipV6ConfigGrp,
       "ipV6TrafficHandling": ipV6TrafficHandling,
       "hostQGrp": hostQGrp,
       "hostQConfigGrp": hostQConfigGrp,
       "hostQFilterTimeOut": hostQFilterTimeOut,
       "hostQDeleteAllFilters": hostQDeleteAllFilters,
       "hostQBulkFilterV4Table": hostQBulkFilterV4Table,
       "hostQBulkFilterV4Entry": hostQBulkFilterV4Entry,
       "hostQBulkFilterIndexV4": hostQBulkFilterIndexV4,
       "hostQBulkFilterSrcIPAddrV4": hostQBulkFilterSrcIPAddrV4,
       "hostQBulkFilterVidsIdV4": hostQBulkFilterVidsIdV4,
       "hostQBulkFilterAttackIdV4": hostQBulkFilterAttackIdV4,
       "hostQBulkFilterEndTimeV4": hostQBulkFilterEndTimeV4,
       "hostQBulkFilterQRStatusV4": hostQBulkFilterQRStatusV4,
       "hostQBulkFilterMPEReplyMsgV4": hostQBulkFilterMPEReplyMsgV4,
       "hostQBulkFilterMonPortIdV4": hostQBulkFilterMonPortIdV4,
       "hostQBulkFilterEZIdV4": hostQBulkFilterEZIdV4,
       "hostQBulkFilterV6Table": hostQBulkFilterV6Table,
       "hostQBulkFilterV6Entry": hostQBulkFilterV6Entry,
       "hostQBulkFilterIndexV6": hostQBulkFilterIndexV6,
       "hostQBulkFilterSrcIPAddrV6": hostQBulkFilterSrcIPAddrV6,
       "hostQBulkFilterVidsIdV6": hostQBulkFilterVidsIdV6,
       "hostQBulkFilterAttackIdV6": hostQBulkFilterAttackIdV6,
       "hostQBulkFilterEndTimeV6": hostQBulkFilterEndTimeV6,
       "hostQBulkFilterQRStatusV6": hostQBulkFilterQRStatusV6,
       "hostQBulkFilterMPEReplyMsgV6": hostQBulkFilterMPEReplyMsgV6,
       "hostQBulkFilterMonPortIdV6": hostQBulkFilterMonPortIdV6,
       "hostQNeverDenyV4Table": hostQNeverDenyV4Table,
       "hostQNeverDenyV4Entry": hostQNeverDenyV4Entry,
       "hostQNeverDenyIpAddressV4": hostQNeverDenyIpAddressV4,
       "hostQNeverDenyActionV4": hostQNeverDenyActionV4,
       "hostQNeverDenyV6Table": hostQNeverDenyV6Table,
       "hostQNeverDenyV6Entry": hostQNeverDenyV6Entry,
       "hostQNeverDenyIpAddressV6": hostQNeverDenyIpAddressV6,
       "hostQNeverDenyActionV6": hostQNeverDenyActionV6,
       "hostQUserDefFilterV4Table": hostQUserDefFilterV4Table,
       "hostQUserDefFilterV4Entry": hostQUserDefFilterV4Entry,
       "hostQUserDefFilterSrcIpV4": hostQUserDefFilterSrcIpV4,
       "hostQUserDefFilterVidsIdV4": hostQUserDefFilterVidsIdV4,
       "hostQUserDefFilterAttackIdV4": hostQUserDefFilterAttackIdV4,
       "hostQUserDefFilterDurationV4": hostQUserDefFilterDurationV4,
       "hostQUserDefFilterActionV4": hostQUserDefFilterActionV4,
       "hostQUserDefFilterRemediationV4": hostQUserDefFilterRemediationV4,
       "hostQUserDefFilterV6Table": hostQUserDefFilterV6Table,
       "hostQUserDefFilterV6Entry": hostQUserDefFilterV6Entry,
       "hostQUserDefFilterSrcIpV6": hostQUserDefFilterSrcIpV6,
       "hostQUserDefFilterVidsIdV6": hostQUserDefFilterVidsIdV6,
       "hostQUserDefFilterAttackIdV6": hostQUserDefFilterAttackIdV6,
       "hostQUserDefFilterDurationV6": hostQUserDefFilterDurationV6,
       "hostQUserDefFilterActionV6": hostQUserDefFilterActionV6,
       "nmsGrp": nmsGrp,
       "nmsUserGrp": nmsUserGrp,
       "nmsUserTable": nmsUserTable,
       "nmsUserEntry": nmsUserEntry,
       "nmsUserName": nmsUserName,
       "nmsAuthKey": nmsAuthKey,
       "nmsEncrKey": nmsEncrKey,
       "nmsUserChangeAction": nmsUserChangeAction,
       "nmsDeleteAllUsers": nmsDeleteAllUsers,
       "nmsCommitUserEntryChanges": nmsCommitUserEntryChanges,
       "nmsIpGrp": nmsIpGrp,
       "nmsIpTable": nmsIpTable,
       "nmsIpEntry": nmsIpEntry,
       "nmsIpAddress": nmsIpAddress,
       "nmsIpChangeAction": nmsIpChangeAction,
       "nmsIpv6Table": nmsIpv6Table,
       "nmsIpv6Entry": nmsIpv6Entry,
       "nmsIpv6Address": nmsIpv6Address,
       "nmsIpv6ChangeAction": nmsIpv6ChangeAction,
       "mpeGrp": mpeGrp,
       "mpeConfigGrp": mpeConfigGrp,
       "mpeQRScope": mpeQRScope,
       "mpeThrottleTimeout": mpeThrottleTimeout,
       "mpeInstallConfigGrp": mpeInstallConfigGrp,
       "mpeIpAddress": mpeIpAddress,
       "mpeAnonymousPort": mpeAnonymousPort,
       "mpeTrustedSSLPort": mpeTrustedSSLPort,
       "mpeePOCred": mpeePOCred,
       "mpeAnonymousURI": mpeAnonymousURI,
       "mpeTrustedURI": mpeTrustedURI,
       "mpeInstallConfigAction": mpeInstallConfigAction,
       "mpeInstallConfigStatus": mpeInstallConfigStatus,
       "mpeRootCertStatus": mpeRootCertStatus,
       "mpeDeleteRootCert": mpeDeleteRootCert,
       "mnacHealthLevelListenPort": mnacHealthLevelListenPort,
       "mnacConnectivityFailureTimeout": mnacConnectivityFailureTimeout,
       "mnacAgentGUIDPort": mnacAgentGUIDPort,
       "mpeExcludedMacTable": mpeExcludedMacTable,
       "mpeExcludedMacEntry": mpeExcludedMacEntry,
       "mpeMacAddress": mpeMacAddress,
       "mpeMacChangeAction": mpeMacChangeAction,
       "remediationGrp": remediationGrp,
       "remediationConfigGrp": remediationConfigGrp,
       "remediationTimeout": remediationTimeout,
       "ezLogAlertGrp": ezLogAlertGrp,
       "ezAlertLogging": ezAlertLogging,
       "ezAlertThrottleMaxIpPair": ezAlertThrottleMaxIpPair,
       "ezAlertThrottleInterval": ezAlertThrottleInterval,
       "ezAlertThrottleAction": ezAlertThrottleAction,
       "ezAlertThrottleThreshold": ezAlertThrottleThreshold,
       "ezAlertDirectToSyslog": ezAlertDirectToSyslog,
       "nbadGrp": nbadGrp,
       "nbadConfigGrp": nbadConfigGrp,
       "nbadSensorIpAddress": nbadSensorIpAddress,
       "nbadSensorPort": nbadSensorPort,
       "nbadIPSPriMonPortId": nbadIPSPriMonPortId,
       "nbadIPSSecMonPortId": nbadIPSSecMonPortId,
       "nbadAppFingerPrintingEnabled": nbadAppFingerPrintingEnabled,
       "nbadOSFingerPrintingEnabled": nbadOSFingerPrintingEnabled,
       "nbadSslFlowDataCaptureEnabled": nbadSslFlowDataCaptureEnabled,
       "nbadFlowProtocolId": nbadFlowProtocolId,
       "nbadFlowProtocolVersion": nbadFlowProtocolVersion,
       "nbadCaptureTCP": nbadCaptureTCP,
       "nbadCaptureUDP": nbadCaptureUDP,
       "nbadCaptureICMP": nbadCaptureICMP,
       "hostDataGrp": hostDataGrp,
       "hostDataTable": hostDataTable,
       "hostDataEntry": hostDataEntry,
       "hostDataIndex": hostDataIndex,
       "hostIPAddress": hostIPAddress,
       "hostMacAddress": hostMacAddress,
       "hostDetectedDHCPMonPortId": hostDetectedDHCPMonPortId,
       "hostName": hostName,
       "hostUpdatedTimeStamp": hostUpdatedTimeStamp,
       "hostAgentGuid": hostAgentGuid,
       "hostNACStatus": hostNACStatus,
       "hostState": hostState,
       "hostDeploymentMode": hostDeploymentMode,
       "hostHealthLevel": hostHealthLevel,
       "hostEZId": hostEZId,
       "hostUserName": hostUserName,
       "hostPolicyId": hostPolicyId,
       "hostDetectedTimeStamp": hostDetectedTimeStamp,
       "hostOSInfo": hostOSInfo,
       "hostMNACAgentOSInfo": hostMNACAgentOSInfo,
       "hostActive": hostActive,
       "hostDetectedStdMonPortId": hostDetectedStdMonPortId,
       "hostDetectionType": hostDetectionType,
       "hostUserAuthProtocol": hostUserAuthProtocol,
       "hostSwitchId": hostSwitchId,
       "hostSwitchPortId": hostSwitchPortId,
       "hostSwitchPortGroupId": hostSwitchPortGroupId,
       "hostQuarantineVlanId": hostQuarantineVlanId,
       "hostProductionVlanId": hostProductionVlanId,
       "nasIpAddress": nasIpAddress,
       "nasGroupObjectId": nasGroupObjectId,
       "userGroupObjectId": userGroupObjectId,
       "deviceProfileString": deviceProfileString,
       "hostOperationalMode": hostOperationalMode,
       "hostEnforcementAction": hostEnforcementAction,
       "flexiblePolicyRuleId": flexiblePolicyRuleId,
       "hostConfigGrp": hostConfigGrp,
       "hostEntryAttribute": hostEntryAttribute,
       "hostEntryIpAddress": hostEntryIpAddress,
       "hostEntryMac": hostEntryMac,
       "hostEntryConfig": hostEntryConfig,
       "hostEntryEZId": hostEntryEZId,
       "hostDataAvailabilityStatus": hostDataAvailabilityStatus,
       "sgapGrp": sgapGrp,
       "sgapConfigGrp": sgapConfigGrp,
       "sgapAuthTimeout": sgapAuthTimeout,
       "sgapCSRConfigGrp": sgapCSRConfigGrp,
       "sgapCSRCountryName": sgapCSRCountryName,
       "sgapCSRStateProvince": sgapCSRStateProvince,
       "sgapCSRLocality": sgapCSRLocality,
       "sgapCSRCompany": sgapCSRCompany,
       "sgapCSROrganizationalUnit": sgapCSROrganizationalUnit,
       "sgapCSRCommonName": sgapCSRCommonName,
       "sgapCSRGenerateAction": sgapCSRGenerateAction,
       "sgapCSRGenerateStatus": sgapCSRGenerateStatus,
       "sgapCertStatus": sgapCertStatus,
       "alarmAndTrendsGrp": alarmAndTrendsGrp,
       "sensorPerfAlertGrp": sensorPerfAlertGrp,
       "sensorPerfAlertEnable": sensorPerfAlertEnable,
       "sensorPerfAlertDuration": sensorPerfAlertDuration,
       "sensorPerfAlertParameters": sensorPerfAlertParameters,
       "alarmConfigGrp": alarmConfigGrp,
       "alarmStatus": alarmStatus,
       "alarmDeleteAllEntries": alarmDeleteAllEntries,
       "alarmDuration": alarmDuration,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmSampleType": alarmSampleType,
       "alarmSampleTypeIndexBitmap": alarmSampleTypeIndexBitmap,
       "alarmSampleTypeDesc": alarmSampleTypeDesc,
       "alarmRaisingThreshold": alarmRaisingThreshold,
       "alarmFallingThreshold": alarmFallingThreshold,
       "alarmStartupType": alarmStartupType,
       "alarmEntryStatus": alarmEntryStatus,
       "bwSavingStatus": bwSavingStatus,
       "oobnacGrp": oobnacGrp,
       "oobnacSwDiscoveryGrp": oobnacSwDiscoveryGrp,
       "swInstanceTable": swInstanceTable,
       "swInstanceEntry": swInstanceEntry,
       "swIdIndex": swIdIndex,
       "swDetDesc": swDetDesc,
       "swProfileId": swProfileId,
       "swIPAddress": swIPAddress,
       "swIPV6Address": swIPV6Address,
       "swName": swName,
       "swDesc": swDesc,
       "swEnable": swEnable,
       "swSNMPsupport": swSNMPsupport,
       "swSnmpVerSupport": swSnmpVerSupport,
       "swREADCommunityStr": swREADCommunityStr,
       "swWRITECommunityStr": swWRITECommunityStr,
       "swTRAPCommunityStr": swTRAPCommunityStr,
       "swSNMPPort": swSNMPPort,
       "swV3UserName": swV3UserName,
       "swV3SecurityLevel": swV3SecurityLevel,
       "swV3AuthProtocol": swV3AuthProtocol,
       "swV3AuthKey": swV3AuthKey,
       "swV3EncrProtocol": swV3EncrProtocol,
       "swV3EncrKey": swV3EncrKey,
       "swCLIsupport": swCLIsupport,
       "swCLINwProtocol": swCLINwProtocol,
       "swCLIUserName": swCLIUserName,
       "swCLIPwd": swCLIPwd,
       "swCLIEnablePwd": swCLIEnablePwd,
       "swCLIAutoSaveConfig": swCLIAutoSaveConfig,
       "swRadiusSupport": swRadiusSupport,
       "swRadiusSharedSecret": swRadiusSharedSecret,
       "swPlaceHolderVlan": swPlaceHolderVlan,
       "swUseDefaultQVlanPool": swUseDefaultQVlanPool,
       "swQVlanPoolRange": swQVlanPoolRange,
       "swDiscoverAction": swDiscoverAction,
       "swCLILoginType": swCLILoginType,
       "swAuthMacAddRadSrvOption": swAuthMacAddRadSrvOption,
       "swActionStatus": swActionStatus,
       "swPortDefaultVlan": swPortDefaultVlan,
       "swActionStatusTime": swActionStatusTime,
       "swIpAddress": swIpAddress,
       "swIpV6Address": swIpV6Address,
       "readCommunityString": readCommunityString,
       "snmpPort": snmpPort,
       "snmpVerSupport": snmpVerSupport,
       "writeCommunityStr": writeCommunityStr,
       "trapCommunityStr": trapCommunityStr,
       "v3UserName": v3UserName,
       "v3SecurityLevel": v3SecurityLevel,
       "v3AuthProtocol": v3AuthProtocol,
       "v3AuthKey": v3AuthKey,
       "v3EncrProtocol": v3EncrProtocol,
       "v3EncrKey": v3EncrKey,
       "cliNwProtocol": cliNwProtocol,
       "cliUserName": cliUserName,
       "cliPwd": cliPwd,
       "cliEnablePwd": cliEnablePwd,
       "swQueryAction": swQueryAction,
       "cliLoginType": cliLoginType,
       "profileId": profileId,
       "switchId": switchId,
       "oobnacAllSwitchesGrp": oobnacAllSwitchesGrp,
       "oobnDefaultQvlanPool": oobnDefaultQvlanPool,
       "oobnacRadNumRetries": oobnacRadNumRetries,
       "oobnacRadRespTimeOut": oobnacRadRespTimeOut,
       "oobnacFailoverGrp": oobnacFailoverGrp,
       "oobnacFloatingIpAddress": oobnacFloatingIpAddress,
       "oobnacFloatingIpv6Address": oobnacFloatingIpv6Address,
       "oobnacFloatingNetMask": oobnacFloatingNetMask,
       "oobnacFloatingv6NetMask": oobnacFloatingv6NetMask,
       "oobnacFloatingGatewayIpAddress": oobnacFloatingGatewayIpAddress,
       "oobnacFloatingGatewayIpv6Address": oobnacFloatingGatewayIpv6Address,
       "oobnacPeerIpAddress": oobnacPeerIpAddress,
       "oobnacPeerIpv6Address": oobnacPeerIpv6Address,
       "oobnacFailoverSensorStatus": oobnacFailoverSensorStatus,
       "malwareGrp": malwareGrp,
       "malwarePriDNSServerIp": malwarePriDNSServerIp,
       "malwareSecDNSServerIp": malwareSecDNSServerIp,
       "malwarePriDNSServerIpV6": malwarePriDNSServerIpV6,
       "malwareSecDNSServerIpV6": malwareSecDNSServerIpV6,
       "malwareRiskLevel": malwareRiskLevel,
       "malwareArtemisDetectionMode": malwareArtemisDetectionMode,
       "malwareUDFDetectionMode": malwareUDFDetectionMode,
       "gamEngSensorCfgGrp": gamEngSensorCfgGrp,
       "gamEngSensorAutoUpdateConfig": gamEngSensorAutoUpdateConfig,
       "gamEngSensorAutoUpdateInterval": gamEngSensorAutoUpdateInterval,
       "gamEngVer": gamEngVer,
       "gamDatVer": gamDatVer,
       "avEngVer": avEngVer,
       "avDatVer": avDatVer,
       "gamEngUpdatedTime": gamEngUpdatedTime,
       "gamManualFullUpdateFileUploadStatus": gamManualFullUpdateFileUploadStatus,
       "miscCfgGrp": miscCfgGrp,
       "jumboframeParsingConfig": jumboframeParsingConfig,
       "currentJumboframeParsingStatus": currentJumboframeParsingStatus,
       "appIdStatsConfigStatus": appIdStatsConfigStatus,
       "hitlessRebootStatus": hitlessRebootStatus,
       "existingGeoDBFilename": existingGeoDBFilename,
       "nsmTrackUserLoggingStatus": nsmTrackUserLoggingStatus,
       "accelerateFTPInboundConfig": accelerateFTPInboundConfig,
       "accelerateFTPOutboundConfig": accelerateFTPOutboundConfig,
       "parseTunnellingConfig": parseTunnellingConfig,
       "prev256ByteLoggingConfig": prev256ByteLoggingConfig,
       "cliAuditLoggingConfig": cliAuditLoggingConfig,
       "snortRuleEngineConfig": snortRuleEngineConfig,
       "currentSnortRuleEngineStatus": currentSnortRuleEngineStatus,
       "insightsTelemetryConfig": insightsTelemetryConfig,
       "layer2FwdGrp": layer2FwdGrp,
       "layer2FwdCfgGrp": layer2FwdCfgGrp,
       "layer2FwdType": layer2FwdType,
       "layer2IntfPort": layer2IntfPort,
       "layer2FwdAction": layer2FwdAction,
       "layer2FwdBeginId": layer2FwdBeginId,
       "layer2FwdEndId": layer2FwdEndId,
       "layer2FwdConfig": layer2FwdConfig,
       "layer2FwdTCPTable": layer2FwdTCPTable,
       "layer2FwdTCPEntry": layer2FwdTCPEntry,
       "tcpIntfPortIndex": tcpIntfPortIndex,
       "tcpEntryIndex": tcpEntryIndex,
       "tcpPortRange": tcpPortRange,
       "layer2FwdUDPTable": layer2FwdUDPTable,
       "layer2FwdUDPEntry": layer2FwdUDPEntry,
       "udpIntfPortIndex": udpIntfPortIndex,
       "udpEntryIndex": udpEntryIndex,
       "udpPortRange": udpPortRange,
       "layer2FwdVLANTable": layer2FwdVLANTable,
       "layer2FwdVLANEntry": layer2FwdVLANEntry,
       "vlanIntfPortIndex": vlanIntfPortIndex,
       "vlanEntryIndex": vlanEntryIndex,
       "vlanPortRange": vlanPortRange,
       "layer2FwdIPTable": layer2FwdIPTable,
       "layer2FwdIPEntry": layer2FwdIPEntry,
       "ipIntfPortIndex": ipIntfPortIndex,
       "ipEntryIndex": ipEntryIndex,
       "ipPortRange": ipPortRange,
       "pktCapCfgGrp": pktCapCfgGrp,
       "pktCapMode": pktCapMode,
       "pktCapDuration": pktCapDuration,
       "pktCapPmSpanPortForCapture": pktCapPmSpanPortForCapture,
       "pktCapFmLocation": pktCapFmLocation,
       "pktCapFmMaxSize": pktCapFmMaxSize,
       "pktCapFmFUServerAddress": pktCapFmFUServerAddress,
       "pktCapFmFUFileName": pktCapFmFUFileName,
       "pktCapFmFUSetting": pktCapFmFUSetting,
       "pktCapFilterFileName": pktCapFilterFileName,
       "pktCapFilterFileTimeStamp": pktCapFilterFileTimeStamp,
       "pktCapCommandGrp": pktCapCommandGrp,
       "pktCapCmd": pktCapCmd,
       "pktCapStatus": pktCapStatus,
       "packetCaptureFmFUControl": packetCaptureFmFUControl,
       "packetCaptureFmFileStatus": packetCaptureFmFileStatus,
       "packetCaptureFmTest": packetCaptureFmTest,
       "packetCaptureFmTestStatus": packetCaptureFmTestStatus,
       "pktCapFmSCPUserName": pktCapFmSCPUserName,
       "pktCapFmSCPPassword": pktCapFmSCPPassword,
       "dnsCfgGrp": dnsCfgGrp,
       "priDNSServerIp": priDNSServerIp,
       "secDNSServerIp": secDNSServerIp,
       "priDNSServerIpV6": priDNSServerIpV6,
       "secDNSServerIpV6": secDNSServerIpV6,
       "dnsSearchList": dnsSearchList,
       "layer7DCapConfigGrp": layer7DCapConfigGrp,
       "layer7DCapPercentageOfFlows": layer7DCapPercentageOfFlows,
       "layer7DCapBuffSize": layer7DCapBuffSize,
       "layer7DCapMaxSupportedFlows": layer7DCapMaxSupportedFlows,
       "interfacePhysicalPortGrp": interfacePhysicalPortGrp,
       "intfPhysicalPortTable": intfPhysicalPortTable,
       "intfPhysicalPortEntry": intfPhysicalPortEntry,
       "intfPhysicalPortIfDescr": intfPhysicalPortIfDescr,
       "intfPhysicalPortIfType": intfPhysicalPortIfType,
       "intfPhysicalPortIfAdminStatus": intfPhysicalPortIfAdminStatus,
       "intfPhysicalPortIfOperStatus": intfPhysicalPortIfOperStatus,
       "intfPhysicalPortEnableFullDuplex": intfPhysicalPortEnableFullDuplex,
       "intfPhysicalPortSpeed": intfPhysicalPortSpeed,
       "intfPhysicalPortSpeedConfig": intfPhysicalPortSpeedConfig,
       "intfPhysicalPortIsMcafeeConnector": intfPhysicalPortIsMcafeeConnector,
       "intfPhysicalPortAllowAnyConnector": intfPhysicalPortAllowAnyConnector,
       "intfPhysicalPortCageType": intfPhysicalPortCageType,
       "intfPhysicalPortGetMediaType": intfPhysicalPortGetMediaType,
       "intfPhysicalPortSetMediaType": intfPhysicalPortSetMediaType,
       "intfPhysicalPortMonPortIpAddress": intfPhysicalPortMonPortIpAddress,
       "intfPhysicalPortMonPortNetMask": intfPhysicalPortMonPortNetMask,
       "intfPhysicalPortGatewayIpAddress": intfPhysicalPortGatewayIpAddress,
       "intfPhysicalPortNbadConfigStatus": intfPhysicalPortNbadConfigStatus,
       "intfPhysicalPortVlanId": intfPhysicalPortVlanId,
       "intfPhysicalPortLBSerialNumber": intfPhysicalPortLBSerialNumber,
       "intfPhysicalPortLBPortNumber": intfPhysicalPortLBPortNumber,
       "intfPhysicalPortConnectorType": intfPhysicalPortConnectorType,
       "intfPhysicalPortLinearIndex": intfPhysicalPortLinearIndex,
       "gtiConfigGrp": gtiConfigGrp,
       "gtiProxyServerName": gtiProxyServerName,
       "gtiProxyPort": gtiProxyPort,
       "gtiProxyUsername": gtiProxyUsername,
       "gtiProxyPassword": gtiProxyPassword,
       "gtiConfigPrivateCloudGrp": gtiConfigPrivateCloudGrp,
       "gtiPrivateCloudServerIPAddressType": gtiPrivateCloudServerIPAddressType,
       "gtiPrivateCloudServerIPv4Address": gtiPrivateCloudServerIPv4Address,
       "gtiPrivateCloudServerIPv6Address": gtiPrivateCloudServerIPv6Address,
       "gtiPrivateCloudServerConnectionConfig": gtiPrivateCloudServerConnectionConfig,
       "gtiPrivateCloudServerDeleteCertificate": gtiPrivateCloudServerDeleteCertificate,
       "gtiPrivateCloudServerCertificateStatus": gtiPrivateCloudServerCertificateStatus,
       "gtiPrivateCloudChannelStatus": gtiPrivateCloudChannelStatus,
       "gtiUnifiedConfigGrp": gtiUnifiedConfigGrp,
       "gtiFileRESTGTIType": gtiFileRESTGTIType,
       "gtiFileRESTPublicGTIFQDN": gtiFileRESTPublicGTIFQDN,
       "gtiFileRESTUsername": gtiFileRESTUsername,
       "gtiFileRESTPassword": gtiFileRESTPassword,
       "gtiFileRESTConnectionConfig": gtiFileRESTConnectionConfig,
       "gtiFileRESTPvtGTIIPType": gtiFileRESTPvtGTIIPType,
       "gtiFileRESTPvtGTIIPv4Address": gtiFileRESTPvtGTIIPv4Address,
       "gtiFileRESTPvtGTIIPV6Address": gtiFileRESTPvtGTIIPV6Address,
       "ntpConfigGrp": ntpConfigGrp,
       "ntpConfigTable": ntpConfigTable,
       "ntpConfigEntry": ntpConfigEntry,
       "ntpConfigServerIPv4": ntpConfigServerIPv4,
       "ntpConfigServerIPv6": ntpConfigServerIPv6,
       "ntpConfigPollInterval": ntpConfigPollInterval,
       "ntpConfigAuthenticationEnable": ntpConfigAuthenticationEnable,
       "ntpConfigKeyId": ntpConfigKeyId,
       "ntpConfigKeyType": ntpConfigKeyType,
       "ntpConfigKeyValue": ntpConfigKeyValue,
       "ntpConfigFileCreate": ntpConfigFileCreate,
       "pluggableModuleGrp": pluggableModuleGrp,
       "pluggableModuleTable": pluggableModuleTable,
       "pluggableModuleEntry": pluggableModuleEntry,
       "moduleSerialNumber": moduleSerialNumber,
       "moduleSysType": moduleSysType,
       "modulePresent": modulePresent,
       "moduleNumPorts": moduleNumPorts,
       "moduleRebootRequired": moduleRebootRequired,
       "insightixNetworkGrp": insightixNetworkGrp,
       "insightixCfgGrp": insightixCfgGrp,
       "ldapServerIPAddressType": ldapServerIPAddressType,
       "ldapServerIPv4Address": ldapServerIPv4Address,
       "ldapServerIPv6Address": ldapServerIPv6Address,
       "ldapServerPort": ldapServerPort,
       "ldapServerSSLConfig": ldapServerSSLConfig,
       "ldapServerBaseDN": ldapServerBaseDN,
       "ldapServerUserName": ldapServerUserName,
       "ldapServerPassword": ldapServerPassword,
       "ldapServerConfigAction": ldapServerConfigAction,
       "ldapServerConfigStatus": ldapServerConfigStatus,
       "ntbaChannelCfgGrp": ntbaChannelCfgGrp,
       "ntbaServerIPAddressType": ntbaServerIPAddressType,
       "ntbaServerIPv4Address": ntbaServerIPv4Address,
       "ntbaServerIPv6Address": ntbaServerIPv6Address,
       "ntbaServerPort": ntbaServerPort,
       "ntbaServerConnectionConfig": ntbaServerConnectionConfig,
       "ntbaServerDeleteCertificate": ntbaServerDeleteCertificate,
       "ntbaServerCertificateStatus": ntbaServerCertificateStatus,
       "ntbaShdKeySHAValue": ntbaShdKeySHAValue,
       "ntbaChannelStatus": ntbaChannelStatus,
       "validEdgeChannelCfgGrp": validEdgeChannelCfgGrp,
       "validEdgeServerIPAddressType": validEdgeServerIPAddressType,
       "validEdgeServerIPv4Address": validEdgeServerIPv4Address,
       "validEdgeServerIPv6Address": validEdgeServerIPv6Address,
       "validEdgeServerPort": validEdgeServerPort,
       "validEdgeServerConnectionConfig": validEdgeServerConnectionConfig,
       "validEdgeServerDeleteCertificate": validEdgeServerDeleteCertificate,
       "validEdgeServerCertificateStatus": validEdgeServerCertificateStatus,
       "validEdgeShdKeySHAValue": validEdgeShdKeySHAValue,
       "validEdgeChannelStatus": validEdgeChannelStatus,
       "validEdgeChannelGlobalUserId": validEdgeChannelGlobalUserId,
       "validEdgeChannelGlobalUserName": validEdgeChannelGlobalUserName,
       "dxlCfgGrp": dxlCfgGrp,
       "dxlConfig": dxlConfig,
       "epoCfgGrp": epoCfgGrp,
       "epoIPAddressType": epoIPAddressType,
       "epoIpAddress": epoIpAddress,
       "epoIPv6Address": epoIPv6Address,
       "epoPort": epoPort,
       "epoCredUsername": epoCredUsername,
       "epoCredPasswd": epoCredPasswd,
       "epoAction": epoAction,
       "radiusAuthGrp": radiusAuthGrp,
       "radiusAuthConfig": radiusAuthConfig,
       "radiusPrimaryServerIPAddrType": radiusPrimaryServerIPAddrType,
       "radiusPrimaryServerIPAddr": radiusPrimaryServerIPAddr,
       "radiusPrimaryServerIPv6Addr": radiusPrimaryServerIPv6Addr,
       "radiusPrimaryServerEncrSecret": radiusPrimaryServerEncrSecret,
       "radiusPriServerAuthPort": radiusPriServerAuthPort,
       "radiusPriServerAccConfig": radiusPriServerAccConfig,
       "radiusPriServerAccPort": radiusPriServerAccPort,
       "radiusPriServerConnTimeOut": radiusPriServerConnTimeOut,
       "radiusBackupServerIPAddrType": radiusBackupServerIPAddrType,
       "radiusBackupServerIPAddr": radiusBackupServerIPAddr,
       "radiusBackupServerIPv6Addr": radiusBackupServerIPv6Addr,
       "radiusBackupServerEncrSecret": radiusBackupServerEncrSecret,
       "radiusBackupServerAuthPort": radiusBackupServerAuthPort,
       "radiusBackupServerAccConfig": radiusBackupServerAccConfig,
       "radiusBackupServerAccPort": radiusBackupServerAccPort,
       "radiusBackupServerConnTimeOut": radiusBackupServerConnTimeOut,
       "sshAccessGrp": sshAccessGrp,
       "sshAccessCfgGrp": sshAccessCfgGrp,
       "sshAccessControlStatus": sshAccessControlStatus,
       "sshAccessControlResetIpv4": sshAccessControlResetIpv4,
       "sshAccessLogSupport": sshAccessLogSupport,
       "sshAccessControlResetIpv6": sshAccessControlResetIpv6,
       "sshAccessNumIpv4Entries": sshAccessNumIpv4Entries,
       "sshAccessIpTable": sshAccessIpTable,
       "sshAccessIpEntry": sshAccessIpEntry,
       "sshIpv4Index": sshIpv4Index,
       "sshIpAddress": sshIpAddress,
       "sshMaskIpv4": sshMaskIpv4,
       "sshAccessIpConfig": sshAccessIpConfig,
       "sshAccessNumIpv6Entries": sshAccessNumIpv6Entries,
       "sshAccessIpv6Table": sshAccessIpv6Table,
       "sshAccessIpv6Entry": sshAccessIpv6Entry,
       "sshIpv6Index": sshIpv6Index,
       "sshAccessIpv6Address": sshAccessIpv6Address,
       "sshAccessIpv6Mask": sshAccessIpv6Mask,
       "sshAccessIpv6Config": sshAccessIpv6Config,
       "virtualPluggableModuleGrp": virtualPluggableModuleGrp,
       "moduleOneNumPorts": moduleOneNumPorts,
       "moduleTwoNumPorts": moduleTwoNumPorts,
       "sslProbeAccessGrp": sslProbeAccessGrp,
       "sslProbeAccessCfgGrp": sslProbeAccessCfgGrp,
       "sslProbeAccessMaxAgentConn": sslProbeAccessMaxAgentConn,
       "sslProbeAccessNumIpv4Entries": sslProbeAccessNumIpv4Entries,
       "sslProbeAccessIpTable": sslProbeAccessIpTable,
       "sslProbeAccessIpEntry": sslProbeAccessIpEntry,
       "sslProbeIpAddress": sslProbeIpAddress,
       "sslProbeMaskIpv4": sslProbeMaskIpv4,
       "sslProbeAccessIpConfig": sslProbeAccessIpConfig,
       "sslProbeAccessNumIpv6Entries": sslProbeAccessNumIpv6Entries,
       "sslProbeAccessIpv6Table": sslProbeAccessIpv6Table,
       "sslProbeAccessIpv6Entry": sslProbeAccessIpv6Entry,
       "sslProbeAccessIpv6Address": sslProbeAccessIpv6Address,
       "sslProbeAccessIpv6Mask": sslProbeAccessIpv6Mask,
       "sslProbeAccessIpv6Config": sslProbeAccessIpv6Config,
       "sensorCertificateGroup": sensorCertificateGroup,
       "sensorCertificateConfigGrp": sensorCertificateConfigGrp,
       "sensorCertificateCSRConfigGrp": sensorCertificateCSRConfigGrp,
       "sensorCertificateCSRCountryName": sensorCertificateCSRCountryName,
       "sensorCertificateCSRStateProvince": sensorCertificateCSRStateProvince,
       "sensorCertificateCSRLocality": sensorCertificateCSRLocality,
       "sensorCertificateCSRCompany": sensorCertificateCSRCompany,
       "sensorCertificateCSROrganizationalUnit": sensorCertificateCSROrganizationalUnit,
       "sensorCertificateCSRCommonName": sensorCertificateCSRCommonName,
       "sensorCertificateCSRGenerateAction": sensorCertificateCSRGenerateAction,
       "sensorCertificateCSRGenerateStatus": sensorCertificateCSRGenerateStatus,
       "sensorCertSubAltName": sensorCertSubAltName,
       "sensorCertificateStatus": sensorCertificateStatus,
       "sensorCertMigrateAction": sensorCertMigrateAction,
       "sensorStackGrp": sensorStackGrp,
       "stackName": stackName,
       "stackNodeId": stackNodeId,
       "stackNodeLeftNeighbour": stackNodeLeftNeighbour,
       "stackNodeRightNeighbour": stackNodeRightNeighbour,
       "interfaceVirtualPortGrp": interfaceVirtualPortGrp,
       "intfVirtualPortTable": intfVirtualPortTable,
       "intfVirtualPortEntry": intfVirtualPortEntry,
       "intfVirtualPortIfDescr": intfVirtualPortIfDescr,
       "intfVirtualPortIfType": intfVirtualPortIfType,
       "intfVirtualPortIfAdminStatus": intfVirtualPortIfAdminStatus,
       "intfVirtualPortOperatingMode": intfVirtualPortOperatingMode,
       "intfVirtualPortEnableFullDuplex": intfVirtualPortEnableFullDuplex,
       "intfVirtualPortSpeedConfig": intfVirtualPortSpeedConfig,
       "intfVirtualPortEnableInternalTap": intfVirtualPortEnableInternalTap,
       "intfVirtualPortInOutType": intfVirtualPortInOutType,
       "intfVirtualFailOpenSwitchStatus": intfVirtualFailOpenSwitchStatus,
       "intfVirtualFailOpenPortStatus": intfVirtualFailOpenPortStatus,
       "intfVirtualPortEnableAntiSpoofing": intfVirtualPortEnableAntiSpoofing,
       "intfVirtualPortAllowAnyConnector": intfVirtualPortAllowAnyConnector,
       "intfVirtualPortCageType": intfVirtualPortCageType,
       "intfVirtualPortSetMediaType": intfVirtualPortSetMediaType,
       "intfVirtualPortMonPortIpAddress": intfVirtualPortMonPortIpAddress,
       "intfVirtualPortMonPortNetMask": intfVirtualPortMonPortNetMask,
       "intfVirtualPortGatewayIpAddress": intfVirtualPortGatewayIpAddress,
       "intfVirtualPortNbadConfigStatus": intfVirtualPortNbadConfigStatus,
       "intfVirtualPortVlanId": intfVirtualPortVlanId,
       "intfVirtualPortAppIdStatsConfigStatus": intfVirtualPortAppIdStatsConfigStatus,
       "intfVirtualPortLinearIndex": intfVirtualPortLinearIndex,
       "intfVirtualPortFECConfig": intfVirtualPortFECConfig,
       "responseVirtualPortGrp": responseVirtualPortGrp,
       "respVirtualPortTable": respVirtualPortTable,
       "respVirtualPortEntry": respVirtualPortEntry,
       "respVirtualPortDescr": respVirtualPortDescr,
       "respVirtualPortType": respVirtualPortType,
       "respVirtualPortAdminStatus": respVirtualPortAdminStatus,
       "respVirtualPortOperStatus": respVirtualPortOperStatus,
       "respVirtualPortEnableFullDuplex": respVirtualPortEnableFullDuplex,
       "respVirtualPortSpeed": respVirtualPortSpeed,
       "respVirtualPortPktDestination": respVirtualPortPktDestination,
       "respVirtualPortMacAddress": respVirtualPortMacAddress,
       "respVirtualCUGEPortSpeed": respVirtualCUGEPortSpeed,
       "respVirtualAdditionalInfo": respVirtualAdditionalInfo,
       "intfVirtualRespTable": intfVirtualRespTable,
       "intfVirtualRespEntry": intfVirtualRespEntry,
       "intfVirtualRespType": intfVirtualRespType,
       "intfVirtualRespPortNo": intfVirtualRespPortNo,
       "mvxCfgGrp": mvxCfgGrp,
       "mvxConnectionConfig": mvxConnectionConfig,
       "mvxIPAddressType": mvxIPAddressType,
       "mvxBrokerIPv4Address": mvxBrokerIPv4Address,
       "mvxBrokerIPv6Address": mvxBrokerIPv6Address,
       "mvxUserName": mvxUserName,
       "mvxPassword": mvxPassword,
       "mvxCertificateValidation": mvxCertificateValidation,
       "mvxAuthStatus": mvxAuthStatus,
       "mvxUseProxy": mvxUseProxy,
       "arpCfgGrp": arpCfgGrp,
       "arpSDEnable": arpSDEnable}
)
