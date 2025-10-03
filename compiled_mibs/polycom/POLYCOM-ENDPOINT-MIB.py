# SNMP MIB module (POLYCOM-ENDPOINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\polycom\POLYCOM-ENDPOINT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:49 2025
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

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType",
    "InetPortNumber")

(polycom,) = mibBuilder.importSymbols(
    "POLYCOM-BASE-MIB",
    "polycom")

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
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

polycom_endpoint_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101)
)
if mibBuilder.loadTexts:
    polycom_endpoint_MIB.setRevisions(
        ("2017-06-09 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Polycom_endpointNotifications_ObjectIdentity = ObjectIdentity
polycom_endpointNotifications = _Polycom_endpointNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0)
)
_Polycom_endpointObjects_ObjectIdentity = ObjectIdentity
polycom_endpointObjects = _Polycom_endpointObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1)
)
_Identity_ObjectIdentity = ObjectIdentity
identity = _Identity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1)
)
_IdentitySoftwareInfo_Type = OctetString
_IdentitySoftwareInfo_Object = MibScalar
identitySoftwareInfo = _IdentitySoftwareInfo_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 1),
    _IdentitySoftwareInfo_Type()
)
identitySoftwareInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identitySoftwareInfo.setStatus("current")
_IdentityBuildDate_Type = DateAndTime
_IdentityBuildDate_Object = MibScalar
identityBuildDate = _IdentityBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 2),
    _IdentityBuildDate_Type()
)
identityBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityBuildDate.setStatus("current")
_IdentityDeviceType_Type = OctetString
_IdentityDeviceType_Object = MibScalar
identityDeviceType = _IdentityDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 3),
    _IdentityDeviceType_Type()
)
identityDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityDeviceType.setStatus("current")
_IdentityDeviceModel_Type = OctetString
_IdentityDeviceModel_Object = MibScalar
identityDeviceModel = _IdentityDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 4),
    _IdentityDeviceModel_Type()
)
identityDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityDeviceModel.setStatus("current")
_IdentityDeviceSerialNumber_Type = OctetString
_IdentityDeviceSerialNumber_Object = MibScalar
identityDeviceSerialNumber = _IdentityDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 5),
    _IdentityDeviceSerialNumber_Type()
)
identityDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityDeviceSerialNumber.setStatus("current")


class _IdentityStatus_Type(Integer32):
    """Custom type identityStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_IdentityStatus_Type.__name__ = "Integer32"
_IdentityStatus_Object = MibScalar
identityStatus = _IdentityStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 6),
    _IdentityStatus_Type()
)
identityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityStatus.setStatus("current")
_IdentityDebugMode_Type = TruthValue
_IdentityDebugMode_Object = MibScalar
identityDebugMode = _IdentityDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 7),
    _IdentityDebugMode_Type()
)
identityDebugMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityDebugMode.setStatus("current")
_IdentityConsoleAccess_Type = TruthValue
_IdentityConsoleAccess_Object = MibScalar
identityConsoleAccess = _IdentityConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 8),
    _IdentityConsoleAccess_Type()
)
identityConsoleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityConsoleAccess.setStatus("current")
_IdentityMIBVersionSupported_Type = DisplayString
_IdentityMIBVersionSupported_Object = MibScalar
identityMIBVersionSupported = _IdentityMIBVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 9),
    _IdentityMIBVersionSupported_Type()
)
identityMIBVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityMIBVersionSupported.setStatus("current")
_IdentityLastDataUpdateTime_Type = DateAndTime
_IdentityLastDataUpdateTime_Object = MibScalar
identityLastDataUpdateTime = _IdentityLastDataUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 1, 10),
    _IdentityLastDataUpdateTime_Type()
)
identityLastDataUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityLastDataUpdateTime.setStatus("current")
_Service_ObjectIdentity = ObjectIdentity
service = _Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2)
)
_ServiceH323_ObjectIdentity = ObjectIdentity
serviceH323 = _ServiceH323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 7)
)


class _ServiceH323Status_Type(Integer32):
    """Custom type serviceH323Status based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ServiceH323Status_Type.__name__ = "Integer32"
_ServiceH323Status_Object = MibScalar
serviceH323Status = _ServiceH323Status_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 7, 1),
    _ServiceH323Status_Type()
)
serviceH323Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceH323Status.setStatus("current")


class _ServiceH323RegistrationStatus_Type(Integer32):
    """Custom type serviceH323RegistrationStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ServiceH323RegistrationStatus_Type.__name__ = "Integer32"
_ServiceH323RegistrationStatus_Object = MibScalar
serviceH323RegistrationStatus = _ServiceH323RegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 7, 2),
    _ServiceH323RegistrationStatus_Type()
)
serviceH323RegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceH323RegistrationStatus.setStatus("current")
_ServiceH323GatekeeperTable_Object = MibTable
serviceH323GatekeeperTable = _ServiceH323GatekeeperTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    serviceH323GatekeeperTable.setStatus("current")
_ServiceH323GatekeeperEntry_Object = MibTableRow
serviceH323GatekeeperEntry = _ServiceH323GatekeeperEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 7, 3, 1)
)
serviceH323GatekeeperEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "serviceH323GatekeeperIndex"),
)
if mibBuilder.loadTexts:
    serviceH323GatekeeperEntry.setStatus("current")
_ServiceH323GatekeeperIndex_Type = Unsigned32
_ServiceH323GatekeeperIndex_Object = MibTableColumn
serviceH323GatekeeperIndex = _ServiceH323GatekeeperIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 7, 3, 1, 1),
    _ServiceH323GatekeeperIndex_Type()
)
serviceH323GatekeeperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceH323GatekeeperIndex.setStatus("current")


class _ServiceH323GatekeeperStatus_Type(Integer32):
    """Custom type serviceH323GatekeeperStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ServiceH323GatekeeperStatus_Type.__name__ = "Integer32"
_ServiceH323GatekeeperStatus_Object = MibTableColumn
serviceH323GatekeeperStatus = _ServiceH323GatekeeperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 7, 3, 1, 2),
    _ServiceH323GatekeeperStatus_Type()
)
serviceH323GatekeeperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceH323GatekeeperStatus.setStatus("current")
_ServiceH323GatekeeperH239Enabled_Type = Integer32
_ServiceH323GatekeeperH239Enabled_Object = MibTableColumn
serviceH323GatekeeperH239Enabled = _ServiceH323GatekeeperH239Enabled_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 7, 3, 1, 3),
    _ServiceH323GatekeeperH239Enabled_Type()
)
serviceH323GatekeeperH239Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceH323GatekeeperH239Enabled.setStatus("current")
_ServiceSip_ObjectIdentity = ObjectIdentity
serviceSip = _ServiceSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8)
)


class _ServiceSipStatus_Type(Integer32):
    """Custom type serviceSipStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ServiceSipStatus_Type.__name__ = "Integer32"
_ServiceSipStatus_Object = MibScalar
serviceSipStatus = _ServiceSipStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 1),
    _ServiceSipStatus_Type()
)
serviceSipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceSipStatus.setStatus("current")
_ServiceSipProxyTable_Object = MibTable
serviceSipProxyTable = _ServiceSipProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    serviceSipProxyTable.setStatus("current")
_ServiceSipProxyEntry_Object = MibTableRow
serviceSipProxyEntry = _ServiceSipProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 2, 1)
)
serviceSipProxyEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "serviceSipProxyIndex"),
)
if mibBuilder.loadTexts:
    serviceSipProxyEntry.setStatus("current")
_ServiceSipProxyIndex_Type = Unsigned32
_ServiceSipProxyIndex_Object = MibTableColumn
serviceSipProxyIndex = _ServiceSipProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 2, 1, 1),
    _ServiceSipProxyIndex_Type()
)
serviceSipProxyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceSipProxyIndex.setStatus("current")


class _ServiceSipProxyStatus_Type(Integer32):
    """Custom type serviceSipProxyStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ServiceSipProxyStatus_Type.__name__ = "Integer32"
_ServiceSipProxyStatus_Object = MibTableColumn
serviceSipProxyStatus = _ServiceSipProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 2, 1, 2),
    _ServiceSipProxyStatus_Type()
)
serviceSipProxyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceSipProxyStatus.setStatus("current")
_ServiceSipRegistrationTable_Object = MibTable
serviceSipRegistrationTable = _ServiceSipRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    serviceSipRegistrationTable.setStatus("current")
_ServiceSipRegistrationEntry_Object = MibTableRow
serviceSipRegistrationEntry = _ServiceSipRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 3, 1)
)
serviceSipRegistrationEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "serviceSipRegistrationIndex"),
)
if mibBuilder.loadTexts:
    serviceSipRegistrationEntry.setStatus("current")
_ServiceSipRegistrationIndex_Type = Unsigned32
_ServiceSipRegistrationIndex_Object = MibTableColumn
serviceSipRegistrationIndex = _ServiceSipRegistrationIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 3, 1, 1),
    _ServiceSipRegistrationIndex_Type()
)
serviceSipRegistrationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceSipRegistrationIndex.setStatus("current")


class _ServiceSipRegistrationStatus_Type(Integer32):
    """Custom type serviceSipRegistrationStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ServiceSipRegistrationStatus_Type.__name__ = "Integer32"
_ServiceSipRegistrationStatus_Object = MibTableColumn
serviceSipRegistrationStatus = _ServiceSipRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 8, 3, 1, 2),
    _ServiceSipRegistrationStatus_Type()
)
serviceSipRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceSipRegistrationStatus.setStatus("current")
_ServiceIsdn_ObjectIdentity = ObjectIdentity
serviceIsdn = _ServiceIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 9)
)


class _ServiceIsdnStatus_Type(Integer32):
    """Custom type serviceIsdnStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ServiceIsdnStatus_Type.__name__ = "Integer32"
_ServiceIsdnStatus_Object = MibScalar
serviceIsdnStatus = _ServiceIsdnStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 9, 1),
    _ServiceIsdnStatus_Type()
)
serviceIsdnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceIsdnStatus.setStatus("current")
_ServiceSecurity_ObjectIdentity = ObjectIdentity
serviceSecurity = _ServiceSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 10)
)
_ServiceSecurityProfile_Type = DisplayString
_ServiceSecurityProfile_Object = MibScalar
serviceSecurityProfile = _ServiceSecurityProfile_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 2, 10, 1),
    _ServiceSecurityProfile_Type()
)
serviceSecurityProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceSecurityProfile.setStatus("current")
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3)
)


class _HardwareOverallStatus_Type(Integer32):
    """Custom type hardwareOverallStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwareOverallStatus_Type.__name__ = "Integer32"
_HardwareOverallStatus_Object = MibScalar
hardwareOverallStatus = _HardwareOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 1),
    _HardwareOverallStatus_Type()
)
hardwareOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareOverallStatus.setStatus("current")
_HardwareMicrophone_ObjectIdentity = ObjectIdentity
hardwareMicrophone = _HardwareMicrophone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 5)
)


class _HardwareMicrophoneStatus_Type(Integer32):
    """Custom type hardwareMicrophoneStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwareMicrophoneStatus_Type.__name__ = "Integer32"
_HardwareMicrophoneStatus_Object = MibScalar
hardwareMicrophoneStatus = _HardwareMicrophoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 5, 1),
    _HardwareMicrophoneStatus_Type()
)
hardwareMicrophoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareMicrophoneStatus.setStatus("current")
_HardwareMicrophoneMicrophonesTable_Object = MibTable
hardwareMicrophoneMicrophonesTable = _HardwareMicrophoneMicrophonesTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    hardwareMicrophoneMicrophonesTable.setStatus("current")
_HardwareMicrophoneMicrophonesEntry_Object = MibTableRow
hardwareMicrophoneMicrophonesEntry = _HardwareMicrophoneMicrophonesEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 5, 2, 1)
)
hardwareMicrophoneMicrophonesEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "hardwareMicrophoneMicrophonesIndex"),
)
if mibBuilder.loadTexts:
    hardwareMicrophoneMicrophonesEntry.setStatus("current")
