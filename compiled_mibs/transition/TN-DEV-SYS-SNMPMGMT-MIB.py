# SNMP MIB module (TN-DEV-SYS-SNMPMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-SYS-SNMPMGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:03 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

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
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY

tnDevSysSnmpmgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tnDevSysSnmpmgmt.setRevisions(
        ("2014-02-19 00:00",
         "2013-05-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevSysSnmpMgmtTable_Object = MibTable
tnDevSysSnmpMgmtTable = _TnDevSysSnmpMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    tnDevSysSnmpMgmtTable.setStatus("current")
_TnDevSysSnmpMgmtEntry_Object = MibTableRow
tnDevSysSnmpMgmtEntry = _TnDevSysSnmpMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 1, 1)
)
tnDevSysSnmpMgmtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysSnmpMgmtEntry.setStatus("current")


class _TnDevSysSnmpAccess_Type(Integer32):
    """Custom type tnDevSysSnmpAccess based on Integer32"""
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


_TnDevSysSnmpAccess_Type.__name__ = "Integer32"
_TnDevSysSnmpAccess_Object = MibTableColumn
tnDevSysSnmpAccess = _TnDevSysSnmpAccess_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 1, 1, 1),
    _TnDevSysSnmpAccess_Type()
)
tnDevSysSnmpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpAccess.setStatus("current")


class _TnDevSysSnmpVersion_Type(DisplayString):
    """Custom type tnDevSysSnmpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_TnDevSysSnmpVersion_Type.__name__ = "DisplayString"
_TnDevSysSnmpVersion_Object = MibTableColumn
tnDevSysSnmpVersion = _TnDevSysSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 1, 1, 2),
    _TnDevSysSnmpVersion_Type()
)
tnDevSysSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpVersion.setStatus("current")


class _TnDevSysSnmpReadCommunity_Type(DisplayString):
    """Custom type tnDevSysSnmpReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDevSysSnmpReadCommunity_Type.__name__ = "DisplayString"
_TnDevSysSnmpReadCommunity_Object = MibTableColumn
tnDevSysSnmpReadCommunity = _TnDevSysSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 1, 1, 3),
    _TnDevSysSnmpReadCommunity_Type()
)
tnDevSysSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpReadCommunity.setStatus("current")


class _TnDevSysSnmpWriteCommunity_Type(DisplayString):
    """Custom type tnDevSysSnmpWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDevSysSnmpWriteCommunity_Type.__name__ = "DisplayString"
_TnDevSysSnmpWriteCommunity_Object = MibTableColumn
tnDevSysSnmpWriteCommunity = _TnDevSysSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 1, 1, 4),
    _TnDevSysSnmpWriteCommunity_Type()
)
tnDevSysSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpWriteCommunity.setStatus("current")
_TnDevSysSnmpLocal_ObjectIdentity = ObjectIdentity
tnDevSysSnmpLocal = _TnDevSysSnmpLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 3)
)
_TnDevSysSnmpLocalEngineID_Type = SnmpEngineID
_TnDevSysSnmpLocalEngineID_Object = MibScalar
tnDevSysSnmpLocalEngineID = _TnDevSysSnmpLocalEngineID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 3, 1),
    _TnDevSysSnmpLocalEngineID_Type()
)
tnDevSysSnmpLocalEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpLocalEngineID.setStatus("current")
_TnDevSysSnmpTrapManagerTable_Object = MibTable
tnDevSysSnmpTrapManagerTable = _TnDevSysSnmpTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 4)
)
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapManagerTable.setStatus("current")
_TnDevSysSnmpTrapManagerEntry_Object = MibTableRow
tnDevSysSnmpTrapManagerEntry = _TnDevSysSnmpTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 4, 1)
)
tnDevSysSnmpTrapManagerEntry.setIndexNames(
    (0, "TN-DEV-SYS-SNMPMGMT-MIB", "tnDevSysSnmpTrapManagerIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapManagerEntry.setStatus("current")


class _TnDevSysSnmpTrapManagerIndex_Type(Integer32):
    """Custom type tnDevSysSnmpTrapManagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnDevSysSnmpTrapManagerIndex_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapManagerIndex_Object = MibTableColumn
