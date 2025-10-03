# SNMP MIB module (CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ucopia\CONTROLLER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:42 2025
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

ucopia = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31218)
)
if mibBuilder.loadTexts:
    ucopia.setRevisions(
        ("2017-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UcpMIBConformance_ObjectIdentity = ObjectIdentity
ucpMIBConformance = _UcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31218, 1)
)
_UcpMIBGroups_ObjectIdentity = ObjectIdentity
ucpMIBGroups = _UcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31218, 1, 1)
)
_UcpMIBCompliances_ObjectIdentity = ObjectIdentity
ucpMIBCompliances = _UcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31218, 1, 2)
)
_UcpNotifications_ObjectIdentity = ObjectIdentity
ucpNotifications = _UcpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31218, 2)
)
_UcpNotificationPrefix_ObjectIdentity = ObjectIdentity
ucpNotificationPrefix = _UcpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31218, 2, 0)
)
_UcpState_ObjectIdentity = ObjectIdentity
ucpState = _UcpState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31218, 3)
)
_TotalConnectedUsers_Type = Gauge32
_TotalConnectedUsers_Object = MibScalar
totalConnectedUsers = _TotalConnectedUsers_Object(
    (1, 3, 6, 1, 4, 1, 31218, 3, 1),
    _TotalConnectedUsers_Type()
)
totalConnectedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalConnectedUsers.setStatus("current")


class _DebugValue_Type(Integer32):
    """Custom type debugValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DebugValue_Type.__name__ = "Integer32"
_DebugValue_Object = MibScalar
debugValue = _DebugValue_Object(
    (1, 3, 6, 1, 4, 1, 31218, 3, 2),
    _DebugValue_Type()
)
debugValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugValue.setStatus("current")


class _CpuTemperature_Type(Integer32):
    """Custom type cpuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuTemperature_Type.__name__ = "Integer32"
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31218, 3, 3),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")


class _DiskTemperature_Type(Integer32):
    """Custom type diskTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskTemperature_Type.__name__ = "Integer32"
_DiskTemperature_Object = MibScalar
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31218, 3, 4),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("current")
_LicenseUsers_Type = Integer32
_LicenseUsers_Object = MibScalar
licenseUsers = _LicenseUsers_Object(
    (1, 3, 6, 1, 4, 1, 31218, 3, 5),
    _LicenseUsers_Type()
)
licenseUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseUsers.setStatus("current")


class _SysObjectDescription_Type(DisplayString):
    """Custom type sysObjectDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysObjectDescription_Type.__name__ = "DisplayString"
_SysObjectDescription_Object = MibScalar
sysObjectDescription = _SysObjectDescription_Object(
    (1, 3, 6, 1, 4, 1, 31218, 3, 6),
    _SysObjectDescription_Type()
)
sysObjectDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectDescription.setStatus("current")


class _HighAvailabilityStatus_Type(Integer32):
    """Custom type highAvailabilityStatus based on Integer32"""
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
        *(("standalone", 0),
          ("master", 1),
          ("active", 2),
          ("passive", 3),
          ("fault", 4))
    )


_HighAvailabilityStatus_Type.__name__ = "Integer32"
_HighAvailabilityStatus_Object = MibScalar
highAvailabilityStatus = _HighAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 31218, 3, 7),
    _HighAvailabilityStatus_Type()
)
highAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailabilityStatus.setStatus("current")
_ServiceStatus_ObjectIdentity = ObjectIdentity
serviceStatus = _ServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31218, 4)
)


class _WebServerService_Type(Integer32):
    """Custom type webServerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_WebServerService_Type.__name__ = "Integer32"
_WebServerService_Object = MibScalar
webServerService = _WebServerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 1),
    _WebServerService_Type()
)
webServerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webServerService.setStatus("current")


class _SqlServerService_Type(Integer32):
    """Custom type sqlServerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_SqlServerService_Type.__name__ = "Integer32"
_SqlServerService_Object = MibScalar
sqlServerService = _SqlServerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 2),
    _SqlServerService_Type()
)
sqlServerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlServerService.setStatus("current")


class _UrlSnifferService_Type(Integer32):
    """Custom type urlSnifferService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_UrlSnifferService_Type.__name__ = "Integer32"
_UrlSnifferService_Object = MibScalar
urlSnifferService = _UrlSnifferService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 3),
    _UrlSnifferService_Type()
)
urlSnifferService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlSnifferService.setStatus("current")


class _PortalService_Type(Integer32):
    """Custom type portalService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_PortalService_Type.__name__ = "Integer32"
_PortalService_Object = MibScalar
portalService = _PortalService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 4),
    _PortalService_Type()
)
portalService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portalService.setStatus("current")


