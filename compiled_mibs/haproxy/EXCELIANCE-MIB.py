# SNMP MIB module (EXCELIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\haproxy\EXCELIANCE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:10 2025
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

exceliance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23263)
)
if mibBuilder.loadTexts:
    exceliance.setRevisions(
        ("2016-06-01 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ETrapsObjects_ObjectIdentity = ObjectIdentity
eTrapsObjects = _ETrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 2)
)


class _AlTrapId_Type(Integer32):
    """Custom type alTrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102,
              103,
              201,
              202,
              203,
              211,
              212,
              213,
              301,
              302,
              311,
              312,
              401,
              402,
              403,
              404,
              411,
              412,
              413,
              414)
        )
    )
    namedValues = NamedValues(
        *(("vrrpmaster", 101),
          ("vrrpbackup", 102),
          ("vrrpfault", 103),
          ("serverdown", 201),
          ("frontendfull", 202),
          ("backenddown", 203),
          ("serverup", 211),
          ("frontendopen", 212),
          ("backendup", 213),
          ("l4serverdown", 301),
          ("l4directordown", 302),
          ("l4serverup", 311),
          ("l4directorup", 312),
          ("synfloodoff", 401),
          ("ackrstfloodoff", 402),
          ("unknownttloff", 403),
          ("surgeoff", 404),
          ("synfloodon", 411),
          ("ackrstfloodon", 412),
          ("unknownttlon", 413),
          ("surgeon", 414))
    )


_AlTrapId_Type.__name__ = "Integer32"
_AlTrapId_Object = MibScalar
alTrapId = _AlTrapId_Object(
    (1, 3, 6, 1, 4, 1, 23263, 2, 1),
    _AlTrapId_Type()
)
alTrapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alTrapId.setStatus("current")


class _AlTrapMsg_Type(DisplayString):
    """Custom type alTrapMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlTrapMsg_Type.__name__ = "DisplayString"
_AlTrapMsg_Object = MibScalar
alTrapMsg = _AlTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 23263, 2, 2),
    _AlTrapMsg_Type()
)
alTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTrapMsg.setStatus("current")


class _AlTrapName_Type(DisplayString):
    """Custom type alTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlTrapName_Type.__name__ = "DisplayString"
_AlTrapName_Object = MibScalar
alTrapName = _AlTrapName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 2, 3),
    _AlTrapName_Type()
)
alTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTrapName.setStatus("current")
_ETraps_ObjectIdentity = ObjectIdentity
eTraps = _ETraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 3)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4)
)
_Landef_ObjectIdentity = ObjectIdentity
landef = _Landef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1)
)
_Compat1_ObjectIdentity = ObjectIdentity
compat1 = _Compat1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1)
)
_Counters_ObjectIdentity = ObjectIdentity
counters = _Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 1)
)
_AttackNumber_Type = Counter32
_AttackNumber_Object = MibScalar
attackNumber = _AttackNumber_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 1, 1),
    _AttackNumber_Type()
)
attackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attackNumber.setStatus("current")
_AcceptedPqts_Type = Counter32
_AcceptedPqts_Object = MibScalar
acceptedPqts = _AcceptedPqts_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 1, 2),
    _AcceptedPqts_Type()
)
acceptedPqts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptedPqts.setStatus("current")
_DroppedPqts_Type = Counter32
_DroppedPqts_Object = MibScalar
droppedPqts = _DroppedPqts_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 1, 3),
    _DroppedPqts_Type()
)
droppedPqts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    droppedPqts.setStatus("current")
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 2)
)


class _ServiceName_Type(OctetString):
    """Custom type serviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ServiceName_Type.__name__ = "OctetString"
_ServiceName_Object = MibScalar
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 2, 1),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")


class _ServiceStatus_Type(Integer32):
    """Custom type serviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 0),
          ("running", 1),
          ("unknown", 3))
    )


_ServiceStatus_Type.__name__ = "Integer32"
_ServiceStatus_Object = MibScalar
serviceStatus = _ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 2, 2),
    _ServiceStatus_Type()
)
serviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatus.setStatus("current")
_HostInfos_ObjectIdentity = ObjectIdentity
hostInfos = _HostInfos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3)
)
_LastIP_Type = IpAddress
_LastIP_Object = MibScalar
lastIP = _LastIP_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 1),
    _LastIP_Type()
)
lastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastIP.setStatus("current")


class _DnsName_Type(OctetString):
    """Custom type dnsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_DnsName_Type.__name__ = "OctetString"
_DnsName_Object = MibScalar
dnsName = _DnsName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 2),
    _DnsName_Type()
)
dnsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsName.setStatus("current")


class _HostStatus_Type(Integer32):
    """Custom type hostStatus based on Integer32"""
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


_HostStatus_Type.__name__ = "Integer32"
_HostStatus_Object = MibScalar
hostStatus = _HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 3),
    _HostStatus_Type()
)
hostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatus.setStatus("current")


class _Os_Type(OctetString):
    """Custom type os based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Os_Type.__name__ = "OctetString"
_Os_Object = MibScalar
os = _Os_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 4),
    _Os_Type()
)
os.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os.setStatus("current")


class _OsDetails_Type(OctetString):
    """Custom type osDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_OsDetails_Type.__name__ = "OctetString"
_OsDetails_Object = MibScalar
osDetails = _OsDetails_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 5),
    _OsDetails_Type()
)
osDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osDetails.setStatus("current")
_Uptime_Type = Counter32
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 6),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")


class _NetbiosName_Type(OctetString):
    """Custom type netbiosName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_NetbiosName_Type.__name__ = "OctetString"
_NetbiosName_Object = MibScalar
netbiosName = _NetbiosName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 7),
    _NetbiosName_Type()
)
netbiosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosName.setStatus("current")


class _NetbiosUser_Type(OctetString):
    """Custom type netbiosUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_NetbiosUser_Type.__name__ = "OctetString"
_NetbiosUser_Object = MibScalar
netbiosUser = _NetbiosUser_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 8),
    _NetbiosUser_Type()
)
netbiosUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbiosUser.setStatus("current")


class _Workgroup_Type(OctetString):
    """Custom type workgroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Workgroup_Type.__name__ = "OctetString"
_Workgroup_Object = MibScalar
workgroup = _Workgroup_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 9),
    _Workgroup_Type()
)
workgroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    workgroup.setStatus("current")


class _HostServer_Type(Integer32):
    """Custom type hostServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HostServer_Type.__name__ = "Integer32"
_HostServer_Object = MibScalar
hostServer = _HostServer_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 10),
    _HostServer_Type()
)
hostServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostServer.setStatus("current")


class _Manufacturer_Type(OctetString):
    """Custom type manufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Manufacturer_Type.__name__ = "OctetString"
_Manufacturer_Object = MibScalar
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 1, 3, 11),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("current")
_Landefgroups_ObjectIdentity = ObjectIdentity
landefgroups = _Landefgroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 2)
)
_Aloha_ObjectIdentity = ObjectIdentity
aloha = _Aloha_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2)
)
_Alcompat1_ObjectIdentity = ObjectIdentity
alcompat1 = _Alcompat1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1)
)
_AlProductInfo_ObjectIdentity = ObjectIdentity
alProductInfo = _AlProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 1)
)


class _AlProductName_Type(OctetString):
    """Custom type alProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProductName_Type.__name__ = "OctetString"
_AlProductName_Object = MibScalar
alProductName = _AlProductName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 1, 1),
    _AlProductName_Type()
)
alProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProductName.setStatus("current")


class _AlProductModel_Type(OctetString):
    """Custom type alProductModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProductModel_Type.__name__ = "OctetString"
_AlProductModel_Object = MibScalar
alProductModel = _AlProductModel_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 1, 2),
    _AlProductModel_Type()
)
alProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProductModel.setStatus("current")


class _AlProductVersion_Type(OctetString):
    """Custom type alProductVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProductVersion_Type.__name__ = "OctetString"
_AlProductVersion_Object = MibScalar
alProductVersion = _AlProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 1, 3),
    _AlProductVersion_Type()
)
alProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProductVersion.setStatus("current")


class _AlProductSubVersion_Type(OctetString):
    """Custom type alProductSubVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProductSubVersion_Type.__name__ = "OctetString"
_AlProductSubVersion_Object = MibScalar
alProductSubVersion = _AlProductSubVersion_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 1, 4),
    _AlProductSubVersion_Type()
)
alProductSubVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProductSubVersion.setStatus("current")


class _AlProductBuildVersion_Type(OctetString):
    """Custom type alProductBuildVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProductBuildVersion_Type.__name__ = "OctetString"
_AlProductBuildVersion_Object = MibScalar
alProductBuildVersion = _AlProductBuildVersion_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 1, 5),
    _AlProductBuildVersion_Type()
)
alProductBuildVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProductBuildVersion.setStatus("current")


class _AlProductBuildDate_Type(OctetString):
    """Custom type alProductBuildDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProductBuildDate_Type.__name__ = "OctetString"
_AlProductBuildDate_Object = MibScalar
alProductBuildDate = _AlProductBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 1, 6),
    _AlProductBuildDate_Type()
)
alProductBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProductBuildDate.setStatus("current")


class _AlProductURL_Type(OctetString):
    """Custom type alProductURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProductURL_Type.__name__ = "OctetString"
_AlProductURL_Object = MibScalar
alProductURL = _AlProductURL_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 1, 7),
    _AlProductURL_Type()
)
alProductURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProductURL.setStatus("current")
_AlServices_ObjectIdentity = ObjectIdentity
alServices = _AlServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2)
)
_AlServiceTable_Object = MibTable
alServiceTable = _AlServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alServiceTable.setStatus("current")
_AlServiceTableEntry_Object = MibTableRow
alServiceTableEntry = _AlServiceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 1, 1)
)
alServiceTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alServiceID"),
)
if mibBuilder.loadTexts:
    alServiceTableEntry.setStatus("current")


class _AlServiceID_Type(Integer32):
    """Custom type alServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlServiceID_Type.__name__ = "Integer32"
_AlServiceID_Object = MibTableColumn
alServiceID = _AlServiceID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 1, 1, 1),
    _AlServiceID_Type()
)
alServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServiceID.setStatus("current")


class _AlServiceName_Type(OctetString):
    """Custom type alServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlServiceName_Type.__name__ = "OctetString"
_AlServiceName_Object = MibTableColumn
alServiceName = _AlServiceName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 1, 1, 2),
    _AlServiceName_Type()
)
alServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServiceName.setStatus("current")


class _AlServiceStatus_Type(Integer32):
    """Custom type alServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 0),
          ("running", 1))
    )


_AlServiceStatus_Type.__name__ = "Integer32"
_AlServiceStatus_Object = MibTableColumn
alServiceStatus = _AlServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 1, 1, 3),
    _AlServiceStatus_Type()
)
alServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServiceStatus.setStatus("current")
_AlInstanceTable_Object = MibTable
alInstanceTable = _AlInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alInstanceTable.setStatus("current")
_AlInstanceTableEntry_Object = MibTableRow
alInstanceTableEntry = _AlInstanceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 2, 1)
)
alInstanceTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alInstanceServiceID"),
    (0, "EXCELIANCE-MIB", "alInstanceID"),
)
if mibBuilder.loadTexts:
    alInstanceTableEntry.setStatus("current")


class _AlInstanceServiceID_Type(Integer32):
    """Custom type alInstanceServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlInstanceServiceID_Type.__name__ = "Integer32"
_AlInstanceServiceID_Object = MibTableColumn
alInstanceServiceID = _AlInstanceServiceID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 2, 1, 1),
    _AlInstanceServiceID_Type()
)
alInstanceServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alInstanceServiceID.setStatus("current")


class _AlInstanceID_Type(Integer32):
    """Custom type alInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlInstanceID_Type.__name__ = "Integer32"
_AlInstanceID_Object = MibTableColumn
alInstanceID = _AlInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 2, 1, 2),
    _AlInstanceID_Type()
)
alInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alInstanceID.setStatus("current")


class _AlInstanceName_Type(OctetString):
    """Custom type alInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlInstanceName_Type.__name__ = "OctetString"
_AlInstanceName_Object = MibTableColumn
alInstanceName = _AlInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 2, 1, 3),
    _AlInstanceName_Type()
)
alInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alInstanceName.setStatus("current")


class _AlInstanceStatus_Type(Integer32):
    """Custom type alInstanceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 0),
          ("running", 1))
    )


_AlInstanceStatus_Type.__name__ = "Integer32"
_AlInstanceStatus_Object = MibTableColumn
alInstanceStatus = _AlInstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 2, 2, 1, 4),
    _AlInstanceStatus_Type()
)
alInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alInstanceStatus.setStatus("current")
_AlStats_ObjectIdentity = ObjectIdentity
alStats = _AlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3)
)
_AlProcessTable_Object = MibTable
alProcessTable = _AlProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alProcessTable.setStatus("current")
_AlProcessTableEntry_Object = MibTableRow
alProcessTableEntry = _AlProcessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1)
)
alProcessTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alProcessID"),
)
if mibBuilder.loadTexts:
    alProcessTableEntry.setStatus("current")


class _AlProcessID_Type(Integer32):
    """Custom type alProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessID_Type.__name__ = "Integer32"
_AlProcessID_Object = MibTableColumn
alProcessID = _AlProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 1),
    _AlProcessID_Type()
)
alProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessID.setStatus("current")


class _AlProcessVersion_Type(OctetString):
    """Custom type alProcessVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProcessVersion_Type.__name__ = "OctetString"
_AlProcessVersion_Object = MibTableColumn
alProcessVersion = _AlProcessVersion_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 2),
    _AlProcessVersion_Type()
)
alProcessVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessVersion.setStatus("current")


class _AlProcessReleaseDate_Type(OctetString):
    """Custom type alProcessReleaseDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProcessReleaseDate_Type.__name__ = "OctetString"
_AlProcessReleaseDate_Object = MibTableColumn
alProcessReleaseDate = _AlProcessReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 3),
    _AlProcessReleaseDate_Type()
)
alProcessReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessReleaseDate.setStatus("current")


class _AlProcessNbProc_Type(Integer32):
    """Custom type alProcessNbProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessNbProc_Type.__name__ = "Integer32"
_AlProcessNbProc_Object = MibTableColumn
alProcessNbProc = _AlProcessNbProc_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 4),
    _AlProcessNbProc_Type()
)
alProcessNbProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessNbProc.setStatus("current")


class _AlProcessProductName_Type(OctetString):
    """Custom type alProcessProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProcessProductName_Type.__name__ = "OctetString"
_AlProcessProductName_Object = MibTableColumn
alProcessProductName = _AlProcessProductName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 5),
    _AlProcessProductName_Type()
)
alProcessProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessProductName.setStatus("current")


class _AlProcessSystemPID_Type(Integer32):
    """Custom type alProcessSystemPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessSystemPID_Type.__name__ = "Integer32"
_AlProcessSystemPID_Object = MibTableColumn
alProcessSystemPID = _AlProcessSystemPID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 6),
    _AlProcessSystemPID_Type()
)
alProcessSystemPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSystemPID.setStatus("current")


class _AlProcessUptime_Type(OctetString):
    """Custom type alProcessUptime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProcessUptime_Type.__name__ = "OctetString"
_AlProcessUptime_Object = MibTableColumn
alProcessUptime = _AlProcessUptime_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 7),
    _AlProcessUptime_Type()
)
alProcessUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessUptime.setStatus("current")


class _AlProcessUptimeSec_Type(Integer32):
    """Custom type alProcessUptimeSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessUptimeSec_Type.__name__ = "Integer32"
_AlProcessUptimeSec_Object = MibTableColumn
alProcessUptimeSec = _AlProcessUptimeSec_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 8),
    _AlProcessUptimeSec_Type()
)
alProcessUptimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessUptimeSec.setStatus("current")


class _AlProcessMemMax_Type(Integer32):
    """Custom type alProcessMemMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMemMax_Type.__name__ = "Integer32"
_AlProcessMemMax_Object = MibTableColumn
alProcessMemMax = _AlProcessMemMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 9),
    _AlProcessMemMax_Type()
)
alProcessMemMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMemMax.setStatus("current")


class _AlProcessPoolAlloc_Type(Integer32):
    """Custom type alProcessPoolAlloc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessPoolAlloc_Type.__name__ = "Integer32"
_AlProcessPoolAlloc_Object = MibTableColumn
alProcessPoolAlloc = _AlProcessPoolAlloc_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 10),
    _AlProcessPoolAlloc_Type()
)
alProcessPoolAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessPoolAlloc.setStatus("current")


class _AlProcessPoolUsed_Type(Integer32):
    """Custom type alProcessPoolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessPoolUsed_Type.__name__ = "Integer32"
_AlProcessPoolUsed_Object = MibTableColumn
alProcessPoolUsed = _AlProcessPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 11),
    _AlProcessPoolUsed_Type()
)
alProcessPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessPoolUsed.setStatus("current")
_AlProcessPoolFailed_Type = Counter32
_AlProcessPoolFailed_Object = MibTableColumn
alProcessPoolFailed = _AlProcessPoolFailed_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 12),
    _AlProcessPoolFailed_Type()
)
alProcessPoolFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessPoolFailed.setStatus("current")


class _AlProcessUlimitn_Type(Integer32):
    """Custom type alProcessUlimitn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessUlimitn_Type.__name__ = "Integer32"
_AlProcessUlimitn_Object = MibTableColumn
alProcessUlimitn = _AlProcessUlimitn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 13),
    _AlProcessUlimitn_Type()
)
alProcessUlimitn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessUlimitn.setStatus("current")


class _AlProcessMaxSock_Type(Integer32):
    """Custom type alProcessMaxSock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxSock_Type.__name__ = "Integer32"
_AlProcessMaxSock_Object = MibTableColumn
alProcessMaxSock = _AlProcessMaxSock_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 14),
    _AlProcessMaxSock_Type()
)
alProcessMaxSock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxSock.setStatus("current")


class _AlProcessMaxConn_Type(Integer32):
    """Custom type alProcessMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxConn_Type.__name__ = "Integer32"
_AlProcessMaxConn_Object = MibTableColumn
alProcessMaxConn = _AlProcessMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 15),
    _AlProcessMaxConn_Type()
)
alProcessMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxConn.setStatus("current")


class _AlProcessHardMaxConn_Type(Integer32):
    """Custom type alProcessHardMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessHardMaxConn_Type.__name__ = "Integer32"
_AlProcessHardMaxConn_Object = MibTableColumn
alProcessHardMaxConn = _AlProcessHardMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 16),
    _AlProcessHardMaxConn_Type()
)
alProcessHardMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessHardMaxConn.setStatus("current")


class _AlProcessCurConn_Type(Integer32):
    """Custom type alProcessCurConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessCurConn_Type.__name__ = "Integer32"
_AlProcessCurConn_Object = MibTableColumn
alProcessCurConn = _AlProcessCurConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 17),
    _AlProcessCurConn_Type()
)
alProcessCurConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessCurConn.setStatus("current")
_AlProcessCumConn_Type = Counter32
_AlProcessCumConn_Object = MibTableColumn
alProcessCumConn = _AlProcessCumConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 18),
    _AlProcessCumConn_Type()
)
alProcessCumConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessCumConn.setStatus("current")
_AlProcessCumReq_Type = Counter32
_AlProcessCumReq_Object = MibTableColumn
alProcessCumReq = _AlProcessCumReq_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 19),
    _AlProcessCumReq_Type()
)
alProcessCumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessCumReq.setStatus("current")


class _AlProcessMaxSslConn_Type(Integer32):
    """Custom type alProcessMaxSslConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxSslConn_Type.__name__ = "Integer32"
_AlProcessMaxSslConn_Object = MibTableColumn
alProcessMaxSslConn = _AlProcessMaxSslConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 20),
    _AlProcessMaxSslConn_Type()
)
alProcessMaxSslConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxSslConn.setStatus("current")


