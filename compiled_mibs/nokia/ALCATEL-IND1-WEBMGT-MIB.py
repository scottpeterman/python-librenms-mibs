# SNMP MIB module (ALCATEL-IND1-WEBMGT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-WEBMGT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:31 2025
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

(softentIND1WebMgt,
 switchMgtTraps) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1WebMgt",
    "switchMgtTraps")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1WebMgtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1WebMgtMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBObjects = _AlcatelIND1WebMgtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBObjects.setStatus("current")


class _AlaIND1WebMgtAdminStatus_Type(Integer32):
    """Custom type alaIND1WebMgtAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaIND1WebMgtAdminStatus_Type.__name__ = "Integer32"
_AlaIND1WebMgtAdminStatus_Object = MibScalar
alaIND1WebMgtAdminStatus = _AlaIND1WebMgtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 1),
    _AlaIND1WebMgtAdminStatus_Type()
)
alaIND1WebMgtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtAdminStatus.setStatus("current")


class _AlaIND1WebMgtSSL_Type(Integer32):
    """Custom type alaIND1WebMgtSSL based on Integer32"""
    defaultValue = 1

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


_AlaIND1WebMgtSSL_Type.__name__ = "Integer32"
_AlaIND1WebMgtSSL_Object = MibScalar
alaIND1WebMgtSSL = _AlaIND1WebMgtSSL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 2),
    _AlaIND1WebMgtSSL_Type()
)
alaIND1WebMgtSSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtSSL.setStatus("current")
_AlaIND1WebMgtRFSConfigTable_Object = MibTable
alaIND1WebMgtRFSConfigTable = _AlaIND1WebMgtRFSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSConfigTable.setStatus("current")
_AlaIND1WebMgtRFSConfigEntry_Object = MibTableRow
alaIND1WebMgtRFSConfigEntry = _AlaIND1WebMgtRFSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1)
)
alaIND1WebMgtRFSConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSAddrType"),
    (0, "ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSIPAddr"),
)
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSConfigEntry.setStatus("current")
_AlaIND1WebMgtRFSAddrType_Type = InetAddressType
_AlaIND1WebMgtRFSAddrType_Object = MibTableColumn
alaIND1WebMgtRFSAddrType = _AlaIND1WebMgtRFSAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1, 1),
    _AlaIND1WebMgtRFSAddrType_Type()
)
alaIND1WebMgtRFSAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSAddrType.setStatus("current")
_AlaIND1WebMgtRFSIPAddr_Type = InetAddress
_AlaIND1WebMgtRFSIPAddr_Object = MibTableColumn
alaIND1WebMgtRFSIPAddr = _AlaIND1WebMgtRFSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1, 2),
    _AlaIND1WebMgtRFSIPAddr_Type()
)
alaIND1WebMgtRFSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSIPAddr.setStatus("current")
_AlaIND1WebMgtRFSIPServerName_Type = DisplayString
_AlaIND1WebMgtRFSIPServerName_Object = MibTableColumn
alaIND1WebMgtRFSIPServerName = _AlaIND1WebMgtRFSIPServerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1, 3),
    _AlaIND1WebMgtRFSIPServerName_Type()
)
alaIND1WebMgtRFSIPServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSIPServerName.setStatus("current")
_AlaIND1WebMgtRFSServerLogin_Type = DisplayString
_AlaIND1WebMgtRFSServerLogin_Object = MibTableColumn
alaIND1WebMgtRFSServerLogin = _AlaIND1WebMgtRFSServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1, 4),
    _AlaIND1WebMgtRFSServerLogin_Type()
)
alaIND1WebMgtRFSServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSServerLogin.setStatus("current")
_AlaIND1WebMgtRFSServerPassword_Type = DisplayString
_AlaIND1WebMgtRFSServerPassword_Object = MibTableColumn
alaIND1WebMgtRFSServerPassword = _AlaIND1WebMgtRFSServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1, 5),
    _AlaIND1WebMgtRFSServerPassword_Type()
)
alaIND1WebMgtRFSServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSServerPassword.setStatus("current")


class _AlaIND1WebMgtRFSPrefServer_Type(Integer32):
    """Custom type alaIND1WebMgtRFSPrefServer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("preferred", 1)
    )