_HardwareMicrophoneMicrophonesIndex_Type = Unsigned32
_HardwareMicrophoneMicrophonesIndex_Object = MibTableColumn
hardwareMicrophoneMicrophonesIndex = _HardwareMicrophoneMicrophonesIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 5, 2, 1, 1),
    _HardwareMicrophoneMicrophonesIndex_Type()
)
hardwareMicrophoneMicrophonesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareMicrophoneMicrophonesIndex.setStatus("current")
_HardwareMicrophoneMicrophonesName_Type = DisplayString
_HardwareMicrophoneMicrophonesName_Object = MibTableColumn
hardwareMicrophoneMicrophonesName = _HardwareMicrophoneMicrophonesName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 5, 2, 1, 2),
    _HardwareMicrophoneMicrophonesName_Type()
)
hardwareMicrophoneMicrophonesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareMicrophoneMicrophonesName.setStatus("current")


class _HardwareMicrophoneMicrophonesStatus_Type(Integer32):
    """Custom type hardwareMicrophoneMicrophonesStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwareMicrophoneMicrophonesStatus_Type.__name__ = "Integer32"
_HardwareMicrophoneMicrophonesStatus_Object = MibTableColumn
hardwareMicrophoneMicrophonesStatus = _HardwareMicrophoneMicrophonesStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 5, 2, 1, 3),
    _HardwareMicrophoneMicrophonesStatus_Type()
)
hardwareMicrophoneMicrophonesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareMicrophoneMicrophonesStatus.setStatus("current")
_HardwareCamera_ObjectIdentity = ObjectIdentity
hardwareCamera = _HardwareCamera_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 6)
)


class _HardwareCameraStatus_Type(Integer32):
    """Custom type hardwareCameraStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwareCameraStatus_Type.__name__ = "Integer32"
_HardwareCameraStatus_Object = MibScalar
hardwareCameraStatus = _HardwareCameraStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 6, 1),
    _HardwareCameraStatus_Type()
)
hardwareCameraStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareCameraStatus.setStatus("current")
_HardwareCameraCamerasTable_Object = MibTable
hardwareCameraCamerasTable = _HardwareCameraCamerasTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    hardwareCameraCamerasTable.setStatus("current")
_HardwareCameraCamerasEntry_Object = MibTableRow
hardwareCameraCamerasEntry = _HardwareCameraCamerasEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 6, 2, 1)
)
hardwareCameraCamerasEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "hardwareCameraCamerasIndex"),
)
if mibBuilder.loadTexts:
    hardwareCameraCamerasEntry.setStatus("current")
_HardwareCameraCamerasIndex_Type = Unsigned32
_HardwareCameraCamerasIndex_Object = MibTableColumn
hardwareCameraCamerasIndex = _HardwareCameraCamerasIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 6, 2, 1, 1),
    _HardwareCameraCamerasIndex_Type()
)
hardwareCameraCamerasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareCameraCamerasIndex.setStatus("current")
_HardwareCameraCamerasName_Type = DisplayString
_HardwareCameraCamerasName_Object = MibTableColumn
hardwareCameraCamerasName = _HardwareCameraCamerasName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 6, 2, 1, 2),
    _HardwareCameraCamerasName_Type()
)
hardwareCameraCamerasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareCameraCamerasName.setStatus("current")


class _HardwareCameraCamerasStatus_Type(Integer32):
    """Custom type hardwareCameraCamerasStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwareCameraCamerasStatus_Type.__name__ = "Integer32"
_HardwareCameraCamerasStatus_Object = MibTableColumn
hardwareCameraCamerasStatus = _HardwareCameraCamerasStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 6, 2, 1, 3),
    _HardwareCameraCamerasStatus_Type()
)
hardwareCameraCamerasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareCameraCamerasStatus.setStatus("current")
_HardwareNIC_ObjectIdentity = ObjectIdentity
hardwareNIC = _HardwareNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10)
)


class _HardwareNICStatus_Type(Integer32):
    """Custom type hardwareNICStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwareNICStatus_Type.__name__ = "Integer32"
_HardwareNICStatus_Object = MibScalar
hardwareNICStatus = _HardwareNICStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 1),
    _HardwareNICStatus_Type()
)
hardwareNICStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNICStatus.setStatus("current")
_HardwareNICNICsTable_Object = MibTable
hardwareNICNICsTable = _HardwareNICNICsTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    hardwareNICNICsTable.setStatus("current")
_HardwareNICNICsEntry_Object = MibTableRow
hardwareNICNICsEntry = _HardwareNICNICsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2, 1)
)
hardwareNICNICsEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "hardwareNICNICsIndex"),
)
if mibBuilder.loadTexts:
    hardwareNICNICsEntry.setStatus("current")
_HardwareNICNICsIndex_Type = Unsigned32
_HardwareNICNICsIndex_Object = MibTableColumn
hardwareNICNICsIndex = _HardwareNICNICsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2, 1, 1),
    _HardwareNICNICsIndex_Type()
)
hardwareNICNICsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNICNICsIndex.setStatus("current")
_HardwareNICNICsName_Type = DisplayString
_HardwareNICNICsName_Object = MibTableColumn
hardwareNICNICsName = _HardwareNICNICsName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2, 1, 2),
    _HardwareNICNICsName_Type()
)
hardwareNICNICsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNICNICsName.setStatus("current")
_HardwareNICNICsMAC_Type = DisplayString
_HardwareNICNICsMAC_Object = MibTableColumn
hardwareNICNICsMAC = _HardwareNICNICsMAC_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2, 1, 3),
    _HardwareNICNICsMAC_Type()
)
hardwareNICNICsMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNICNICsMAC.setStatus("current")
_HardwareNICNICsSpeed_Type = Unsigned32
_HardwareNICNICsSpeed_Object = MibTableColumn
hardwareNICNICsSpeed = _HardwareNICNICsSpeed_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2, 1, 4),
    _HardwareNICNICsSpeed_Type()
)
hardwareNICNICsSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNICNICsSpeed.setStatus("current")
_HardwareNICNICsDuplex_Type = DisplayString
_HardwareNICNICsDuplex_Object = MibTableColumn
hardwareNICNICsDuplex = _HardwareNICNICsDuplex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2, 1, 5),
    _HardwareNICNICsDuplex_Type()
)
hardwareNICNICsDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNICNICsDuplex.setStatus("current")


class _HardwareNICNICsStatus_Type(Integer32):
    """Custom type hardwareNICNICsStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwareNICNICsStatus_Type.__name__ = "Integer32"
_HardwareNICNICsStatus_Object = MibTableColumn
hardwareNICNICsStatus = _HardwareNICNICsStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2, 1, 6),
    _HardwareNICNICsStatus_Type()
)
hardwareNICNICsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNICNICsStatus.setStatus("current")
_HardwareNICNICsIPType_Type = Integer32
_HardwareNICNICsIPType_Object = MibTableColumn
hardwareNICNICsIPType = _HardwareNICNICsIPType_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 10, 2, 1, 7),
    _HardwareNICNICsIPType_Type()
)
hardwareNICNICsIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNICNICsIPType.setStatus("current")
_HardwarePTC_ObjectIdentity = ObjectIdentity
hardwarePTC = _HardwarePTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 11)
)


class _HardwarePTCStatus_Type(Integer32):
    """Custom type hardwarePTCStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwarePTCStatus_Type.__name__ = "Integer32"
_HardwarePTCStatus_Object = MibScalar
hardwarePTCStatus = _HardwarePTCStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 11, 1),
    _HardwarePTCStatus_Type()
)
hardwarePTCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePTCStatus.setStatus("current")
_HardwarePTCPTCsTable_Object = MibTable
hardwarePTCPTCsTable = _HardwarePTCPTCsTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 11, 2)
)
if mibBuilder.loadTexts:
    hardwarePTCPTCsTable.setStatus("current")
_HardwarePTCPTCsEntry_Object = MibTableRow
hardwarePTCPTCsEntry = _HardwarePTCPTCsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 11, 2, 1)
)
hardwarePTCPTCsEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "hardwarePTCPTCsIndex"),
)
if mibBuilder.loadTexts:
    hardwarePTCPTCsEntry.setStatus("current")
_HardwarePTCPTCsIndex_Type = Unsigned32
_HardwarePTCPTCsIndex_Object = MibTableColumn
hardwarePTCPTCsIndex = _HardwarePTCPTCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 11, 2, 1, 1),
    _HardwarePTCPTCsIndex_Type()
)
hardwarePTCPTCsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePTCPTCsIndex.setStatus("current")
_HardwarePTCPTCsStatus_Type = DisplayString
_HardwarePTCPTCsStatus_Object = MibTableColumn
hardwarePTCPTCsStatus = _HardwarePTCPTCsStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 11, 2, 1, 2),
    _HardwarePTCPTCsStatus_Type()
)
hardwarePTCPTCsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePTCPTCsStatus.setStatus("current")
_HardwareUcBoard_ObjectIdentity = ObjectIdentity
hardwareUcBoard = _HardwareUcBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 12)
)