class _AlProcessCurSslConn_Type(Integer32):
    """Custom type alProcessCurSslConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessCurSslConn_Type.__name__ = "Integer32"
_AlProcessCurSslConn_Object = MibTableColumn
alProcessCurSslConn = _AlProcessCurSslConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 21),
    _AlProcessCurSslConn_Type()
)
alProcessCurSslConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessCurSslConn.setStatus("current")
_AlProcessCumSslConn_Type = Counter32
_AlProcessCumSslConn_Object = MibTableColumn
alProcessCumSslConn = _AlProcessCumSslConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 22),
    _AlProcessCumSslConn_Type()
)
alProcessCumSslConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessCumSslConn.setStatus("current")


class _AlProcessMaxPipes_Type(Integer32):
    """Custom type alProcessMaxPipes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxPipes_Type.__name__ = "Integer32"
_AlProcessMaxPipes_Object = MibTableColumn
alProcessMaxPipes = _AlProcessMaxPipes_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 23),
    _AlProcessMaxPipes_Type()
)
alProcessMaxPipes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxPipes.setStatus("current")


class _AlProcessPipesUsed_Type(Integer32):
    """Custom type alProcessPipesUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessPipesUsed_Type.__name__ = "Integer32"
_AlProcessPipesUsed_Object = MibTableColumn
alProcessPipesUsed = _AlProcessPipesUsed_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 24),
    _AlProcessPipesUsed_Type()
)
alProcessPipesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessPipesUsed.setStatus("current")


class _AlProcessPipesFree_Type(Integer32):
    """Custom type alProcessPipesFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessPipesFree_Type.__name__ = "Integer32"
_AlProcessPipesFree_Object = MibTableColumn
alProcessPipesFree = _AlProcessPipesFree_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 25),
    _AlProcessPipesFree_Type()
)
alProcessPipesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessPipesFree.setStatus("current")


class _AlProcessConnRate_Type(Integer32):
    """Custom type alProcessConnRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessConnRate_Type.__name__ = "Integer32"
_AlProcessConnRate_Object = MibTableColumn
alProcessConnRate = _AlProcessConnRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 26),
    _AlProcessConnRate_Type()
)
alProcessConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessConnRate.setStatus("current")


class _AlProcessConnRateLimit_Type(Integer32):
    """Custom type alProcessConnRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessConnRateLimit_Type.__name__ = "Integer32"
_AlProcessConnRateLimit_Object = MibTableColumn
alProcessConnRateLimit = _AlProcessConnRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 27),
    _AlProcessConnRateLimit_Type()
)
alProcessConnRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessConnRateLimit.setStatus("current")


class _AlProcessMaxConnRate_Type(Integer32):
    """Custom type alProcessMaxConnRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxConnRate_Type.__name__ = "Integer32"
_AlProcessMaxConnRate_Object = MibTableColumn
alProcessMaxConnRate = _AlProcessMaxConnRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 28),
    _AlProcessMaxConnRate_Type()
)
alProcessMaxConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxConnRate.setStatus("current")


class _AlProcessSessRate_Type(Integer32):
    """Custom type alProcessSessRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessSessRate_Type.__name__ = "Integer32"
_AlProcessSessRate_Object = MibTableColumn
alProcessSessRate = _AlProcessSessRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 29),
    _AlProcessSessRate_Type()
)
alProcessSessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSessRate.setStatus("current")


class _AlProcessSessRateLimit_Type(Integer32):
    """Custom type alProcessSessRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessSessRateLimit_Type.__name__ = "Integer32"
_AlProcessSessRateLimit_Object = MibTableColumn
alProcessSessRateLimit = _AlProcessSessRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 30),
    _AlProcessSessRateLimit_Type()
)
alProcessSessRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSessRateLimit.setStatus("current")


class _AlProcessMaxSessRate_Type(Integer32):
    """Custom type alProcessMaxSessRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxSessRate_Type.__name__ = "Integer32"
_AlProcessMaxSessRate_Object = MibTableColumn
alProcessMaxSessRate = _AlProcessMaxSessRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 31),
    _AlProcessMaxSessRate_Type()
)
alProcessMaxSessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxSessRate.setStatus("current")


class _AlProcessSslRate_Type(Integer32):
    """Custom type alProcessSslRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessSslRate_Type.__name__ = "Integer32"
_AlProcessSslRate_Object = MibTableColumn
alProcessSslRate = _AlProcessSslRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 32),
    _AlProcessSslRate_Type()
)
alProcessSslRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSslRate.setStatus("current")


class _AlProcessSslRateLimit_Type(Integer32):
    """Custom type alProcessSslRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessSslRateLimit_Type.__name__ = "Integer32"
_AlProcessSslRateLimit_Object = MibTableColumn
alProcessSslRateLimit = _AlProcessSslRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 33),
    _AlProcessSslRateLimit_Type()
)
alProcessSslRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSslRateLimit.setStatus("current")


class _AlProcessMaxSslRate_Type(Integer32):
    """Custom type alProcessMaxSslRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxSslRate_Type.__name__ = "Integer32"
_AlProcessMaxSslRate_Object = MibTableColumn
alProcessMaxSslRate = _AlProcessMaxSslRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 34),
    _AlProcessMaxSslRate_Type()
)
alProcessMaxSslRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxSslRate.setStatus("current")


class _AlProcessSslFrontendKeyRate_Type(Integer32):
    """Custom type alProcessSslFrontendKeyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessSslFrontendKeyRate_Type.__name__ = "Integer32"
_AlProcessSslFrontendKeyRate_Object = MibTableColumn
alProcessSslFrontendKeyRate = _AlProcessSslFrontendKeyRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 35),
    _AlProcessSslFrontendKeyRate_Type()
)
alProcessSslFrontendKeyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSslFrontendKeyRate.setStatus("current")


class _AlProcessMaxSslFrontendKeyRate_Type(Integer32):
    """Custom type alProcessMaxSslFrontendKeyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxSslFrontendKeyRate_Type.__name__ = "Integer32"
_AlProcessMaxSslFrontendKeyRate_Object = MibTableColumn
alProcessMaxSslFrontendKeyRate = _AlProcessMaxSslFrontendKeyRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 36),
    _AlProcessMaxSslFrontendKeyRate_Type()
)
alProcessMaxSslFrontendKeyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxSslFrontendKeyRate.setStatus("current")


class _AlProcessSslFrontendSessReuse_Type(Integer32):
    """Custom type alProcessSslFrontendSessReuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessSslFrontendSessReuse_Type.__name__ = "Integer32"
_AlProcessSslFrontendSessReuse_Object = MibTableColumn
alProcessSslFrontendSessReuse = _AlProcessSslFrontendSessReuse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 37),
    _AlProcessSslFrontendSessReuse_Type()
)
alProcessSslFrontendSessReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSslFrontendSessReuse.setStatus("current")


class _AlProcessSslBackendKeyRate_Type(Integer32):
    """Custom type alProcessSslBackendKeyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessSslBackendKeyRate_Type.__name__ = "Integer32"
_AlProcessSslBackendKeyRate_Object = MibTableColumn
alProcessSslBackendKeyRate = _AlProcessSslBackendKeyRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 38),
    _AlProcessSslBackendKeyRate_Type()
)
alProcessSslBackendKeyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSslBackendKeyRate.setStatus("current")


class _AlProcessMaxSslBackendKeyRate_Type(Integer32):
    """Custom type alProcessMaxSslBackendKeyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxSslBackendKeyRate_Type.__name__ = "Integer32"
_AlProcessMaxSslBackendKeyRate_Object = MibTableColumn
alProcessMaxSslBackendKeyRate = _AlProcessMaxSslBackendKeyRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 39),
    _AlProcessMaxSslBackendKeyRate_Type()
)
alProcessMaxSslBackendKeyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxSslBackendKeyRate.setStatus("current")
_AlProcessSslCacheLookups_Type = Counter32
_AlProcessSslCacheLookups_Object = MibTableColumn
alProcessSslCacheLookups = _AlProcessSslCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 40),
    _AlProcessSslCacheLookups_Type()
)
alProcessSslCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSslCacheLookups.setStatus("current")
_AlProcessSslCacheMisses_Type = Counter32
_AlProcessSslCacheMisses_Object = MibTableColumn
alProcessSslCacheMisses = _AlProcessSslCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 41),
    _AlProcessSslCacheMisses_Type()
)
alProcessSslCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessSslCacheMisses.setStatus("current")


class _AlProcessCompressBpsIn_Type(Integer32):
    """Custom type alProcessCompressBpsIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessCompressBpsIn_Type.__name__ = "Integer32"
_AlProcessCompressBpsIn_Object = MibTableColumn
alProcessCompressBpsIn = _AlProcessCompressBpsIn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 42),
    _AlProcessCompressBpsIn_Type()
)
alProcessCompressBpsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessCompressBpsIn.setStatus("current")


class _AlProcessCompressBpsOut_Type(Integer32):
    """Custom type alProcessCompressBpsOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessCompressBpsOut_Type.__name__ = "Integer32"
_AlProcessCompressBpsOut_Object = MibTableColumn
alProcessCompressBpsOut = _AlProcessCompressBpsOut_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 43),
    _AlProcessCompressBpsOut_Type()
)
alProcessCompressBpsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessCompressBpsOut.setStatus("current")


class _AlProcessCompressRateLimit_Type(Integer32):
    """Custom type alProcessCompressRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessCompressRateLimit_Type.__name__ = "Integer32"
_AlProcessCompressRateLimit_Object = MibTableColumn
alProcessCompressRateLimit = _AlProcessCompressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 44),
    _AlProcessCompressRateLimit_Type()
)
alProcessCompressRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessCompressRateLimit.setStatus("current")


class _AlProcessZlibMemUsage_Type(Integer32):
    """Custom type alProcessZlibMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessZlibMemUsage_Type.__name__ = "Integer32"
_AlProcessZlibMemUsage_Object = MibTableColumn
alProcessZlibMemUsage = _AlProcessZlibMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 45),
    _AlProcessZlibMemUsage_Type()
)
alProcessZlibMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessZlibMemUsage.setStatus("current")


class _AlProcessMaxZlibMemUsage_Type(Integer32):
    """Custom type alProcessMaxZlibMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessMaxZlibMemUsage_Type.__name__ = "Integer32"
_AlProcessMaxZlibMemUsage_Object = MibTableColumn
alProcessMaxZlibMemUsage = _AlProcessMaxZlibMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 46),
    _AlProcessMaxZlibMemUsage_Type()
)
alProcessMaxZlibMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessMaxZlibMemUsage.setStatus("current")


class _AlProcessTasks_Type(Integer32):
    """Custom type alProcessTasks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessTasks_Type.__name__ = "Integer32"
_AlProcessTasks_Object = MibTableColumn
alProcessTasks = _AlProcessTasks_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 47),
    _AlProcessTasks_Type()
)
alProcessTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessTasks.setStatus("current")


class _AlProcessRunQueue_Type(Integer32):
    """Custom type alProcessRunQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessRunQueue_Type.__name__ = "Integer32"
_AlProcessRunQueue_Object = MibTableColumn
alProcessRunQueue = _AlProcessRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 48),
    _AlProcessRunQueue_Type()
)
alProcessRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessRunQueue.setStatus("current")


class _AlProcessIdle_Type(Integer32):
    """Custom type alProcessIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlProcessIdle_Type.__name__ = "Integer32"
_AlProcessIdle_Object = MibTableColumn
alProcessIdle = _AlProcessIdle_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 49),
    _AlProcessIdle_Type()
)
alProcessIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessIdle.setStatus("current")


class _AlProcessNodeName_Type(OctetString):
    """Custom type alProcessNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProcessNodeName_Type.__name__ = "OctetString"
_AlProcessNodeName_Object = MibTableColumn
alProcessNodeName = _AlProcessNodeName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 50),
    _AlProcessNodeName_Type()
)
alProcessNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessNodeName.setStatus("current")


class _AlProcessDescription_Type(OctetString):
    """Custom type alProcessDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlProcessDescription_Type.__name__ = "OctetString"
_AlProcessDescription_Object = MibTableColumn
alProcessDescription = _AlProcessDescription_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 1, 1, 51),
    _AlProcessDescription_Type()
)
alProcessDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alProcessDescription.setStatus("current")
_AlFrontendTable_Object = MibTable
alFrontendTable = _AlFrontendTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alFrontendTable.setStatus("current")
_AlFrontendTableEntry_Object = MibTableRow
alFrontendTableEntry = _AlFrontendTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1)
)
alFrontendTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alFrontendProcessID"),
    (0, "EXCELIANCE-MIB", "alFrontendID"),
)
if mibBuilder.loadTexts:
    alFrontendTableEntry.setStatus("current")


class _AlFrontendProcessID_Type(Integer32):
    """Custom type alFrontendProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlFrontendProcessID_Type.__name__ = "Integer32"
_AlFrontendProcessID_Object = MibTableColumn
alFrontendProcessID = _AlFrontendProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 1),
    _AlFrontendProcessID_Type()
)
alFrontendProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendProcessID.setStatus("current")


class _AlFrontendID_Type(Integer32):
    """Custom type alFrontendID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlFrontendID_Type.__name__ = "Integer32"
_AlFrontendID_Object = MibTableColumn
alFrontendID = _AlFrontendID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 2),
    _AlFrontendID_Type()
)
alFrontendID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendID.setStatus("current")


class _AlFrontendName_Type(OctetString):
    """Custom type alFrontendName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlFrontendName_Type.__name__ = "OctetString"
_AlFrontendName_Object = MibTableColumn
alFrontendName = _AlFrontendName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 3),
    _AlFrontendName_Type()
)
alFrontendName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendName.setStatus("current")
_AlFrontendSessionCur_Type = Counter64
_AlFrontendSessionCur_Object = MibTableColumn
alFrontendSessionCur = _AlFrontendSessionCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 4),
    _AlFrontendSessionCur_Type()
)
alFrontendSessionCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendSessionCur.setStatus("current")
_AlFrontendSessionMax_Type = Counter64
_AlFrontendSessionMax_Object = MibTableColumn
alFrontendSessionMax = _AlFrontendSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 5),
    _AlFrontendSessionMax_Type()
)
alFrontendSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendSessionMax.setStatus("current")
_AlFrontendSessionLimit_Type = Counter64
_AlFrontendSessionLimit_Object = MibTableColumn
alFrontendSessionLimit = _AlFrontendSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 6),
    _AlFrontendSessionLimit_Type()
)
alFrontendSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendSessionLimit.setStatus("current")
_AlFrontendSessionTotal_Type = Counter64
_AlFrontendSessionTotal_Object = MibTableColumn
alFrontendSessionTotal = _AlFrontendSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 7),
    _AlFrontendSessionTotal_Type()
)
alFrontendSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendSessionTotal.setStatus("current")
_AlFrontendBytesIN_Type = Counter64
_AlFrontendBytesIN_Object = MibTableColumn
alFrontendBytesIN = _AlFrontendBytesIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 8),
    _AlFrontendBytesIN_Type()
)
alFrontendBytesIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendBytesIN.setStatus("current")
_AlFrontendBytesOUT_Type = Counter64
_AlFrontendBytesOUT_Object = MibTableColumn
alFrontendBytesOUT = _AlFrontendBytesOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 9),
    _AlFrontendBytesOUT_Type()
)
alFrontendBytesOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendBytesOUT.setStatus("current")
_AlFrontendErrorRequest_Type = Counter64
_AlFrontendErrorRequest_Object = MibTableColumn
alFrontendErrorRequest = _AlFrontendErrorRequest_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 10),
    _AlFrontendErrorRequest_Type()
)
alFrontendErrorRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendErrorRequest.setStatus("current")
_AlFrontendDenyRequest_Type = Counter64
_AlFrontendDenyRequest_Object = MibTableColumn
alFrontendDenyRequest = _AlFrontendDenyRequest_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 11),
    _AlFrontendDenyRequest_Type()
)
alFrontendDenyRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendDenyRequest.setStatus("current")
_AlFrontendDenyResponse_Type = Counter64
_AlFrontendDenyResponse_Object = MibTableColumn
alFrontendDenyResponse = _AlFrontendDenyResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 12),
    _AlFrontendDenyResponse_Type()
)
alFrontendDenyResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendDenyResponse.setStatus("current")


class _AlFrontendStatus_Type(OctetString):
    """Custom type alFrontendStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlFrontendStatus_Type.__name__ = "OctetString"
_AlFrontendStatus_Object = MibTableColumn
alFrontendStatus = _AlFrontendStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 2, 1, 13),
    _AlFrontendStatus_Type()
)
alFrontendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFrontendStatus.setStatus("current")
_AlBackendTable_Object = MibTable
alBackendTable = _AlBackendTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    alBackendTable.setStatus("current")
_AlBackendTableEntry_Object = MibTableRow
alBackendTableEntry = _AlBackendTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1)
)
alBackendTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alBackendProcessID"),
    (0, "EXCELIANCE-MIB", "alBackendID"),
)
if mibBuilder.loadTexts:
    alBackendTableEntry.setStatus("current")


class _AlBackendProcessID_Type(Integer32):
    """Custom type alBackendProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlBackendProcessID_Type.__name__ = "Integer32"
_AlBackendProcessID_Object = MibTableColumn
alBackendProcessID = _AlBackendProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 1),
    _AlBackendProcessID_Type()
)
alBackendProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendProcessID.setStatus("current")


class _AlBackendID_Type(Integer32):
    """Custom type alBackendID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlBackendID_Type.__name__ = "Integer32"
_AlBackendID_Object = MibTableColumn
alBackendID = _AlBackendID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 2),
    _AlBackendID_Type()
)
alBackendID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendID.setStatus("current")


class _AlBackendName_Type(OctetString):
    """Custom type alBackendName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlBackendName_Type.__name__ = "OctetString"
_AlBackendName_Object = MibTableColumn
alBackendName = _AlBackendName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 3),
    _AlBackendName_Type()
)
alBackendName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendName.setStatus("current")
_AlBackendQueueCur_Type = Counter64
_AlBackendQueueCur_Object = MibTableColumn
alBackendQueueCur = _AlBackendQueueCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 4),
    _AlBackendQueueCur_Type()
)
alBackendQueueCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendQueueCur.setStatus("current")
_AlBackendQueueMax_Type = Counter64
_AlBackendQueueMax_Object = MibTableColumn
alBackendQueueMax = _AlBackendQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 5),
    _AlBackendQueueMax_Type()
)
alBackendQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendQueueMax.setStatus("current")
_AlBackendQueueLimit_Type = Counter64
_AlBackendQueueLimit_Object = MibTableColumn
alBackendQueueLimit = _AlBackendQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 6),
    _AlBackendQueueLimit_Type()
)
alBackendQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendQueueLimit.setStatus("current")
_AlBackendSessionCur_Type = Counter64
_AlBackendSessionCur_Object = MibTableColumn
alBackendSessionCur = _AlBackendSessionCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 7),
    _AlBackendSessionCur_Type()
)
alBackendSessionCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendSessionCur.setStatus("current")
_AlBackendSessionMax_Type = Counter64
_AlBackendSessionMax_Object = MibTableColumn
alBackendSessionMax = _AlBackendSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 8),
    _AlBackendSessionMax_Type()
)
alBackendSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendSessionMax.setStatus("current")
_AlBackendSessionLimit_Type = Counter64
_AlBackendSessionLimit_Object = MibTableColumn
alBackendSessionLimit = _AlBackendSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 9),
    _AlBackendSessionLimit_Type()
)
alBackendSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendSessionLimit.setStatus("current")
_AlBackendSessionTotal_Type = Counter64
_AlBackendSessionTotal_Object = MibTableColumn
alBackendSessionTotal = _AlBackendSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 10),
    _AlBackendSessionTotal_Type()
)
alBackendSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendSessionTotal.setStatus("current")
_AlBackendSessionLoadBalanced_Type = Counter64
_AlBackendSessionLoadBalanced_Object = MibTableColumn
alBackendSessionLoadBalanced = _AlBackendSessionLoadBalanced_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 11),
    _AlBackendSessionLoadBalanced_Type()
)
alBackendSessionLoadBalanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendSessionLoadBalanced.setStatus("current")
_AlBackendBytesIN_Type = Counter64
_AlBackendBytesIN_Object = MibTableColumn
alBackendBytesIN = _AlBackendBytesIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 12),
    _AlBackendBytesIN_Type()
)
alBackendBytesIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendBytesIN.setStatus("current")
_AlBackendBytesOUT_Type = Counter64
_AlBackendBytesOUT_Object = MibTableColumn
alBackendBytesOUT = _AlBackendBytesOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 13),
    _AlBackendBytesOUT_Type()
)
alBackendBytesOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendBytesOUT.setStatus("current")
_AlBackendErrorConnection_Type = Counter64
_AlBackendErrorConnection_Object = MibTableColumn
alBackendErrorConnection = _AlBackendErrorConnection_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 14),
    _AlBackendErrorConnection_Type()
)
alBackendErrorConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendErrorConnection.setStatus("current")
_AlBackendErrorResponse_Type = Counter64
_AlBackendErrorResponse_Object = MibTableColumn
alBackendErrorResponse = _AlBackendErrorResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 15),
    _AlBackendErrorResponse_Type()
)
alBackendErrorResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendErrorResponse.setStatus("current")
_AlBackendDenyRequest_Type = Counter64
_AlBackendDenyRequest_Object = MibTableColumn
alBackendDenyRequest = _AlBackendDenyRequest_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 16),
    _AlBackendDenyRequest_Type()
)
alBackendDenyRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendDenyRequest.setStatus("current")
_AlBackendDenyResponse_Type = Counter64
_AlBackendDenyResponse_Object = MibTableColumn
alBackendDenyResponse = _AlBackendDenyResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 17),
    _AlBackendDenyResponse_Type()
)
alBackendDenyResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendDenyResponse.setStatus("current")
_AlBackendWarningRetry_Type = Counter64
_AlBackendWarningRetry_Object = MibTableColumn
alBackendWarningRetry = _AlBackendWarningRetry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 18),
    _AlBackendWarningRetry_Type()
)
alBackendWarningRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendWarningRetry.setStatus("current")
_AlBackendWarningRedispatch_Type = Counter64
_AlBackendWarningRedispatch_Object = MibTableColumn
alBackendWarningRedispatch = _AlBackendWarningRedispatch_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 19),
    _AlBackendWarningRedispatch_Type()
)
alBackendWarningRedispatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendWarningRedispatch.setStatus("current")


class _AlBackendStatus_Type(OctetString):
    """Custom type alBackendStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlBackendStatus_Type.__name__ = "OctetString"