_AlaIND1WebMgtRFSPrefServer_Type.__name__ = "Integer32"
_AlaIND1WebMgtRFSPrefServer_Object = MibTableColumn
alaIND1WebMgtRFSPrefServer = _AlaIND1WebMgtRFSPrefServer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1, 6),
    _AlaIND1WebMgtRFSPrefServer_Type()
)
alaIND1WebMgtRFSPrefServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSPrefServer.setStatus("current")
_AlaIND1WebMgtRFSPath_Type = DisplayString
_AlaIND1WebMgtRFSPath_Object = MibTableColumn
alaIND1WebMgtRFSPath = _AlaIND1WebMgtRFSPath_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1, 7),
    _AlaIND1WebMgtRFSPath_Type()
)
alaIND1WebMgtRFSPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSPath.setStatus("current")
_AlaIND1WebMgtRFSRowStatus_Type = RowStatus
_AlaIND1WebMgtRFSRowStatus_Object = MibTableColumn
alaIND1WebMgtRFSRowStatus = _AlaIND1WebMgtRFSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 3, 1, 8),
    _AlaIND1WebMgtRFSRowStatus_Type()
)
alaIND1WebMgtRFSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSRowStatus.setStatus("current")


class _AlaIND1WebMgtDigestAuth_Type(Integer32):
    """Custom type alaIND1WebMgtDigestAuth based on Integer32"""
    defaultValue = 1

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


_AlaIND1WebMgtDigestAuth_Type.__name__ = "Integer32"
_AlaIND1WebMgtDigestAuth_Object = MibScalar
alaIND1WebMgtDigestAuth = _AlaIND1WebMgtDigestAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 4),
    _AlaIND1WebMgtDigestAuth_Type()
)
alaIND1WebMgtDigestAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtDigestAuth.setStatus("current")


class _AlaIND1WebMgtHttpPort_Type(Integer32):
    """Custom type alaIND1WebMgtHttpPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaIND1WebMgtHttpPort_Type.__name__ = "Integer32"
_AlaIND1WebMgtHttpPort_Object = MibScalar
alaIND1WebMgtHttpPort = _AlaIND1WebMgtHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 5),
    _AlaIND1WebMgtHttpPort_Type()
)
alaIND1WebMgtHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtHttpPort.setStatus("current")


class _AlaIND1WebMgtHttpsPort_Type(Integer32):
    """Custom type alaIND1WebMgtHttpsPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaIND1WebMgtHttpsPort_Type.__name__ = "Integer32"
_AlaIND1WebMgtHttpsPort_Object = MibScalar
alaIND1WebMgtHttpsPort = _AlaIND1WebMgtHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 1, 6),
    _AlaIND1WebMgtHttpsPort_Type()
)
alaIND1WebMgtHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIND1WebMgtHttpsPort.setStatus("current")
_AlcatelIND1WebMgtMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBConformance = _AlcatelIND1WebMgtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBConformance.setStatus("current")
_AlcatelIND1WebMgtMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBGroups = _AlcatelIND1WebMgtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBGroups.setStatus("current")
_AlcatelIND1WebMgtMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1WebMgtMIBCompliances = _AlcatelIND1WebMgtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1WebMgtMIBCompliances.setStatus("current")
_WebMgtTrapsDesc_ObjectIdentity = ObjectIdentity
webMgtTrapsDesc = _WebMgtTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 11, 3)
)
_WebMgtTrapsObj_ObjectIdentity = ObjectIdentity
webMgtTrapsObj = _WebMgtTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 11, 4)
)
_HttpConnectionStats_Type = Counter32
_HttpConnectionStats_Object = MibScalar
httpConnectionStats = _HttpConnectionStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 11, 4, 1),
    _HttpConnectionStats_Type()
)
httpConnectionStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpConnectionStats.setStatus("current")
_HttpsConnectionStats_Type = Counter32
_HttpsConnectionStats_Object = MibScalar
httpsConnectionStats = _HttpsConnectionStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 11, 4, 2),
    _HttpsConnectionStats_Type()
)
httpsConnectionStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpsConnectionStats.setStatus("current")
_HttpServerDoSAttackSrcIp_Type = IpAddress
_HttpServerDoSAttackSrcIp_Object = MibScalar
httpServerDoSAttackSrcIp = _HttpServerDoSAttackSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 11, 4, 3),
    _HttpServerDoSAttackSrcIp_Type()
)
httpServerDoSAttackSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpServerDoSAttackSrcIp.setStatus("current")