tnDevSysSnmpTrapManagerIndex = _TnDevSysSnmpTrapManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 4, 1, 1),
    _TnDevSysSnmpTrapManagerIndex_Type()
)
tnDevSysSnmpTrapManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapManagerIndex.setStatus("current")
_TnDevSysSnmpTrapManagerAddrTDomain_Type = TDomain
_TnDevSysSnmpTrapManagerAddrTDomain_Object = MibTableColumn
tnDevSysSnmpTrapManagerAddrTDomain = _TnDevSysSnmpTrapManagerAddrTDomain_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 4, 1, 2),
    _TnDevSysSnmpTrapManagerAddrTDomain_Type()
)
tnDevSysSnmpTrapManagerAddrTDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapManagerAddrTDomain.setStatus("current")
_TnDevSysSnmpTrapManagerAddrTAddress_Type = TAddress
_TnDevSysSnmpTrapManagerAddrTAddress_Object = MibTableColumn
tnDevSysSnmpTrapManagerAddrTAddress = _TnDevSysSnmpTrapManagerAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 4, 1, 3),
    _TnDevSysSnmpTrapManagerAddrTAddress_Type()
)
tnDevSysSnmpTrapManagerAddrTAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapManagerAddrTAddress.setStatus("current")
_TnDevSysSnmpTrapManagerEngineID_Type = SnmpEngineID
_TnDevSysSnmpTrapManagerEngineID_Object = MibTableColumn
tnDevSysSnmpTrapManagerEngineID = _TnDevSysSnmpTrapManagerEngineID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 4, 1, 4),
    _TnDevSysSnmpTrapManagerEngineID_Type()
)
tnDevSysSnmpTrapManagerEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapManagerEngineID.setStatus("current")
_TnDevSysSnmpTrapManagerStatus_Type = RowStatus
_TnDevSysSnmpTrapManagerStatus_Object = MibTableColumn
tnDevSysSnmpTrapManagerStatus = _TnDevSysSnmpTrapManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 4, 1, 20),
    _TnDevSysSnmpTrapManagerStatus_Type()
)
tnDevSysSnmpTrapManagerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapManagerStatus.setStatus("current")
_TnDevSysSnmpTrapCfgTable_Object = MibTable
tnDevSysSnmpTrapCfgTable = _TnDevSysSnmpTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5)
)
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgTable.setStatus("current")
_TnDevSysSnmpTrapCfgEntry_Object = MibTableRow
tnDevSysSnmpTrapCfgEntry = _TnDevSysSnmpTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1)
)
tnDevSysSnmpTrapCfgEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgEntry.setStatus("current")


class _TnDevSysSnmpTrapCfgMode_Type(Integer32):
    """Custom type tnDevSysSnmpTrapCfgMode based on Integer32"""
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


_TnDevSysSnmpTrapCfgMode_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapCfgMode_Object = MibTableColumn
tnDevSysSnmpTrapCfgMode = _TnDevSysSnmpTrapCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 1),
    _TnDevSysSnmpTrapCfgMode_Type()
)
tnDevSysSnmpTrapCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgMode.setStatus("current")
_TnDevSysSnmpTrapCfgCommunity_Type = SnmpAdminString
_TnDevSysSnmpTrapCfgCommunity_Object = MibTableColumn
tnDevSysSnmpTrapCfgCommunity = _TnDevSysSnmpTrapCfgCommunity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 2),
    _TnDevSysSnmpTrapCfgCommunity_Type()
)
tnDevSysSnmpTrapCfgCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgCommunity.setStatus("current")


class _TnDevSysSnmpTrapCfgAuthFailure_Type(Integer32):
    """Custom type tnDevSysSnmpTrapCfgAuthFailure based on Integer32"""
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


_TnDevSysSnmpTrapCfgAuthFailure_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapCfgAuthFailure_Object = MibTableColumn
tnDevSysSnmpTrapCfgAuthFailure = _TnDevSysSnmpTrapCfgAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 3),
    _TnDevSysSnmpTrapCfgAuthFailure_Type()
)
tnDevSysSnmpTrapCfgAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgAuthFailure.setStatus("current")