_AlBackendStatus_Object = MibTableColumn
alBackendStatus = _AlBackendStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 20),
    _AlBackendStatus_Type()
)
alBackendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendStatus.setStatus("current")
_AlBackendLastChange_Type = Counter32
_AlBackendLastChange_Object = MibTableColumn
alBackendLastChange = _AlBackendLastChange_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 21),
    _AlBackendLastChange_Type()
)
alBackendLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendLastChange.setStatus("current")
_AlBackendCheckDown_Type = Counter32
_AlBackendCheckDown_Object = MibTableColumn
alBackendCheckDown = _AlBackendCheckDown_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 22),
    _AlBackendCheckDown_Type()
)
alBackendCheckDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendCheckDown.setStatus("current")
_AlBackendDownTime_Type = Counter32
_AlBackendDownTime_Object = MibTableColumn
alBackendDownTime = _AlBackendDownTime_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 3, 1, 23),
    _AlBackendDownTime_Type()
)
alBackendDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackendDownTime.setStatus("current")
_AlServerTable_Object = MibTable
alServerTable = _AlServerTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    alServerTable.setStatus("current")
_AlServerTableEntry_Object = MibTableRow
alServerTableEntry = _AlServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1)
)
alServerTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alServerProcessID"),
    (0, "EXCELIANCE-MIB", "alServerBackendID"),
    (0, "EXCELIANCE-MIB", "alServerID"),
)
if mibBuilder.loadTexts:
    alServerTableEntry.setStatus("current")


class _AlServerProcessID_Type(Integer32):
    """Custom type alServerProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlServerProcessID_Type.__name__ = "Integer32"
_AlServerProcessID_Object = MibTableColumn
alServerProcessID = _AlServerProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 1),
    _AlServerProcessID_Type()
)
alServerProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerProcessID.setStatus("current")


class _AlServerBackendID_Type(Integer32):
    """Custom type alServerBackendID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlServerBackendID_Type.__name__ = "Integer32"
_AlServerBackendID_Object = MibTableColumn
alServerBackendID = _AlServerBackendID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 2),
    _AlServerBackendID_Type()
)
alServerBackendID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerBackendID.setStatus("current")


class _AlServerID_Type(Integer32):
    """Custom type alServerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlServerID_Type.__name__ = "Integer32"
_AlServerID_Object = MibTableColumn
alServerID = _AlServerID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 3),
    _AlServerID_Type()
)
alServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerID.setStatus("current")


class _AlServerName_Type(OctetString):
    """Custom type alServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlServerName_Type.__name__ = "OctetString"
_AlServerName_Object = MibTableColumn
alServerName = _AlServerName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 4),
    _AlServerName_Type()
)
alServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerName.setStatus("current")
_AlServerQueueCur_Type = Counter64
_AlServerQueueCur_Object = MibTableColumn
alServerQueueCur = _AlServerQueueCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 5),
    _AlServerQueueCur_Type()
)
alServerQueueCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerQueueCur.setStatus("current")
_AlServerQueueMax_Type = Counter64
_AlServerQueueMax_Object = MibTableColumn
alServerQueueMax = _AlServerQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 6),
    _AlServerQueueMax_Type()
)
alServerQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerQueueMax.setStatus("current")
_AlServerQueueLimit_Type = Counter64
_AlServerQueueLimit_Object = MibTableColumn
alServerQueueLimit = _AlServerQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 7),
    _AlServerQueueLimit_Type()
)
alServerQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerQueueLimit.setStatus("current")
_AlServerSessionCur_Type = Counter64
_AlServerSessionCur_Object = MibTableColumn
alServerSessionCur = _AlServerSessionCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 8),
    _AlServerSessionCur_Type()
)
alServerSessionCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerSessionCur.setStatus("current")
_AlServerSessionMax_Type = Counter64
_AlServerSessionMax_Object = MibTableColumn
alServerSessionMax = _AlServerSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 9),
    _AlServerSessionMax_Type()
)
alServerSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerSessionMax.setStatus("current")
_AlServerSessionLimit_Type = Counter64
_AlServerSessionLimit_Object = MibTableColumn
alServerSessionLimit = _AlServerSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 10),
    _AlServerSessionLimit_Type()
)
alServerSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerSessionLimit.setStatus("current")
_AlServerSessionTotal_Type = Counter64
_AlServerSessionTotal_Object = MibTableColumn
alServerSessionTotal = _AlServerSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 11),
    _AlServerSessionTotal_Type()
)
alServerSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerSessionTotal.setStatus("current")
_AlServerSessionLoadBalanced_Type = Counter64
_AlServerSessionLoadBalanced_Object = MibTableColumn
alServerSessionLoadBalanced = _AlServerSessionLoadBalanced_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 12),
    _AlServerSessionLoadBalanced_Type()
)
alServerSessionLoadBalanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerSessionLoadBalanced.setStatus("current")
_AlServerBytesIN_Type = Counter64
_AlServerBytesIN_Object = MibTableColumn
alServerBytesIN = _AlServerBytesIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 13),
    _AlServerBytesIN_Type()
)
alServerBytesIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerBytesIN.setStatus("current")
_AlServerBytesOUT_Type = Counter64
_AlServerBytesOUT_Object = MibTableColumn
alServerBytesOUT = _AlServerBytesOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 14),
    _AlServerBytesOUT_Type()
)
alServerBytesOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerBytesOUT.setStatus("current")
_AlServerErrorConnection_Type = Counter64
_AlServerErrorConnection_Object = MibTableColumn
alServerErrorConnection = _AlServerErrorConnection_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 15),
    _AlServerErrorConnection_Type()
)
alServerErrorConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerErrorConnection.setStatus("current")
_AlServerErrorResponse_Type = Counter64
_AlServerErrorResponse_Object = MibTableColumn
alServerErrorResponse = _AlServerErrorResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 16),
    _AlServerErrorResponse_Type()
)
alServerErrorResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerErrorResponse.setStatus("current")
_AlServerDenyResponse_Type = Counter64
_AlServerDenyResponse_Object = MibTableColumn
alServerDenyResponse = _AlServerDenyResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 17),
    _AlServerDenyResponse_Type()
)
alServerDenyResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerDenyResponse.setStatus("current")
_AlServerWarningRetry_Type = Counter64
_AlServerWarningRetry_Object = MibTableColumn
alServerWarningRetry = _AlServerWarningRetry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 18),
    _AlServerWarningRetry_Type()
)
alServerWarningRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerWarningRetry.setStatus("current")


class _AlServerStatus_Type(OctetString):
    """Custom type alServerStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlServerStatus_Type.__name__ = "OctetString"
_AlServerStatus_Object = MibTableColumn
alServerStatus = _AlServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 19),
    _AlServerStatus_Type()
)
alServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerStatus.setStatus("current")
_AlServerLastChange_Type = Counter32
_AlServerLastChange_Object = MibTableColumn
alServerLastChange = _AlServerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 20),
    _AlServerLastChange_Type()
)
alServerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerLastChange.setStatus("current")
_AlServerWeight_Type = Counter32
_AlServerWeight_Object = MibTableColumn
alServerWeight = _AlServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 21),
    _AlServerWeight_Type()
)
alServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerWeight.setStatus("current")


class _AlServerActive_Type(Integer32):
    """Custom type alServerActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlServerActive_Type.__name__ = "Integer32"
_AlServerActive_Object = MibTableColumn
alServerActive = _AlServerActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 22),
    _AlServerActive_Type()
)
alServerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerActive.setStatus("current")


class _AlServerBackup_Type(Integer32):
    """Custom type alServerBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlServerBackup_Type.__name__ = "Integer32"
_AlServerBackup_Object = MibTableColumn
alServerBackup = _AlServerBackup_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 23),
    _AlServerBackup_Type()
)
alServerBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerBackup.setStatus("current")
_AlServerCheckFailure_Type = Counter32
_AlServerCheckFailure_Object = MibTableColumn
alServerCheckFailure = _AlServerCheckFailure_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 24),
    _AlServerCheckFailure_Type()
)
alServerCheckFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerCheckFailure.setStatus("current")
_AlServerCheckDown_Type = Counter32
_AlServerCheckDown_Object = MibTableColumn
alServerCheckDown = _AlServerCheckDown_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 25),
    _AlServerCheckDown_Type()
)
alServerCheckDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerCheckDown.setStatus("current")
_AlServerDownTime_Type = Counter32
_AlServerDownTime_Object = MibTableColumn
alServerDownTime = _AlServerDownTime_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 26),
    _AlServerDownTime_Type()
)
alServerDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerDownTime.setStatus("current")


class _AlServerThrottle_Type(Integer32):
    """Custom type alServerThrottle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlServerThrottle_Type.__name__ = "Integer32"
_AlServerThrottle_Object = MibTableColumn
alServerThrottle = _AlServerThrottle_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 3, 4, 1, 27),
    _AlServerThrottle_Type()
)
alServerThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alServerThrottle.setStatus("current")
_AlL4Stats_ObjectIdentity = ObjectIdentity
alL4Stats = _AlL4Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4)
)
_AlL4ProcessTable_Object = MibTable
alL4ProcessTable = _AlL4ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alL4ProcessTable.setStatus("current")
_AlL4ProcessTableEntry_Object = MibTableRow
alL4ProcessTableEntry = _AlL4ProcessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 1, 1)
)
alL4ProcessTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alL4ProcessID"),
)
if mibBuilder.loadTexts:
    alL4ProcessTableEntry.setStatus("current")


class _AlL4ProcessID_Type(Integer32):
    """Custom type alL4ProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlL4ProcessID_Type.__name__ = "Integer32"
_AlL4ProcessID_Object = MibTableColumn
alL4ProcessID = _AlL4ProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 1, 1, 1),
    _AlL4ProcessID_Type()
)
alL4ProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ProcessID.setStatus("current")
_AlL4DirectorTable_Object = MibTable
alL4DirectorTable = _AlL4DirectorTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    alL4DirectorTable.setStatus("current")
_AlL4DirectorTableEntry_Object = MibTableRow
alL4DirectorTableEntry = _AlL4DirectorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1)
)
alL4DirectorTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alL4DirectorProcessID"),
    (0, "EXCELIANCE-MIB", "alL4DirectorID"),
)
if mibBuilder.loadTexts:
    alL4DirectorTableEntry.setStatus("current")


class _AlL4DirectorProcessID_Type(Integer32):
    """Custom type alL4DirectorProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlL4DirectorProcessID_Type.__name__ = "Integer32"
_AlL4DirectorProcessID_Object = MibTableColumn
alL4DirectorProcessID = _AlL4DirectorProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 1),
    _AlL4DirectorProcessID_Type()
)
alL4DirectorProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorProcessID.setStatus("current")


class _AlL4DirectorID_Type(Integer32):
    """Custom type alL4DirectorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlL4DirectorID_Type.__name__ = "Integer32"
_AlL4DirectorID_Object = MibTableColumn
alL4DirectorID = _AlL4DirectorID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 2),
    _AlL4DirectorID_Type()
)
alL4DirectorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorID.setStatus("current")


class _AlL4DirectorName_Type(OctetString):
    """Custom type alL4DirectorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlL4DirectorName_Type.__name__ = "OctetString"
_AlL4DirectorName_Object = MibTableColumn
alL4DirectorName = _AlL4DirectorName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 3),
    _AlL4DirectorName_Type()
)
alL4DirectorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorName.setStatus("current")
_AlL4DirectorSessionCur_Type = Counter32
_AlL4DirectorSessionCur_Object = MibTableColumn
alL4DirectorSessionCur = _AlL4DirectorSessionCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 4),
    _AlL4DirectorSessionCur_Type()
)
alL4DirectorSessionCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorSessionCur.setStatus("current")
_AlL4DirectorSessionTotal_Type = Counter32
_AlL4DirectorSessionTotal_Object = MibTableColumn
alL4DirectorSessionTotal = _AlL4DirectorSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 5),
    _AlL4DirectorSessionTotal_Type()
)
alL4DirectorSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorSessionTotal.setStatus("current")
_AlL4DirectorPacketsIN_Type = Counter32
_AlL4DirectorPacketsIN_Object = MibTableColumn
alL4DirectorPacketsIN = _AlL4DirectorPacketsIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 6),
    _AlL4DirectorPacketsIN_Type()
)
alL4DirectorPacketsIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorPacketsIN.setStatus("current")
_AlL4DirectorPacketsOUT_Type = Counter32
_AlL4DirectorPacketsOUT_Object = MibTableColumn
alL4DirectorPacketsOUT = _AlL4DirectorPacketsOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 7),
    _AlL4DirectorPacketsOUT_Type()
)
alL4DirectorPacketsOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorPacketsOUT.setStatus("current")
_AlL4DirectorBytesIN_Type = Counter64
_AlL4DirectorBytesIN_Object = MibTableColumn
alL4DirectorBytesIN = _AlL4DirectorBytesIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 8),
    _AlL4DirectorBytesIN_Type()
)
alL4DirectorBytesIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorBytesIN.setStatus("current")
_AlL4DirectorBytesOUT_Type = Counter64
_AlL4DirectorBytesOUT_Object = MibTableColumn
alL4DirectorBytesOUT = _AlL4DirectorBytesOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 9),
    _AlL4DirectorBytesOUT_Type()
)
alL4DirectorBytesOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorBytesOUT.setStatus("current")


class _AlL4DirectorStatus_Type(OctetString):
    """Custom type alL4DirectorStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlL4DirectorStatus_Type.__name__ = "OctetString"
_AlL4DirectorStatus_Object = MibTableColumn
alL4DirectorStatus = _AlL4DirectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 2, 1, 10),
    _AlL4DirectorStatus_Type()
)
alL4DirectorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4DirectorStatus.setStatus("current")
_AlL4ServerTable_Object = MibTable
alL4ServerTable = _AlL4ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    alL4ServerTable.setStatus("current")
_AlL4ServerTableEntry_Object = MibTableRow
alL4ServerTableEntry = _AlL4ServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1)
)
alL4ServerTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alL4ServerProcessID"),
    (0, "EXCELIANCE-MIB", "alL4ServerDirectorID"),
    (0, "EXCELIANCE-MIB", "alL4ServerID"),
)
if mibBuilder.loadTexts:
    alL4ServerTableEntry.setStatus("current")


class _AlL4ServerProcessID_Type(Integer32):
    """Custom type alL4ServerProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlL4ServerProcessID_Type.__name__ = "Integer32"
_AlL4ServerProcessID_Object = MibTableColumn
alL4ServerProcessID = _AlL4ServerProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 1),
    _AlL4ServerProcessID_Type()
)
alL4ServerProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerProcessID.setStatus("current")


class _AlL4ServerDirectorID_Type(Integer32):
    """Custom type alL4ServerDirectorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlL4ServerDirectorID_Type.__name__ = "Integer32"
_AlL4ServerDirectorID_Object = MibTableColumn
alL4ServerDirectorID = _AlL4ServerDirectorID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 2),
    _AlL4ServerDirectorID_Type()
)
alL4ServerDirectorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerDirectorID.setStatus("current")


class _AlL4ServerID_Type(Integer32):
    """Custom type alL4ServerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlL4ServerID_Type.__name__ = "Integer32"
_AlL4ServerID_Object = MibTableColumn
alL4ServerID = _AlL4ServerID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 3),
    _AlL4ServerID_Type()
)
alL4ServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerID.setStatus("current")


class _AlL4ServerName_Type(OctetString):
    """Custom type alL4ServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlL4ServerName_Type.__name__ = "OctetString"
_AlL4ServerName_Object = MibTableColumn
alL4ServerName = _AlL4ServerName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 4),
    _AlL4ServerName_Type()
)
alL4ServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerName.setStatus("current")
_AlL4ServerSessionCur_Type = Counter32
_AlL4ServerSessionCur_Object = MibTableColumn
alL4ServerSessionCur = _AlL4ServerSessionCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 5),
    _AlL4ServerSessionCur_Type()
)
alL4ServerSessionCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerSessionCur.setStatus("current")
_AlL4ServerSessionTotal_Type = Counter32
_AlL4ServerSessionTotal_Object = MibTableColumn
alL4ServerSessionTotal = _AlL4ServerSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 6),
    _AlL4ServerSessionTotal_Type()
)
alL4ServerSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerSessionTotal.setStatus("current")
_AlL4ServerPacketsIN_Type = Counter32
_AlL4ServerPacketsIN_Object = MibTableColumn
alL4ServerPacketsIN = _AlL4ServerPacketsIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 7),
    _AlL4ServerPacketsIN_Type()
)
alL4ServerPacketsIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerPacketsIN.setStatus("current")
_AlL4ServerPacketsOUT_Type = Counter32
_AlL4ServerPacketsOUT_Object = MibTableColumn
alL4ServerPacketsOUT = _AlL4ServerPacketsOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 8),
    _AlL4ServerPacketsOUT_Type()
)
alL4ServerPacketsOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerPacketsOUT.setStatus("current")
_AlL4ServerBytesIN_Type = Counter64
_AlL4ServerBytesIN_Object = MibTableColumn
alL4ServerBytesIN = _AlL4ServerBytesIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 9),
    _AlL4ServerBytesIN_Type()
)
alL4ServerBytesIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerBytesIN.setStatus("current")
_AlL4ServerBytesOUT_Type = Counter64
_AlL4ServerBytesOUT_Object = MibTableColumn
alL4ServerBytesOUT = _AlL4ServerBytesOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 10),
    _AlL4ServerBytesOUT_Type()
)
alL4ServerBytesOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerBytesOUT.setStatus("current")


class _AlL4ServerStatus_Type(OctetString):
    """Custom type alL4ServerStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlL4ServerStatus_Type.__name__ = "OctetString"
_AlL4ServerStatus_Object = MibTableColumn
alL4ServerStatus = _AlL4ServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 11),
    _AlL4ServerStatus_Type()
)
alL4ServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerStatus.setStatus("current")
_AlL4ServerWeight_Type = Counter32
_AlL4ServerWeight_Object = MibTableColumn
alL4ServerWeight = _AlL4ServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 12),
    _AlL4ServerWeight_Type()
)
alL4ServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerWeight.setStatus("current")


class _AlL4ServerActive_Type(Integer32):
    """Custom type alL4ServerActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlL4ServerActive_Type.__name__ = "Integer32"
_AlL4ServerActive_Object = MibTableColumn
alL4ServerActive = _AlL4ServerActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 13),
    _AlL4ServerActive_Type()
)
alL4ServerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerActive.setStatus("current")


class _AlL4ServerBackup_Type(Integer32):
    """Custom type alL4ServerBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlL4ServerBackup_Type.__name__ = "Integer32"