# Managed Objects groups

alaIND1WebMgtConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 2, 1, 1)
)
alaIND1WebMgtConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtAdminStatus"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtSSL"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtHttpPort"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtHttpsPort"))
)
if mibBuilder.loadTexts:
    alaIND1WebMgtConfigMIBGroup.setStatus("current")

alaIND1WebMgtRFSMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 17, 1, 2, 1, 2)
)
alaIND1WebMgtRFSMIBGroup.setObjects(
      *(("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSAddrType"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSIPAddr"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSIPServerName"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSServerLogin"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSServerPassword"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSPrefServer"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSPath"),
        ("ALCATEL-IND1-WEBMGT-MIB", "alaIND1WebMgtRFSRowStatus"))
)
if mibBuilder.loadTexts:
    alaIND1WebMgtRFSMIBGroup.setStatus("current")


# Notification objects

httpServerDoSAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 11, 3, 0, 1)
)
httpServerDoSAttackTrap.setObjects(
      *(("ALCATEL-IND1-WEBMGT-MIB", "httpConnectionStats"),
        ("ALCATEL-IND1-WEBMGT-MIB", "httpsConnectionStats"),
        ("ALCATEL-IND1-WEBMGT-MIB", "httpServerDoSAttackSrcIp"))
)
if mibBuilder.loadTexts:
    httpServerDoSAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-WEBMGT-MIB",
    **{"alcatelIND1WebMgtMIB": alcatelIND1WebMgtMIB,
       "alcatelIND1WebMgtMIBObjects": alcatelIND1WebMgtMIBObjects,
       "alaIND1WebMgtAdminStatus": alaIND1WebMgtAdminStatus,
       "alaIND1WebMgtSSL": alaIND1WebMgtSSL,
       "alaIND1WebMgtRFSConfigTable": alaIND1WebMgtRFSConfigTable,
       "alaIND1WebMgtRFSConfigEntry": alaIND1WebMgtRFSConfigEntry,
       "alaIND1WebMgtRFSAddrType": alaIND1WebMgtRFSAddrType,
       "alaIND1WebMgtRFSIPAddr": alaIND1WebMgtRFSIPAddr,
       "alaIND1WebMgtRFSIPServerName": alaIND1WebMgtRFSIPServerName,
       "alaIND1WebMgtRFSServerLogin": alaIND1WebMgtRFSServerLogin,
       "alaIND1WebMgtRFSServerPassword": alaIND1WebMgtRFSServerPassword,
       "alaIND1WebMgtRFSPrefServer": alaIND1WebMgtRFSPrefServer,
       "alaIND1WebMgtRFSPath": alaIND1WebMgtRFSPath,
       "alaIND1WebMgtRFSRowStatus": alaIND1WebMgtRFSRowStatus,
       "alaIND1WebMgtDigestAuth": alaIND1WebMgtDigestAuth,
       "alaIND1WebMgtHttpPort": alaIND1WebMgtHttpPort,
       "alaIND1WebMgtHttpsPort": alaIND1WebMgtHttpsPort,
       "alcatelIND1WebMgtMIBConformance": alcatelIND1WebMgtMIBConformance,
       "alcatelIND1WebMgtMIBGroups": alcatelIND1WebMgtMIBGroups,
       "alaIND1WebMgtConfigMIBGroup": alaIND1WebMgtConfigMIBGroup,
       "alaIND1WebMgtRFSMIBGroup": alaIND1WebMgtRFSMIBGroup,
       "alcatelIND1WebMgtMIBCompliances": alcatelIND1WebMgtMIBCompliances,
       "webMgtTrapsDesc": webMgtTrapsDesc,
       "httpServerDoSAttackTrap": httpServerDoSAttackTrap,
       "webMgtTrapsObj": webMgtTrapsObj,
       "httpConnectionStats": httpConnectionStats,
       "httpsConnectionStats": httpsConnectionStats,
       "httpServerDoSAttackSrcIp": httpServerDoSAttackSrcIp}
)