class _HardwareUcBoardStatus_Type(Integer32):
    """Custom type hardwareUcBoardStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_HardwareUcBoardStatus_Type.__name__ = "Integer32"
_HardwareUcBoardStatus_Object = MibScalar
hardwareUcBoardStatus = _HardwareUcBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 12, 1),
    _HardwareUcBoardStatus_Type()
)
hardwareUcBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareUcBoardStatus.setStatus("current")
_HardwareUcBoardUcBoardsTable_Object = MibTable
hardwareUcBoardUcBoardsTable = _HardwareUcBoardUcBoardsTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 12, 2)
)
if mibBuilder.loadTexts:
    hardwareUcBoardUcBoardsTable.setStatus("current")
_HardwareUcBoardUcBoardsEntry_Object = MibTableRow
hardwareUcBoardUcBoardsEntry = _HardwareUcBoardUcBoardsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 12, 2, 1)
)
hardwareUcBoardUcBoardsEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "hardwareUcBoardUcBoardsIndex"),
)
if mibBuilder.loadTexts:
    hardwareUcBoardUcBoardsEntry.setStatus("current")
_HardwareUcBoardUcBoardsIndex_Type = Unsigned32
_HardwareUcBoardUcBoardsIndex_Object = MibTableColumn
hardwareUcBoardUcBoardsIndex = _HardwareUcBoardUcBoardsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 12, 2, 1, 1),
    _HardwareUcBoardUcBoardsIndex_Type()
)
hardwareUcBoardUcBoardsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareUcBoardUcBoardsIndex.setStatus("current")
_HardwareUcBoardUcBoardsStatus_Type = DisplayString
_HardwareUcBoardUcBoardsStatus_Object = MibTableColumn
hardwareUcBoardUcBoardsStatus = _HardwareUcBoardUcBoardsStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 3, 12, 2, 1, 2),
    _HardwareUcBoardUcBoardsStatus_Type()
)
hardwareUcBoardUcBoardsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareUcBoardUcBoardsStatus.setStatus("current")
_Call_ObjectIdentity = ObjectIdentity
call = _Call_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4)
)
_CallActiveCallsTable_Object = MibTable
callActiveCallsTable = _CallActiveCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1)
)
if mibBuilder.loadTexts:
    callActiveCallsTable.setStatus("current")
_CallActiveCallsEntry_Object = MibTableRow
callActiveCallsEntry = _CallActiveCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1)
)
callActiveCallsEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "callActiveCallsIndex"),
)
if mibBuilder.loadTexts:
    callActiveCallsEntry.setStatus("current")
_CallActiveCallsIndex_Type = Unsigned32
_CallActiveCallsIndex_Object = MibTableColumn
callActiveCallsIndex = _CallActiveCallsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 1),
    _CallActiveCallsIndex_Type()
)
callActiveCallsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsIndex.setStatus("current")
_CallActiveCallsCallID_Type = DisplayString
_CallActiveCallsCallID_Object = MibTableColumn
callActiveCallsCallID = _CallActiveCallsCallID_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 2),
    _CallActiveCallsCallID_Type()
)
callActiveCallsCallID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsCallID.setStatus("current")
_CallActiveCallsConfID_Type = DisplayString
_CallActiveCallsConfID_Object = MibTableColumn
callActiveCallsConfID = _CallActiveCallsConfID_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 3),
    _CallActiveCallsConfID_Type()
)
callActiveCallsConfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsConfID.setStatus("current")
_CallActiveCallsVoiceJitterRX_Type = Unsigned32
_CallActiveCallsVoiceJitterRX_Object = MibTableColumn
callActiveCallsVoiceJitterRX = _CallActiveCallsVoiceJitterRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 4),
    _CallActiveCallsVoiceJitterRX_Type()
)
callActiveCallsVoiceJitterRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVoiceJitterRX.setStatus("current")
_CallActiveCallsVoiceJitterTX_Type = Unsigned32
_CallActiveCallsVoiceJitterTX_Object = MibTableColumn
callActiveCallsVoiceJitterTX = _CallActiveCallsVoiceJitterTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 5),
    _CallActiveCallsVoiceJitterTX_Type()
)
callActiveCallsVoiceJitterTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVoiceJitterTX.setStatus("current")
_CallActiveCallsVoiceLatencyRX_Type = Unsigned32
_CallActiveCallsVoiceLatencyRX_Object = MibTableColumn
callActiveCallsVoiceLatencyRX = _CallActiveCallsVoiceLatencyRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 6),
    _CallActiveCallsVoiceLatencyRX_Type()
)
callActiveCallsVoiceLatencyRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVoiceLatencyRX.setStatus("current")
_CallActiveCallsVoiceLatencyTX_Type = Unsigned32
_CallActiveCallsVoiceLatencyTX_Object = MibTableColumn
callActiveCallsVoiceLatencyTX = _CallActiveCallsVoiceLatencyTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 7),
    _CallActiveCallsVoiceLatencyTX_Type()
)
callActiveCallsVoiceLatencyTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVoiceLatencyTX.setStatus("current")
_CallActiveCallsVoicePacketLossRX_Type = Unsigned32
_CallActiveCallsVoicePacketLossRX_Object = MibTableColumn
callActiveCallsVoicePacketLossRX = _CallActiveCallsVoicePacketLossRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 8),
    _CallActiveCallsVoicePacketLossRX_Type()
)
callActiveCallsVoicePacketLossRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVoicePacketLossRX.setStatus("current")
_CallActiveCallsVoicePacketLossTX_Type = Unsigned32
_CallActiveCallsVoicePacketLossTX_Object = MibTableColumn
callActiveCallsVoicePacketLossTX = _CallActiveCallsVoicePacketLossTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 9),
    _CallActiveCallsVoicePacketLossTX_Type()
)
callActiveCallsVoicePacketLossTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVoicePacketLossTX.setStatus("current")
_CallActiveCallsVoiceProtocolRX_Type = DisplayString
_CallActiveCallsVoiceProtocolRX_Object = MibTableColumn
callActiveCallsVoiceProtocolRX = _CallActiveCallsVoiceProtocolRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 10),
    _CallActiveCallsVoiceProtocolRX_Type()
)
callActiveCallsVoiceProtocolRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVoiceProtocolRX.setStatus("current")
_CallActiveCallsVoiceProtocolTX_Type = DisplayString
_CallActiveCallsVoiceProtocolTX_Object = MibTableColumn
callActiveCallsVoiceProtocolTX = _CallActiveCallsVoiceProtocolTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 11),
    _CallActiveCallsVoiceProtocolTX_Type()
)
callActiveCallsVoiceProtocolTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVoiceProtocolTX.setStatus("current")
_CallActiveCallsMaxVoiceJitterRX_Type = Unsigned32
_CallActiveCallsMaxVoiceJitterRX_Object = MibTableColumn
callActiveCallsMaxVoiceJitterRX = _CallActiveCallsMaxVoiceJitterRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 12),
    _CallActiveCallsMaxVoiceJitterRX_Type()
)
callActiveCallsMaxVoiceJitterRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsMaxVoiceJitterRX.setStatus("current")
_CallActiveCallsMaxVoiceJitterTX_Type = Unsigned32
_CallActiveCallsMaxVoiceJitterTX_Object = MibTableColumn
callActiveCallsMaxVoiceJitterTX = _CallActiveCallsMaxVoiceJitterTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 13),
    _CallActiveCallsMaxVoiceJitterTX_Type()
)
callActiveCallsMaxVoiceJitterTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsMaxVoiceJitterTX.setStatus("current")
_CallActiveCallsTotalPacketsLostRX_Type = Unsigned32
_CallActiveCallsTotalPacketsLostRX_Object = MibTableColumn
callActiveCallsTotalPacketsLostRX = _CallActiveCallsTotalPacketsLostRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 14),
    _CallActiveCallsTotalPacketsLostRX_Type()
)
callActiveCallsTotalPacketsLostRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsTotalPacketsLostRX.setStatus("current")
_CallActiveCallsTotalPacketsLostTX_Type = Unsigned32
_CallActiveCallsTotalPacketsLostTX_Object = MibTableColumn
callActiveCallsTotalPacketsLostTX = _CallActiveCallsTotalPacketsLostTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 15),
    _CallActiveCallsTotalPacketsLostTX_Type()
)
callActiveCallsTotalPacketsLostTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsTotalPacketsLostTX.setStatus("current")
_CallActiveCallsPctPacketLostRX_Type = Unsigned32
_CallActiveCallsPctPacketLostRX_Object = MibTableColumn
callActiveCallsPctPacketLostRX = _CallActiveCallsPctPacketLostRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 16),
    _CallActiveCallsPctPacketLostRX_Type()
)
callActiveCallsPctPacketLostRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsPctPacketLostRX.setStatus("current")
_CallActiveCallsPctPacketLostTX_Type = Unsigned32
_CallActiveCallsPctPacketLostTX_Object = MibTableColumn
callActiveCallsPctPacketLostTX = _CallActiveCallsPctPacketLostTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 17),
    _CallActiveCallsPctPacketLostTX_Type()
)
callActiveCallsPctPacketLostTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsPctPacketLostTX.setStatus("current")
_CallActiveCallsOverallLatencyRX_Type = Unsigned32
_CallActiveCallsOverallLatencyRX_Object = MibTableColumn
callActiveCallsOverallLatencyRX = _CallActiveCallsOverallLatencyRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 18),
    _CallActiveCallsOverallLatencyRX_Type()
)
callActiveCallsOverallLatencyRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsOverallLatencyRX.setStatus("current")
_CallActiveCallsOverallLatencyTX_Type = Unsigned32
_CallActiveCallsOverallLatencyTX_Object = MibTableColumn
callActiveCallsOverallLatencyTX = _CallActiveCallsOverallLatencyTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 19),
    _CallActiveCallsOverallLatencyTX_Type()
)
callActiveCallsOverallLatencyTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsOverallLatencyTX.setStatus("current")
_CallActiveCallsOverallJitterRX_Type = Unsigned32
_CallActiveCallsOverallJitterRX_Object = MibTableColumn
callActiveCallsOverallJitterRX = _CallActiveCallsOverallJitterRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 20),
    _CallActiveCallsOverallJitterRX_Type()
)
callActiveCallsOverallJitterRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsOverallJitterRX.setStatus("current")
_CallActiveCallsOverallJitterTX_Type = Unsigned32
_CallActiveCallsOverallJitterTX_Object = MibTableColumn
callActiveCallsOverallJitterTX = _CallActiveCallsOverallJitterTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 21),
    _CallActiveCallsOverallJitterTX_Type()
)
callActiveCallsOverallJitterTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsOverallJitterTX.setStatus("current")
_CallActiveCallsContentFormatRsltnRX_Type = DisplayString
_CallActiveCallsContentFormatRsltnRX_Object = MibTableColumn
callActiveCallsContentFormatRsltnRX = _CallActiveCallsContentFormatRsltnRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 22),
    _CallActiveCallsContentFormatRsltnRX_Type()
)
callActiveCallsContentFormatRsltnRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentFormatRsltnRX.setStatus("current")
_CallActiveCallsContentFormatRsltnTX_Type = DisplayString
_CallActiveCallsContentFormatRsltnTX_Object = MibTableColumn
callActiveCallsContentFormatRsltnTX = _CallActiveCallsContentFormatRsltnTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 23),
    _CallActiveCallsContentFormatRsltnTX_Type()
)
callActiveCallsContentFormatRsltnTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentFormatRsltnTX.setStatus("current")
_CallActiveCallsContentFrameRateRX_Type = DisplayString
_CallActiveCallsContentFrameRateRX_Object = MibTableColumn
callActiveCallsContentFrameRateRX = _CallActiveCallsContentFrameRateRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 24),
    _CallActiveCallsContentFrameRateRX_Type()
)
callActiveCallsContentFrameRateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentFrameRateRX.setStatus("current")
_CallActiveCallsContentFrameRateTX_Type = DisplayString
_CallActiveCallsContentFrameRateTX_Object = MibTableColumn
callActiveCallsContentFrameRateTX = _CallActiveCallsContentFrameRateTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 25),
    _CallActiveCallsContentFrameRateTX_Type()
)
callActiveCallsContentFrameRateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentFrameRateTX.setStatus("current")
_CallActiveCallsContentJitterRX_Type = Unsigned32
_CallActiveCallsContentJitterRX_Object = MibTableColumn
callActiveCallsContentJitterRX = _CallActiveCallsContentJitterRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 26),
    _CallActiveCallsContentJitterRX_Type()
)
callActiveCallsContentJitterRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentJitterRX.setStatus("current")
_CallActiveCallsContentJitterTX_Type = Unsigned32
_CallActiveCallsContentJitterTX_Object = MibTableColumn
callActiveCallsContentJitterTX = _CallActiveCallsContentJitterTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 27),
    _CallActiveCallsContentJitterTX_Type()
)
callActiveCallsContentJitterTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentJitterTX.setStatus("current")
_CallActiveCallsContentLatencyRX_Type = Unsigned32
_CallActiveCallsContentLatencyRX_Object = MibTableColumn
callActiveCallsContentLatencyRX = _CallActiveCallsContentLatencyRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 28),
    _CallActiveCallsContentLatencyRX_Type()
)
callActiveCallsContentLatencyRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentLatencyRX.setStatus("current")
_CallActiveCallsContentLatencyTX_Type = Unsigned32
_CallActiveCallsContentLatencyTX_Object = MibTableColumn
callActiveCallsContentLatencyTX = _CallActiveCallsContentLatencyTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 29),
    _CallActiveCallsContentLatencyTX_Type()
)
callActiveCallsContentLatencyTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentLatencyTX.setStatus("current")
_CallActiveCallsContentPacketLossRX_Type = Unsigned32
_CallActiveCallsContentPacketLossRX_Object = MibTableColumn
callActiveCallsContentPacketLossRX = _CallActiveCallsContentPacketLossRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 30),
    _CallActiveCallsContentPacketLossRX_Type()
)
callActiveCallsContentPacketLossRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentPacketLossRX.setStatus("current")
_CallActiveCallsContentPacketLossTX_Type = Unsigned32
_CallActiveCallsContentPacketLossTX_Object = MibTableColumn
callActiveCallsContentPacketLossTX = _CallActiveCallsContentPacketLossTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 31),
    _CallActiveCallsContentPacketLossTX_Type()
)
callActiveCallsContentPacketLossTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentPacketLossTX.setStatus("current")
_CallActiveCallsContentProtocolRX_Type = DisplayString
_CallActiveCallsContentProtocolRX_Object = MibTableColumn
callActiveCallsContentProtocolRX = _CallActiveCallsContentProtocolRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 32),
    _CallActiveCallsContentProtocolRX_Type()
)
callActiveCallsContentProtocolRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentProtocolRX.setStatus("current")
_CallActiveCallsContentProtocolTX_Type = DisplayString
_CallActiveCallsContentProtocolTX_Object = MibTableColumn
callActiveCallsContentProtocolTX = _CallActiveCallsContentProtocolTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 33),
    _CallActiveCallsContentProtocolTX_Type()
)
callActiveCallsContentProtocolTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentProtocolTX.setStatus("current")
_CallActiveCallsContentRateRX_Type = Unsigned32
_CallActiveCallsContentRateRX_Object = MibTableColumn
callActiveCallsContentRateRX = _CallActiveCallsContentRateRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 34),
    _CallActiveCallsContentRateRX_Type()
)
callActiveCallsContentRateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentRateRX.setStatus("current")
_CallActiveCallsContentRateTX_Type = Unsigned32
_CallActiveCallsContentRateTX_Object = MibTableColumn
callActiveCallsContentRateTX = _CallActiveCallsContentRateTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 35),
    _CallActiveCallsContentRateTX_Type()
)
callActiveCallsContentRateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentRateTX.setStatus("current")
_CallActiveCallsContentRateUsedRX_Type = Unsigned32
_CallActiveCallsContentRateUsedRX_Object = MibTableColumn
callActiveCallsContentRateUsedRX = _CallActiveCallsContentRateUsedRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 36),
    _CallActiveCallsContentRateUsedRX_Type()
)
callActiveCallsContentRateUsedRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentRateUsedRX.setStatus("current")
_CallActiveCallsContentRateUsedTX_Type = Unsigned32
_CallActiveCallsContentRateUsedTX_Object = MibTableColumn
callActiveCallsContentRateUsedTX = _CallActiveCallsContentRateUsedTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 37),
    _CallActiveCallsContentRateUsedTX_Type()
)
callActiveCallsContentRateUsedTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsContentRateUsedTX.setStatus("current")
_CallActiveCallsVideoAnnexRX_Type = DisplayString
_CallActiveCallsVideoAnnexRX_Object = MibTableColumn
callActiveCallsVideoAnnexRX = _CallActiveCallsVideoAnnexRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 38),
    _CallActiveCallsVideoAnnexRX_Type()
)
callActiveCallsVideoAnnexRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoAnnexRX.setStatus("current")
_CallActiveCallsVideoAnnexTX_Type = DisplayString
_CallActiveCallsVideoAnnexTX_Object = MibTableColumn
callActiveCallsVideoAnnexTX = _CallActiveCallsVideoAnnexTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 39),
    _CallActiveCallsVideoAnnexTX_Type()
)
callActiveCallsVideoAnnexTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoAnnexTX.setStatus("current")
_CallActiveCallsVideoFECErrorsRX_Type = Unsigned32
_CallActiveCallsVideoFECErrorsRX_Object = MibTableColumn
callActiveCallsVideoFECErrorsRX = _CallActiveCallsVideoFECErrorsRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 40),
    _CallActiveCallsVideoFECErrorsRX_Type()
)
callActiveCallsVideoFECErrorsRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoFECErrorsRX.setStatus("current")
_CallActiveCallsVideoFECErrorsTX_Type = Unsigned32
_CallActiveCallsVideoFECErrorsTX_Object = MibTableColumn
callActiveCallsVideoFECErrorsTX = _CallActiveCallsVideoFECErrorsTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 41),
    _CallActiveCallsVideoFECErrorsTX_Type()
)
callActiveCallsVideoFECErrorsTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoFECErrorsTX.setStatus("current")
_CallActiveCallsVideoRsltnRX_Type = DisplayString
_CallActiveCallsVideoRsltnRX_Object = MibTableColumn
callActiveCallsVideoRsltnRX = _CallActiveCallsVideoRsltnRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 42),
    _CallActiveCallsVideoRsltnRX_Type()
)
callActiveCallsVideoRsltnRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoRsltnRX.setStatus("current")
_CallActiveCallsVideoRsltnTX_Type = DisplayString
_CallActiveCallsVideoRsltnTX_Object = MibTableColumn
callActiveCallsVideoRsltnTX = _CallActiveCallsVideoRsltnTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 43),
    _CallActiveCallsVideoRsltnTX_Type()
)
callActiveCallsVideoRsltnTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoRsltnTX.setStatus("current")
_CallActiveCallsVideoFrameRateRX_Type = DisplayString
_CallActiveCallsVideoFrameRateRX_Object = MibTableColumn
callActiveCallsVideoFrameRateRX = _CallActiveCallsVideoFrameRateRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 44),
    _CallActiveCallsVideoFrameRateRX_Type()
)
callActiveCallsVideoFrameRateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoFrameRateRX.setStatus("current")
_CallActiveCallsVideoFrameRateTX_Type = DisplayString
_CallActiveCallsVideoFrameRateTX_Object = MibTableColumn
callActiveCallsVideoFrameRateTX = _CallActiveCallsVideoFrameRateTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 45),
    _CallActiveCallsVideoFrameRateTX_Type()
)
callActiveCallsVideoFrameRateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoFrameRateTX.setStatus("current")
_CallActiveCallsVideoJitterRX_Type = Unsigned32
_CallActiveCallsVideoJitterRX_Object = MibTableColumn
callActiveCallsVideoJitterRX = _CallActiveCallsVideoJitterRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 46),
    _CallActiveCallsVideoJitterRX_Type()
)
callActiveCallsVideoJitterRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoJitterRX.setStatus("current")
_CallActiveCallsVideoJitterTX_Type = Unsigned32
_CallActiveCallsVideoJitterTX_Object = MibTableColumn
callActiveCallsVideoJitterTX = _CallActiveCallsVideoJitterTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 47),
    _CallActiveCallsVideoJitterTX_Type()
)
callActiveCallsVideoJitterTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoJitterTX.setStatus("current")
_CallActiveCallsVideoLatencyRX_Type = Unsigned32
_CallActiveCallsVideoLatencyRX_Object = MibTableColumn
callActiveCallsVideoLatencyRX = _CallActiveCallsVideoLatencyRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 48),
    _CallActiveCallsVideoLatencyRX_Type()
)
callActiveCallsVideoLatencyRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoLatencyRX.setStatus("current")
_CallActiveCallsVideoLatencyTX_Type = Unsigned32
_CallActiveCallsVideoLatencyTX_Object = MibTableColumn
callActiveCallsVideoLatencyTX = _CallActiveCallsVideoLatencyTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 49),
    _CallActiveCallsVideoLatencyTX_Type()
)
callActiveCallsVideoLatencyTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoLatencyTX.setStatus("current")
_CallActiveCallsVideoPacketLossRX_Type = Unsigned32
_CallActiveCallsVideoPacketLossRX_Object = MibTableColumn
callActiveCallsVideoPacketLossRX = _CallActiveCallsVideoPacketLossRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 50),
    _CallActiveCallsVideoPacketLossRX_Type()
)
callActiveCallsVideoPacketLossRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoPacketLossRX.setStatus("current")
_CallActiveCallsVideoPacketLossTX_Type = Unsigned32
_CallActiveCallsVideoPacketLossTX_Object = MibTableColumn
callActiveCallsVideoPacketLossTX = _CallActiveCallsVideoPacketLossTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 51),
    _CallActiveCallsVideoPacketLossTX_Type()
)
callActiveCallsVideoPacketLossTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoPacketLossTX.setStatus("current")
_CallActiveCallsVideoProtocolRX_Type = DisplayString
_CallActiveCallsVideoProtocolRX_Object = MibTableColumn
callActiveCallsVideoProtocolRX = _CallActiveCallsVideoProtocolRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 52),
    _CallActiveCallsVideoProtocolRX_Type()
)
callActiveCallsVideoProtocolRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoProtocolRX.setStatus("current")
_CallActiveCallsVideoProtocolTX_Type = DisplayString
_CallActiveCallsVideoProtocolTX_Object = MibTableColumn
callActiveCallsVideoProtocolTX = _CallActiveCallsVideoProtocolTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 53),
    _CallActiveCallsVideoProtocolTX_Type()
)
callActiveCallsVideoProtocolTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoProtocolTX.setStatus("current")
_CallActiveCallsVideoRateRX_Type = Unsigned32
_CallActiveCallsVideoRateRX_Object = MibTableColumn
callActiveCallsVideoRateRX = _CallActiveCallsVideoRateRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 54),
    _CallActiveCallsVideoRateRX_Type()
)
callActiveCallsVideoRateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoRateRX.setStatus("current")
_CallActiveCallsVideoRateTX_Type = Unsigned32
_CallActiveCallsVideoRateTX_Object = MibTableColumn
callActiveCallsVideoRateTX = _CallActiveCallsVideoRateTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 55),
    _CallActiveCallsVideoRateTX_Type()
)
callActiveCallsVideoRateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoRateTX.setStatus("current")
_CallActiveCallsVideoRateUsedRX_Type = Unsigned32
_CallActiveCallsVideoRateUsedRX_Object = MibTableColumn
callActiveCallsVideoRateUsedRX = _CallActiveCallsVideoRateUsedRX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 56),
    _CallActiveCallsVideoRateUsedRX_Type()
)
callActiveCallsVideoRateUsedRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoRateUsedRX.setStatus("current")
_CallActiveCallsVideoRateUsedTX_Type = Unsigned32
_CallActiveCallsVideoRateUsedTX_Object = MibTableColumn
callActiveCallsVideoRateUsedTX = _CallActiveCallsVideoRateUsedTX_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 57),
    _CallActiveCallsVideoRateUsedTX_Type()
)
callActiveCallsVideoRateUsedTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsVideoRateUsedTX.setStatus("current")
_CallActiveCallsFarSiteName_Type = DisplayString
_CallActiveCallsFarSiteName_Object = MibTableColumn
callActiveCallsFarSiteName = _CallActiveCallsFarSiteName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 58),
    _CallActiveCallsFarSiteName_Type()
)
callActiveCallsFarSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsFarSiteName.setStatus("current")
_CallActiveCallsFarSiteSystemType_Type = DisplayString
_CallActiveCallsFarSiteSystemType_Object = MibTableColumn
callActiveCallsFarSiteSystemType = _CallActiveCallsFarSiteSystemType_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 59),
    _CallActiveCallsFarSiteSystemType_Type()
)
callActiveCallsFarSiteSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsFarSiteSystemType.setStatus("current")
_CallActiveCallsCallType_Type = DisplayString
_CallActiveCallsCallType_Object = MibTableColumn
callActiveCallsCallType = _CallActiveCallsCallType_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 60),
    _CallActiveCallsCallType_Type()
)
callActiveCallsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsCallType.setStatus("current")
_CallActiveCallsEncryption_Type = DisplayString
_CallActiveCallsEncryption_Object = MibTableColumn
callActiveCallsEncryption = _CallActiveCallsEncryption_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 61),
    _CallActiveCallsEncryption_Type()
)
callActiveCallsEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsEncryption.setStatus("current")
_CallActiveCallsPrecedenceLevel_Type = DisplayString
_CallActiveCallsPrecedenceLevel_Object = MibTableColumn
callActiveCallsPrecedenceLevel = _CallActiveCallsPrecedenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 62),
    _CallActiveCallsPrecedenceLevel_Type()
)
callActiveCallsPrecedenceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsPrecedenceLevel.setStatus("current")
_CallActiveCallsSendingContent_Type = TruthValue
_CallActiveCallsSendingContent_Object = MibTableColumn
callActiveCallsSendingContent = _CallActiveCallsSendingContent_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 4, 1, 1, 63),
    _CallActiveCallsSendingContent_Type()
)
callActiveCallsSendingContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallsSendingContent.setStatus("current")
_Conference_ObjectIdentity = ObjectIdentity
conference = _Conference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 5)
)
_ConferenceNumberActiveConferences_Type = Unsigned32
_ConferenceNumberActiveConferences_Object = MibScalar
conferenceNumberActiveConferences = _ConferenceNumberActiveConferences_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 5, 1),
    _ConferenceNumberActiveConferences_Type()
)
conferenceNumberActiveConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conferenceNumberActiveConferences.setStatus("current")
_ExternalIntegration_ObjectIdentity = ObjectIdentity
externalIntegration = _ExternalIntegration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6)
)


class _ExternalIntegrationStatus_Type(Integer32):
    """Custom type externalIntegrationStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationStatus_Type.__name__ = "Integer32"