class _WebProxyService_Type(Integer32):
    """Custom type webProxyService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_WebProxyService_Type.__name__ = "Integer32"
_WebProxyService_Object = MibScalar
webProxyService = _WebProxyService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 5),
    _WebProxyService_Type()
)
webProxyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webProxyService.setStatus("current")


class _AutodisconnectService_Type(Integer32):
    """Custom type autodisconnectService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_AutodisconnectService_Type.__name__ = "Integer32"
_AutodisconnectService_Object = MibScalar
autodisconnectService = _AutodisconnectService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 6),
    _AutodisconnectService_Type()
)
autodisconnectService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autodisconnectService.setStatus("current")


class _PrintingServerService_Type(Integer32):
    """Custom type printingServerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_PrintingServerService_Type.__name__ = "Integer32"
_PrintingServerService_Object = MibScalar
printingServerService = _PrintingServerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 7),
    _PrintingServerService_Type()
)
printingServerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printingServerService.setStatus("current")


class _DhcpServerService_Type(Integer32):
    """Custom type dhcpServerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_DhcpServerService_Type.__name__ = "Integer32"
_DhcpServerService_Object = MibScalar
dhcpServerService = _DhcpServerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 8),
    _DhcpServerService_Type()
)
dhcpServerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerService.setStatus("current")


class _DnsServerService_Type(Integer32):
    """Custom type dnsServerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_DnsServerService_Type.__name__ = "Integer32"
_DnsServerService_Object = MibScalar
dnsServerService = _DnsServerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 9),
    _DnsServerService_Type()
)
dnsServerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerService.setStatus("current")


class _StaticIpManagerService_Type(Integer32):
    """Custom type staticIpManagerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_StaticIpManagerService_Type.__name__ = "Integer32"
_StaticIpManagerService_Object = MibScalar
staticIpManagerService = _StaticIpManagerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 10),
    _StaticIpManagerService_Type()
)
staticIpManagerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticIpManagerService.setStatus("current")


class _HighAvailabilityService_Type(Integer32):
    """Custom type highAvailabilityService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_HighAvailabilityService_Type.__name__ = "Integer32"
_HighAvailabilityService_Object = MibScalar
highAvailabilityService = _HighAvailabilityService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 11),
    _HighAvailabilityService_Type()
)
highAvailabilityService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailabilityService.setStatus("current")


class _LdapDirectoryService_Type(Integer32):
    """Custom type ldapDirectoryService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_LdapDirectoryService_Type.__name__ = "Integer32"
_LdapDirectoryService_Object = MibScalar
ldapDirectoryService = _LdapDirectoryService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 12),
    _LdapDirectoryService_Type()
)
ldapDirectoryService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapDirectoryService.setStatus("current")


class _LdapReplicationManagerService_Type(Integer32):
    """Custom type ldapReplicationManagerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_LdapReplicationManagerService_Type.__name__ = "Integer32"
_LdapReplicationManagerService_Object = MibScalar
ldapReplicationManagerService = _LdapReplicationManagerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 13),
    _LdapReplicationManagerService_Type()
)
ldapReplicationManagerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapReplicationManagerService.setStatus("current")


class _TimeServerService_Type(Integer32):
    """Custom type timeServerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_TimeServerService_Type.__name__ = "Integer32"
_TimeServerService_Object = MibScalar
timeServerService = _TimeServerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 14),
    _TimeServerService_Type()
)
timeServerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerService.setStatus("current")


class _RadiusServerService_Type(Integer32):
    """Custom type radiusServerService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_RadiusServerService_Type.__name__ = "Integer32"
_RadiusServerService_Object = MibScalar
radiusServerService = _RadiusServerService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 15),
    _RadiusServerService_Type()
)
radiusServerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerService.setStatus("current")


class _SambaService_Type(Integer32):
    """Custom type sambaService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_SambaService_Type.__name__ = "Integer32"
_SambaService_Object = MibScalar
sambaService = _SambaService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 16),
    _SambaService_Type()
)
sambaService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sambaService.setStatus("current")


class _SshService_Type(Integer32):
    """Custom type sshService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_SshService_Type.__name__ = "Integer32"
_SshService_Object = MibScalar
sshService = _SshService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 17),
    _SshService_Type()
)
sshService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshService.setStatus("current")


class _SyslogService_Type(Integer32):
    """Custom type syslogService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_SyslogService_Type.__name__ = "Integer32"
_SyslogService_Object = MibScalar
syslogService = _SyslogService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 18),
    _SyslogService_Type()
)
syslogService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogService.setStatus("current")


class _UsersLogService_Type(Integer32):
    """Custom type usersLogService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_UsersLogService_Type.__name__ = "Integer32"
_UsersLogService_Object = MibScalar
usersLogService = _UsersLogService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 19),
    _UsersLogService_Type()
)
usersLogService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersLogService.setStatus("current")


class _PmsClientService_Type(Integer32):
    """Custom type pmsClientService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("disabled", 3))
    )