class _TnDevSysSnmpTrapCfgLinkChange_Type(Integer32):
    """Custom type tnDevSysSnmpTrapCfgLinkChange based on Integer32"""
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


_TnDevSysSnmpTrapCfgLinkChange_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapCfgLinkChange_Object = MibTableColumn
tnDevSysSnmpTrapCfgLinkChange = _TnDevSysSnmpTrapCfgLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 4),
    _TnDevSysSnmpTrapCfgLinkChange_Type()
)
tnDevSysSnmpTrapCfgLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgLinkChange.setStatus("current")


class _TnDevSysSnmpTrapCfgEngineIdProbe_Type(Integer32):
    """Custom type tnDevSysSnmpTrapCfgEngineIdProbe based on Integer32"""
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


_TnDevSysSnmpTrapCfgEngineIdProbe_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapCfgEngineIdProbe_Object = MibTableColumn
tnDevSysSnmpTrapCfgEngineIdProbe = _TnDevSysSnmpTrapCfgEngineIdProbe_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 5),
    _TnDevSysSnmpTrapCfgEngineIdProbe_Type()
)
tnDevSysSnmpTrapCfgEngineIdProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgEngineIdProbe.setStatus("current")
_TnDevSysSnmpTrapCfgAdminEngineId_Type = SnmpEngineID
_TnDevSysSnmpTrapCfgAdminEngineId_Object = MibTableColumn
tnDevSysSnmpTrapCfgAdminEngineId = _TnDevSysSnmpTrapCfgAdminEngineId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 6),
    _TnDevSysSnmpTrapCfgAdminEngineId_Type()
)
tnDevSysSnmpTrapCfgAdminEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgAdminEngineId.setStatus("current")
_TnDevSysSnmpTrapCfgSecurityName_Type = SnmpAdminString
_TnDevSysSnmpTrapCfgSecurityName_Object = MibTableColumn
tnDevSysSnmpTrapCfgSecurityName = _TnDevSysSnmpTrapCfgSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 7),
    _TnDevSysSnmpTrapCfgSecurityName_Type()
)
tnDevSysSnmpTrapCfgSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgSecurityName.setStatus("current")


class _TnDevSysSnmpTrapCfgVersion_Type(Integer32):
    """Custom type tnDevSysSnmpTrapCfgVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_TnDevSysSnmpTrapCfgVersion_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapCfgVersion_Object = MibTableColumn
tnDevSysSnmpTrapCfgVersion = _TnDevSysSnmpTrapCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 8),
    _TnDevSysSnmpTrapCfgVersion_Type()
)
tnDevSysSnmpTrapCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgVersion.setStatus("current")


class _TnDevSysSnmpTrapCfgInformMode_Type(Integer32):
    """Custom type tnDevSysSnmpTrapCfgInformMode based on Integer32"""
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


_TnDevSysSnmpTrapCfgInformMode_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapCfgInformMode_Object = MibTableColumn
tnDevSysSnmpTrapCfgInformMode = _TnDevSysSnmpTrapCfgInformMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 9),
    _TnDevSysSnmpTrapCfgInformMode_Type()
)
tnDevSysSnmpTrapCfgInformMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgInformMode.setStatus("current")
_TnDevSysSnmpTrapCfgInformTimeout_Type = Integer32
_TnDevSysSnmpTrapCfgInformTimeout_Object = MibTableColumn
tnDevSysSnmpTrapCfgInformTimeout = _TnDevSysSnmpTrapCfgInformTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 10),
    _TnDevSysSnmpTrapCfgInformTimeout_Type()
)
tnDevSysSnmpTrapCfgInformTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgInformTimeout.setStatus("current")
_TnDevSysSnmpTrapCfgInformRetry_Type = Integer32
_TnDevSysSnmpTrapCfgInformRetry_Object = MibTableColumn
tnDevSysSnmpTrapCfgInformRetry = _TnDevSysSnmpTrapCfgInformRetry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 5, 1, 11),
    _TnDevSysSnmpTrapCfgInformRetry_Type()
)
tnDevSysSnmpTrapCfgInformRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapCfgInformRetry.setStatus("current")
_TnDevSysSnmpTrapServerCfgTable_Object = MibTable
tnDevSysSnmpTrapServerCfgTable = _TnDevSysSnmpTrapServerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6)
)
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgTable.setStatus("current")
_TnDevSysSnmpTrapServerCfgEntry_Object = MibTableRow
tnDevSysSnmpTrapServerCfgEntry = _TnDevSysSnmpTrapServerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1)
)
tnDevSysSnmpTrapServerCfgEntry.setIndexNames(
    (1, "TN-DEV-SYS-SNMPMGMT-MIB", "tnDevSysSnmpTrapServerCfgName"),
)
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEntry.setStatus("current")
_TnDevSysSnmpTrapServerCfgName_Type = SnmpAdminString
_TnDevSysSnmpTrapServerCfgName_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgName = _TnDevSysSnmpTrapServerCfgName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 1),
    _TnDevSysSnmpTrapServerCfgName_Type()
)
tnDevSysSnmpTrapServerCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgName.setStatus("current")


class _TnDevSysSnmpTrapServerCfgMode_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgMode based on Integer32"""
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