_ExternalIntegrationStatus_Object = MibScalar
externalIntegrationStatus = _ExternalIntegrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 1),
    _ExternalIntegrationStatus_Type()
)
externalIntegrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationStatus.setStatus("current")
_ExternalIntegrationPresence_ObjectIdentity = ObjectIdentity
externalIntegrationPresence = _ExternalIntegrationPresence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 7)
)


class _ExternalIntegrationPresenceStatus_Type(Integer32):
    """Custom type externalIntegrationPresenceStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationPresenceStatus_Type.__name__ = "Integer32"
_ExternalIntegrationPresenceStatus_Object = MibScalar
externalIntegrationPresenceStatus = _ExternalIntegrationPresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 7, 1),
    _ExternalIntegrationPresenceStatus_Type()
)
externalIntegrationPresenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationPresenceStatus.setStatus("current")
_ExternalIntegrationCDR_ObjectIdentity = ObjectIdentity
externalIntegrationCDR = _ExternalIntegrationCDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 8)
)


class _ExternalIntegrationCDRStatus_Type(Integer32):
    """Custom type externalIntegrationCDRStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationCDRStatus_Type.__name__ = "Integer32"
_ExternalIntegrationCDRStatus_Object = MibScalar
externalIntegrationCDRStatus = _ExternalIntegrationCDRStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 8, 1),
    _ExternalIntegrationCDRStatus_Type()
)
externalIntegrationCDRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationCDRStatus.setStatus("current")
_ExternalIntegrationSyslog_ObjectIdentity = ObjectIdentity
externalIntegrationSyslog = _ExternalIntegrationSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 9)
)