_AlL4ServerBackup_Object = MibTableColumn
alL4ServerBackup = _AlL4ServerBackup_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 4, 3, 1, 14),
    _AlL4ServerBackup_Type()
)
alL4ServerBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL4ServerBackup.setStatus("current")
_AlHardwareInfo_ObjectIdentity = ObjectIdentity
alHardwareInfo = _AlHardwareInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 5)
)


class _AlHardwareModel_Type(OctetString):
    """Custom type alHardwareModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlHardwareModel_Type.__name__ = "OctetString"
_AlHardwareModel_Object = MibScalar
alHardwareModel = _AlHardwareModel_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 5, 1),
    _AlHardwareModel_Type()
)
alHardwareModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareModel.setStatus("current")


class _AlHardwareUUID_Type(OctetString):
    """Custom type alHardwareUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlHardwareUUID_Type.__name__ = "OctetString"
_AlHardwareUUID_Object = MibScalar
alHardwareUUID = _AlHardwareUUID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 5, 2),
    _AlHardwareUUID_Type()
)
alHardwareUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareUUID.setStatus("current")


class _AlHardwareETHID_Type(OctetString):
    """Custom type alHardwareETHID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlHardwareETHID_Type.__name__ = "OctetString"
_AlHardwareETHID_Object = MibScalar
alHardwareETHID = _AlHardwareETHID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 5, 3),
    _AlHardwareETHID_Type()
)
alHardwareETHID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareETHID.setStatus("current")
_AlPshieldStats_ObjectIdentity = ObjectIdentity
alPshieldStats = _AlPshieldStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6)
)
_AlPshieldInstanceTable_Object = MibTable
alPshieldInstanceTable = _AlPshieldInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alPshieldInstanceTable.setStatus("current")
_AlPshieldInstanceTableEntry_Object = MibTableRow
alPshieldInstanceTableEntry = _AlPshieldInstanceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1)
)
alPshieldInstanceTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alPshieldInstanceID"),
)
if mibBuilder.loadTexts:
    alPshieldInstanceTableEntry.setStatus("current")


class _AlPshieldInstanceID_Type(Integer32):
    """Custom type alPshieldInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlPshieldInstanceID_Type.__name__ = "Integer32"
_AlPshieldInstanceID_Object = MibTableColumn
alPshieldInstanceID = _AlPshieldInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 1),
    _AlPshieldInstanceID_Type()
)
alPshieldInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceID.setStatus("current")


class _AlPshieldInstanceName_Type(OctetString):
    """Custom type alPshieldInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlPshieldInstanceName_Type.__name__ = "OctetString"
_AlPshieldInstanceName_Object = MibTableColumn
alPshieldInstanceName = _AlPshieldInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 2),
    _AlPshieldInstanceName_Type()
)
alPshieldInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceName.setStatus("current")
_AlPshieldInstanceRxTotal_Type = Counter64
_AlPshieldInstanceRxTotal_Object = MibTableColumn
alPshieldInstanceRxTotal = _AlPshieldInstanceRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 3),
    _AlPshieldInstanceRxTotal_Type()
)
alPshieldInstanceRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceRxTotal.setStatus("current")
_AlPshieldInstanceRxTotL3B_Type = Counter64
_AlPshieldInstanceRxTotL3B_Object = MibTableColumn
alPshieldInstanceRxTotL3B = _AlPshieldInstanceRxTotL3B_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 4),
    _AlPshieldInstanceRxTotL3B_Type()
)
alPshieldInstanceRxTotL3B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceRxTotL3B.setStatus("current")
_AlPshieldInstanceRxTotL1b_Type = Counter64
_AlPshieldInstanceRxTotL1b_Object = MibTableColumn
alPshieldInstanceRxTotL1b = _AlPshieldInstanceRxTotL1b_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 5),
    _AlPshieldInstanceRxTotL1b_Type()
)
alPshieldInstanceRxTotL1b.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceRxTotL1b.setStatus("current")
_AlPshieldInstanceCaptureMissed_Type = Counter64
_AlPshieldInstanceCaptureMissed_Object = MibTableColumn
alPshieldInstanceCaptureMissed = _AlPshieldInstanceCaptureMissed_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 6),
    _AlPshieldInstanceCaptureMissed_Type()
)
alPshieldInstanceCaptureMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceCaptureMissed.setStatus("current")
_AlPshieldInstanceDelivered_Type = Counter64
_AlPshieldInstanceDelivered_Object = MibTableColumn
alPshieldInstanceDelivered = _AlPshieldInstanceDelivered_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 7),
    _AlPshieldInstanceDelivered_Type()
)
alPshieldInstanceDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceDelivered.setStatus("current")
_AlPshieldInstanceDelivL3B_Type = Counter64
_AlPshieldInstanceDelivL3B_Object = MibTableColumn
alPshieldInstanceDelivL3B = _AlPshieldInstanceDelivL3B_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 8),
    _AlPshieldInstanceDelivL3B_Type()
)
alPshieldInstanceDelivL3B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceDelivL3B.setStatus("current")
_AlPshieldInstanceDelivL1b_Type = Counter64
_AlPshieldInstanceDelivL1b_Object = MibTableColumn
alPshieldInstanceDelivL1b = _AlPshieldInstanceDelivL1b_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 9),
    _AlPshieldInstanceDelivL1b_Type()
)
alPshieldInstanceDelivL1b.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceDelivL1b.setStatus("current")
_AlPshieldInstanceResponses_Type = Counter64
_AlPshieldInstanceResponses_Object = MibTableColumn
alPshieldInstanceResponses = _AlPshieldInstanceResponses_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 10),
    _AlPshieldInstanceResponses_Type()
)
alPshieldInstanceResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceResponses.setStatus("current")
_AlPshieldInstanceTxTotal_Type = Counter64
_AlPshieldInstanceTxTotal_Object = MibTableColumn
alPshieldInstanceTxTotal = _AlPshieldInstanceTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 11),
    _AlPshieldInstanceTxTotal_Type()
)
alPshieldInstanceTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceTxTotal.setStatus("current")
_AlPshieldInstanceSessionMax_Type = Gauge32
_AlPshieldInstanceSessionMax_Object = MibTableColumn
alPshieldInstanceSessionMax = _AlPshieldInstanceSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 12),
    _AlPshieldInstanceSessionMax_Type()
)
alPshieldInstanceSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionMax.setStatus("current")
_AlPshieldInstanceSessionOutgoing_Type = Gauge32
_AlPshieldInstanceSessionOutgoing_Object = MibTableColumn
alPshieldInstanceSessionOutgoing = _AlPshieldInstanceSessionOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 13),
    _AlPshieldInstanceSessionOutgoing_Type()
)
alPshieldInstanceSessionOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionOutgoing.setStatus("current")
_AlPshieldInstanceSessionUpload_Type = Gauge32
_AlPshieldInstanceSessionUpload_Object = MibTableColumn
alPshieldInstanceSessionUpload = _AlPshieldInstanceSessionUpload_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 14),
    _AlPshieldInstanceSessionUpload_Type()
)
alPshieldInstanceSessionUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionUpload.setStatus("current")
_AlPshieldInstanceSessionIncoming_Type = Gauge32
_AlPshieldInstanceSessionIncoming_Object = MibTableColumn
alPshieldInstanceSessionIncoming = _AlPshieldInstanceSessionIncoming_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 15),
    _AlPshieldInstanceSessionIncoming_Type()
)
alPshieldInstanceSessionIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionIncoming.setStatus("current")
_AlPshieldInstanceSessionTotActive_Type = Gauge32
_AlPshieldInstanceSessionTotActive_Object = MibTableColumn
alPshieldInstanceSessionTotActive = _AlPshieldInstanceSessionTotActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 16),
    _AlPshieldInstanceSessionTotActive_Type()
)
alPshieldInstanceSessionTotActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionTotActive.setStatus("current")
_AlPshieldInstanceSessionSynActive_Type = Gauge32
_AlPshieldInstanceSessionSynActive_Object = MibTableColumn
alPshieldInstanceSessionSynActive = _AlPshieldInstanceSessionSynActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 17),
    _AlPshieldInstanceSessionSynActive_Type()
)
alPshieldInstanceSessionSynActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionSynActive.setStatus("current")
_AlPshieldInstanceSessionRstActive_Type = Gauge32
_AlPshieldInstanceSessionRstActive_Object = MibTableColumn
alPshieldInstanceSessionRstActive = _AlPshieldInstanceSessionRstActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 18),
    _AlPshieldInstanceSessionRstActive_Type()
)
alPshieldInstanceSessionRstActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionRstActive.setStatus("current")
_AlPshieldInstanceSessionAckActive_Type = Gauge32
_AlPshieldInstanceSessionAckActive_Object = MibTableColumn
alPshieldInstanceSessionAckActive = _AlPshieldInstanceSessionAckActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 19),
    _AlPshieldInstanceSessionAckActive_Type()
)
alPshieldInstanceSessionAckActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionAckActive.setStatus("current")
_AlPshieldInstanceSessionDnsActive_Type = Gauge32
_AlPshieldInstanceSessionDnsActive_Object = MibTableColumn
alPshieldInstanceSessionDnsActive = _AlPshieldInstanceSessionDnsActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 20),
    _AlPshieldInstanceSessionDnsActive_Type()
)
alPshieldInstanceSessionDnsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionDnsActive.setStatus("current")
_AlPshieldInstanceSessionOutActive_Type = Gauge32
_AlPshieldInstanceSessionOutActive_Object = MibTableColumn
alPshieldInstanceSessionOutActive = _AlPshieldInstanceSessionOutActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 21),
    _AlPshieldInstanceSessionOutActive_Type()
)
alPshieldInstanceSessionOutActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionOutActive.setStatus("current")
_AlPshieldInstanceSessionRetransmit_Type = Gauge32
_AlPshieldInstanceSessionRetransmit_Object = MibTableColumn
alPshieldInstanceSessionRetransmit = _AlPshieldInstanceSessionRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 22),
    _AlPshieldInstanceSessionRetransmit_Type()
)
alPshieldInstanceSessionRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionRetransmit.setStatus("current")
_AlPshieldInstanceSessionForcedHash_Type = Integer32
_AlPshieldInstanceSessionForcedHash_Object = MibTableColumn
alPshieldInstanceSessionForcedHash = _AlPshieldInstanceSessionForcedHash_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 23),
    _AlPshieldInstanceSessionForcedHash_Type()
)
alPshieldInstanceSessionForcedHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionForcedHash.setStatus("current")
_AlPshieldInstanceSessionForcedKernel_Type = Integer32
_AlPshieldInstanceSessionForcedKernel_Object = MibTableColumn
alPshieldInstanceSessionForcedKernel = _AlPshieldInstanceSessionForcedKernel_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 1, 1, 24),
    _AlPshieldInstanceSessionForcedKernel_Type()
)
alPshieldInstanceSessionForcedKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldInstanceSessionForcedKernel.setStatus("current")
_AlPshieldContextTable_Object = MibTable
alPshieldContextTable = _AlPshieldContextTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    alPshieldContextTable.setStatus("current")
_AlPshieldContextTableEntry_Object = MibTableRow
alPshieldContextTableEntry = _AlPshieldContextTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1)
)
alPshieldContextTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "alPshieldContextInstanceID"),
    (0, "EXCELIANCE-MIB", "alPshieldContextID"),
)
if mibBuilder.loadTexts:
    alPshieldContextTableEntry.setStatus("current")


class _AlPshieldContextInstanceID_Type(Integer32):
    """Custom type alPshieldContextInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlPshieldContextInstanceID_Type.__name__ = "Integer32"
_AlPshieldContextInstanceID_Object = MibTableColumn
alPshieldContextInstanceID = _AlPshieldContextInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 1),
    _AlPshieldContextInstanceID_Type()
)
alPshieldContextInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextInstanceID.setStatus("current")


class _AlPshieldContextID_Type(Integer32):
    """Custom type alPshieldContextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlPshieldContextID_Type.__name__ = "Integer32"
_AlPshieldContextID_Object = MibTableColumn
alPshieldContextID = _AlPshieldContextID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 2),
    _AlPshieldContextID_Type()
)
alPshieldContextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextID.setStatus("current")


class _AlPshieldContextName_Type(OctetString):
    """Custom type alPshieldContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlPshieldContextName_Type.__name__ = "OctetString"
_AlPshieldContextName_Object = MibTableColumn
alPshieldContextName = _AlPshieldContextName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 3),
    _AlPshieldContextName_Type()
)
alPshieldContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextName.setStatus("current")


class _AlPshieldContextStatus_Type(Bits):
    """Custom type alPshieldContextStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("syncookie", 1),
          ("unkownttl", 2),
          ("unmatched", 4),
          ("surge", 8))
    )

_AlPshieldContextStatus_Type.__name__ = "Bits"
_AlPshieldContextStatus_Object = MibTableColumn
alPshieldContextStatus = _AlPshieldContextStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 4),
    _AlPshieldContextStatus_Type()
)
alPshieldContextStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextStatus.setStatus("current")
_AlPshieldContextRxTotal_Type = Counter64
_AlPshieldContextRxTotal_Object = MibTableColumn
alPshieldContextRxTotal = _AlPshieldContextRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 5),
    _AlPshieldContextRxTotal_Type()
)
alPshieldContextRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextRxTotal.setStatus("current")
_AlPshieldContextInvalid_Type = Counter64
_AlPshieldContextInvalid_Object = MibTableColumn
alPshieldContextInvalid = _AlPshieldContextInvalid_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 6),
    _AlPshieldContextInvalid_Type()
)
alPshieldContextInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextInvalid.setStatus("current")
_AlPshieldContextWhitelisted_Type = Counter64
_AlPshieldContextWhitelisted_Object = MibTableColumn
alPshieldContextWhitelisted = _AlPshieldContextWhitelisted_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 7),
    _AlPshieldContextWhitelisted_Type()
)
alPshieldContextWhitelisted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextWhitelisted.setStatus("current")
_AlPshieldContextFiltered_Type = Counter64
_AlPshieldContextFiltered_Object = MibTableColumn
alPshieldContextFiltered = _AlPshieldContextFiltered_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 8),
    _AlPshieldContextFiltered_Type()
)
alPshieldContextFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextFiltered.setStatus("current")
_AlPshieldContextOutRelated_Type = Counter64
_AlPshieldContextOutRelated_Object = MibTableColumn
alPshieldContextOutRelated = _AlPshieldContextOutRelated_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 9),
    _AlPshieldContextOutRelated_Type()
)
alPshieldContextOutRelated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextOutRelated.setStatus("current")
_AlPshieldContextDnsResponses_Type = Counter64
_AlPshieldContextDnsResponses_Object = MibTableColumn
alPshieldContextDnsResponses = _AlPshieldContextDnsResponses_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 10),
    _AlPshieldContextDnsResponses_Type()
)
alPshieldContextDnsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextDnsResponses.setStatus("current")
_AlPshieldContextSyn_Type = Counter64
_AlPshieldContextSyn_Object = MibTableColumn
alPshieldContextSyn = _AlPshieldContextSyn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 11),
    _AlPshieldContextSyn_Type()
)
alPshieldContextSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextSyn.setStatus("current")
_AlPshieldContextRst_Type = Counter64
_AlPshieldContextRst_Object = MibTableColumn
alPshieldContextRst = _AlPshieldContextRst_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 12),
    _AlPshieldContextRst_Type()
)
alPshieldContextRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextRst.setStatus("current")
_AlPshieldContextAck_Type = Counter64
_AlPshieldContextAck_Object = MibTableColumn
alPshieldContextAck = _AlPshieldContextAck_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 13),
    _AlPshieldContextAck_Type()
)
alPshieldContextAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextAck.setStatus("current")
_AlPshieldContextUnknownTtl_Type = Counter64
_AlPshieldContextUnknownTtl_Object = MibTableColumn
alPshieldContextUnknownTtl = _AlPshieldContextUnknownTtl_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 14),
    _AlPshieldContextUnknownTtl_Type()
)
alPshieldContextUnknownTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextUnknownTtl.setStatus("current")
_AlPshieldContextTtlFiltered_Type = Counter64
_AlPshieldContextTtlFiltered_Object = MibTableColumn
alPshieldContextTtlFiltered = _AlPshieldContextTtlFiltered_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 15),
    _AlPshieldContextTtlFiltered_Type()
)
alPshieldContextTtlFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextTtlFiltered.setStatus("current")
_AlPshieldContextEstablished_Type = Counter64
_AlPshieldContextEstablished_Object = MibTableColumn
alPshieldContextEstablished = _AlPshieldContextEstablished_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 16),
    _AlPshieldContextEstablished_Type()
)
alPshieldContextEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextEstablished.setStatus("current")
_AlPshieldContextNewConnections_Type = Counter64
_AlPshieldContextNewConnections_Object = MibTableColumn
alPshieldContextNewConnections = _AlPshieldContextNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 17),
    _AlPshieldContextNewConnections_Type()
)
alPshieldContextNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextNewConnections.setStatus("current")
_AlPshieldContextUnmatched_Type = Counter64
_AlPshieldContextUnmatched_Object = MibTableColumn
alPshieldContextUnmatched = _AlPshieldContextUnmatched_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 18),
    _AlPshieldContextUnmatched_Type()
)
alPshieldContextUnmatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextUnmatched.setStatus("current")
_AlPshieldContextSynCookie_Type = Counter64
_AlPshieldContextSynCookie_Object = MibTableColumn
alPshieldContextSynCookie = _AlPshieldContextSynCookie_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 19),
    _AlPshieldContextSynCookie_Type()
)
alPshieldContextSynCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextSynCookie.setStatus("current")
_AlPshieldContextDropSyn_Type = Counter64
_AlPshieldContextDropSyn_Object = MibTableColumn
alPshieldContextDropSyn = _AlPshieldContextDropSyn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 20),
    _AlPshieldContextDropSyn_Type()
)
alPshieldContextDropSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextDropSyn.setStatus("current")
_AlPshieldContextDropRst_Type = Counter64
_AlPshieldContextDropRst_Object = MibTableColumn
alPshieldContextDropRst = _AlPshieldContextDropRst_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 21),
    _AlPshieldContextDropRst_Type()
)
alPshieldContextDropRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextDropRst.setStatus("current")
_AlPshieldContextDropAck_Type = Counter64
_AlPshieldContextDropAck_Object = MibTableColumn
alPshieldContextDropAck = _AlPshieldContextDropAck_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 22),
    _AlPshieldContextDropAck_Type()
)
alPshieldContextDropAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextDropAck.setStatus("current")
_AlPshieldContextDelivered_Type = Counter64
_AlPshieldContextDelivered_Object = MibTableColumn
alPshieldContextDelivered = _AlPshieldContextDelivered_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 23),
    _AlPshieldContextDelivered_Type()
)
alPshieldContextDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextDelivered.setStatus("current")
_AlPshieldContextTxTotal_Type = Counter64
_AlPshieldContextTxTotal_Object = MibTableColumn
alPshieldContextTxTotal = _AlPshieldContextTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 1, 6, 2, 1, 24),
    _AlPshieldContextTxTotal_Type()
)
alPshieldContextTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPshieldContextTxTotal.setStatus("current")
_Algroups_ObjectIdentity = ObjectIdentity
algroups = _Algroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2)
)
_Hapee_ObjectIdentity = ObjectIdentity
hapee = _Hapee_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3)
)
_Lbcompat1_ObjectIdentity = ObjectIdentity
lbcompat1 = _Lbcompat1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1)
)
_LbProductInfo_ObjectIdentity = ObjectIdentity
lbProductInfo = _LbProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 1)
)
_LbStats_ObjectIdentity = ObjectIdentity
lbStats = _LbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3)
)
_LbProcessTable_Object = MibTable
lbProcessTable = _LbProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lbProcessTable.setStatus("current")
_LbProcessTableEntry_Object = MibTableRow
lbProcessTableEntry = _LbProcessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1)
)
lbProcessTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "lbProcessID"),
)
if mibBuilder.loadTexts:
    lbProcessTableEntry.setStatus("current")


class _LbProcessID_Type(Integer32):
    """Custom type lbProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessID_Type.__name__ = "Integer32"