_TnDevSysSnmpTrapServerCfgMode_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgMode_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgMode = _TnDevSysSnmpTrapServerCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 2),
    _TnDevSysSnmpTrapServerCfgMode_Type()
)
tnDevSysSnmpTrapServerCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgMode.setStatus("current")


class _TnDevSysSnmpTrapServerCfgVersion_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_TnDevSysSnmpTrapServerCfgVersion_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgVersion_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgVersion = _TnDevSysSnmpTrapServerCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 3),
    _TnDevSysSnmpTrapServerCfgVersion_Type()
)
tnDevSysSnmpTrapServerCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgVersion.setStatus("current")
_TnDevSysSnmpTrapServerCfgCommunity_Type = SnmpAdminString
_TnDevSysSnmpTrapServerCfgCommunity_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgCommunity = _TnDevSysSnmpTrapServerCfgCommunity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 4),
    _TnDevSysSnmpTrapServerCfgCommunity_Type()
)
tnDevSysSnmpTrapServerCfgCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgCommunity.setStatus("current")
_TnDevSysSnmpTrapServerCfgDstAddress_Type = InetAddress
_TnDevSysSnmpTrapServerCfgDstAddress_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgDstAddress = _TnDevSysSnmpTrapServerCfgDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 5),
    _TnDevSysSnmpTrapServerCfgDstAddress_Type()
)
tnDevSysSnmpTrapServerCfgDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgDstAddress.setStatus("current")


class _TnDevSysSnmpTrapServerCfgDstPort_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnDevSysSnmpTrapServerCfgDstPort_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgDstPort_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgDstPort = _TnDevSysSnmpTrapServerCfgDstPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 6),
    _TnDevSysSnmpTrapServerCfgDstPort_Type()
)
tnDevSysSnmpTrapServerCfgDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgDstPort.setStatus("current")


class _TnDevSysSnmpTrapServerCfgInformMode_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgInformMode based on Integer32"""
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


_TnDevSysSnmpTrapServerCfgInformMode_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgInformMode_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgInformMode = _TnDevSysSnmpTrapServerCfgInformMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 7),
    _TnDevSysSnmpTrapServerCfgInformMode_Type()
)
tnDevSysSnmpTrapServerCfgInformMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgInformMode.setStatus("current")
_TnDevSysSnmpTrapServerCfgInformTimeout_Type = Integer32
_TnDevSysSnmpTrapServerCfgInformTimeout_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgInformTimeout = _TnDevSysSnmpTrapServerCfgInformTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 8),
    _TnDevSysSnmpTrapServerCfgInformTimeout_Type()
)
tnDevSysSnmpTrapServerCfgInformTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgInformTimeout.setStatus("current")
_TnDevSysSnmpTrapServerCfgInformRetry_Type = Integer32
_TnDevSysSnmpTrapServerCfgInformRetry_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgInformRetry = _TnDevSysSnmpTrapServerCfgInformRetry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 9),
    _TnDevSysSnmpTrapServerCfgInformRetry_Type()
)
tnDevSysSnmpTrapServerCfgInformRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgInformRetry.setStatus("current")


class _TnDevSysSnmpTrapServerCfgEngineIdProbe_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgEngineIdProbe based on Integer32"""
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