class _ExternalIntegrationSyslogStatus_Type(Integer32):
    """Custom type externalIntegrationSyslogStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationSyslogStatus_Type.__name__ = "Integer32"
_ExternalIntegrationSyslogStatus_Object = MibScalar
externalIntegrationSyslogStatus = _ExternalIntegrationSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 9, 1),
    _ExternalIntegrationSyslogStatus_Type()
)
externalIntegrationSyslogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationSyslogStatus.setStatus("current")
_ExternalIntegrationSoftwareUpdate_ObjectIdentity = ObjectIdentity
externalIntegrationSoftwareUpdate = _ExternalIntegrationSoftwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 10)
)


class _ExternalIntegrationSoftwareUpdateStatus_Type(Integer32):
    """Custom type externalIntegrationSoftwareUpdateStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationSoftwareUpdateStatus_Type.__name__ = "Integer32"
_ExternalIntegrationSoftwareUpdateStatus_Object = MibScalar
externalIntegrationSoftwareUpdateStatus = _ExternalIntegrationSoftwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 10, 1),
    _ExternalIntegrationSoftwareUpdateStatus_Type()
)
externalIntegrationSoftwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationSoftwareUpdateStatus.setStatus("current")
_ExternalIntegrationProvisioning_ObjectIdentity = ObjectIdentity
externalIntegrationProvisioning = _ExternalIntegrationProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 11)
)


class _ExternalIntegrationProvisioningStatus_Type(Integer32):
    """Custom type externalIntegrationProvisioningStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationProvisioningStatus_Type.__name__ = "Integer32"
_ExternalIntegrationProvisioningStatus_Object = MibScalar
externalIntegrationProvisioningStatus = _ExternalIntegrationProvisioningStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 11, 1),
    _ExternalIntegrationProvisioningStatus_Type()
)
externalIntegrationProvisioningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationProvisioningStatus.setStatus("current")
_ExternalIntegrationExchange_ObjectIdentity = ObjectIdentity
externalIntegrationExchange = _ExternalIntegrationExchange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12)
)


class _ExternalIntegrationExchangeStatus_Type(Integer32):
    """Custom type externalIntegrationExchangeStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationExchangeStatus_Type.__name__ = "Integer32"
_ExternalIntegrationExchangeStatus_Object = MibScalar
externalIntegrationExchangeStatus = _ExternalIntegrationExchangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 1),
    _ExternalIntegrationExchangeStatus_Type()
)
externalIntegrationExchangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationExchangeStatus.setStatus("current")
_ExternalIntegrationExchangeServerTable_Object = MibTable
externalIntegrationExchangeServerTable = _ExternalIntegrationExchangeServerTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 2)
)
if mibBuilder.loadTexts:
    externalIntegrationExchangeServerTable.setStatus("current")
_ExternalIntegrationExchangeServerEntry_Object = MibTableRow
externalIntegrationExchangeServerEntry = _ExternalIntegrationExchangeServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 2, 1)
)
externalIntegrationExchangeServerEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "externalIntegrationExchangeServerIndex"),
)
if mibBuilder.loadTexts:
    externalIntegrationExchangeServerEntry.setStatus("current")
_ExternalIntegrationExchangeServerIndex_Type = Unsigned32
_ExternalIntegrationExchangeServerIndex_Object = MibTableColumn
externalIntegrationExchangeServerIndex = _ExternalIntegrationExchangeServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 2, 1, 1),
    _ExternalIntegrationExchangeServerIndex_Type()
)
externalIntegrationExchangeServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationExchangeServerIndex.setStatus("current")
_ExternalIntegrationExchangeServerName_Type = DisplayString
_ExternalIntegrationExchangeServerName_Object = MibTableColumn
externalIntegrationExchangeServerName = _ExternalIntegrationExchangeServerName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 2, 1, 2),
    _ExternalIntegrationExchangeServerName_Type()
)
externalIntegrationExchangeServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationExchangeServerName.setStatus("current")
_ExternalIntegrationExchangeServerIpAddress_Type = InetAddress
_ExternalIntegrationExchangeServerIpAddress_Object = MibTableColumn
externalIntegrationExchangeServerIpAddress = _ExternalIntegrationExchangeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 2, 1, 3),
    _ExternalIntegrationExchangeServerIpAddress_Type()
)
externalIntegrationExchangeServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationExchangeServerIpAddress.setStatus("current")


class _ExternalIntegrationExchangeServerSubscriptionStatus_Type(Integer32):
    """Custom type externalIntegrationExchangeServerSubscriptionStatus based on Integer32"""
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
        *(("unknown", 1),
          ("unavailable", 2),
          ("error", 3),
          ("disabled", 4),
          ("ignoredNoEnterpriseDirectory", 5),
          ("ignoredMailboxNotFound", 6),
          ("authFailed", 7),
          ("subscriptionPending", 8),
          ("subscriptionOK", 9))
    )


_ExternalIntegrationExchangeServerSubscriptionStatus_Type.__name__ = "Integer32"
_ExternalIntegrationExchangeServerSubscriptionStatus_Object = MibTableColumn
externalIntegrationExchangeServerSubscriptionStatus = _ExternalIntegrationExchangeServerSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 2, 1, 4),
    _ExternalIntegrationExchangeServerSubscriptionStatus_Type()
)
externalIntegrationExchangeServerSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationExchangeServerSubscriptionStatus.setStatus("current")
_ExternalIntegrationExchangeServerMeetingsScheduledToday_Type = Unsigned32
_ExternalIntegrationExchangeServerMeetingsScheduledToday_Object = MibTableColumn
externalIntegrationExchangeServerMeetingsScheduledToday = _ExternalIntegrationExchangeServerMeetingsScheduledToday_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 2, 1, 5),
    _ExternalIntegrationExchangeServerMeetingsScheduledToday_Type()
)
externalIntegrationExchangeServerMeetingsScheduledToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationExchangeServerMeetingsScheduledToday.setStatus("current")
_ExternalIntegrationExchangeServerIntegrator_Type = DisplayString
_ExternalIntegrationExchangeServerIntegrator_Object = MibTableColumn
externalIntegrationExchangeServerIntegrator = _ExternalIntegrationExchangeServerIntegrator_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 12, 2, 1, 6),
    _ExternalIntegrationExchangeServerIntegrator_Type()
)
externalIntegrationExchangeServerIntegrator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationExchangeServerIntegrator.setStatus("current")
_ExternalIntegrationDirectorySvcs_ObjectIdentity = ObjectIdentity
externalIntegrationDirectorySvcs = _ExternalIntegrationDirectorySvcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13)
)


class _ExternalIntegrationDirectorySvcsStatus_Type(Integer32):
    """Custom type externalIntegrationDirectorySvcsStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationDirectorySvcsStatus_Type.__name__ = "Integer32"
_ExternalIntegrationDirectorySvcsStatus_Object = MibScalar
externalIntegrationDirectorySvcsStatus = _ExternalIntegrationDirectorySvcsStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 1),
    _ExternalIntegrationDirectorySvcsStatus_Type()
)
externalIntegrationDirectorySvcsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsStatus.setStatus("current")
_ExternalIntegrationDirectorySvcsServerTable_Object = MibTable
externalIntegrationDirectorySvcsServerTable = _ExternalIntegrationDirectorySvcsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3)
)
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerTable.setStatus("current")
_ExternalIntegrationDirectorySvcsServerEntry_Object = MibTableRow
externalIntegrationDirectorySvcsServerEntry = _ExternalIntegrationDirectorySvcsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1)
)
externalIntegrationDirectorySvcsServerEntry.setIndexNames(
    (0, "POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerIndex"),
)
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerEntry.setStatus("current")
_ExternalIntegrationDirectorySvcsServerIndex_Type = Unsigned32
_ExternalIntegrationDirectorySvcsServerIndex_Object = MibTableColumn
externalIntegrationDirectorySvcsServerIndex = _ExternalIntegrationDirectorySvcsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1, 1),
    _ExternalIntegrationDirectorySvcsServerIndex_Type()
)
externalIntegrationDirectorySvcsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerIndex.setStatus("current")


class _ExternalIntegrationDirectorySvcsServerStatus_Type(Integer32):
    """Custom type externalIntegrationDirectorySvcsServerStatus based on Integer32"""
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
          ("ok", 2),
          ("failed", 3))
    )


_ExternalIntegrationDirectorySvcsServerStatus_Type.__name__ = "Integer32"
_ExternalIntegrationDirectorySvcsServerStatus_Object = MibTableColumn
externalIntegrationDirectorySvcsServerStatus = _ExternalIntegrationDirectorySvcsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1, 2),
    _ExternalIntegrationDirectorySvcsServerStatus_Type()
)
externalIntegrationDirectorySvcsServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerStatus.setStatus("current")
_ExternalIntegrationDirectorySvcsServerId_Type = DisplayString
_ExternalIntegrationDirectorySvcsServerId_Object = MibTableColumn
externalIntegrationDirectorySvcsServerId = _ExternalIntegrationDirectorySvcsServerId_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1, 3),
    _ExternalIntegrationDirectorySvcsServerId_Type()
)
externalIntegrationDirectorySvcsServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerId.setStatus("current")


class _ExternalIntegrationDirectorySvcsServerCacheStatus_Type(Integer32):
    """Custom type externalIntegrationDirectorySvcsServerCacheStatus based on Integer32"""
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
        *(("disabled", 1),
          ("connecting", 2),
          ("integratedWithEncryption", 3),
          ("integratedWithoutEncryption", 4),
          ("failed", 5),
          ("outdated", 6),
          ("failedNoSuchEnterpriseUser", 7),
          ("failedEnterpriseAuthentication", 8),
          ("failedInvalidEnterpriseCredentials", 9),
          ("failedEnterpriseAuthenticationWithCode", 10),
          ("failedConnection", 11))
    )


_ExternalIntegrationDirectorySvcsServerCacheStatus_Type.__name__ = "Integer32"
_ExternalIntegrationDirectorySvcsServerCacheStatus_Object = MibTableColumn
externalIntegrationDirectorySvcsServerCacheStatus = _ExternalIntegrationDirectorySvcsServerCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1, 4),
    _ExternalIntegrationDirectorySvcsServerCacheStatus_Type()
)
externalIntegrationDirectorySvcsServerCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerCacheStatus.setStatus("current")
_ExternalIntegrationDirectorySvcsServerConnectionSecure_Type = TruthValue
_ExternalIntegrationDirectorySvcsServerConnectionSecure_Object = MibTableColumn
externalIntegrationDirectorySvcsServerConnectionSecure = _ExternalIntegrationDirectorySvcsServerConnectionSecure_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1, 5),
    _ExternalIntegrationDirectorySvcsServerConnectionSecure_Type()
)
externalIntegrationDirectorySvcsServerConnectionSecure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerConnectionSecure.setStatus("current")
_ExternalIntegrationDirectorySvcsServerCacheRefreshDate_Type = DateAndTime
_ExternalIntegrationDirectorySvcsServerCacheRefreshDate_Object = MibTableColumn
externalIntegrationDirectorySvcsServerCacheRefreshDate = _ExternalIntegrationDirectorySvcsServerCacheRefreshDate_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1, 6),
    _ExternalIntegrationDirectorySvcsServerCacheRefreshDate_Type()
)
externalIntegrationDirectorySvcsServerCacheRefreshDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerCacheRefreshDate.setStatus("current")
_ExternalIntegrationDirectorySvcsServerEnterpriseConferenceRooms_Type = Unsigned32
_ExternalIntegrationDirectorySvcsServerEnterpriseConferenceRooms_Object = MibTableColumn
externalIntegrationDirectorySvcsServerEnterpriseConferenceRooms = _ExternalIntegrationDirectorySvcsServerEnterpriseConferenceRooms_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1, 7),
    _ExternalIntegrationDirectorySvcsServerEnterpriseConferenceRooms_Type()
)
externalIntegrationDirectorySvcsServerEnterpriseConferenceRooms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerEnterpriseConferenceRooms.setStatus("current")
_ExternalIntegrationDirectorySvcsServerIntegrator_Type = DisplayString
_ExternalIntegrationDirectorySvcsServerIntegrator_Object = MibTableColumn
externalIntegrationDirectorySvcsServerIntegrator = _ExternalIntegrationDirectorySvcsServerIntegrator_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 13, 3, 1, 8),
    _ExternalIntegrationDirectorySvcsServerIntegrator_Type()
)
externalIntegrationDirectorySvcsServerIntegrator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIntegrationDirectorySvcsServerIntegrator.setStatus("current")
_ExternalIntegrationNTP_ObjectIdentity = ObjectIdentity
externalIntegrationNTP = _ExternalIntegrationNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 6, 15)
)
_NotificationVariable_ObjectIdentity = ObjectIdentity
notificationVariable = _NotificationVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99)
)
_NotificationVariableNodeName_Type = DisplayString
_NotificationVariableNodeName_Object = MibScalar
notificationVariableNodeName = _NotificationVariableNodeName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 1),
    _NotificationVariableNodeName_Type()
)
notificationVariableNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableNodeName.setStatus("current")
_NotificationVariableReportingNodeName_Type = DisplayString
_NotificationVariableReportingNodeName_Object = MibScalar
notificationVariableReportingNodeName = _NotificationVariableReportingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 2),
    _NotificationVariableReportingNodeName_Type()
)
notificationVariableReportingNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableReportingNodeName.setStatus("current")


class _NotificationVariableType_Type(Integer32):
    """Custom type notificationVariableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("problem", 1),
          ("resolution", 2),
          ("info", 3))
    )