_LbProcessID_Object = MibTableColumn
lbProcessID = _LbProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 1),
    _LbProcessID_Type()
)
lbProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessID.setStatus("current")


class _LbProcessVersion_Type(OctetString):
    """Custom type lbProcessVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbProcessVersion_Type.__name__ = "OctetString"
_LbProcessVersion_Object = MibTableColumn
lbProcessVersion = _LbProcessVersion_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 2),
    _LbProcessVersion_Type()
)
lbProcessVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessVersion.setStatus("current")


class _LbProcessReleaseDate_Type(OctetString):
    """Custom type lbProcessReleaseDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbProcessReleaseDate_Type.__name__ = "OctetString"
_LbProcessReleaseDate_Object = MibTableColumn
lbProcessReleaseDate = _LbProcessReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 3),
    _LbProcessReleaseDate_Type()
)
lbProcessReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessReleaseDate.setStatus("current")


class _LbProcessNbProc_Type(Integer32):
    """Custom type lbProcessNbProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessNbProc_Type.__name__ = "Integer32"
_LbProcessNbProc_Object = MibTableColumn
lbProcessNbProc = _LbProcessNbProc_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 4),
    _LbProcessNbProc_Type()
)
lbProcessNbProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessNbProc.setStatus("current")


class _LbProcessProductName_Type(OctetString):
    """Custom type lbProcessProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbProcessProductName_Type.__name__ = "OctetString"
_LbProcessProductName_Object = MibTableColumn
lbProcessProductName = _LbProcessProductName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 5),
    _LbProcessProductName_Type()
)
lbProcessProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessProductName.setStatus("current")


class _LbProcessSystemPID_Type(Integer32):
    """Custom type lbProcessSystemPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessSystemPID_Type.__name__ = "Integer32"
_LbProcessSystemPID_Object = MibTableColumn
lbProcessSystemPID = _LbProcessSystemPID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 6),
    _LbProcessSystemPID_Type()
)
lbProcessSystemPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSystemPID.setStatus("current")


class _LbProcessUptime_Type(OctetString):
    """Custom type lbProcessUptime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbProcessUptime_Type.__name__ = "OctetString"
_LbProcessUptime_Object = MibTableColumn
lbProcessUptime = _LbProcessUptime_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 7),
    _LbProcessUptime_Type()
)
lbProcessUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessUptime.setStatus("current")


class _LbProcessUptimeSec_Type(Integer32):
    """Custom type lbProcessUptimeSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessUptimeSec_Type.__name__ = "Integer32"
_LbProcessUptimeSec_Object = MibTableColumn
lbProcessUptimeSec = _LbProcessUptimeSec_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 8),
    _LbProcessUptimeSec_Type()
)
lbProcessUptimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessUptimeSec.setStatus("current")


class _LbProcessMemMax_Type(Integer32):
    """Custom type lbProcessMemMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMemMax_Type.__name__ = "Integer32"
_LbProcessMemMax_Object = MibTableColumn
lbProcessMemMax = _LbProcessMemMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 9),
    _LbProcessMemMax_Type()
)
lbProcessMemMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMemMax.setStatus("current")


class _LbProcessPoolAlloc_Type(Integer32):
    """Custom type lbProcessPoolAlloc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessPoolAlloc_Type.__name__ = "Integer32"
_LbProcessPoolAlloc_Object = MibTableColumn
lbProcessPoolAlloc = _LbProcessPoolAlloc_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 10),
    _LbProcessPoolAlloc_Type()
)
lbProcessPoolAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessPoolAlloc.setStatus("current")


class _LbProcessPoolUsed_Type(Integer32):
    """Custom type lbProcessPoolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessPoolUsed_Type.__name__ = "Integer32"
_LbProcessPoolUsed_Object = MibTableColumn
lbProcessPoolUsed = _LbProcessPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 11),
    _LbProcessPoolUsed_Type()
)
lbProcessPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessPoolUsed.setStatus("current")
_LbProcessPoolFailed_Type = Counter32
_LbProcessPoolFailed_Object = MibTableColumn
lbProcessPoolFailed = _LbProcessPoolFailed_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 12),
    _LbProcessPoolFailed_Type()
)
lbProcessPoolFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessPoolFailed.setStatus("current")


class _LbProcessUlimitn_Type(Integer32):
    """Custom type lbProcessUlimitn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessUlimitn_Type.__name__ = "Integer32"
_LbProcessUlimitn_Object = MibTableColumn
lbProcessUlimitn = _LbProcessUlimitn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 13),
    _LbProcessUlimitn_Type()
)
lbProcessUlimitn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessUlimitn.setStatus("current")


class _LbProcessMaxSock_Type(Integer32):
    """Custom type lbProcessMaxSock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxSock_Type.__name__ = "Integer32"
_LbProcessMaxSock_Object = MibTableColumn
lbProcessMaxSock = _LbProcessMaxSock_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 14),
    _LbProcessMaxSock_Type()
)
lbProcessMaxSock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxSock.setStatus("current")


class _LbProcessMaxConn_Type(Integer32):
    """Custom type lbProcessMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxConn_Type.__name__ = "Integer32"
_LbProcessMaxConn_Object = MibTableColumn
lbProcessMaxConn = _LbProcessMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 15),
    _LbProcessMaxConn_Type()
)
lbProcessMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxConn.setStatus("current")


class _LbProcessHardMaxConn_Type(Integer32):
    """Custom type lbProcessHardMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessHardMaxConn_Type.__name__ = "Integer32"
_LbProcessHardMaxConn_Object = MibTableColumn
lbProcessHardMaxConn = _LbProcessHardMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 16),
    _LbProcessHardMaxConn_Type()
)
lbProcessHardMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessHardMaxConn.setStatus("current")


class _LbProcessCurConn_Type(Integer32):
    """Custom type lbProcessCurConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessCurConn_Type.__name__ = "Integer32"
_LbProcessCurConn_Object = MibTableColumn
lbProcessCurConn = _LbProcessCurConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 17),
    _LbProcessCurConn_Type()
)
lbProcessCurConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessCurConn.setStatus("current")
_LbProcessCumConn_Type = Counter32
_LbProcessCumConn_Object = MibTableColumn
lbProcessCumConn = _LbProcessCumConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 18),
    _LbProcessCumConn_Type()
)
lbProcessCumConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessCumConn.setStatus("current")
_LbProcessCumReq_Type = Counter32
_LbProcessCumReq_Object = MibTableColumn
lbProcessCumReq = _LbProcessCumReq_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 19),
    _LbProcessCumReq_Type()
)
lbProcessCumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessCumReq.setStatus("current")


class _LbProcessMaxSslConn_Type(Integer32):
    """Custom type lbProcessMaxSslConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxSslConn_Type.__name__ = "Integer32"
_LbProcessMaxSslConn_Object = MibTableColumn
lbProcessMaxSslConn = _LbProcessMaxSslConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 20),
    _LbProcessMaxSslConn_Type()
)
lbProcessMaxSslConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxSslConn.setStatus("current")


class _LbProcessCurSslConn_Type(Integer32):
    """Custom type lbProcessCurSslConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessCurSslConn_Type.__name__ = "Integer32"
_LbProcessCurSslConn_Object = MibTableColumn
lbProcessCurSslConn = _LbProcessCurSslConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 21),
    _LbProcessCurSslConn_Type()
)
lbProcessCurSslConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessCurSslConn.setStatus("current")
_LbProcessCumSslConn_Type = Counter32
_LbProcessCumSslConn_Object = MibTableColumn
lbProcessCumSslConn = _LbProcessCumSslConn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 22),
    _LbProcessCumSslConn_Type()
)
lbProcessCumSslConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessCumSslConn.setStatus("current")


class _LbProcessMaxPipes_Type(Integer32):
    """Custom type lbProcessMaxPipes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxPipes_Type.__name__ = "Integer32"
_LbProcessMaxPipes_Object = MibTableColumn
lbProcessMaxPipes = _LbProcessMaxPipes_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 23),
    _LbProcessMaxPipes_Type()
)
lbProcessMaxPipes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxPipes.setStatus("current")


class _LbProcessPipesUsed_Type(Integer32):
    """Custom type lbProcessPipesUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessPipesUsed_Type.__name__ = "Integer32"
_LbProcessPipesUsed_Object = MibTableColumn
lbProcessPipesUsed = _LbProcessPipesUsed_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 24),
    _LbProcessPipesUsed_Type()
)
lbProcessPipesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessPipesUsed.setStatus("current")


class _LbProcessPipesFree_Type(Integer32):
    """Custom type lbProcessPipesFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessPipesFree_Type.__name__ = "Integer32"
_LbProcessPipesFree_Object = MibTableColumn
lbProcessPipesFree = _LbProcessPipesFree_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 25),
    _LbProcessPipesFree_Type()
)
lbProcessPipesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessPipesFree.setStatus("current")


class _LbProcessConnRate_Type(Integer32):
    """Custom type lbProcessConnRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessConnRate_Type.__name__ = "Integer32"
_LbProcessConnRate_Object = MibTableColumn
lbProcessConnRate = _LbProcessConnRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 26),
    _LbProcessConnRate_Type()
)
lbProcessConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessConnRate.setStatus("current")


class _LbProcessConnRateLimit_Type(Integer32):
    """Custom type lbProcessConnRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessConnRateLimit_Type.__name__ = "Integer32"
_LbProcessConnRateLimit_Object = MibTableColumn
lbProcessConnRateLimit = _LbProcessConnRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 27),
    _LbProcessConnRateLimit_Type()
)
lbProcessConnRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessConnRateLimit.setStatus("current")


class _LbProcessMaxConnRate_Type(Integer32):
    """Custom type lbProcessMaxConnRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxConnRate_Type.__name__ = "Integer32"
_LbProcessMaxConnRate_Object = MibTableColumn
lbProcessMaxConnRate = _LbProcessMaxConnRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 28),
    _LbProcessMaxConnRate_Type()
)
lbProcessMaxConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxConnRate.setStatus("current")


class _LbProcessSessRate_Type(Integer32):
    """Custom type lbProcessSessRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessSessRate_Type.__name__ = "Integer32"
_LbProcessSessRate_Object = MibTableColumn
lbProcessSessRate = _LbProcessSessRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 29),
    _LbProcessSessRate_Type()
)
lbProcessSessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSessRate.setStatus("current")


class _LbProcessSessRateLimit_Type(Integer32):
    """Custom type lbProcessSessRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessSessRateLimit_Type.__name__ = "Integer32"
_LbProcessSessRateLimit_Object = MibTableColumn
lbProcessSessRateLimit = _LbProcessSessRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 30),
    _LbProcessSessRateLimit_Type()
)
lbProcessSessRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSessRateLimit.setStatus("current")


class _LbProcessMaxSessRate_Type(Integer32):
    """Custom type lbProcessMaxSessRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxSessRate_Type.__name__ = "Integer32"
_LbProcessMaxSessRate_Object = MibTableColumn
lbProcessMaxSessRate = _LbProcessMaxSessRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 31),
    _LbProcessMaxSessRate_Type()
)
lbProcessMaxSessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxSessRate.setStatus("current")


class _LbProcessSslRate_Type(Integer32):
    """Custom type lbProcessSslRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessSslRate_Type.__name__ = "Integer32"
_LbProcessSslRate_Object = MibTableColumn
lbProcessSslRate = _LbProcessSslRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 32),
    _LbProcessSslRate_Type()
)
lbProcessSslRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSslRate.setStatus("current")


class _LbProcessSslRateLimit_Type(Integer32):
    """Custom type lbProcessSslRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessSslRateLimit_Type.__name__ = "Integer32"
_LbProcessSslRateLimit_Object = MibTableColumn
lbProcessSslRateLimit = _LbProcessSslRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 33),
    _LbProcessSslRateLimit_Type()
)
lbProcessSslRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSslRateLimit.setStatus("current")


class _LbProcessMaxSslRate_Type(Integer32):
    """Custom type lbProcessMaxSslRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxSslRate_Type.__name__ = "Integer32"
_LbProcessMaxSslRate_Object = MibTableColumn
lbProcessMaxSslRate = _LbProcessMaxSslRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 34),
    _LbProcessMaxSslRate_Type()
)
lbProcessMaxSslRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxSslRate.setStatus("current")


class _LbProcessSslFrontendKeyRate_Type(Integer32):
    """Custom type lbProcessSslFrontendKeyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessSslFrontendKeyRate_Type.__name__ = "Integer32"
_LbProcessSslFrontendKeyRate_Object = MibTableColumn
lbProcessSslFrontendKeyRate = _LbProcessSslFrontendKeyRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 35),
    _LbProcessSslFrontendKeyRate_Type()
)
lbProcessSslFrontendKeyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSslFrontendKeyRate.setStatus("current")


class _LbProcessMaxSslFrontendKeyRate_Type(Integer32):
    """Custom type lbProcessMaxSslFrontendKeyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxSslFrontendKeyRate_Type.__name__ = "Integer32"
_LbProcessMaxSslFrontendKeyRate_Object = MibTableColumn
lbProcessMaxSslFrontendKeyRate = _LbProcessMaxSslFrontendKeyRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 36),
    _LbProcessMaxSslFrontendKeyRate_Type()
)
lbProcessMaxSslFrontendKeyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxSslFrontendKeyRate.setStatus("current")


class _LbProcessSslFrontendSessReuse_Type(Integer32):
    """Custom type lbProcessSslFrontendSessReuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessSslFrontendSessReuse_Type.__name__ = "Integer32"
_LbProcessSslFrontendSessReuse_Object = MibTableColumn
lbProcessSslFrontendSessReuse = _LbProcessSslFrontendSessReuse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 37),
    _LbProcessSslFrontendSessReuse_Type()
)
lbProcessSslFrontendSessReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSslFrontendSessReuse.setStatus("current")


class _LbProcessSslBackendKeyRate_Type(Integer32):
    """Custom type lbProcessSslBackendKeyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessSslBackendKeyRate_Type.__name__ = "Integer32"
_LbProcessSslBackendKeyRate_Object = MibTableColumn
lbProcessSslBackendKeyRate = _LbProcessSslBackendKeyRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 38),
    _LbProcessSslBackendKeyRate_Type()
)
lbProcessSslBackendKeyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSslBackendKeyRate.setStatus("current")


class _LbProcessMaxSslBackendKeyRate_Type(Integer32):
    """Custom type lbProcessMaxSslBackendKeyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxSslBackendKeyRate_Type.__name__ = "Integer32"
_LbProcessMaxSslBackendKeyRate_Object = MibTableColumn
lbProcessMaxSslBackendKeyRate = _LbProcessMaxSslBackendKeyRate_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 39),
    _LbProcessMaxSslBackendKeyRate_Type()
)
lbProcessMaxSslBackendKeyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxSslBackendKeyRate.setStatus("current")
_LbProcessSslCacheLookups_Type = Counter32
_LbProcessSslCacheLookups_Object = MibTableColumn
lbProcessSslCacheLookups = _LbProcessSslCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 40),
    _LbProcessSslCacheLookups_Type()
)
lbProcessSslCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSslCacheLookups.setStatus("current")
_LbProcessSslCacheMisses_Type = Counter32
_LbProcessSslCacheMisses_Object = MibTableColumn
lbProcessSslCacheMisses = _LbProcessSslCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 41),
    _LbProcessSslCacheMisses_Type()
)
lbProcessSslCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessSslCacheMisses.setStatus("current")


class _LbProcessCompressBpsIn_Type(Integer32):
    """Custom type lbProcessCompressBpsIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessCompressBpsIn_Type.__name__ = "Integer32"
_LbProcessCompressBpsIn_Object = MibTableColumn
lbProcessCompressBpsIn = _LbProcessCompressBpsIn_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 42),
    _LbProcessCompressBpsIn_Type()
)
lbProcessCompressBpsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessCompressBpsIn.setStatus("current")


class _LbProcessCompressBpsOut_Type(Integer32):
    """Custom type lbProcessCompressBpsOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessCompressBpsOut_Type.__name__ = "Integer32"
_LbProcessCompressBpsOut_Object = MibTableColumn
lbProcessCompressBpsOut = _LbProcessCompressBpsOut_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 43),
    _LbProcessCompressBpsOut_Type()
)
lbProcessCompressBpsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessCompressBpsOut.setStatus("current")


class _LbProcessCompressRateLimit_Type(Integer32):
    """Custom type lbProcessCompressRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessCompressRateLimit_Type.__name__ = "Integer32"
_LbProcessCompressRateLimit_Object = MibTableColumn
lbProcessCompressRateLimit = _LbProcessCompressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 44),
    _LbProcessCompressRateLimit_Type()
)
lbProcessCompressRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessCompressRateLimit.setStatus("current")


class _LbProcessZlibMemUsage_Type(Integer32):
    """Custom type lbProcessZlibMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessZlibMemUsage_Type.__name__ = "Integer32"
_LbProcessZlibMemUsage_Object = MibTableColumn
lbProcessZlibMemUsage = _LbProcessZlibMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 45),
    _LbProcessZlibMemUsage_Type()
)
lbProcessZlibMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessZlibMemUsage.setStatus("current")


class _LbProcessMaxZlibMemUsage_Type(Integer32):
    """Custom type lbProcessMaxZlibMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessMaxZlibMemUsage_Type.__name__ = "Integer32"
_LbProcessMaxZlibMemUsage_Object = MibTableColumn
lbProcessMaxZlibMemUsage = _LbProcessMaxZlibMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 46),
    _LbProcessMaxZlibMemUsage_Type()
)
lbProcessMaxZlibMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessMaxZlibMemUsage.setStatus("current")


class _LbProcessTasks_Type(Integer32):
    """Custom type lbProcessTasks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessTasks_Type.__name__ = "Integer32"
_LbProcessTasks_Object = MibTableColumn
lbProcessTasks = _LbProcessTasks_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 47),
    _LbProcessTasks_Type()
)
lbProcessTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessTasks.setStatus("current")


class _LbProcessRunQueue_Type(Integer32):
    """Custom type lbProcessRunQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessRunQueue_Type.__name__ = "Integer32"
_LbProcessRunQueue_Object = MibTableColumn
lbProcessRunQueue = _LbProcessRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 48),
    _LbProcessRunQueue_Type()
)
lbProcessRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessRunQueue.setStatus("current")


class _LbProcessIdle_Type(Integer32):
    """Custom type lbProcessIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbProcessIdle_Type.__name__ = "Integer32"
_LbProcessIdle_Object = MibTableColumn
lbProcessIdle = _LbProcessIdle_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 49),
    _LbProcessIdle_Type()
)
lbProcessIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessIdle.setStatus("current")


class _LbProcessNodeName_Type(OctetString):
    """Custom type lbProcessNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbProcessNodeName_Type.__name__ = "OctetString"
_LbProcessNodeName_Object = MibTableColumn
lbProcessNodeName = _LbProcessNodeName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 50),
    _LbProcessNodeName_Type()
)
lbProcessNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessNodeName.setStatus("current")


class _LbProcessDescription_Type(OctetString):
    """Custom type lbProcessDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbProcessDescription_Type.__name__ = "OctetString"
_LbProcessDescription_Object = MibTableColumn
lbProcessDescription = _LbProcessDescription_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 1, 1, 51),
    _LbProcessDescription_Type()
)
lbProcessDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbProcessDescription.setStatus("current")
_LbFrontendTable_Object = MibTable
lbFrontendTable = _LbFrontendTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lbFrontendTable.setStatus("current")
_LbFrontendTableEntry_Object = MibTableRow
lbFrontendTableEntry = _LbFrontendTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1)
)
lbFrontendTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "lbFrontendProcessID"),
    (0, "EXCELIANCE-MIB", "lbFrontendID"),
)
if mibBuilder.loadTexts:
    lbFrontendTableEntry.setStatus("current")


class _LbFrontendProcessID_Type(Integer32):
    """Custom type lbFrontendProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbFrontendProcessID_Type.__name__ = "Integer32"
_LbFrontendProcessID_Object = MibTableColumn
lbFrontendProcessID = _LbFrontendProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 1),
    _LbFrontendProcessID_Type()
)
lbFrontendProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendProcessID.setStatus("current")


class _LbFrontendID_Type(Integer32):
    """Custom type lbFrontendID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbFrontendID_Type.__name__ = "Integer32"
_LbFrontendID_Object = MibTableColumn
lbFrontendID = _LbFrontendID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 2),
    _LbFrontendID_Type()
)
lbFrontendID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendID.setStatus("current")