_TnDevSysSnmpTrapServerCfgEngineIdProbe_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgEngineIdProbe_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEngineIdProbe = _TnDevSysSnmpTrapServerCfgEngineIdProbe_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 10),
    _TnDevSysSnmpTrapServerCfgEngineIdProbe_Type()
)
tnDevSysSnmpTrapServerCfgEngineIdProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEngineIdProbe.setStatus("current")
_TnDevSysSnmpTrapServerCfgAdminEngineId_Type = SnmpEngineID
_TnDevSysSnmpTrapServerCfgAdminEngineId_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgAdminEngineId = _TnDevSysSnmpTrapServerCfgAdminEngineId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 11),
    _TnDevSysSnmpTrapServerCfgAdminEngineId_Type()
)
tnDevSysSnmpTrapServerCfgAdminEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgAdminEngineId.setStatus("current")
_TnDevSysSnmpTrapServerCfgSecurityName_Type = SnmpAdminString
_TnDevSysSnmpTrapServerCfgSecurityName_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgSecurityName = _TnDevSysSnmpTrapServerCfgSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 12),
    _TnDevSysSnmpTrapServerCfgSecurityName_Type()
)
tnDevSysSnmpTrapServerCfgSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgSecurityName.setStatus("current")


class _TnDevSysSnmpTrapServerCfgEvtWstart_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgEvtWstart based on Integer32"""
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


_TnDevSysSnmpTrapServerCfgEvtWstart_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgEvtWstart_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEvtWstart = _TnDevSysSnmpTrapServerCfgEvtWstart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 13),
    _TnDevSysSnmpTrapServerCfgEvtWstart_Type()
)
tnDevSysSnmpTrapServerCfgEvtWstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEvtWstart.setStatus("current")


class _TnDevSysSnmpTrapServerCfgEvtCstart_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgEvtCstart based on Integer32"""
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


_TnDevSysSnmpTrapServerCfgEvtCstart_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgEvtCstart_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEvtCstart = _TnDevSysSnmpTrapServerCfgEvtCstart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 14),
    _TnDevSysSnmpTrapServerCfgEvtCstart_Type()
)
tnDevSysSnmpTrapServerCfgEvtCstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEvtCstart.setStatus("current")
_TnDevSysSnmpTrapServerCfgEvtLinkUp_Type = PortList
_TnDevSysSnmpTrapServerCfgEvtLinkUp_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEvtLinkUp = _TnDevSysSnmpTrapServerCfgEvtLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 15),
    _TnDevSysSnmpTrapServerCfgEvtLinkUp_Type()
)
tnDevSysSnmpTrapServerCfgEvtLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEvtLinkUp.setStatus("current")
_TnDevSysSnmpTrapServerCfgEvtLinkDown_Type = PortList
_TnDevSysSnmpTrapServerCfgEvtLinkDown_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEvtLinkDown = _TnDevSysSnmpTrapServerCfgEvtLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 16),
    _TnDevSysSnmpTrapServerCfgEvtLinkDown_Type()
)
tnDevSysSnmpTrapServerCfgEvtLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEvtLinkDown.setStatus("current")
_TnDevSysSnmpTrapServerCfgEvtLldp_Type = PortList
_TnDevSysSnmpTrapServerCfgEvtLldp_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEvtLldp = _TnDevSysSnmpTrapServerCfgEvtLldp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 17),
    _TnDevSysSnmpTrapServerCfgEvtLldp_Type()
)
tnDevSysSnmpTrapServerCfgEvtLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEvtLldp.setStatus("current")


class _TnDevSysSnmpTrapServerCfgEvtAuthFail_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgEvtAuthFail based on Integer32"""
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


_TnDevSysSnmpTrapServerCfgEvtAuthFail_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgEvtAuthFail_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEvtAuthFail = _TnDevSysSnmpTrapServerCfgEvtAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 18),
    _TnDevSysSnmpTrapServerCfgEvtAuthFail_Type()
)
tnDevSysSnmpTrapServerCfgEvtAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEvtAuthFail.setStatus("current")


class _TnDevSysSnmpTrapServerCfgEvtStp_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgEvtStp based on Integer32"""
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