_NotificationVariableType_Type.__name__ = "Integer32"
_NotificationVariableType_Object = MibScalar
notificationVariableType = _NotificationVariableType_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 3),
    _NotificationVariableType_Type()
)
notificationVariableType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableType.setStatus("current")
_NotificationVariableClass_Type = DisplayString
_NotificationVariableClass_Object = MibScalar
notificationVariableClass = _NotificationVariableClass_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 4),
    _NotificationVariableClass_Type()
)
notificationVariableClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableClass.setStatus("current")
_NotificationVariableKey_Type = DisplayString
_NotificationVariableKey_Object = MibScalar
notificationVariableKey = _NotificationVariableKey_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 5),
    _NotificationVariableKey_Type()
)
notificationVariableKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableKey.setStatus("current")
_NotificationVariableSummary_Type = DisplayString
_NotificationVariableSummary_Object = MibScalar
notificationVariableSummary = _NotificationVariableSummary_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 6),
    _NotificationVariableSummary_Type()
)
notificationVariableSummary.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableSummary.setStatus("current")


class _NotificationVariableSeverity_Type(Integer32):
    """Custom type notificationVariableSeverity based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )


_NotificationVariableSeverity_Type.__name__ = "Integer32"
_NotificationVariableSeverity_Object = MibScalar
notificationVariableSeverity = _NotificationVariableSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 7),
    _NotificationVariableSeverity_Type()
)
notificationVariableSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableSeverity.setStatus("current")
_NotificationVariableValueOID_Type = ObjectIdentifier
_NotificationVariableValueOID_Object = MibScalar
notificationVariableValueOID = _NotificationVariableValueOID_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 8),
    _NotificationVariableValueOID_Type()
)
notificationVariableValueOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableValueOID.setStatus("current")
_NotificationVariableThreshold_Type = Integer32
_NotificationVariableThreshold_Object = MibScalar
notificationVariableThreshold = _NotificationVariableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 9),
    _NotificationVariableThreshold_Type()
)
notificationVariableThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableThreshold.setStatus("current")
_NotificationVariableConferenceID_Type = OctetString
_NotificationVariableConferenceID_Object = MibScalar
notificationVariableConferenceID = _NotificationVariableConferenceID_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 10),
    _NotificationVariableConferenceID_Type()
)
notificationVariableConferenceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableConferenceID.setStatus("current")
_NotificationVariableServerName_Type = OctetString
_NotificationVariableServerName_Object = MibScalar
notificationVariableServerName = _NotificationVariableServerName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 101, 1, 99, 11),
    _NotificationVariableServerName_Type()
)
notificationVariableServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationVariableServerName.setStatus("current")
_Polycom_endpointMIBConformance_ObjectIdentity = ObjectIdentity
polycom_endpointMIBConformance = _Polycom_endpointMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2)
)
_Polycom_endpointMIBGroups_ObjectIdentity = ObjectIdentity
polycom_endpointMIBGroups = _Polycom_endpointMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2)
)

# Managed Objects groups

identityObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2, 1)
)
identityObjects.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "identitySoftwareInfo"),
        ("POLYCOM-ENDPOINT-MIB", "identityBuildDate"),
        ("POLYCOM-ENDPOINT-MIB", "identityDeviceType"),
        ("POLYCOM-ENDPOINT-MIB", "identityDeviceModel"),
        ("POLYCOM-ENDPOINT-MIB", "identityDeviceSerialNumber"),
        ("POLYCOM-ENDPOINT-MIB", "identityStatus"),
        ("POLYCOM-ENDPOINT-MIB", "identityDebugMode"),
        ("POLYCOM-ENDPOINT-MIB", "identityConsoleAccess"),
        ("POLYCOM-ENDPOINT-MIB", "identityMIBVersionSupported"),
        ("POLYCOM-ENDPOINT-MIB", "identityLastDataUpdateTime"))
)
if mibBuilder.loadTexts:
    identityObjects.setStatus("current")

serviceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2, 2)
)
serviceObjects.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "serviceH323Status"),
        ("POLYCOM-ENDPOINT-MIB", "serviceH323RegistrationStatus"),
        ("POLYCOM-ENDPOINT-MIB", "serviceH323GatekeeperIndex"),
        ("POLYCOM-ENDPOINT-MIB", "serviceH323GatekeeperStatus"),
        ("POLYCOM-ENDPOINT-MIB", "serviceH323GatekeeperH239Enabled"),
        ("POLYCOM-ENDPOINT-MIB", "serviceSipStatus"),
        ("POLYCOM-ENDPOINT-MIB", "serviceSipProxyIndex"),
        ("POLYCOM-ENDPOINT-MIB", "serviceSipProxyStatus"),
        ("POLYCOM-ENDPOINT-MIB", "serviceSipRegistrationIndex"),
        ("POLYCOM-ENDPOINT-MIB", "serviceSipRegistrationStatus"),
        ("POLYCOM-ENDPOINT-MIB", "serviceIsdnStatus"),
        ("POLYCOM-ENDPOINT-MIB", "serviceSecurityProfile"))
)
if mibBuilder.loadTexts:
    serviceObjects.setStatus("current")

hardwareObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2, 3)
)
hardwareObjects.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "hardwareOverallStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareMicrophoneStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareMicrophoneMicrophonesIndex"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareMicrophoneMicrophonesName"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareMicrophoneMicrophonesStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareCameraStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareCameraCamerasIndex"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareCameraCamerasName"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareCameraCamerasStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareNICStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareNICNICsIndex"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareNICNICsName"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareNICNICsMAC"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareNICNICsSpeed"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareNICNICsDuplex"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareNICNICsStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareNICNICsIPType"),
        ("POLYCOM-ENDPOINT-MIB", "hardwarePTCStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwarePTCPTCsIndex"),
        ("POLYCOM-ENDPOINT-MIB", "hardwarePTCPTCsStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareUcBoardStatus"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareUcBoardUcBoardsIndex"),
        ("POLYCOM-ENDPOINT-MIB", "hardwareUcBoardUcBoardsStatus"))
)
if mibBuilder.loadTexts:
    hardwareObjects.setStatus("current")

callObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2, 4)
)
callObjects.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "callActiveCallsIndex"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsCallID"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsConfID"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVoiceJitterRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVoiceJitterTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVoiceLatencyRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVoiceLatencyTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVoicePacketLossRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVoicePacketLossTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVoiceProtocolRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVoiceProtocolTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsMaxVoiceJitterRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsMaxVoiceJitterTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsTotalPacketsLostRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsTotalPacketsLostTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsPctPacketLostRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsPctPacketLostTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsOverallLatencyRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsOverallLatencyTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsOverallJitterRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsOverallJitterTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentFormatRsltnRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentFormatRsltnTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentFrameRateRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentFrameRateTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentJitterRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentJitterTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentLatencyRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentLatencyTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentPacketLossRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentPacketLossTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentProtocolRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentProtocolTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentRateRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentRateTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentRateUsedRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsContentRateUsedTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoAnnexRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoAnnexTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoFECErrorsRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoFECErrorsTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoRsltnRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoRsltnTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoFrameRateRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoFrameRateTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoJitterRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoJitterTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoLatencyRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoLatencyTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoPacketLossRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoPacketLossTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoProtocolRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoProtocolTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoRateRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoRateTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoRateUsedRX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsVideoRateUsedTX"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsFarSiteName"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsFarSiteSystemType"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsCallType"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsEncryption"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsPrecedenceLevel"),
        ("POLYCOM-ENDPOINT-MIB", "callActiveCallsSendingContent"))
)
if mibBuilder.loadTexts:
    callObjects.setStatus("current")

conferenceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2, 5)
)
conferenceObjects.setObjects(
    ("POLYCOM-ENDPOINT-MIB", "conferenceNumberActiveConferences")
)
if mibBuilder.loadTexts:
    conferenceObjects.setStatus("current")

externalIntegrationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2, 6)
)
externalIntegrationObjects.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "externalIntegrationStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationPresenceStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationCDRStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationSyslogStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationSoftwareUpdateStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationProvisioningStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationExchangeStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationExchangeServerIndex"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationExchangeServerName"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationExchangeServerIpAddress"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationExchangeServerSubscriptionStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationExchangeServerMeetingsScheduledToday"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationExchangeServerIntegrator"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerIndex"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerId"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerCacheStatus"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerConnectionSecure"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerCacheRefreshDate"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerEnterpriseConferenceRooms"),
        ("POLYCOM-ENDPOINT-MIB", "externalIntegrationDirectorySvcsServerIntegrator"))
)
if mibBuilder.loadTexts:
    externalIntegrationObjects.setStatus("current")

notificationVariableObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2, 7)
)
notificationVariableObjects.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableThreshold"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableServerName"))
)
if mibBuilder.loadTexts:
    notificationVariableObjects.setStatus("current")


# Notification objects

securityFailedAuthAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 17)
)
securityFailedAuthAttempt.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableServerName"))
)
if mibBuilder.loadTexts:
    securityFailedAuthAttempt.setStatus(
        "current"
    )

securitySuccessfulAuthAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 19)
)
securitySuccessfulAuthAttempt.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableServerName"))
)
if mibBuilder.loadTexts:
    securitySuccessfulAuthAttempt.setStatus(
        "current"
    )

securityPortLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 21)
)
securityPortLocked.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    securityPortLocked.setStatus(
        "current"
    )

securityPortUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 22)
)
securityPortUnlocked.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    securityPortUnlocked.setStatus(
        "current"
    )

securityAccountLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 23)
)
securityAccountLocked.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    securityAccountLocked.setStatus(
        "current"
    )

securityAccountUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 24)
)
securityAccountUnlocked.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    securityAccountUnlocked.setStatus(
        "current"
    )

securityConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 25)
)
securityConfigChange.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    securityConfigChange.setStatus(
        "current"
    )

softwareUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 67)
)
softwareUpdateStarted.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    softwareUpdateStarted.setStatus(
        "current"
    )

softwareUpdateComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 68)
)
softwareUpdateComplete.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    softwareUpdateComplete.setStatus(
        "current"
    )

softwareUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 69)
)
softwareUpdateFailed.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    softwareUpdateFailed.setStatus(
        "current"
    )

h323GateKeeperRegistrationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 70)
)
h323GateKeeperRegistrationFailed.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    h323GateKeeperRegistrationFailed.setStatus(
        "current"
    )

h323GateKeeperRegistrationOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 71)
)
h323GateKeeperRegistrationOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    h323GateKeeperRegistrationOK.setStatus(
        "current"
    )

sipRegistrationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 72)
)
sipRegistrationFailed.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    sipRegistrationFailed.setStatus(
        "current"
    )

sipRegistrationOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 73)
)
sipRegistrationOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    sipRegistrationOK.setStatus(
        "current"
    )

isdnLineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 74)
)
isdnLineDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    isdnLineDown.setStatus(
        "current"
    )

isdnLineUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 75)
)
isdnLineUp.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    isdnLineUp.setStatus(
        "current"
    )

primaryCameraDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 76)
)
primaryCameraDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    primaryCameraDown.setStatus(
        "current"
    )

primaryCameraOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 77)
)
primaryCameraOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    primaryCameraOK.setStatus(
        "current"
    )

callConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 78)
)
callConnected.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    callConnected.setStatus(
        "current"
    )

callDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 79)
)
callDisconnected.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    callDisconnected.setStatus(
        "current"
    )

callFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 80)
)
callFailed.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    callFailed.setStatus(
        "current"
    )

jitterExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 81)
)
jitterExcessive.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableThreshold"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    jitterExcessive.setStatus(
        "current"
    )

jitterOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 82)
)
jitterOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableThreshold"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    jitterOK.setStatus(
        "current"
    )

latencyExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 83)
)
latencyExcessive.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableThreshold"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    latencyExcessive.setStatus(
        "current"
    )

latencyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 84)
)
latencyOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableThreshold"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    latencyOK.setStatus(
        "current"
    )

packetLossExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 85)
)
packetLossExcessive.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableThreshold"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    packetLossExcessive.setStatus(
        "current"
    )

packetLossOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 86)
)
packetLossOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableThreshold"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableConferenceID"))
)
if mibBuilder.loadTexts:
    packetLossOK.setStatus(
        "current"
    )

presenceServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 87)
)
presenceServerDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableServerName"))
)
if mibBuilder.loadTexts:
    presenceServerDown.setStatus(
        "current"
    )

presenceServerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 88)
)
presenceServerOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableServerName"))
)
if mibBuilder.loadTexts:
    presenceServerOK.setStatus(
        "current"
    )

cdrServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 89)
)
cdrServerDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    cdrServerDown.setStatus(
        "current"
    )

cdrServerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 90)
)
cdrServerOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    cdrServerOK.setStatus(
        "current"
    )

syslogServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 91)
)
syslogServerDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    syslogServerDown.setStatus(
        "current"
    )

syslogServerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 92)
)
syslogServerOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    syslogServerOK.setStatus(
        "current"
    )

softwareUpdateServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 93)
)
softwareUpdateServerDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    softwareUpdateServerDown.setStatus(
        "current"
    )

softwareUpdateServerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 94)
)
softwareUpdateServerOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    softwareUpdateServerOK.setStatus(
        "current"
    )

provisioningServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 95)
)
provisioningServerDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    provisioningServerDown.setStatus(
        "current"
    )

provisioningServerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 96)
)
provisioningServerOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    provisioningServerOK.setStatus(
        "current"
    )

calendarServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 97)
)
calendarServerDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    calendarServerDown.setStatus(
        "current"
    )

calendarServerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 98)
)
calendarServerOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    calendarServerOK.setStatus(
        "current"
    )

directoryServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 99)
)
directoryServerDown.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    directoryServerDown.setStatus(
        "current"
    )

directoryServerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 100)
)
directoryServerOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableValueOID"))
)
if mibBuilder.loadTexts:
    directoryServerOK.setStatus(
        "current"
    )

remoteControlBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 101)
)
remoteControlBatteryLow.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    remoteControlBatteryLow.setStatus(
        "current"
    )

remoteControlBatteryOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 101, 0, 102)
)
remoteControlBatteryOK.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "notificationVariableReportingNodeName"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableType"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableClass"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableKey"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSummary"),
        ("POLYCOM-ENDPOINT-MIB", "notificationVariableSeverity"))
)
if mibBuilder.loadTexts:
    remoteControlBatteryOK.setStatus(
        "current"
    )


# Notifications groups

notificationObjects = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13885, 101, 2, 2, 99)
)
notificationObjects.setObjects(
      *(("POLYCOM-ENDPOINT-MIB", "securityFailedAuthAttempt"),
        ("POLYCOM-ENDPOINT-MIB", "securitySuccessfulAuthAttempt"),
        ("POLYCOM-ENDPOINT-MIB", "securityAccountLocked"),
        ("POLYCOM-ENDPOINT-MIB", "securityAccountUnlocked"),
        ("POLYCOM-ENDPOINT-MIB", "securityConfigChange"),
        ("POLYCOM-ENDPOINT-MIB", "softwareUpdateStarted"),
        ("POLYCOM-ENDPOINT-MIB", "softwareUpdateComplete"),
        ("POLYCOM-ENDPOINT-MIB", "softwareUpdateFailed"),
        ("POLYCOM-ENDPOINT-MIB", "h323GateKeeperRegistrationFailed"),
        ("POLYCOM-ENDPOINT-MIB", "h323GateKeeperRegistrationOK"),
        ("POLYCOM-ENDPOINT-MIB", "sipRegistrationFailed"),
        ("POLYCOM-ENDPOINT-MIB", "sipRegistrationOK"),
        ("POLYCOM-ENDPOINT-MIB", "isdnLineDown"),
        ("POLYCOM-ENDPOINT-MIB", "isdnLineUp"),
        ("POLYCOM-ENDPOINT-MIB", "primaryCameraDown"),
        ("POLYCOM-ENDPOINT-MIB", "primaryCameraOK"),
        ("POLYCOM-ENDPOINT-MIB", "callConnected"),
        ("POLYCOM-ENDPOINT-MIB", "callDisconnected"),
        ("POLYCOM-ENDPOINT-MIB", "callFailed"),
        ("POLYCOM-ENDPOINT-MIB", "jitterExcessive"),
        ("POLYCOM-ENDPOINT-MIB", "jitterOK"),
        ("POLYCOM-ENDPOINT-MIB", "latencyExcessive"),
        ("POLYCOM-ENDPOINT-MIB", "latencyOK"),
        ("POLYCOM-ENDPOINT-MIB", "packetLossExcessive"),
        ("POLYCOM-ENDPOINT-MIB", "packetLossOK"),
        ("POLYCOM-ENDPOINT-MIB", "presenceServerDown"),
        ("POLYCOM-ENDPOINT-MIB", "presenceServerOK"),
        ("POLYCOM-ENDPOINT-MIB", "cdrServerDown"),
        ("POLYCOM-ENDPOINT-MIB", "cdrServerOK"),
        ("POLYCOM-ENDPOINT-MIB", "syslogServerDown"),
        ("POLYCOM-ENDPOINT-MIB", "syslogServerOK"),
        ("POLYCOM-ENDPOINT-MIB", "softwareUpdateServerDown"),
        ("POLYCOM-ENDPOINT-MIB", "softwareUpdateServerOK"),
        ("POLYCOM-ENDPOINT-MIB", "provisioningServerDown"),
        ("POLYCOM-ENDPOINT-MIB", "provisioningServerOK"),
        ("POLYCOM-ENDPOINT-MIB", "calendarServerDown"),
        ("POLYCOM-ENDPOINT-MIB", "calendarServerOK"),
        ("POLYCOM-ENDPOINT-MIB", "directoryServerDown"),
        ("POLYCOM-ENDPOINT-MIB", "directoryServerOK"),
        ("POLYCOM-ENDPOINT-MIB", "remoteControlBatteryLow"),
        ("POLYCOM-ENDPOINT-MIB", "remoteControlBatteryOK"))
)
if mibBuilder.loadTexts:
    notificationObjects.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLYCOM-ENDPOINT-MIB",
    **{"polycom-endpoint-MIB": polycom_endpoint_MIB,
       "polycom-endpointNotifications": polycom_endpointNotifications,
       "securityFailedAuthAttempt": securityFailedAuthAttempt,
       "securitySuccessfulAuthAttempt": securitySuccessfulAuthAttempt,
       "securityPortLocked": securityPortLocked,
       "securityPortUnlocked": securityPortUnlocked,
       "securityAccountLocked": securityAccountLocked,
       "securityAccountUnlocked": securityAccountUnlocked,
       "securityConfigChange": securityConfigChange,
       "softwareUpdateStarted": softwareUpdateStarted,
       "softwareUpdateComplete": softwareUpdateComplete,
       "softwareUpdateFailed": softwareUpdateFailed,
       "h323GateKeeperRegistrationFailed": h323GateKeeperRegistrationFailed,
       "h323GateKeeperRegistrationOK": h323GateKeeperRegistrationOK,
       "sipRegistrationFailed": sipRegistrationFailed,
       "sipRegistrationOK": sipRegistrationOK,
       "isdnLineDown": isdnLineDown,
       "isdnLineUp": isdnLineUp,
       "primaryCameraDown": primaryCameraDown,
       "primaryCameraOK": primaryCameraOK,
       "callConnected": callConnected,
       "callDisconnected": callDisconnected,
       "callFailed": callFailed,
       "jitterExcessive": jitterExcessive,
       "jitterOK": jitterOK,
       "latencyExcessive": latencyExcessive,
       "latencyOK": latencyOK,
       "packetLossExcessive": packetLossExcessive,
       "packetLossOK": packetLossOK,
       "presenceServerDown": presenceServerDown,
       "presenceServerOK": presenceServerOK,
       "cdrServerDown": cdrServerDown,
       "cdrServerOK": cdrServerOK,
       "syslogServerDown": syslogServerDown,
       "syslogServerOK": syslogServerOK,
       "softwareUpdateServerDown": softwareUpdateServerDown,
       "softwareUpdateServerOK": softwareUpdateServerOK,
       "provisioningServerDown": provisioningServerDown,
       "provisioningServerOK": provisioningServerOK,
       "calendarServerDown": calendarServerDown,
       "calendarServerOK": calendarServerOK,
       "directoryServerDown": directoryServerDown,
       "directoryServerOK": directoryServerOK,
       "remoteControlBatteryLow": remoteControlBatteryLow,
       "remoteControlBatteryOK": remoteControlBatteryOK,
       "polycom-endpointObjects": polycom_endpointObjects,
       "identity": identity,
       "identitySoftwareInfo": identitySoftwareInfo,
       "identityBuildDate": identityBuildDate,
       "identityDeviceType": identityDeviceType,
       "identityDeviceModel": identityDeviceModel,
       "identityDeviceSerialNumber": identityDeviceSerialNumber,
       "identityStatus": identityStatus,
       "identityDebugMode": identityDebugMode,
       "identityConsoleAccess": identityConsoleAccess,
       "identityMIBVersionSupported": identityMIBVersionSupported,
       "identityLastDataUpdateTime": identityLastDataUpdateTime,
       "service": service,
       "serviceH323": serviceH323,
       "serviceH323Status": serviceH323Status,
       "serviceH323RegistrationStatus": serviceH323RegistrationStatus,
       "serviceH323GatekeeperTable": serviceH323GatekeeperTable,
       "serviceH323GatekeeperEntry": serviceH323GatekeeperEntry,
       "serviceH323GatekeeperIndex": serviceH323GatekeeperIndex,
       "serviceH323GatekeeperStatus": serviceH323GatekeeperStatus,
       "serviceH323GatekeeperH239Enabled": serviceH323GatekeeperH239Enabled,
       "serviceSip": serviceSip,
       "serviceSipStatus": serviceSipStatus,
       "serviceSipProxyTable": serviceSipProxyTable,
       "serviceSipProxyEntry": serviceSipProxyEntry,
       "serviceSipProxyIndex": serviceSipProxyIndex,
       "serviceSipProxyStatus": serviceSipProxyStatus,
       "serviceSipRegistrationTable": serviceSipRegistrationTable,
       "serviceSipRegistrationEntry": serviceSipRegistrationEntry,
       "serviceSipRegistrationIndex": serviceSipRegistrationIndex,
       "serviceSipRegistrationStatus": serviceSipRegistrationStatus,
       "serviceIsdn": serviceIsdn,
       "serviceIsdnStatus": serviceIsdnStatus,
       "serviceSecurity": serviceSecurity,
       "serviceSecurityProfile": serviceSecurityProfile,
       "hardware": hardware,
       "hardwareOverallStatus": hardwareOverallStatus,
       "hardwareMicrophone": hardwareMicrophone,
       "hardwareMicrophoneStatus": hardwareMicrophoneStatus,
       "hardwareMicrophoneMicrophonesTable": hardwareMicrophoneMicrophonesTable,
       "hardwareMicrophoneMicrophonesEntry": hardwareMicrophoneMicrophonesEntry,
       "hardwareMicrophoneMicrophonesIndex": hardwareMicrophoneMicrophonesIndex,
       "hardwareMicrophoneMicrophonesName": hardwareMicrophoneMicrophonesName,
       "hardwareMicrophoneMicrophonesStatus": hardwareMicrophoneMicrophonesStatus,
       "hardwareCamera": hardwareCamera,
       "hardwareCameraStatus": hardwareCameraStatus,
       "hardwareCameraCamerasTable": hardwareCameraCamerasTable,
       "hardwareCameraCamerasEntry": hardwareCameraCamerasEntry,
       "hardwareCameraCamerasIndex": hardwareCameraCamerasIndex,
       "hardwareCameraCamerasName": hardwareCameraCamerasName,
       "hardwareCameraCamerasStatus": hardwareCameraCamerasStatus,
       "hardwareNIC": hardwareNIC,
       "hardwareNICStatus": hardwareNICStatus,
       "hardwareNICNICsTable": hardwareNICNICsTable,
       "hardwareNICNICsEntry": hardwareNICNICsEntry,
       "hardwareNICNICsIndex": hardwareNICNICsIndex,
       "hardwareNICNICsName": hardwareNICNICsName,
       "hardwareNICNICsMAC": hardwareNICNICsMAC,
       "hardwareNICNICsSpeed": hardwareNICNICsSpeed,
       "hardwareNICNICsDuplex": hardwareNICNICsDuplex,
       "hardwareNICNICsStatus": hardwareNICNICsStatus,
       "hardwareNICNICsIPType": hardwareNICNICsIPType,
       "hardwarePTC": hardwarePTC,
       "hardwarePTCStatus": hardwarePTCStatus,
       "hardwarePTCPTCsTable": hardwarePTCPTCsTable,
       "hardwarePTCPTCsEntry": hardwarePTCPTCsEntry,
       "hardwarePTCPTCsIndex": hardwarePTCPTCsIndex,
       "hardwarePTCPTCsStatus": hardwarePTCPTCsStatus,
       "hardwareUcBoard": hardwareUcBoard,
       "hardwareUcBoardStatus": hardwareUcBoardStatus,
       "hardwareUcBoardUcBoardsTable": hardwareUcBoardUcBoardsTable,
       "hardwareUcBoardUcBoardsEntry": hardwareUcBoardUcBoardsEntry,
       "hardwareUcBoardUcBoardsIndex": hardwareUcBoardUcBoardsIndex,
       "hardwareUcBoardUcBoardsStatus": hardwareUcBoardUcBoardsStatus,
       "call": call,
       "callActiveCallsTable": callActiveCallsTable,
       "callActiveCallsEntry": callActiveCallsEntry,
       "callActiveCallsIndex": callActiveCallsIndex,
       "callActiveCallsCallID": callActiveCallsCallID,
       "callActiveCallsConfID": callActiveCallsConfID,
       "callActiveCallsVoiceJitterRX": callActiveCallsVoiceJitterRX,
       "callActiveCallsVoiceJitterTX": callActiveCallsVoiceJitterTX,
       "callActiveCallsVoiceLatencyRX": callActiveCallsVoiceLatencyRX,
       "callActiveCallsVoiceLatencyTX": callActiveCallsVoiceLatencyTX,
       "callActiveCallsVoicePacketLossRX": callActiveCallsVoicePacketLossRX,
       "callActiveCallsVoicePacketLossTX": callActiveCallsVoicePacketLossTX,
       "callActiveCallsVoiceProtocolRX": callActiveCallsVoiceProtocolRX,
       "callActiveCallsVoiceProtocolTX": callActiveCallsVoiceProtocolTX,
       "callActiveCallsMaxVoiceJitterRX": callActiveCallsMaxVoiceJitterRX,
       "callActiveCallsMaxVoiceJitterTX": callActiveCallsMaxVoiceJitterTX,
       "callActiveCallsTotalPacketsLostRX": callActiveCallsTotalPacketsLostRX,
       "callActiveCallsTotalPacketsLostTX": callActiveCallsTotalPacketsLostTX,
       "callActiveCallsPctPacketLostRX": callActiveCallsPctPacketLostRX,
       "callActiveCallsPctPacketLostTX": callActiveCallsPctPacketLostTX,
       "callActiveCallsOverallLatencyRX": callActiveCallsOverallLatencyRX,
       "callActiveCallsOverallLatencyTX": callActiveCallsOverallLatencyTX,
       "callActiveCallsOverallJitterRX": callActiveCallsOverallJitterRX,
       "callActiveCallsOverallJitterTX": callActiveCallsOverallJitterTX,
       "callActiveCallsContentFormatRsltnRX": callActiveCallsContentFormatRsltnRX,
       "callActiveCallsContentFormatRsltnTX": callActiveCallsContentFormatRsltnTX,
       "callActiveCallsContentFrameRateRX": callActiveCallsContentFrameRateRX,
       "callActiveCallsContentFrameRateTX": callActiveCallsContentFrameRateTX,
       "callActiveCallsContentJitterRX": callActiveCallsContentJitterRX,
       "callActiveCallsContentJitterTX": callActiveCallsContentJitterTX,
       "callActiveCallsContentLatencyRX": callActiveCallsContentLatencyRX,
       "callActiveCallsContentLatencyTX": callActiveCallsContentLatencyTX,
       "callActiveCallsContentPacketLossRX": callActiveCallsContentPacketLossRX,
       "callActiveCallsContentPacketLossTX": callActiveCallsContentPacketLossTX,
       "callActiveCallsContentProtocolRX": callActiveCallsContentProtocolRX,
       "callActiveCallsContentProtocolTX": callActiveCallsContentProtocolTX,
       "callActiveCallsContentRateRX": callActiveCallsContentRateRX,
       "callActiveCallsContentRateTX": callActiveCallsContentRateTX,
       "callActiveCallsContentRateUsedRX": callActiveCallsContentRateUsedRX,
       "callActiveCallsContentRateUsedTX": callActiveCallsContentRateUsedTX,
       "callActiveCallsVideoAnnexRX": callActiveCallsVideoAnnexRX,
       "callActiveCallsVideoAnnexTX": callActiveCallsVideoAnnexTX,
       "callActiveCallsVideoFECErrorsRX": callActiveCallsVideoFECErrorsRX,
       "callActiveCallsVideoFECErrorsTX": callActiveCallsVideoFECErrorsTX,
       "callActiveCallsVideoRsltnRX": callActiveCallsVideoRsltnRX,
       "callActiveCallsVideoRsltnTX": callActiveCallsVideoRsltnTX,
       "callActiveCallsVideoFrameRateRX": callActiveCallsVideoFrameRateRX,
       "callActiveCallsVideoFrameRateTX": callActiveCallsVideoFrameRateTX,
       "callActiveCallsVideoJitterRX": callActiveCallsVideoJitterRX,
       "callActiveCallsVideoJitterTX": callActiveCallsVideoJitterTX,
       "callActiveCallsVideoLatencyRX": callActiveCallsVideoLatencyRX,
       "callActiveCallsVideoLatencyTX": callActiveCallsVideoLatencyTX,
       "callActiveCallsVideoPacketLossRX": callActiveCallsVideoPacketLossRX,
       "callActiveCallsVideoPacketLossTX": callActiveCallsVideoPacketLossTX,
       "callActiveCallsVideoProtocolRX": callActiveCallsVideoProtocolRX,
       "callActiveCallsVideoProtocolTX": callActiveCallsVideoProtocolTX,
       "callActiveCallsVideoRateRX": callActiveCallsVideoRateRX,
       "callActiveCallsVideoRateTX": callActiveCallsVideoRateTX,
       "callActiveCallsVideoRateUsedRX": callActiveCallsVideoRateUsedRX,
       "callActiveCallsVideoRateUsedTX": callActiveCallsVideoRateUsedTX,
       "callActiveCallsFarSiteName": callActiveCallsFarSiteName,
       "callActiveCallsFarSiteSystemType": callActiveCallsFarSiteSystemType,
       "callActiveCallsCallType": callActiveCallsCallType,
       "callActiveCallsEncryption": callActiveCallsEncryption,
       "callActiveCallsPrecedenceLevel": callActiveCallsPrecedenceLevel,
       "callActiveCallsSendingContent": callActiveCallsSendingContent,
       "conference": conference,
       "conferenceNumberActiveConferences": conferenceNumberActiveConferences,
       "externalIntegration": externalIntegration,
       "externalIntegrationStatus": externalIntegrationStatus,
       "externalIntegrationPresence": externalIntegrationPresence,
       "externalIntegrationPresenceStatus": externalIntegrationPresenceStatus,
       "externalIntegrationCDR": externalIntegrationCDR,
       "externalIntegrationCDRStatus": externalIntegrationCDRStatus,
       "externalIntegrationSyslog": externalIntegrationSyslog,
       "externalIntegrationSyslogStatus": externalIntegrationSyslogStatus,
       "externalIntegrationSoftwareUpdate": externalIntegrationSoftwareUpdate,
       "externalIntegrationSoftwareUpdateStatus": externalIntegrationSoftwareUpdateStatus,
       "externalIntegrationProvisioning": externalIntegrationProvisioning,
       "externalIntegrationProvisioningStatus": externalIntegrationProvisioningStatus,
       "externalIntegrationExchange": externalIntegrationExchange,
       "externalIntegrationExchangeStatus": externalIntegrationExchangeStatus,
       "externalIntegrationExchangeServerTable": externalIntegrationExchangeServerTable,
       "externalIntegrationExchangeServerEntry": externalIntegrationExchangeServerEntry,
       "externalIntegrationExchangeServerIndex": externalIntegrationExchangeServerIndex,
       "externalIntegrationExchangeServerName": externalIntegrationExchangeServerName,
       "externalIntegrationExchangeServerIpAddress": externalIntegrationExchangeServerIpAddress,
       "externalIntegrationExchangeServerSubscriptionStatus": externalIntegrationExchangeServerSubscriptionStatus,
       "externalIntegrationExchangeServerMeetingsScheduledToday": externalIntegrationExchangeServerMeetingsScheduledToday,
       "externalIntegrationExchangeServerIntegrator": externalIntegrationExchangeServerIntegrator,
       "externalIntegrationDirectorySvcs": externalIntegrationDirectorySvcs,
       "externalIntegrationDirectorySvcsStatus": externalIntegrationDirectorySvcsStatus,
       "externalIntegrationDirectorySvcsServerTable": externalIntegrationDirectorySvcsServerTable,
       "externalIntegrationDirectorySvcsServerEntry": externalIntegrationDirectorySvcsServerEntry,
       "externalIntegrationDirectorySvcsServerIndex": externalIntegrationDirectorySvcsServerIndex,
       "externalIntegrationDirectorySvcsServerStatus": externalIntegrationDirectorySvcsServerStatus,
       "externalIntegrationDirectorySvcsServerId": externalIntegrationDirectorySvcsServerId,
       "externalIntegrationDirectorySvcsServerCacheStatus": externalIntegrationDirectorySvcsServerCacheStatus,
       "externalIntegrationDirectorySvcsServerConnectionSecure": externalIntegrationDirectorySvcsServerConnectionSecure,
       "externalIntegrationDirectorySvcsServerCacheRefreshDate": externalIntegrationDirectorySvcsServerCacheRefreshDate,
       "externalIntegrationDirectorySvcsServerEnterpriseConferenceRooms": externalIntegrationDirectorySvcsServerEnterpriseConferenceRooms,
       "externalIntegrationDirectorySvcsServerIntegrator": externalIntegrationDirectorySvcsServerIntegrator,
       "externalIntegrationNTP": externalIntegrationNTP,
       "notificationVariable": notificationVariable,
       "notificationVariableNodeName": notificationVariableNodeName,
       "notificationVariableReportingNodeName": notificationVariableReportingNodeName,
       "notificationVariableType": notificationVariableType,
       "notificationVariableClass": notificationVariableClass,
       "notificationVariableKey": notificationVariableKey,
       "notificationVariableSummary": notificationVariableSummary,
       "notificationVariableSeverity": notificationVariableSeverity,
       "notificationVariableValueOID": notificationVariableValueOID,
       "notificationVariableThreshold": notificationVariableThreshold,
       "notificationVariableConferenceID": notificationVariableConferenceID,
       "notificationVariableServerName": notificationVariableServerName,
       "polycom-endpointMIBConformance": polycom_endpointMIBConformance,
       "polycom-endpointMIBGroups": polycom_endpointMIBGroups,
       "identityObjects": identityObjects,
       "serviceObjects": serviceObjects,
       "hardwareObjects": hardwareObjects,
       "callObjects": callObjects,
       "conferenceObjects": conferenceObjects,
       "externalIntegrationObjects": externalIntegrationObjects,
       "notificationVariableObjects": notificationVariableObjects,
       "notificationObjects": notificationObjects}
)