class _LbFrontendName_Type(OctetString):
    """Custom type lbFrontendName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbFrontendName_Type.__name__ = "OctetString"
_LbFrontendName_Object = MibTableColumn
lbFrontendName = _LbFrontendName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 3),
    _LbFrontendName_Type()
)
lbFrontendName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendName.setStatus("current")
_LbFrontendSessionCur_Type = Counter64
_LbFrontendSessionCur_Object = MibTableColumn
lbFrontendSessionCur = _LbFrontendSessionCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 4),
    _LbFrontendSessionCur_Type()
)
lbFrontendSessionCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendSessionCur.setStatus("current")
_LbFrontendSessionMax_Type = Counter64
_LbFrontendSessionMax_Object = MibTableColumn
lbFrontendSessionMax = _LbFrontendSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 5),
    _LbFrontendSessionMax_Type()
)
lbFrontendSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendSessionMax.setStatus("current")
_LbFrontendSessionLimit_Type = Counter64
_LbFrontendSessionLimit_Object = MibTableColumn
lbFrontendSessionLimit = _LbFrontendSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 6),
    _LbFrontendSessionLimit_Type()
)
lbFrontendSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendSessionLimit.setStatus("current")
_LbFrontendSessionTotal_Type = Counter64
_LbFrontendSessionTotal_Object = MibTableColumn
lbFrontendSessionTotal = _LbFrontendSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 7),
    _LbFrontendSessionTotal_Type()
)
lbFrontendSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendSessionTotal.setStatus("current")
_LbFrontendBytesIN_Type = Counter64
_LbFrontendBytesIN_Object = MibTableColumn
lbFrontendBytesIN = _LbFrontendBytesIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 8),
    _LbFrontendBytesIN_Type()
)
lbFrontendBytesIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendBytesIN.setStatus("current")
_LbFrontendBytesOUT_Type = Counter64
_LbFrontendBytesOUT_Object = MibTableColumn
lbFrontendBytesOUT = _LbFrontendBytesOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 9),
    _LbFrontendBytesOUT_Type()
)
lbFrontendBytesOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendBytesOUT.setStatus("current")
_LbFrontendErrorRequest_Type = Counter64
_LbFrontendErrorRequest_Object = MibTableColumn
lbFrontendErrorRequest = _LbFrontendErrorRequest_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 10),
    _LbFrontendErrorRequest_Type()
)
lbFrontendErrorRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendErrorRequest.setStatus("current")
_LbFrontendDenyRequest_Type = Counter64
_LbFrontendDenyRequest_Object = MibTableColumn
lbFrontendDenyRequest = _LbFrontendDenyRequest_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 11),
    _LbFrontendDenyRequest_Type()
)
lbFrontendDenyRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendDenyRequest.setStatus("current")
_LbFrontendDenyResponse_Type = Counter64
_LbFrontendDenyResponse_Object = MibTableColumn
lbFrontendDenyResponse = _LbFrontendDenyResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 12),
    _LbFrontendDenyResponse_Type()
)
lbFrontendDenyResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendDenyResponse.setStatus("current")


class _LbFrontendStatus_Type(OctetString):
    """Custom type lbFrontendStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbFrontendStatus_Type.__name__ = "OctetString"
_LbFrontendStatus_Object = MibTableColumn
lbFrontendStatus = _LbFrontendStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 2, 1, 13),
    _LbFrontendStatus_Type()
)
lbFrontendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFrontendStatus.setStatus("current")
_LbBackendTable_Object = MibTable
lbBackendTable = _LbBackendTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lbBackendTable.setStatus("current")
_LbBackendTableEntry_Object = MibTableRow
lbBackendTableEntry = _LbBackendTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1)
)
lbBackendTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "lbBackendProcessID"),
    (0, "EXCELIANCE-MIB", "lbBackendID"),
)
if mibBuilder.loadTexts:
    lbBackendTableEntry.setStatus("current")


class _LbBackendProcessID_Type(Integer32):
    """Custom type lbBackendProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbBackendProcessID_Type.__name__ = "Integer32"
_LbBackendProcessID_Object = MibTableColumn
lbBackendProcessID = _LbBackendProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 1),
    _LbBackendProcessID_Type()
)
lbBackendProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendProcessID.setStatus("current")


class _LbBackendID_Type(Integer32):
    """Custom type lbBackendID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbBackendID_Type.__name__ = "Integer32"
_LbBackendID_Object = MibTableColumn
lbBackendID = _LbBackendID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 2),
    _LbBackendID_Type()
)
lbBackendID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendID.setStatus("current")


class _LbBackendName_Type(OctetString):
    """Custom type lbBackendName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbBackendName_Type.__name__ = "OctetString"
_LbBackendName_Object = MibTableColumn
lbBackendName = _LbBackendName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 3),
    _LbBackendName_Type()
)
lbBackendName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendName.setStatus("current")
_LbBackendQueueCur_Type = Counter64
_LbBackendQueueCur_Object = MibTableColumn
lbBackendQueueCur = _LbBackendQueueCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 4),
    _LbBackendQueueCur_Type()
)
lbBackendQueueCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendQueueCur.setStatus("current")
_LbBackendQueueMax_Type = Counter64
_LbBackendQueueMax_Object = MibTableColumn
lbBackendQueueMax = _LbBackendQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 5),
    _LbBackendQueueMax_Type()
)
lbBackendQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendQueueMax.setStatus("current")
_LbBackendQueueLimit_Type = Counter64
_LbBackendQueueLimit_Object = MibTableColumn
lbBackendQueueLimit = _LbBackendQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 6),
    _LbBackendQueueLimit_Type()
)
lbBackendQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendQueueLimit.setStatus("current")
_LbBackendSessionCur_Type = Counter64
_LbBackendSessionCur_Object = MibTableColumn
lbBackendSessionCur = _LbBackendSessionCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 7),
    _LbBackendSessionCur_Type()
)
lbBackendSessionCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendSessionCur.setStatus("current")
_LbBackendSessionMax_Type = Counter64
_LbBackendSessionMax_Object = MibTableColumn
lbBackendSessionMax = _LbBackendSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 8),
    _LbBackendSessionMax_Type()
)
lbBackendSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendSessionMax.setStatus("current")
_LbBackendSessionLimit_Type = Counter64
_LbBackendSessionLimit_Object = MibTableColumn
lbBackendSessionLimit = _LbBackendSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 9),
    _LbBackendSessionLimit_Type()
)
lbBackendSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendSessionLimit.setStatus("current")
_LbBackendSessionTotal_Type = Counter64
_LbBackendSessionTotal_Object = MibTableColumn
lbBackendSessionTotal = _LbBackendSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 10),
    _LbBackendSessionTotal_Type()
)
lbBackendSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendSessionTotal.setStatus("current")
_LbBackendSessionLoadBalanced_Type = Counter64
_LbBackendSessionLoadBalanced_Object = MibTableColumn
lbBackendSessionLoadBalanced = _LbBackendSessionLoadBalanced_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 11),
    _LbBackendSessionLoadBalanced_Type()
)
lbBackendSessionLoadBalanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendSessionLoadBalanced.setStatus("current")
_LbBackendBytesIN_Type = Counter64
_LbBackendBytesIN_Object = MibTableColumn
lbBackendBytesIN = _LbBackendBytesIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 12),
    _LbBackendBytesIN_Type()
)
lbBackendBytesIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendBytesIN.setStatus("current")
_LbBackendBytesOUT_Type = Counter64
_LbBackendBytesOUT_Object = MibTableColumn
lbBackendBytesOUT = _LbBackendBytesOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 13),
    _LbBackendBytesOUT_Type()
)
lbBackendBytesOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendBytesOUT.setStatus("current")
_LbBackendErrorConnection_Type = Counter64
_LbBackendErrorConnection_Object = MibTableColumn
lbBackendErrorConnection = _LbBackendErrorConnection_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 14),
    _LbBackendErrorConnection_Type()
)
lbBackendErrorConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendErrorConnection.setStatus("current")
_LbBackendErrorResponse_Type = Counter64
_LbBackendErrorResponse_Object = MibTableColumn
lbBackendErrorResponse = _LbBackendErrorResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 15),
    _LbBackendErrorResponse_Type()
)
lbBackendErrorResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendErrorResponse.setStatus("current")
_LbBackendDenyRequest_Type = Counter64
_LbBackendDenyRequest_Object = MibTableColumn
lbBackendDenyRequest = _LbBackendDenyRequest_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 16),
    _LbBackendDenyRequest_Type()
)
lbBackendDenyRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendDenyRequest.setStatus("current")
_LbBackendDenyResponse_Type = Counter64
_LbBackendDenyResponse_Object = MibTableColumn
lbBackendDenyResponse = _LbBackendDenyResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 17),
    _LbBackendDenyResponse_Type()
)
lbBackendDenyResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendDenyResponse.setStatus("current")
_LbBackendWarningRetry_Type = Counter64
_LbBackendWarningRetry_Object = MibTableColumn
lbBackendWarningRetry = _LbBackendWarningRetry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 18),
    _LbBackendWarningRetry_Type()
)
lbBackendWarningRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendWarningRetry.setStatus("current")
_LbBackendWarningRedispatch_Type = Counter64
_LbBackendWarningRedispatch_Object = MibTableColumn
lbBackendWarningRedispatch = _LbBackendWarningRedispatch_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 19),
    _LbBackendWarningRedispatch_Type()
)
lbBackendWarningRedispatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendWarningRedispatch.setStatus("current")


class _LbBackendStatus_Type(OctetString):
    """Custom type lbBackendStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbBackendStatus_Type.__name__ = "OctetString"
_LbBackendStatus_Object = MibTableColumn
lbBackendStatus = _LbBackendStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 20),
    _LbBackendStatus_Type()
)
lbBackendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendStatus.setStatus("current")
_LbBackendLastChange_Type = Counter32
_LbBackendLastChange_Object = MibTableColumn
lbBackendLastChange = _LbBackendLastChange_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 21),
    _LbBackendLastChange_Type()
)
lbBackendLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendLastChange.setStatus("current")
_LbBackendCheckDown_Type = Counter32
_LbBackendCheckDown_Object = MibTableColumn
lbBackendCheckDown = _LbBackendCheckDown_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 22),
    _LbBackendCheckDown_Type()
)
lbBackendCheckDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendCheckDown.setStatus("current")
_LbBackendDownTime_Type = Counter32
_LbBackendDownTime_Object = MibTableColumn
lbBackendDownTime = _LbBackendDownTime_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 3, 1, 23),
    _LbBackendDownTime_Type()
)
lbBackendDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBackendDownTime.setStatus("current")
_LbServerTable_Object = MibTable
lbServerTable = _LbServerTable_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lbServerTable.setStatus("current")
_LbServerTableEntry_Object = MibTableRow
lbServerTableEntry = _LbServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1)
)
lbServerTableEntry.setIndexNames(
    (0, "EXCELIANCE-MIB", "lbServerProcessID"),
    (0, "EXCELIANCE-MIB", "lbServerBackendID"),
    (0, "EXCELIANCE-MIB", "lbServerID"),
)
if mibBuilder.loadTexts:
    lbServerTableEntry.setStatus("current")


class _LbServerProcessID_Type(Integer32):
    """Custom type lbServerProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbServerProcessID_Type.__name__ = "Integer32"
_LbServerProcessID_Object = MibTableColumn
lbServerProcessID = _LbServerProcessID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 1),
    _LbServerProcessID_Type()
)
lbServerProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerProcessID.setStatus("current")


class _LbServerBackendID_Type(Integer32):
    """Custom type lbServerBackendID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbServerBackendID_Type.__name__ = "Integer32"
_LbServerBackendID_Object = MibTableColumn
lbServerBackendID = _LbServerBackendID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 2),
    _LbServerBackendID_Type()
)
lbServerBackendID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerBackendID.setStatus("current")


class _LbServerID_Type(Integer32):
    """Custom type lbServerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbServerID_Type.__name__ = "Integer32"
_LbServerID_Object = MibTableColumn
lbServerID = _LbServerID_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 3),
    _LbServerID_Type()
)
lbServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerID.setStatus("current")


class _LbServerName_Type(OctetString):
    """Custom type lbServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbServerName_Type.__name__ = "OctetString"
_LbServerName_Object = MibTableColumn
lbServerName = _LbServerName_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 4),
    _LbServerName_Type()
)
lbServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerName.setStatus("current")
_LbServerQueueCur_Type = Counter64
_LbServerQueueCur_Object = MibTableColumn
lbServerQueueCur = _LbServerQueueCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 5),
    _LbServerQueueCur_Type()
)
lbServerQueueCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerQueueCur.setStatus("current")
_LbServerQueueMax_Type = Counter64
_LbServerQueueMax_Object = MibTableColumn
lbServerQueueMax = _LbServerQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 6),
    _LbServerQueueMax_Type()
)
lbServerQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerQueueMax.setStatus("current")
_LbServerQueueLimit_Type = Counter64
_LbServerQueueLimit_Object = MibTableColumn
lbServerQueueLimit = _LbServerQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 7),
    _LbServerQueueLimit_Type()
)
lbServerQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerQueueLimit.setStatus("current")
_LbServerSessionCur_Type = Counter64
_LbServerSessionCur_Object = MibTableColumn
lbServerSessionCur = _LbServerSessionCur_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 8),
    _LbServerSessionCur_Type()
)
lbServerSessionCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerSessionCur.setStatus("current")
_LbServerSessionMax_Type = Counter64
_LbServerSessionMax_Object = MibTableColumn
lbServerSessionMax = _LbServerSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 9),
    _LbServerSessionMax_Type()
)
lbServerSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerSessionMax.setStatus("current")
_LbServerSessionLimit_Type = Counter64
_LbServerSessionLimit_Object = MibTableColumn
lbServerSessionLimit = _LbServerSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 10),
    _LbServerSessionLimit_Type()
)
lbServerSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerSessionLimit.setStatus("current")
_LbServerSessionTotal_Type = Counter64
_LbServerSessionTotal_Object = MibTableColumn
lbServerSessionTotal = _LbServerSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 11),
    _LbServerSessionTotal_Type()
)
lbServerSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerSessionTotal.setStatus("current")
_LbServerSessionLoadBalanced_Type = Counter64
_LbServerSessionLoadBalanced_Object = MibTableColumn
lbServerSessionLoadBalanced = _LbServerSessionLoadBalanced_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 12),
    _LbServerSessionLoadBalanced_Type()
)
lbServerSessionLoadBalanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerSessionLoadBalanced.setStatus("current")
_LbServerBytesIN_Type = Counter64
_LbServerBytesIN_Object = MibTableColumn
lbServerBytesIN = _LbServerBytesIN_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 13),
    _LbServerBytesIN_Type()
)
lbServerBytesIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerBytesIN.setStatus("current")
_LbServerBytesOUT_Type = Counter64
_LbServerBytesOUT_Object = MibTableColumn
lbServerBytesOUT = _LbServerBytesOUT_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 14),
    _LbServerBytesOUT_Type()
)
lbServerBytesOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerBytesOUT.setStatus("current")
_LbServerErrorConnection_Type = Counter64
_LbServerErrorConnection_Object = MibTableColumn
lbServerErrorConnection = _LbServerErrorConnection_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 15),
    _LbServerErrorConnection_Type()
)
lbServerErrorConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerErrorConnection.setStatus("current")
_LbServerErrorResponse_Type = Counter64
_LbServerErrorResponse_Object = MibTableColumn
lbServerErrorResponse = _LbServerErrorResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 16),
    _LbServerErrorResponse_Type()
)
lbServerErrorResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerErrorResponse.setStatus("current")
_LbServerDenyResponse_Type = Counter64
_LbServerDenyResponse_Object = MibTableColumn
lbServerDenyResponse = _LbServerDenyResponse_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 17),
    _LbServerDenyResponse_Type()
)
lbServerDenyResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerDenyResponse.setStatus("current")
_LbServerWarningRetry_Type = Counter64
_LbServerWarningRetry_Object = MibTableColumn
lbServerWarningRetry = _LbServerWarningRetry_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 18),
    _LbServerWarningRetry_Type()
)
lbServerWarningRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerWarningRetry.setStatus("current")


class _LbServerStatus_Type(OctetString):
    """Custom type lbServerStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_LbServerStatus_Type.__name__ = "OctetString"
_LbServerStatus_Object = MibTableColumn
lbServerStatus = _LbServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 19),
    _LbServerStatus_Type()
)
lbServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerStatus.setStatus("current")
_LbServerLastChange_Type = Counter32
_LbServerLastChange_Object = MibTableColumn
lbServerLastChange = _LbServerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 20),
    _LbServerLastChange_Type()
)
lbServerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerLastChange.setStatus("current")
_LbServerWeight_Type = Counter32
_LbServerWeight_Object = MibTableColumn
lbServerWeight = _LbServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 21),
    _LbServerWeight_Type()
)
lbServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerWeight.setStatus("current")


class _LbServerActive_Type(Integer32):
    """Custom type lbServerActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_LbServerActive_Type.__name__ = "Integer32"
_LbServerActive_Object = MibTableColumn
lbServerActive = _LbServerActive_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 22),
    _LbServerActive_Type()
)
lbServerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerActive.setStatus("current")


class _LbServerBackup_Type(Integer32):
    """Custom type lbServerBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_LbServerBackup_Type.__name__ = "Integer32"
_LbServerBackup_Object = MibTableColumn
lbServerBackup = _LbServerBackup_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 23),
    _LbServerBackup_Type()
)
lbServerBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerBackup.setStatus("current")
_LbServerCheckFailure_Type = Counter32
_LbServerCheckFailure_Object = MibTableColumn
lbServerCheckFailure = _LbServerCheckFailure_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 24),
    _LbServerCheckFailure_Type()
)
lbServerCheckFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerCheckFailure.setStatus("current")
_LbServerCheckDown_Type = Counter32
_LbServerCheckDown_Object = MibTableColumn
lbServerCheckDown = _LbServerCheckDown_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 25),
    _LbServerCheckDown_Type()
)
lbServerCheckDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerCheckDown.setStatus("current")
_LbServerDownTime_Type = Counter32
_LbServerDownTime_Object = MibTableColumn
lbServerDownTime = _LbServerDownTime_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 26),
    _LbServerDownTime_Type()
)
lbServerDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerDownTime.setStatus("current")


class _LbServerThrottle_Type(Integer32):
    """Custom type lbServerThrottle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LbServerThrottle_Type.__name__ = "Integer32"
_LbServerThrottle_Object = MibTableColumn
lbServerThrottle = _LbServerThrottle_Object(
    (1, 3, 6, 1, 4, 1, 23263, 4, 3, 1, 3, 4, 1, 27),
    _LbServerThrottle_Type()
)
lbServerThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbServerThrottle.setStatus("current")

# Managed Objects groups

landefObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 1, 2, 1)
)
landefObjectGroup.setObjects(
      *(("EXCELIANCE-MIB", "attackNumber"),
        ("EXCELIANCE-MIB", "acceptedPqts"),
        ("EXCELIANCE-MIB", "droppedPqts"),
        ("EXCELIANCE-MIB", "serviceName"),
        ("EXCELIANCE-MIB", "serviceStatus"),
        ("EXCELIANCE-MIB", "lastIP"),
        ("EXCELIANCE-MIB", "dnsName"),
        ("EXCELIANCE-MIB", "hostStatus"),
        ("EXCELIANCE-MIB", "os"),
        ("EXCELIANCE-MIB", "osDetails"),
        ("EXCELIANCE-MIB", "uptime"),
        ("EXCELIANCE-MIB", "netbiosName"),
        ("EXCELIANCE-MIB", "netbiosUser"),
        ("EXCELIANCE-MIB", "workgroup"),
        ("EXCELIANCE-MIB", "hostServer"),
        ("EXCELIANCE-MIB", "manufacturer"))
)
if mibBuilder.loadTexts:
    landefObjectGroup.setStatus("current")

alTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 2)
)
alTrapGroup.setObjects(
      *(("EXCELIANCE-MIB", "alTrapId"),
        ("EXCELIANCE-MIB", "alTrapMsg"),
        ("EXCELIANCE-MIB", "alTrapName"))
)
if mibBuilder.loadTexts:
    alTrapGroup.setStatus("current")

alProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 3)
)
alProductGroup.setObjects(
      *(("EXCELIANCE-MIB", "alProductName"),
        ("EXCELIANCE-MIB", "alProductModel"),
        ("EXCELIANCE-MIB", "alProductVersion"),
        ("EXCELIANCE-MIB", "alProductSubVersion"),
        ("EXCELIANCE-MIB", "alProductBuildVersion"),
        ("EXCELIANCE-MIB", "alProductBuildDate"),
        ("EXCELIANCE-MIB", "alProductURL"))
)
if mibBuilder.loadTexts:
    alProductGroup.setStatus("current")

alServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 4)
)
alServiceGroup.setObjects(
      *(("EXCELIANCE-MIB", "alServiceID"),
        ("EXCELIANCE-MIB", "alServiceName"),
        ("EXCELIANCE-MIB", "alServiceStatus"))
)
if mibBuilder.loadTexts:
    alServiceGroup.setStatus("current")

alInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 5)
)
alInstanceGroup.setObjects(
      *(("EXCELIANCE-MIB", "alInstanceServiceID"),
        ("EXCELIANCE-MIB", "alInstanceID"),
        ("EXCELIANCE-MIB", "alInstanceName"),
        ("EXCELIANCE-MIB", "alInstanceStatus"))
)
if mibBuilder.loadTexts:
    alInstanceGroup.setStatus("current")

alProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 6)
)
alProcessGroup.setObjects(
      *(("EXCELIANCE-MIB", "alProcessID"),
        ("EXCELIANCE-MIB", "alProcessVersion"),
        ("EXCELIANCE-MIB", "alProcessReleaseDate"),
        ("EXCELIANCE-MIB", "alProcessNbProc"),
        ("EXCELIANCE-MIB", "alProcessProductName"),
        ("EXCELIANCE-MIB", "alProcessSystemPID"),
        ("EXCELIANCE-MIB", "alProcessUptime"),
        ("EXCELIANCE-MIB", "alProcessUptimeSec"),
        ("EXCELIANCE-MIB", "alProcessMemMax"),
        ("EXCELIANCE-MIB", "alProcessPoolAlloc"),
        ("EXCELIANCE-MIB", "alProcessPoolUsed"),
        ("EXCELIANCE-MIB", "alProcessPoolFailed"),
        ("EXCELIANCE-MIB", "alProcessUlimitn"),
        ("EXCELIANCE-MIB", "alProcessMaxSock"),
        ("EXCELIANCE-MIB", "alProcessMaxConn"),
        ("EXCELIANCE-MIB", "alProcessHardMaxConn"),
        ("EXCELIANCE-MIB", "alProcessCurConn"),
        ("EXCELIANCE-MIB", "alProcessCumConn"),
        ("EXCELIANCE-MIB", "alProcessCumReq"),
        ("EXCELIANCE-MIB", "alProcessMaxSslConn"),
        ("EXCELIANCE-MIB", "alProcessCurSslConn"),
        ("EXCELIANCE-MIB", "alProcessCumSslConn"),
        ("EXCELIANCE-MIB", "alProcessMaxPipes"),
        ("EXCELIANCE-MIB", "alProcessPipesUsed"),
        ("EXCELIANCE-MIB", "alProcessPipesFree"),
        ("EXCELIANCE-MIB", "alProcessConnRate"),
        ("EXCELIANCE-MIB", "alProcessConnRateLimit"),
        ("EXCELIANCE-MIB", "alProcessMaxConnRate"),
        ("EXCELIANCE-MIB", "alProcessSessRate"),
        ("EXCELIANCE-MIB", "alProcessSessRateLimit"),
        ("EXCELIANCE-MIB", "alProcessMaxSessRate"),
        ("EXCELIANCE-MIB", "alProcessSslRate"),
        ("EXCELIANCE-MIB", "alProcessSslRateLimit"),
        ("EXCELIANCE-MIB", "alProcessMaxSslRate"),
        ("EXCELIANCE-MIB", "alProcessSslFrontendKeyRate"),
        ("EXCELIANCE-MIB", "alProcessMaxSslFrontendKeyRate"),
        ("EXCELIANCE-MIB", "alProcessSslFrontendSessReuse"),
        ("EXCELIANCE-MIB", "alProcessSslBackendKeyRate"),
        ("EXCELIANCE-MIB", "alProcessMaxSslBackendKeyRate"),
        ("EXCELIANCE-MIB", "alProcessSslCacheLookups"),
        ("EXCELIANCE-MIB", "alProcessSslCacheMisses"),
        ("EXCELIANCE-MIB", "alProcessCompressBpsIn"),
        ("EXCELIANCE-MIB", "alProcessCompressBpsOut"),
        ("EXCELIANCE-MIB", "alProcessCompressRateLimit"),
        ("EXCELIANCE-MIB", "alProcessZlibMemUsage"),
        ("EXCELIANCE-MIB", "alProcessMaxZlibMemUsage"),
        ("EXCELIANCE-MIB", "alProcessTasks"),
        ("EXCELIANCE-MIB", "alProcessRunQueue"),
        ("EXCELIANCE-MIB", "alProcessIdle"),
        ("EXCELIANCE-MIB", "alProcessNodeName"),
        ("EXCELIANCE-MIB", "alProcessDescription"))
)
if mibBuilder.loadTexts:
    alProcessGroup.setStatus("current")

alBackendGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 7)
)
alBackendGroup.setObjects(
      *(("EXCELIANCE-MIB", "alBackendProcessID"),
        ("EXCELIANCE-MIB", "alBackendID"),
        ("EXCELIANCE-MIB", "alBackendName"),
        ("EXCELIANCE-MIB", "alBackendQueueCur"),
        ("EXCELIANCE-MIB", "alBackendQueueMax"),
        ("EXCELIANCE-MIB", "alBackendQueueLimit"),
        ("EXCELIANCE-MIB", "alBackendSessionCur"),
        ("EXCELIANCE-MIB", "alBackendSessionMax"),
        ("EXCELIANCE-MIB", "alBackendSessionLimit"),
        ("EXCELIANCE-MIB", "alBackendSessionTotal"),
        ("EXCELIANCE-MIB", "alBackendSessionLoadBalanced"),
        ("EXCELIANCE-MIB", "alBackendBytesIN"),
        ("EXCELIANCE-MIB", "alBackendBytesOUT"),
        ("EXCELIANCE-MIB", "alBackendErrorConnection"),
        ("EXCELIANCE-MIB", "alBackendErrorResponse"),
        ("EXCELIANCE-MIB", "alBackendDenyRequest"),
        ("EXCELIANCE-MIB", "alBackendDenyResponse"),
        ("EXCELIANCE-MIB", "alBackendWarningRetry"),
        ("EXCELIANCE-MIB", "alBackendWarningRedispatch"),
        ("EXCELIANCE-MIB", "alBackendStatus"),
        ("EXCELIANCE-MIB", "alBackendLastChange"),
        ("EXCELIANCE-MIB", "alBackendCheckDown"),
        ("EXCELIANCE-MIB", "alBackendDownTime"))
)
if mibBuilder.loadTexts:
    alBackendGroup.setStatus("current")

alFrontendGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 8)
)
alFrontendGroup.setObjects(
      *(("EXCELIANCE-MIB", "alFrontendProcessID"),
        ("EXCELIANCE-MIB", "alFrontendID"),
        ("EXCELIANCE-MIB", "alFrontendName"),
        ("EXCELIANCE-MIB", "alFrontendSessionCur"),
        ("EXCELIANCE-MIB", "alFrontendSessionMax"),
        ("EXCELIANCE-MIB", "alFrontendSessionLimit"),
        ("EXCELIANCE-MIB", "alFrontendSessionTotal"),
        ("EXCELIANCE-MIB", "alFrontendBytesIN"),
        ("EXCELIANCE-MIB", "alFrontendBytesOUT"),
        ("EXCELIANCE-MIB", "alFrontendErrorRequest"),
        ("EXCELIANCE-MIB", "alFrontendDenyRequest"),
        ("EXCELIANCE-MIB", "alFrontendDenyResponse"),
        ("EXCELIANCE-MIB", "alFrontendStatus"))
)
if mibBuilder.loadTexts:
    alFrontendGroup.setStatus("current")

alServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 9)
)
alServerGroup.setObjects(
      *(("EXCELIANCE-MIB", "alServerProcessID"),
        ("EXCELIANCE-MIB", "alServerBackendID"),
        ("EXCELIANCE-MIB", "alServerID"),
        ("EXCELIANCE-MIB", "alServerName"),
        ("EXCELIANCE-MIB", "alServerQueueCur"),
        ("EXCELIANCE-MIB", "alServerQueueMax"),
        ("EXCELIANCE-MIB", "alServerQueueLimit"),
        ("EXCELIANCE-MIB", "alServerSessionCur"),
        ("EXCELIANCE-MIB", "alServerSessionMax"),
        ("EXCELIANCE-MIB", "alServerSessionLimit"),
        ("EXCELIANCE-MIB", "alServerSessionTotal"),
        ("EXCELIANCE-MIB", "alServerSessionLoadBalanced"),
        ("EXCELIANCE-MIB", "alServerBytesIN"),
        ("EXCELIANCE-MIB", "alServerBytesOUT"),
        ("EXCELIANCE-MIB", "alServerErrorConnection"),
        ("EXCELIANCE-MIB", "alServerErrorResponse"),
        ("EXCELIANCE-MIB", "alServerDenyResponse"),
        ("EXCELIANCE-MIB", "alServerWarningRetry"),
        ("EXCELIANCE-MIB", "alServerStatus"),
        ("EXCELIANCE-MIB", "alServerLastChange"),
        ("EXCELIANCE-MIB", "alServerWeight"),
        ("EXCELIANCE-MIB", "alServerActive"),
        ("EXCELIANCE-MIB", "alServerBackup"),
        ("EXCELIANCE-MIB", "alServerCheckFailure"),
        ("EXCELIANCE-MIB", "alServerCheckDown"),
        ("EXCELIANCE-MIB", "alServerDownTime"),
        ("EXCELIANCE-MIB", "alServerThrottle"))
)
if mibBuilder.loadTexts:
    alServerGroup.setStatus("current")

alL4ProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 10)
)
alL4ProcessGroup.setObjects(
    ("EXCELIANCE-MIB", "alL4ProcessID")
)
if mibBuilder.loadTexts:
    alL4ProcessGroup.setStatus("current")

alL4DirectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 11)
)
alL4DirectorGroup.setObjects(
      *(("EXCELIANCE-MIB", "alL4DirectorProcessID"),
        ("EXCELIANCE-MIB", "alL4DirectorID"),
        ("EXCELIANCE-MIB", "alL4DirectorName"),
        ("EXCELIANCE-MIB", "alL4DirectorSessionCur"),
        ("EXCELIANCE-MIB", "alL4DirectorSessionTotal"),
        ("EXCELIANCE-MIB", "alL4DirectorPacketsIN"),
        ("EXCELIANCE-MIB", "alL4DirectorPacketsOUT"),
        ("EXCELIANCE-MIB", "alL4DirectorBytesIN"),
        ("EXCELIANCE-MIB", "alL4DirectorBytesOUT"),
        ("EXCELIANCE-MIB", "alL4DirectorStatus"))
)
if mibBuilder.loadTexts:
    alL4DirectorGroup.setStatus("current")

alL4ServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 12)
)
alL4ServerGroup.setObjects(
      *(("EXCELIANCE-MIB", "alL4ServerProcessID"),
        ("EXCELIANCE-MIB", "alL4ServerDirectorID"),
        ("EXCELIANCE-MIB", "alL4ServerID"),
        ("EXCELIANCE-MIB", "alL4ServerName"),
        ("EXCELIANCE-MIB", "alL4ServerSessionCur"),
        ("EXCELIANCE-MIB", "alL4ServerSessionTotal"),
        ("EXCELIANCE-MIB", "alL4ServerPacketsIN"),
        ("EXCELIANCE-MIB", "alL4ServerPacketsOUT"),
        ("EXCELIANCE-MIB", "alL4ServerBytesIN"),
        ("EXCELIANCE-MIB", "alL4ServerBytesOUT"),
        ("EXCELIANCE-MIB", "alL4ServerStatus"),
        ("EXCELIANCE-MIB", "alL4ServerWeight"),
        ("EXCELIANCE-MIB", "alL4ServerActive"),
        ("EXCELIANCE-MIB", "alL4ServerBackup"))
)
if mibBuilder.loadTexts:
    alL4ServerGroup.setStatus("current")

alHardwareInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 13)
)
alHardwareInfoGroup.setObjects(
      *(("EXCELIANCE-MIB", "alHardwareModel"),
        ("EXCELIANCE-MIB", "alHardwareUUID"),
        ("EXCELIANCE-MIB", "alHardwareETHID"))
)
if mibBuilder.loadTexts:
    alHardwareInfoGroup.setStatus("current")

alPshieldInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 14)
)
alPshieldInstanceGroup.setObjects(
      *(("EXCELIANCE-MIB", "alPshieldInstanceID"),
        ("EXCELIANCE-MIB", "alPshieldInstanceName"),
        ("EXCELIANCE-MIB", "alPshieldInstanceRxTotal"),
        ("EXCELIANCE-MIB", "alPshieldInstanceRxTotL3B"),
        ("EXCELIANCE-MIB", "alPshieldInstanceRxTotL1b"),
        ("EXCELIANCE-MIB", "alPshieldInstanceCaptureMissed"),
        ("EXCELIANCE-MIB", "alPshieldInstanceDelivered"),
        ("EXCELIANCE-MIB", "alPshieldInstanceDelivL3B"),
        ("EXCELIANCE-MIB", "alPshieldInstanceDelivL1b"),
        ("EXCELIANCE-MIB", "alPshieldInstanceResponses"),
        ("EXCELIANCE-MIB", "alPshieldInstanceTxTotal"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionMax"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionOutgoing"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionUpload"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionIncoming"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionTotActive"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionSynActive"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionRstActive"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionAckActive"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionDnsActive"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionOutActive"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionRetransmit"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionForcedHash"),
        ("EXCELIANCE-MIB", "alPshieldInstanceSessionForcedKernel"))
)
if mibBuilder.loadTexts:
    alPshieldInstanceGroup.setStatus("current")

alPshieldContextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 15)
)
alPshieldContextGroup.setObjects(
      *(("EXCELIANCE-MIB", "alPshieldContextInstanceID"),
        ("EXCELIANCE-MIB", "alPshieldContextID"),
        ("EXCELIANCE-MIB", "alPshieldContextName"),
        ("EXCELIANCE-MIB", "alPshieldContextStatus"),
        ("EXCELIANCE-MIB", "alPshieldContextRxTotal"),
        ("EXCELIANCE-MIB", "alPshieldContextInvalid"),
        ("EXCELIANCE-MIB", "alPshieldContextWhitelisted"),
        ("EXCELIANCE-MIB", "alPshieldContextFiltered"),
        ("EXCELIANCE-MIB", "alPshieldContextOutRelated"),
        ("EXCELIANCE-MIB", "alPshieldContextDnsResponses"),
        ("EXCELIANCE-MIB", "alPshieldContextSyn"),
        ("EXCELIANCE-MIB", "alPshieldContextRst"),
        ("EXCELIANCE-MIB", "alPshieldContextAck"),
        ("EXCELIANCE-MIB", "alPshieldContextUnknownTtl"),
        ("EXCELIANCE-MIB", "alPshieldContextTtlFiltered"),
        ("EXCELIANCE-MIB", "alPshieldContextEstablished"),
        ("EXCELIANCE-MIB", "alPshieldContextNewConnections"),
        ("EXCELIANCE-MIB", "alPshieldContextUnmatched"),
        ("EXCELIANCE-MIB", "alPshieldContextSynCookie"),
        ("EXCELIANCE-MIB", "alPshieldContextDropSyn"),
        ("EXCELIANCE-MIB", "alPshieldContextDropRst"),
        ("EXCELIANCE-MIB", "alPshieldContextDropAck"),
        ("EXCELIANCE-MIB", "alPshieldContextDelivered"),
        ("EXCELIANCE-MIB", "alPshieldContextTxTotal"))
)
if mibBuilder.loadTexts:
    alPshieldContextGroup.setStatus("current")


# Notification objects

eNotificationMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23263, 3, 1001)
)
if mibBuilder.loadTexts:
    eNotificationMsg.setStatus(
        "current"
    )

alTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23263, 3, 1002)
)
alTrap.setObjects(
      *(("EXCELIANCE-MIB", "alTrapId"),
        ("EXCELIANCE-MIB", "alTrapMsg"),
        ("EXCELIANCE-MIB", "alTrapName"))
)
if mibBuilder.loadTexts:
    alTrap.setStatus(
        "current"
    )


# Notifications groups

alTrapNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 23263, 4, 2, 2, 1)
)
alTrapNotifGroup.setObjects(
      *(("EXCELIANCE-MIB", "eNotificationMsg"),
        ("EXCELIANCE-MIB", "alTrap"))
)
if mibBuilder.loadTexts:
    alTrapNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXCELIANCE-MIB",
    **{"exceliance": exceliance,
       "eTrapsObjects": eTrapsObjects,
       "alTrapId": alTrapId,
       "alTrapMsg": alTrapMsg,
       "alTrapName": alTrapName,
       "eTraps": eTraps,
       "eNotificationMsg": eNotificationMsg,
       "alTrap": alTrap,
       "products": products,
       "landef": landef,
       "compat1": compat1,
       "counters": counters,
       "attackNumber": attackNumber,
       "acceptedPqts": acceptedPqts,
       "droppedPqts": droppedPqts,
       "services": services,
       "serviceName": serviceName,
       "serviceStatus": serviceStatus,
       "hostInfos": hostInfos,
       "lastIP": lastIP,
       "dnsName": dnsName,
       "hostStatus": hostStatus,
       "os": os,
       "osDetails": osDetails,
       "uptime": uptime,
       "netbiosName": netbiosName,
       "netbiosUser": netbiosUser,
       "workgroup": workgroup,
       "hostServer": hostServer,
       "manufacturer": manufacturer,
       "landefgroups": landefgroups,
       "landefObjectGroup": landefObjectGroup,
       "aloha": aloha,
       "alcompat1": alcompat1,
       "alProductInfo": alProductInfo,
       "alProductName": alProductName,
       "alProductModel": alProductModel,
       "alProductVersion": alProductVersion,
       "alProductSubVersion": alProductSubVersion,
       "alProductBuildVersion": alProductBuildVersion,
       "alProductBuildDate": alProductBuildDate,
       "alProductURL": alProductURL,
       "alServices": alServices,
       "alServiceTable": alServiceTable,
       "alServiceTableEntry": alServiceTableEntry,
       "alServiceID": alServiceID,
       "alServiceName": alServiceName,
       "alServiceStatus": alServiceStatus,
       "alInstanceTable": alInstanceTable,
       "alInstanceTableEntry": alInstanceTableEntry,
       "alInstanceServiceID": alInstanceServiceID,
       "alInstanceID": alInstanceID,
       "alInstanceName": alInstanceName,
       "alInstanceStatus": alInstanceStatus,
       "alStats": alStats,
       "alProcessTable": alProcessTable,
       "alProcessTableEntry": alProcessTableEntry,
       "alProcessID": alProcessID,
       "alProcessVersion": alProcessVersion,
       "alProcessReleaseDate": alProcessReleaseDate,
       "alProcessNbProc": alProcessNbProc,
       "alProcessProductName": alProcessProductName,
       "alProcessSystemPID": alProcessSystemPID,
       "alProcessUptime": alProcessUptime,
       "alProcessUptimeSec": alProcessUptimeSec,
       "alProcessMemMax": alProcessMemMax,
       "alProcessPoolAlloc": alProcessPoolAlloc,
       "alProcessPoolUsed": alProcessPoolUsed,
       "alProcessPoolFailed": alProcessPoolFailed,
       "alProcessUlimitn": alProcessUlimitn,
       "alProcessMaxSock": alProcessMaxSock,
       "alProcessMaxConn": alProcessMaxConn,
       "alProcessHardMaxConn": alProcessHardMaxConn,
       "alProcessCurConn": alProcessCurConn,
       "alProcessCumConn": alProcessCumConn,
       "alProcessCumReq": alProcessCumReq,
       "alProcessMaxSslConn": alProcessMaxSslConn,
       "alProcessCurSslConn": alProcessCurSslConn,
       "alProcessCumSslConn": alProcessCumSslConn,
       "alProcessMaxPipes": alProcessMaxPipes,
       "alProcessPipesUsed": alProcessPipesUsed,
       "alProcessPipesFree": alProcessPipesFree,
       "alProcessConnRate": alProcessConnRate,
       "alProcessConnRateLimit": alProcessConnRateLimit,
       "alProcessMaxConnRate": alProcessMaxConnRate,
       "alProcessSessRate": alProcessSessRate,
       "alProcessSessRateLimit": alProcessSessRateLimit,
       "alProcessMaxSessRate": alProcessMaxSessRate,
       "alProcessSslRate": alProcessSslRate,
       "alProcessSslRateLimit": alProcessSslRateLimit,
       "alProcessMaxSslRate": alProcessMaxSslRate,
       "alProcessSslFrontendKeyRate": alProcessSslFrontendKeyRate,
       "alProcessMaxSslFrontendKeyRate": alProcessMaxSslFrontendKeyRate,
       "alProcessSslFrontendSessReuse": alProcessSslFrontendSessReuse,
       "alProcessSslBackendKeyRate": alProcessSslBackendKeyRate,
       "alProcessMaxSslBackendKeyRate": alProcessMaxSslBackendKeyRate,
       "alProcessSslCacheLookups": alProcessSslCacheLookups,
       "alProcessSslCacheMisses": alProcessSslCacheMisses,
       "alProcessCompressBpsIn": alProcessCompressBpsIn,
       "alProcessCompressBpsOut": alProcessCompressBpsOut,
       "alProcessCompressRateLimit": alProcessCompressRateLimit,
       "alProcessZlibMemUsage": alProcessZlibMemUsage,
       "alProcessMaxZlibMemUsage": alProcessMaxZlibMemUsage,
       "alProcessTasks": alProcessTasks,
       "alProcessRunQueue": alProcessRunQueue,
       "alProcessIdle": alProcessIdle,
       "alProcessNodeName": alProcessNodeName,
       "alProcessDescription": alProcessDescription,
       "alFrontendTable": alFrontendTable,
       "alFrontendTableEntry": alFrontendTableEntry,
       "alFrontendProcessID": alFrontendProcessID,
       "alFrontendID": alFrontendID,
       "alFrontendName": alFrontendName,
       "alFrontendSessionCur": alFrontendSessionCur,
       "alFrontendSessionMax": alFrontendSessionMax,
       "alFrontendSessionLimit": alFrontendSessionLimit,
       "alFrontendSessionTotal": alFrontendSessionTotal,
       "alFrontendBytesIN": alFrontendBytesIN,
       "alFrontendBytesOUT": alFrontendBytesOUT,
       "alFrontendErrorRequest": alFrontendErrorRequest,
       "alFrontendDenyRequest": alFrontendDenyRequest,
       "alFrontendDenyResponse": alFrontendDenyResponse,
       "alFrontendStatus": alFrontendStatus,
       "alBackendTable": alBackendTable,
       "alBackendTableEntry": alBackendTableEntry,
       "alBackendProcessID": alBackendProcessID,
       "alBackendID": alBackendID,
       "alBackendName": alBackendName,
       "alBackendQueueCur": alBackendQueueCur,
       "alBackendQueueMax": alBackendQueueMax,
       "alBackendQueueLimit": alBackendQueueLimit,
       "alBackendSessionCur": alBackendSessionCur,
       "alBackendSessionMax": alBackendSessionMax,
       "alBackendSessionLimit": alBackendSessionLimit,
       "alBackendSessionTotal": alBackendSessionTotal,
       "alBackendSessionLoadBalanced": alBackendSessionLoadBalanced,
       "alBackendBytesIN": alBackendBytesIN,
       "alBackendBytesOUT": alBackendBytesOUT,
       "alBackendErrorConnection": alBackendErrorConnection,
       "alBackendErrorResponse": alBackendErrorResponse,
       "alBackendDenyRequest": alBackendDenyRequest,
       "alBackendDenyResponse": alBackendDenyResponse,
       "alBackendWarningRetry": alBackendWarningRetry,
       "alBackendWarningRedispatch": alBackendWarningRedispatch,
       "alBackendStatus": alBackendStatus,
       "alBackendLastChange": alBackendLastChange,
       "alBackendCheckDown": alBackendCheckDown,
       "alBackendDownTime": alBackendDownTime,
       "alServerTable": alServerTable,
       "alServerTableEntry": alServerTableEntry,
       "alServerProcessID": alServerProcessID,
       "alServerBackendID": alServerBackendID,
       "alServerID": alServerID,
       "alServerName": alServerName,
       "alServerQueueCur": alServerQueueCur,
       "alServerQueueMax": alServerQueueMax,
       "alServerQueueLimit": alServerQueueLimit,
       "alServerSessionCur": alServerSessionCur,
       "alServerSessionMax": alServerSessionMax,
       "alServerSessionLimit": alServerSessionLimit,
       "alServerSessionTotal": alServerSessionTotal,
       "alServerSessionLoadBalanced": alServerSessionLoadBalanced,
       "alServerBytesIN": alServerBytesIN,
       "alServerBytesOUT": alServerBytesOUT,
       "alServerErrorConnection": alServerErrorConnection,
       "alServerErrorResponse": alServerErrorResponse,
       "alServerDenyResponse": alServerDenyResponse,
       "alServerWarningRetry": alServerWarningRetry,
       "alServerStatus": alServerStatus,
       "alServerLastChange": alServerLastChange,
       "alServerWeight": alServerWeight,
       "alServerActive": alServerActive,
       "alServerBackup": alServerBackup,
       "alServerCheckFailure": alServerCheckFailure,
       "alServerCheckDown": alServerCheckDown,
       "alServerDownTime": alServerDownTime,
       "alServerThrottle": alServerThrottle,
       "alL4Stats": alL4Stats,
       "alL4ProcessTable": alL4ProcessTable,
       "alL4ProcessTableEntry": alL4ProcessTableEntry,
       "alL4ProcessID": alL4ProcessID,
       "alL4DirectorTable": alL4DirectorTable,
       "alL4DirectorTableEntry": alL4DirectorTableEntry,
       "alL4DirectorProcessID": alL4DirectorProcessID,
       "alL4DirectorID": alL4DirectorID,
       "alL4DirectorName": alL4DirectorName,
       "alL4DirectorSessionCur": alL4DirectorSessionCur,
       "alL4DirectorSessionTotal": alL4DirectorSessionTotal,
       "alL4DirectorPacketsIN": alL4DirectorPacketsIN,
       "alL4DirectorPacketsOUT": alL4DirectorPacketsOUT,
       "alL4DirectorBytesIN": alL4DirectorBytesIN,
       "alL4DirectorBytesOUT": alL4DirectorBytesOUT,
       "alL4DirectorStatus": alL4DirectorStatus,
       "alL4ServerTable": alL4ServerTable,
       "alL4ServerTableEntry": alL4ServerTableEntry,
       "alL4ServerProcessID": alL4ServerProcessID,
       "alL4ServerDirectorID": alL4ServerDirectorID,
       "alL4ServerID": alL4ServerID,
       "alL4ServerName": alL4ServerName,
       "alL4ServerSessionCur": alL4ServerSessionCur,
       "alL4ServerSessionTotal": alL4ServerSessionTotal,
       "alL4ServerPacketsIN": alL4ServerPacketsIN,
       "alL4ServerPacketsOUT": alL4ServerPacketsOUT,
       "alL4ServerBytesIN": alL4ServerBytesIN,
       "alL4ServerBytesOUT": alL4ServerBytesOUT,
       "alL4ServerStatus": alL4ServerStatus,
       "alL4ServerWeight": alL4ServerWeight,
       "alL4ServerActive": alL4ServerActive,
       "alL4ServerBackup": alL4ServerBackup,
       "alHardwareInfo": alHardwareInfo,
       "alHardwareModel": alHardwareModel,
       "alHardwareUUID": alHardwareUUID,
       "alHardwareETHID": alHardwareETHID,
       "alPshieldStats": alPshieldStats,
       "alPshieldInstanceTable": alPshieldInstanceTable,
       "alPshieldInstanceTableEntry": alPshieldInstanceTableEntry,
       "alPshieldInstanceID": alPshieldInstanceID,
       "alPshieldInstanceName": alPshieldInstanceName,
       "alPshieldInstanceRxTotal": alPshieldInstanceRxTotal,
       "alPshieldInstanceRxTotL3B": alPshieldInstanceRxTotL3B,
       "alPshieldInstanceRxTotL1b": alPshieldInstanceRxTotL1b,
       "alPshieldInstanceCaptureMissed": alPshieldInstanceCaptureMissed,
       "alPshieldInstanceDelivered": alPshieldInstanceDelivered,
       "alPshieldInstanceDelivL3B": alPshieldInstanceDelivL3B,
       "alPshieldInstanceDelivL1b": alPshieldInstanceDelivL1b,
       "alPshieldInstanceResponses": alPshieldInstanceResponses,
       "alPshieldInstanceTxTotal": alPshieldInstanceTxTotal,
       "alPshieldInstanceSessionMax": alPshieldInstanceSessionMax,
       "alPshieldInstanceSessionOutgoing": alPshieldInstanceSessionOutgoing,
       "alPshieldInstanceSessionUpload": alPshieldInstanceSessionUpload,
       "alPshieldInstanceSessionIncoming": alPshieldInstanceSessionIncoming,
       "alPshieldInstanceSessionTotActive": alPshieldInstanceSessionTotActive,
       "alPshieldInstanceSessionSynActive": alPshieldInstanceSessionSynActive,
       "alPshieldInstanceSessionRstActive": alPshieldInstanceSessionRstActive,
       "alPshieldInstanceSessionAckActive": alPshieldInstanceSessionAckActive,
       "alPshieldInstanceSessionDnsActive": alPshieldInstanceSessionDnsActive,
       "alPshieldInstanceSessionOutActive": alPshieldInstanceSessionOutActive,
       "alPshieldInstanceSessionRetransmit": alPshieldInstanceSessionRetransmit,
       "alPshieldInstanceSessionForcedHash": alPshieldInstanceSessionForcedHash,
       "alPshieldInstanceSessionForcedKernel": alPshieldInstanceSessionForcedKernel,
       "alPshieldContextTable": alPshieldContextTable,
       "alPshieldContextTableEntry": alPshieldContextTableEntry,
       "alPshieldContextInstanceID": alPshieldContextInstanceID,
       "alPshieldContextID": alPshieldContextID,
       "alPshieldContextName": alPshieldContextName,
       "alPshieldContextStatus": alPshieldContextStatus,
       "alPshieldContextRxTotal": alPshieldContextRxTotal,
       "alPshieldContextInvalid": alPshieldContextInvalid,
       "alPshieldContextWhitelisted": alPshieldContextWhitelisted,
       "alPshieldContextFiltered": alPshieldContextFiltered,
       "alPshieldContextOutRelated": alPshieldContextOutRelated,
       "alPshieldContextDnsResponses": alPshieldContextDnsResponses,
       "alPshieldContextSyn": alPshieldContextSyn,
       "alPshieldContextRst": alPshieldContextRst,
       "alPshieldContextAck": alPshieldContextAck,
       "alPshieldContextUnknownTtl": alPshieldContextUnknownTtl,
       "alPshieldContextTtlFiltered": alPshieldContextTtlFiltered,
       "alPshieldContextEstablished": alPshieldContextEstablished,
       "alPshieldContextNewConnections": alPshieldContextNewConnections,
       "alPshieldContextUnmatched": alPshieldContextUnmatched,
       "alPshieldContextSynCookie": alPshieldContextSynCookie,
       "alPshieldContextDropSyn": alPshieldContextDropSyn,
       "alPshieldContextDropRst": alPshieldContextDropRst,
       "alPshieldContextDropAck": alPshieldContextDropAck,
       "alPshieldContextDelivered": alPshieldContextDelivered,
       "alPshieldContextTxTotal": alPshieldContextTxTotal,
       "algroups": algroups,
       "alTrapNotifGroup": alTrapNotifGroup,
       "alTrapGroup": alTrapGroup,
       "alProductGroup": alProductGroup,
       "alServiceGroup": alServiceGroup,
       "alInstanceGroup": alInstanceGroup,
       "alProcessGroup": alProcessGroup,
       "alBackendGroup": alBackendGroup,
       "alFrontendGroup": alFrontendGroup,
       "alServerGroup": alServerGroup,
       "alL4ProcessGroup": alL4ProcessGroup,
       "alL4DirectorGroup": alL4DirectorGroup,
       "alL4ServerGroup": alL4ServerGroup,
       "alHardwareInfoGroup": alHardwareInfoGroup,
       "alPshieldInstanceGroup": alPshieldInstanceGroup,
       "alPshieldContextGroup": alPshieldContextGroup,
       "hapee": hapee,
       "lbcompat1": lbcompat1,
       "lbProductInfo": lbProductInfo,
       "lbStats": lbStats,
       "lbProcessTable": lbProcessTable,
       "lbProcessTableEntry": lbProcessTableEntry,
       "lbProcessID": lbProcessID,
       "lbProcessVersion": lbProcessVersion,
       "lbProcessReleaseDate": lbProcessReleaseDate,
       "lbProcessNbProc": lbProcessNbProc,
       "lbProcessProductName": lbProcessProductName,
       "lbProcessSystemPID": lbProcessSystemPID,
       "lbProcessUptime": lbProcessUptime,
       "lbProcessUptimeSec": lbProcessUptimeSec,
       "lbProcessMemMax": lbProcessMemMax,
       "lbProcessPoolAlloc": lbProcessPoolAlloc,
       "lbProcessPoolUsed": lbProcessPoolUsed,
       "lbProcessPoolFailed": lbProcessPoolFailed,
       "lbProcessUlimitn": lbProcessUlimitn,
       "lbProcessMaxSock": lbProcessMaxSock,
       "lbProcessMaxConn": lbProcessMaxConn,
       "lbProcessHardMaxConn": lbProcessHardMaxConn,
       "lbProcessCurConn": lbProcessCurConn,
       "lbProcessCumConn": lbProcessCumConn,
       "lbProcessCumReq": lbProcessCumReq,
       "lbProcessMaxSslConn": lbProcessMaxSslConn,
       "lbProcessCurSslConn": lbProcessCurSslConn,
       "lbProcessCumSslConn": lbProcessCumSslConn,
       "lbProcessMaxPipes": lbProcessMaxPipes,
       "lbProcessPipesUsed": lbProcessPipesUsed,
       "lbProcessPipesFree": lbProcessPipesFree,
       "lbProcessConnRate": lbProcessConnRate,
       "lbProcessConnRateLimit": lbProcessConnRateLimit,
       "lbProcessMaxConnRate": lbProcessMaxConnRate,
       "lbProcessSessRate": lbProcessSessRate,
       "lbProcessSessRateLimit": lbProcessSessRateLimit,
       "lbProcessMaxSessRate": lbProcessMaxSessRate,
       "lbProcessSslRate": lbProcessSslRate,
       "lbProcessSslRateLimit": lbProcessSslRateLimit,
       "lbProcessMaxSslRate": lbProcessMaxSslRate,
       "lbProcessSslFrontendKeyRate": lbProcessSslFrontendKeyRate,
       "lbProcessMaxSslFrontendKeyRate": lbProcessMaxSslFrontendKeyRate,
       "lbProcessSslFrontendSessReuse": lbProcessSslFrontendSessReuse,
       "lbProcessSslBackendKeyRate": lbProcessSslBackendKeyRate,
       "lbProcessMaxSslBackendKeyRate": lbProcessMaxSslBackendKeyRate,
       "lbProcessSslCacheLookups": lbProcessSslCacheLookups,
       "lbProcessSslCacheMisses": lbProcessSslCacheMisses,
       "lbProcessCompressBpsIn": lbProcessCompressBpsIn,
       "lbProcessCompressBpsOut": lbProcessCompressBpsOut,
       "lbProcessCompressRateLimit": lbProcessCompressRateLimit,
       "lbProcessZlibMemUsage": lbProcessZlibMemUsage,
       "lbProcessMaxZlibMemUsage": lbProcessMaxZlibMemUsage,
       "lbProcessTasks": lbProcessTasks,
       "lbProcessRunQueue": lbProcessRunQueue,
       "lbProcessIdle": lbProcessIdle,
       "lbProcessNodeName": lbProcessNodeName,
       "lbProcessDescription": lbProcessDescription,
       "lbFrontendTable": lbFrontendTable,
       "lbFrontendTableEntry": lbFrontendTableEntry,
       "lbFrontendProcessID": lbFrontendProcessID,
       "lbFrontendID": lbFrontendID,
       "lbFrontendName": lbFrontendName,
       "lbFrontendSessionCur": lbFrontendSessionCur,
       "lbFrontendSessionMax": lbFrontendSessionMax,
       "lbFrontendSessionLimit": lbFrontendSessionLimit,
       "lbFrontendSessionTotal": lbFrontendSessionTotal,
       "lbFrontendBytesIN": lbFrontendBytesIN,
       "lbFrontendBytesOUT": lbFrontendBytesOUT,
       "lbFrontendErrorRequest": lbFrontendErrorRequest,
       "lbFrontendDenyRequest": lbFrontendDenyRequest,
       "lbFrontendDenyResponse": lbFrontendDenyResponse,
       "lbFrontendStatus": lbFrontendStatus,
       "lbBackendTable": lbBackendTable,
       "lbBackendTableEntry": lbBackendTableEntry,
       "lbBackendProcessID": lbBackendProcessID,
       "lbBackendID": lbBackendID,
       "lbBackendName": lbBackendName,
       "lbBackendQueueCur": lbBackendQueueCur,
       "lbBackendQueueMax": lbBackendQueueMax,
       "lbBackendQueueLimit": lbBackendQueueLimit,
       "lbBackendSessionCur": lbBackendSessionCur,
       "lbBackendSessionMax": lbBackendSessionMax,
       "lbBackendSessionLimit": lbBackendSessionLimit,
       "lbBackendSessionTotal": lbBackendSessionTotal,
       "lbBackendSessionLoadBalanced": lbBackendSessionLoadBalanced,
       "lbBackendBytesIN": lbBackendBytesIN,
       "lbBackendBytesOUT": lbBackendBytesOUT,
       "lbBackendErrorConnection": lbBackendErrorConnection,
       "lbBackendErrorResponse": lbBackendErrorResponse,
       "lbBackendDenyRequest": lbBackendDenyRequest,
       "lbBackendDenyResponse": lbBackendDenyResponse,
       "lbBackendWarningRetry": lbBackendWarningRetry,
       "lbBackendWarningRedispatch": lbBackendWarningRedispatch,
       "lbBackendStatus": lbBackendStatus,
       "lbBackendLastChange": lbBackendLastChange,
       "lbBackendCheckDown": lbBackendCheckDown,
       "lbBackendDownTime": lbBackendDownTime,
       "lbServerTable": lbServerTable,
       "lbServerTableEntry": lbServerTableEntry,
       "lbServerProcessID": lbServerProcessID,
       "lbServerBackendID": lbServerBackendID,
       "lbServerID": lbServerID,
       "lbServerName": lbServerName,
       "lbServerQueueCur": lbServerQueueCur,
       "lbServerQueueMax": lbServerQueueMax,
       "lbServerQueueLimit": lbServerQueueLimit,
       "lbServerSessionCur": lbServerSessionCur,
       "lbServerSessionMax": lbServerSessionMax,
       "lbServerSessionLimit": lbServerSessionLimit,
       "lbServerSessionTotal": lbServerSessionTotal,
       "lbServerSessionLoadBalanced": lbServerSessionLoadBalanced,
       "lbServerBytesIN": lbServerBytesIN,
       "lbServerBytesOUT": lbServerBytesOUT,
       "lbServerErrorConnection": lbServerErrorConnection,
       "lbServerErrorResponse": lbServerErrorResponse,
       "lbServerDenyResponse": lbServerDenyResponse,
       "lbServerWarningRetry": lbServerWarningRetry,
       "lbServerStatus": lbServerStatus,
       "lbServerLastChange": lbServerLastChange,
       "lbServerWeight": lbServerWeight,
       "lbServerActive": lbServerActive,
       "lbServerBackup": lbServerBackup,
       "lbServerCheckFailure": lbServerCheckFailure,
       "lbServerCheckDown": lbServerCheckDown,
       "lbServerDownTime": lbServerDownTime,
       "lbServerThrottle": lbServerThrottle}
)