_TnDevSysSnmpTrapServerCfgEvtStp_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgEvtStp_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEvtStp = _TnDevSysSnmpTrapServerCfgEvtStp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 19),
    _TnDevSysSnmpTrapServerCfgEvtStp_Type()
)
tnDevSysSnmpTrapServerCfgEvtStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEvtStp.setStatus("current")


class _TnDevSysSnmpTrapServerCfgEvtRmon_Type(Integer32):
    """Custom type tnDevSysSnmpTrapServerCfgEvtRmon based on Integer32"""
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


_TnDevSysSnmpTrapServerCfgEvtRmon_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapServerCfgEvtRmon_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgEvtRmon = _TnDevSysSnmpTrapServerCfgEvtRmon_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 20),
    _TnDevSysSnmpTrapServerCfgEvtRmon_Type()
)
tnDevSysSnmpTrapServerCfgEvtRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgEvtRmon.setStatus("current")
_TnDevSysSnmpTrapServerCfgRowStatus_Type = RowStatus
_TnDevSysSnmpTrapServerCfgRowStatus_Object = MibTableColumn
tnDevSysSnmpTrapServerCfgRowStatus = _TnDevSysSnmpTrapServerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 6, 1, 21),
    _TnDevSysSnmpTrapServerCfgRowStatus_Type()
)
tnDevSysSnmpTrapServerCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapServerCfgRowStatus.setStatus("current")


class _TnDevSysSnmpTrapGlobalCfgMode_Type(Integer32):
    """Custom type tnDevSysSnmpTrapGlobalCfgMode based on Integer32"""
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