_PmsClientService_Type.__name__ = "Integer32"
_PmsClientService_Object = MibScalar
pmsClientService = _PmsClientService_Object(
    (1, 3, 6, 1, 4, 1, 31218, 4, 20),
    _PmsClientService_Type()
)
pmsClientService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmsClientService.setStatus("current")

# Managed Objects groups

statesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31218, 1, 1, 1)
)
statesGroup.setObjects(
      *(("CONTROLLER-MIB", "totalConnectedUsers"),
        ("CONTROLLER-MIB", "debugValue"),
        ("CONTROLLER-MIB", "cpuTemperature"),
        ("CONTROLLER-MIB", "diskTemperature"),
        ("CONTROLLER-MIB", "licenseUsers"),
        ("CONTROLLER-MIB", "sysObjectDescription"),
        ("CONTROLLER-MIB", "highAvailabilityStatus"))
)
if mibBuilder.loadTexts:
    statesGroup.setStatus("current")

servicesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31218, 1, 1, 2)
)
servicesGroup.setObjects(
      *(("CONTROLLER-MIB", "webServerService"),
        ("CONTROLLER-MIB", "sqlServerService"),
        ("CONTROLLER-MIB", "urlSnifferService"),
        ("CONTROLLER-MIB", "portalService"),
        ("CONTROLLER-MIB", "webProxyService"),
        ("CONTROLLER-MIB", "autodisconnectService"),
        ("CONTROLLER-MIB", "printingServerService"),
        ("CONTROLLER-MIB", "dhcpServerService"),
        ("CONTROLLER-MIB", "dnsServerService"),
        ("CONTROLLER-MIB", "staticIpManagerService"),
        ("CONTROLLER-MIB", "highAvailabilityService"),
        ("CONTROLLER-MIB", "ldapDirectoryService"),
        ("CONTROLLER-MIB", "ldapReplicationManagerService"),
        ("CONTROLLER-MIB", "timeServerService"),
        ("CONTROLLER-MIB", "radiusServerService"),
        ("CONTROLLER-MIB", "sambaService"),
        ("CONTROLLER-MIB", "sshService"),
        ("CONTROLLER-MIB", "syslogService"),
        ("CONTROLLER-MIB", "usersLogService"),
        ("CONTROLLER-MIB", "pmsClientService"))
)
if mibBuilder.loadTexts:
    servicesGroup.setStatus("current")


# Notification objects

ucpServiceFaultStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 31218, 2, 0, 1)
)
if mibBuilder.loadTexts:
    ucpServiceFaultStateNotification.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 31218, 1, 1, 3)
)
notificationsGroup.setObjects(
    ("CONTROLLER-MIB", "ucpServiceFaultStateNotification")
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ucpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31218, 1, 2, 2)
)
ucpCompliance.setObjects(
      *(("CONTROLLER-MIB", "statesGroup"),
        ("CONTROLLER-MIB", "servicesGroup"),
        ("CONTROLLER-MIB", "notificationsGroup"))
)
if mibBuilder.loadTexts:
    ucpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTROLLER-MIB",
    **{"ucopia": ucopia,
       "ucpMIBConformance": ucpMIBConformance,
       "ucpMIBGroups": ucpMIBGroups,
       "statesGroup": statesGroup,
       "servicesGroup": servicesGroup,
       "notificationsGroup": notificationsGroup,
       "ucpMIBCompliances": ucpMIBCompliances,
       "ucpCompliance": ucpCompliance,
       "ucpNotifications": ucpNotifications,
       "ucpNotificationPrefix": ucpNotificationPrefix,
       "ucpServiceFaultStateNotification": ucpServiceFaultStateNotification,
       "ucpState": ucpState,
       "totalConnectedUsers": totalConnectedUsers,
       "debugValue": debugValue,
       "cpuTemperature": cpuTemperature,
       "diskTemperature": diskTemperature,
       "licenseUsers": licenseUsers,
       "sysObjectDescription": sysObjectDescription,
       "highAvailabilityStatus": highAvailabilityStatus,
       "serviceStatus": serviceStatus,
       "webServerService": webServerService,
       "sqlServerService": sqlServerService,
       "urlSnifferService": urlSnifferService,
       "portalService": portalService,
       "webProxyService": webProxyService,
       "autodisconnectService": autodisconnectService,
       "printingServerService": printingServerService,
       "dhcpServerService": dhcpServerService,
       "dnsServerService": dnsServerService,
       "staticIpManagerService": staticIpManagerService,
       "highAvailabilityService": highAvailabilityService,
       "ldapDirectoryService": ldapDirectoryService,
       "ldapReplicationManagerService": ldapReplicationManagerService,
       "timeServerService": timeServerService,
       "radiusServerService": radiusServerService,
       "sambaService": sambaService,
       "sshService": sshService,
       "syslogService": syslogService,
       "usersLogService": usersLogService,
       "pmsClientService": pmsClientService}
)