_TnDevSysSnmpTrapGlobalCfgMode_Type.__name__ = "Integer32"
_TnDevSysSnmpTrapGlobalCfgMode_Object = MibScalar
tnDevSysSnmpTrapGlobalCfgMode = _TnDevSysSnmpTrapGlobalCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 14, 7),
    _TnDevSysSnmpTrapGlobalCfgMode_Type()
)
tnDevSysSnmpTrapGlobalCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysSnmpTrapGlobalCfgMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-SYS-SNMPMGMT-MIB",
    **{"tnDevSysSnmpmgmt": tnDevSysSnmpmgmt,
       "tnDevSysSnmpMgmtTable": tnDevSysSnmpMgmtTable,
       "tnDevSysSnmpMgmtEntry": tnDevSysSnmpMgmtEntry,
       "tnDevSysSnmpAccess": tnDevSysSnmpAccess,
       "tnDevSysSnmpVersion": tnDevSysSnmpVersion,
       "tnDevSysSnmpReadCommunity": tnDevSysSnmpReadCommunity,
       "tnDevSysSnmpWriteCommunity": tnDevSysSnmpWriteCommunity,
       "tnDevSysSnmpLocal": tnDevSysSnmpLocal,
       "tnDevSysSnmpLocalEngineID": tnDevSysSnmpLocalEngineID,
       "tnDevSysSnmpTrapManagerTable": tnDevSysSnmpTrapManagerTable,
       "tnDevSysSnmpTrapManagerEntry": tnDevSysSnmpTrapManagerEntry,
       "tnDevSysSnmpTrapManagerIndex": tnDevSysSnmpTrapManagerIndex,
       "tnDevSysSnmpTrapManagerAddrTDomain": tnDevSysSnmpTrapManagerAddrTDomain,
       "tnDevSysSnmpTrapManagerAddrTAddress": tnDevSysSnmpTrapManagerAddrTAddress,
       "tnDevSysSnmpTrapManagerEngineID": tnDevSysSnmpTrapManagerEngineID,
       "tnDevSysSnmpTrapManagerStatus": tnDevSysSnmpTrapManagerStatus,
       "tnDevSysSnmpTrapCfgTable": tnDevSysSnmpTrapCfgTable,
       "tnDevSysSnmpTrapCfgEntry": tnDevSysSnmpTrapCfgEntry,
       "tnDevSysSnmpTrapCfgMode": tnDevSysSnmpTrapCfgMode,
       "tnDevSysSnmpTrapCfgCommunity": tnDevSysSnmpTrapCfgCommunity,
       "tnDevSysSnmpTrapCfgAuthFailure": tnDevSysSnmpTrapCfgAuthFailure,
       "tnDevSysSnmpTrapCfgLinkChange": tnDevSysSnmpTrapCfgLinkChange,
       "tnDevSysSnmpTrapCfgEngineIdProbe": tnDevSysSnmpTrapCfgEngineIdProbe,
       "tnDevSysSnmpTrapCfgAdminEngineId": tnDevSysSnmpTrapCfgAdminEngineId,
       "tnDevSysSnmpTrapCfgSecurityName": tnDevSysSnmpTrapCfgSecurityName,
       "tnDevSysSnmpTrapCfgVersion": tnDevSysSnmpTrapCfgVersion,
       "tnDevSysSnmpTrapCfgInformMode": tnDevSysSnmpTrapCfgInformMode,
       "tnDevSysSnmpTrapCfgInformTimeout": tnDevSysSnmpTrapCfgInformTimeout,
       "tnDevSysSnmpTrapCfgInformRetry": tnDevSysSnmpTrapCfgInformRetry,
       "tnDevSysSnmpTrapServerCfgTable": tnDevSysSnmpTrapServerCfgTable,
       "tnDevSysSnmpTrapServerCfgEntry": tnDevSysSnmpTrapServerCfgEntry,
       "tnDevSysSnmpTrapServerCfgName": tnDevSysSnmpTrapServerCfgName,
       "tnDevSysSnmpTrapServerCfgMode": tnDevSysSnmpTrapServerCfgMode,
       "tnDevSysSnmpTrapServerCfgVersion": tnDevSysSnmpTrapServerCfgVersion,
       "tnDevSysSnmpTrapServerCfgCommunity": tnDevSysSnmpTrapServerCfgCommunity,
       "tnDevSysSnmpTrapServerCfgDstAddress": tnDevSysSnmpTrapServerCfgDstAddress,
       "tnDevSysSnmpTrapServerCfgDstPort": tnDevSysSnmpTrapServerCfgDstPort,
       "tnDevSysSnmpTrapServerCfgInformMode": tnDevSysSnmpTrapServerCfgInformMode,
       "tnDevSysSnmpTrapServerCfgInformTimeout": tnDevSysSnmpTrapServerCfgInformTimeout,
       "tnDevSysSnmpTrapServerCfgInformRetry": tnDevSysSnmpTrapServerCfgInformRetry,
       "tnDevSysSnmpTrapServerCfgEngineIdProbe": tnDevSysSnmpTrapServerCfgEngineIdProbe,
       "tnDevSysSnmpTrapServerCfgAdminEngineId": tnDevSysSnmpTrapServerCfgAdminEngineId,
       "tnDevSysSnmpTrapServerCfgSecurityName": tnDevSysSnmpTrapServerCfgSecurityName,
       "tnDevSysSnmpTrapServerCfgEvtWstart": tnDevSysSnmpTrapServerCfgEvtWstart,
       "tnDevSysSnmpTrapServerCfgEvtCstart": tnDevSysSnmpTrapServerCfgEvtCstart,
       "tnDevSysSnmpTrapServerCfgEvtLinkUp": tnDevSysSnmpTrapServerCfgEvtLinkUp,
       "tnDevSysSnmpTrapServerCfgEvtLinkDown": tnDevSysSnmpTrapServerCfgEvtLinkDown,
       "tnDevSysSnmpTrapServerCfgEvtLldp": tnDevSysSnmpTrapServerCfgEvtLldp,
       "tnDevSysSnmpTrapServerCfgEvtAuthFail": tnDevSysSnmpTrapServerCfgEvtAuthFail,
       "tnDevSysSnmpTrapServerCfgEvtStp": tnDevSysSnmpTrapServerCfgEvtStp,
       "tnDevSysSnmpTrapServerCfgEvtRmon": tnDevSysSnmpTrapServerCfgEvtRmon,
       "tnDevSysSnmpTrapServerCfgRowStatus": tnDevSysSnmpTrapServerCfgRowStatus,
       "tnDevSysSnmpTrapGlobalCfgMode": tnDevSysSnmpTrapGlobalCfgMode}
)
