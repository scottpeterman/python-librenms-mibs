# SNMP MIB module (CIENA-CES-TACACS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-TACACS-CLIENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:56 2025
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

(cienaCesStatistics,
 cienaCommon) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesStatistics",
    "cienaCommon")

(CienaGlobalState,
 CienaStatsClear) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState",
    "CienaStatsClear")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesTacacsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientMIB.setRevisions(
        ("2017-06-07 00:00",
         "2017-05-31 00:00",
         "2016-04-25 00:00",
         "2016-02-22 00:00",
         "2014-05-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TacacsString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 127),
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesTacacsClientMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientMIBObjects = _CienaCesTacacsClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1)
)
_CienaCesTacacsClient_ObjectIdentity = ObjectIdentity
cienaCesTacacsClient = _CienaCesTacacsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1)
)
_CienaCesTacacsClientGlobal_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientGlobal = _CienaCesTacacsClientGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1)
)
_CienaCesTacacsClientAdminState_Type = CienaGlobalState
_CienaCesTacacsClientAdminState_Object = MibScalar
cienaCesTacacsClientAdminState = _CienaCesTacacsClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 1),
    _CienaCesTacacsClientAdminState_Type()
)
cienaCesTacacsClientAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAdminState.setStatus("current")
_CienaCesTacacsClientOperState_Type = CienaGlobalState
_CienaCesTacacsClientOperState_Object = MibScalar
cienaCesTacacsClientOperState = _CienaCesTacacsClientOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 2),
    _CienaCesTacacsClientOperState_Type()
)
cienaCesTacacsClientOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientOperState.setStatus("current")


class _CienaCesTacacsClientTimeout_Type(Integer32):
    """Custom type cienaCesTacacsClientTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CienaCesTacacsClientTimeout_Type.__name__ = "Integer32"
_CienaCesTacacsClientTimeout_Object = MibScalar
cienaCesTacacsClientTimeout = _CienaCesTacacsClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 3),
    _CienaCesTacacsClientTimeout_Type()
)
cienaCesTacacsClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesTacacsClientTimeout.setUnits("seconds")


class _CienaCesTacacsClientRetries_Type(Integer32):
    """Custom type cienaCesTacacsClientRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CienaCesTacacsClientRetries_Type.__name__ = "Integer32"
_CienaCesTacacsClientRetries_Object = MibScalar
cienaCesTacacsClientRetries = _CienaCesTacacsClientRetries_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 4),
    _CienaCesTacacsClientRetries_Type()
)
cienaCesTacacsClientRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientRetries.setStatus("deprecated")


class _CienaCesTacacsClientPrivilegeLevelAdmin_Type(Integer32):
    """Custom type cienaCesTacacsClientPrivilegeLevelAdmin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_CienaCesTacacsClientPrivilegeLevelAdmin_Type.__name__ = "Integer32"
_CienaCesTacacsClientPrivilegeLevelAdmin_Object = MibScalar
cienaCesTacacsClientPrivilegeLevelAdmin = _CienaCesTacacsClientPrivilegeLevelAdmin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 5),
    _CienaCesTacacsClientPrivilegeLevelAdmin_Type()
)
cienaCesTacacsClientPrivilegeLevelAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientPrivilegeLevelAdmin.setStatus("current")


class _CienaCesTacacsClientPrivilegeLevelRW_Type(Integer32):
    """Custom type cienaCesTacacsClientPrivilegeLevelRW based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 14),
    )


_CienaCesTacacsClientPrivilegeLevelRW_Type.__name__ = "Integer32"
_CienaCesTacacsClientPrivilegeLevelRW_Object = MibScalar
cienaCesTacacsClientPrivilegeLevelRW = _CienaCesTacacsClientPrivilegeLevelRW_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 6),
    _CienaCesTacacsClientPrivilegeLevelRW_Type()
)
cienaCesTacacsClientPrivilegeLevelRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientPrivilegeLevelRW.setStatus("current")


class _CienaCesTacacsClientPrivilegeLevelDiag_Type(Integer32):
    """Custom type cienaCesTacacsClientPrivilegeLevelDiag based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 15),
    )


_CienaCesTacacsClientPrivilegeLevelDiag_Type.__name__ = "Integer32"
_CienaCesTacacsClientPrivilegeLevelDiag_Object = MibScalar
cienaCesTacacsClientPrivilegeLevelDiag = _CienaCesTacacsClientPrivilegeLevelDiag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 7),
    _CienaCesTacacsClientPrivilegeLevelDiag_Type()
)
cienaCesTacacsClientPrivilegeLevelDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientPrivilegeLevelDiag.setStatus("current")
_CienaCesTacacsClientAuthKey_Type = TacacsString
_CienaCesTacacsClientAuthKey_Object = MibScalar
cienaCesTacacsClientAuthKey = _CienaCesTacacsClientAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 8),
    _CienaCesTacacsClientAuthKey_Type()
)
cienaCesTacacsClientAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthKey.setStatus("current")


class _CienaCesTacacsClientAuthenticationAdminState_Type(CienaGlobalState):
    """Custom type cienaCesTacacsClientAuthenticationAdminState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesTacacsClientAuthenticationAdminState_Type.__name__ = "CienaGlobalState"
_CienaCesTacacsClientAuthenticationAdminState_Object = MibScalar
cienaCesTacacsClientAuthenticationAdminState = _CienaCesTacacsClientAuthenticationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 9),
    _CienaCesTacacsClientAuthenticationAdminState_Type()
)
cienaCesTacacsClientAuthenticationAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationAdminState.setStatus("current")


class _CienaCesTacacsClientAuthorizationAdminState_Type(CienaGlobalState):
    """Custom type cienaCesTacacsClientAuthorizationAdminState based on CienaGlobalState"""
    defaultValue = 2


_CienaCesTacacsClientAuthorizationAdminState_Type.__name__ = "CienaGlobalState"
_CienaCesTacacsClientAuthorizationAdminState_Object = MibScalar
cienaCesTacacsClientAuthorizationAdminState = _CienaCesTacacsClientAuthorizationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 10),
    _CienaCesTacacsClientAuthorizationAdminState_Type()
)
cienaCesTacacsClientAuthorizationAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationAdminState.setStatus("current")


class _CienaCesTacacsClientAccountingAdminState_Type(CienaGlobalState):
    """Custom type cienaCesTacacsClientAccountingAdminState based on CienaGlobalState"""
    defaultValue = 2


_CienaCesTacacsClientAccountingAdminState_Type.__name__ = "CienaGlobalState"
_CienaCesTacacsClientAccountingAdminState_Object = MibScalar
cienaCesTacacsClientAccountingAdminState = _CienaCesTacacsClientAccountingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 11),
    _CienaCesTacacsClientAccountingAdminState_Type()
)
cienaCesTacacsClientAccountingAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingAdminState.setStatus("current")


class _CienaCesTacacsClientSyslogAdminState_Type(CienaGlobalState):
    """Custom type cienaCesTacacsClientSyslogAdminState based on CienaGlobalState"""
    defaultValue = 2


_CienaCesTacacsClientSyslogAdminState_Type.__name__ = "CienaGlobalState"
_CienaCesTacacsClientSyslogAdminState_Object = MibScalar
cienaCesTacacsClientSyslogAdminState = _CienaCesTacacsClientSyslogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 12),
    _CienaCesTacacsClientSyslogAdminState_Type()
)
cienaCesTacacsClientSyslogAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientSyslogAdminState.setStatus("current")


class _CienaCesTacacsClientAccountingSession_Type(Integer32):
    """Custom type cienaCesTacacsClientAccountingSession based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesTacacsClientAccountingSession_Type.__name__ = "Integer32"
_CienaCesTacacsClientAccountingSession_Object = MibScalar
cienaCesTacacsClientAccountingSession = _CienaCesTacacsClientAccountingSession_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 13),
    _CienaCesTacacsClientAccountingSession_Type()
)
cienaCesTacacsClientAccountingSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingSession.setStatus("current")


class _CienaCesTacacsClientAccountingCommand_Type(Integer32):
    """Custom type cienaCesTacacsClientAccountingCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesTacacsClientAccountingCommand_Type.__name__ = "Integer32"
_CienaCesTacacsClientAccountingCommand_Object = MibScalar
cienaCesTacacsClientAccountingCommand = _CienaCesTacacsClientAccountingCommand_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 14),
    _CienaCesTacacsClientAccountingCommand_Type()
)
cienaCesTacacsClientAccountingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingCommand.setStatus("current")


class _CienaCesTacacsClientGlobalServers_Type(Integer32):
    """Custom type cienaCesTacacsClientGlobalServers based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesTacacsClientGlobalServers_Type.__name__ = "Integer32"
_CienaCesTacacsClientGlobalServers_Object = MibScalar
cienaCesTacacsClientGlobalServers = _CienaCesTacacsClientGlobalServers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 15),
    _CienaCesTacacsClientGlobalServers_Type()
)
cienaCesTacacsClientGlobalServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalServers.setStatus("current")


class _CienaCesTacacsClientSearchMethod_Type(Integer32):
    """Custom type cienaCesTacacsClientSearchMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priority", 1),
          ("cached", 2))
    )


_CienaCesTacacsClientSearchMethod_Type.__name__ = "Integer32"
_CienaCesTacacsClientSearchMethod_Object = MibScalar
cienaCesTacacsClientSearchMethod = _CienaCesTacacsClientSearchMethod_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 16),
    _CienaCesTacacsClientSearchMethod_Type()
)
cienaCesTacacsClientSearchMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientSearchMethod.setStatus("current")
_CienaCesTacacsClientAuthKeyUnset_Type = TruthValue
_CienaCesTacacsClientAuthKeyUnset_Object = MibScalar
cienaCesTacacsClientAuthKeyUnset = _CienaCesTacacsClientAuthKeyUnset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 17),
    _CienaCesTacacsClientAuthKeyUnset_Type()
)
cienaCesTacacsClientAuthKeyUnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthKeyUnset.setStatus("current")


class _CienaCesTacacsClientKeyMinLen_Type(Integer32):
    """Custom type cienaCesTacacsClientKeyMinLen based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_CienaCesTacacsClientKeyMinLen_Type.__name__ = "Integer32"
_CienaCesTacacsClientKeyMinLen_Object = MibScalar
cienaCesTacacsClientKeyMinLen = _CienaCesTacacsClientKeyMinLen_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 1, 18),
    _CienaCesTacacsClientKeyMinLen_Type()
)
cienaCesTacacsClientKeyMinLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientKeyMinLen.setStatus("current")
_CienaCesTacacsClientServer_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientServer = _CienaCesTacacsClientServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2)
)
_CienaCesTacacsClientServerTable_Object = MibTable
cienaCesTacacsClientServerTable = _CienaCesTacacsClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerTable.setStatus("current")
_CienaCesTacacsClientServerEntry_Object = MibTableRow
cienaCesTacacsClientServerEntry = _CienaCesTacacsClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1)
)
cienaCesTacacsClientServerEntry.setIndexNames(
    (0, "CIENA-CES-TACACS-CLIENT-MIB", "cienaCesTacacsClientServerIndex"),
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerEntry.setStatus("current")


class _CienaCesTacacsClientServerIndex_Type(Integer32):
    """Custom type cienaCesTacacsClientServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesTacacsClientServerIndex_Type.__name__ = "Integer32"
_CienaCesTacacsClientServerIndex_Object = MibTableColumn
cienaCesTacacsClientServerIndex = _CienaCesTacacsClientServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 1),
    _CienaCesTacacsClientServerIndex_Type()
)
cienaCesTacacsClientServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerIndex.setStatus("current")


class _CienaCesTacacsClientServerAddr_Type(DisplayString):
    """Custom type cienaCesTacacsClientServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CienaCesTacacsClientServerAddr_Type.__name__ = "DisplayString"
_CienaCesTacacsClientServerAddr_Object = MibTableColumn
cienaCesTacacsClientServerAddr = _CienaCesTacacsClientServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 2),
    _CienaCesTacacsClientServerAddr_Type()
)
cienaCesTacacsClientServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerAddr.setStatus("current")
_CienaCesTacacsClientServerResolvedAddr_Type = IpAddress
_CienaCesTacacsClientServerResolvedAddr_Object = MibTableColumn
cienaCesTacacsClientServerResolvedAddr = _CienaCesTacacsClientServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 3),
    _CienaCesTacacsClientServerResolvedAddr_Type()
)
cienaCesTacacsClientServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerResolvedAddr.setStatus("current")


class _CienaCesTacacsClientServerPriority_Type(Integer32):
    """Custom type cienaCesTacacsClientServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesTacacsClientServerPriority_Type.__name__ = "Integer32"
_CienaCesTacacsClientServerPriority_Object = MibTableColumn
cienaCesTacacsClientServerPriority = _CienaCesTacacsClientServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 4),
    _CienaCesTacacsClientServerPriority_Type()
)
cienaCesTacacsClientServerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerPriority.setStatus("current")


class _CienaCesTacacsClientServerAuthPort_Type(Integer32):
    """Custom type cienaCesTacacsClientServerAuthPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesTacacsClientServerAuthPort_Type.__name__ = "Integer32"
_CienaCesTacacsClientServerAuthPort_Object = MibTableColumn
cienaCesTacacsClientServerAuthPort = _CienaCesTacacsClientServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 5),
    _CienaCesTacacsClientServerAuthPort_Type()
)
cienaCesTacacsClientServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerAuthPort.setStatus("current")


class _CienaCesTacacsClientServerApplication_Type(Integer32):
    """Custom type cienaCesTacacsClientServerApplication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userLogin", 1),
          ("dot1x", 2),
          ("all", 3))
    )


_CienaCesTacacsClientServerApplication_Type.__name__ = "Integer32"
_CienaCesTacacsClientServerApplication_Object = MibTableColumn
cienaCesTacacsClientServerApplication = _CienaCesTacacsClientServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 6),
    _CienaCesTacacsClientServerApplication_Type()
)
cienaCesTacacsClientServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerApplication.setStatus("deprecated")
_CienaCesTacacsClientServerStatus_Type = RowStatus
_CienaCesTacacsClientServerStatus_Object = MibTableColumn
cienaCesTacacsClientServerStatus = _CienaCesTacacsClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 7),
    _CienaCesTacacsClientServerStatus_Type()
)
cienaCesTacacsClientServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerStatus.setStatus("current")
_CienaCesTacacsClientServerResolvedInetAddrType_Type = InetAddressType
_CienaCesTacacsClientServerResolvedInetAddrType_Object = MibTableColumn
cienaCesTacacsClientServerResolvedInetAddrType = _CienaCesTacacsClientServerResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 8),
    _CienaCesTacacsClientServerResolvedInetAddrType_Type()
)
cienaCesTacacsClientServerResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerResolvedInetAddrType.setStatus("current")
_CienaCesTacacsClientServerResolvedInetAddr_Type = InetAddress
_CienaCesTacacsClientServerResolvedInetAddr_Object = MibTableColumn
cienaCesTacacsClientServerResolvedInetAddr = _CienaCesTacacsClientServerResolvedInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 2, 1, 1, 9),
    _CienaCesTacacsClientServerResolvedInetAddr_Type()
)
cienaCesTacacsClientServerResolvedInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientServerResolvedInetAddr.setStatus("current")
_CienaCesTacacsClientGlobalStatistics_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientGlobalStatistics = _CienaCesTacacsClientGlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3)
)
_CienaCesTacacsClientGlobalStatisticsTable_Object = MibTable
cienaCesTacacsClientGlobalStatisticsTable = _CienaCesTacacsClientGlobalStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalStatisticsTable.setStatus("current")
_CienaCesTacacsClientGlobalStatisticsEntry_Object = MibTableRow
cienaCesTacacsClientGlobalStatisticsEntry = _CienaCesTacacsClientGlobalStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1)
)
cienaCesTacacsClientGlobalStatisticsEntry.setIndexNames(
    (0, "CIENA-CES-TACACS-CLIENT-MIB", "cienaCesTacacsClientServerIndex"),
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalStatisticsEntry.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationAccessRequests_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationAccessRequests_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationAccessRequests = _CienaCesTacacsClientGlobalAuthenticationAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 1),
    _CienaCesTacacsClientGlobalAuthenticationAccessRequests_Type()
)
cienaCesTacacsClientGlobalAuthenticationAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationAccessRequests.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationAccessRetransmissions_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationAccessRetransmissions_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationAccessRetransmissions = _CienaCesTacacsClientGlobalAuthenticationAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 2),
    _CienaCesTacacsClientGlobalAuthenticationAccessRetransmissions_Type()
)
cienaCesTacacsClientGlobalAuthenticationAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationAccessRetransmissions.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationAccessAccepts_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationAccessAccepts_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationAccessAccepts = _CienaCesTacacsClientGlobalAuthenticationAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 3),
    _CienaCesTacacsClientGlobalAuthenticationAccessAccepts_Type()
)
cienaCesTacacsClientGlobalAuthenticationAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationAccessAccepts.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationAccessRejects_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationAccessRejects_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationAccessRejects = _CienaCesTacacsClientGlobalAuthenticationAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 4),
    _CienaCesTacacsClientGlobalAuthenticationAccessRejects_Type()
)
cienaCesTacacsClientGlobalAuthenticationAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationAccessRejects.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses = _CienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 5),
    _CienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses_Type()
)
cienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationBadAuthenticators_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationBadAuthenticators_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationBadAuthenticators = _CienaCesTacacsClientGlobalAuthenticationBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 6),
    _CienaCesTacacsClientGlobalAuthenticationBadAuthenticators_Type()
)
cienaCesTacacsClientGlobalAuthenticationBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationBadAuthenticators.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationTimeouts_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationTimeouts_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationTimeouts = _CienaCesTacacsClientGlobalAuthenticationTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 7),
    _CienaCesTacacsClientGlobalAuthenticationTimeouts_Type()
)
cienaCesTacacsClientGlobalAuthenticationTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationTimeouts.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationUnknownTypes_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationUnknownTypes_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationUnknownTypes = _CienaCesTacacsClientGlobalAuthenticationUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 8),
    _CienaCesTacacsClientGlobalAuthenticationUnknownTypes_Type()
)
cienaCesTacacsClientGlobalAuthenticationUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationUnknownTypes.setStatus("current")
_CienaCesTacacsClientGlobalAuthenticationBadHeaderSequence_Type = Counter32
_CienaCesTacacsClientGlobalAuthenticationBadHeaderSequence_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthenticationBadHeaderSequence = _CienaCesTacacsClientGlobalAuthenticationBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 9),
    _CienaCesTacacsClientGlobalAuthenticationBadHeaderSequence_Type()
)
cienaCesTacacsClientGlobalAuthenticationBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthenticationBadHeaderSequence.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationAccessRequests_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationAccessRequests_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationAccessRequests = _CienaCesTacacsClientGlobalAuthorizationAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 10),
    _CienaCesTacacsClientGlobalAuthorizationAccessRequests_Type()
)
cienaCesTacacsClientGlobalAuthorizationAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationAccessRequests.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationAccessRetransmissions_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationAccessRetransmissions_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationAccessRetransmissions = _CienaCesTacacsClientGlobalAuthorizationAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 11),
    _CienaCesTacacsClientGlobalAuthorizationAccessRetransmissions_Type()
)
cienaCesTacacsClientGlobalAuthorizationAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationAccessRetransmissions.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationAccessAccepts_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationAccessAccepts_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationAccessAccepts = _CienaCesTacacsClientGlobalAuthorizationAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 12),
    _CienaCesTacacsClientGlobalAuthorizationAccessAccepts_Type()
)
cienaCesTacacsClientGlobalAuthorizationAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationAccessAccepts.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationAccessRejects_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationAccessRejects_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationAccessRejects = _CienaCesTacacsClientGlobalAuthorizationAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 13),
    _CienaCesTacacsClientGlobalAuthorizationAccessRejects_Type()
)
cienaCesTacacsClientGlobalAuthorizationAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationAccessRejects.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons = _CienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 14),
    _CienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons_Type()
)
cienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationBadAuthenticators_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationBadAuthenticators_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationBadAuthenticators = _CienaCesTacacsClientGlobalAuthorizationBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 15),
    _CienaCesTacacsClientGlobalAuthorizationBadAuthenticators_Type()
)
cienaCesTacacsClientGlobalAuthorizationBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationBadAuthenticators.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationTimeouts_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationTimeouts_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationTimeouts = _CienaCesTacacsClientGlobalAuthorizationTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 16),
    _CienaCesTacacsClientGlobalAuthorizationTimeouts_Type()
)
cienaCesTacacsClientGlobalAuthorizationTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationTimeouts.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationUnknownTypes_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationUnknownTypes_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationUnknownTypes = _CienaCesTacacsClientGlobalAuthorizationUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 17),
    _CienaCesTacacsClientGlobalAuthorizationUnknownTypes_Type()
)
cienaCesTacacsClientGlobalAuthorizationUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationUnknownTypes.setStatus("current")
_CienaCesTacacsClientGlobalAuthorizationBadHeaderSequence_Type = Counter32
_CienaCesTacacsClientGlobalAuthorizationBadHeaderSequence_Object = MibTableColumn
cienaCesTacacsClientGlobalAuthorizationBadHeaderSequence = _CienaCesTacacsClientGlobalAuthorizationBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 18),
    _CienaCesTacacsClientGlobalAuthorizationBadHeaderSequence_Type()
)
cienaCesTacacsClientGlobalAuthorizationBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAuthorizationBadHeaderSequence.setStatus("current")
_CienaCesTacacsClientGlobalAccountingAccessRequests_Type = Counter32
_CienaCesTacacsClientGlobalAccountingAccessRequests_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingAccessRequests = _CienaCesTacacsClientGlobalAccountingAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 19),
    _CienaCesTacacsClientGlobalAccountingAccessRequests_Type()
)
cienaCesTacacsClientGlobalAccountingAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingAccessRequests.setStatus("current")
_CienaCesTacacsClientGlobalAccountingAccessRetransmissions_Type = Counter32
_CienaCesTacacsClientGlobalAccountingAccessRetransmissions_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingAccessRetransmissions = _CienaCesTacacsClientGlobalAccountingAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 20),
    _CienaCesTacacsClientGlobalAccountingAccessRetransmissions_Type()
)
cienaCesTacacsClientGlobalAccountingAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingAccessRetransmissions.setStatus("current")
_CienaCesTacacsClientGlobalAccountingAccessAccepts_Type = Counter32
_CienaCesTacacsClientGlobalAccountingAccessAccepts_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingAccessAccepts = _CienaCesTacacsClientGlobalAccountingAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 21),
    _CienaCesTacacsClientGlobalAccountingAccessAccepts_Type()
)
cienaCesTacacsClientGlobalAccountingAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingAccessAccepts.setStatus("current")
_CienaCesTacacsClientGlobalAccountingAccessRejects_Type = Counter32
_CienaCesTacacsClientGlobalAccountingAccessRejects_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingAccessRejects = _CienaCesTacacsClientGlobalAccountingAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 22),
    _CienaCesTacacsClientGlobalAccountingAccessRejects_Type()
)
cienaCesTacacsClientGlobalAccountingAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingAccessRejects.setStatus("current")
_CienaCesTacacsClientGlobalAccountingMalformedAccessResponses_Type = Counter32
_CienaCesTacacsClientGlobalAccountingMalformedAccessResponses_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingMalformedAccessResponses = _CienaCesTacacsClientGlobalAccountingMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 23),
    _CienaCesTacacsClientGlobalAccountingMalformedAccessResponses_Type()
)
cienaCesTacacsClientGlobalAccountingMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingMalformedAccessResponses.setStatus("current")
_CienaCesTacacsClientGlobalAccountingBadAuthenticators_Type = Counter32
_CienaCesTacacsClientGlobalAccountingBadAuthenticators_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingBadAuthenticators = _CienaCesTacacsClientGlobalAccountingBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 24),
    _CienaCesTacacsClientGlobalAccountingBadAuthenticators_Type()
)
cienaCesTacacsClientGlobalAccountingBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingBadAuthenticators.setStatus("current")
_CienaCesTacacsClientGlobalAccountingTimeouts_Type = Counter32
_CienaCesTacacsClientGlobalAccountingTimeouts_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingTimeouts = _CienaCesTacacsClientGlobalAccountingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 25),
    _CienaCesTacacsClientGlobalAccountingTimeouts_Type()
)
cienaCesTacacsClientGlobalAccountingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingTimeouts.setStatus("current")
_CienaCesTacacsClientGlobalAccountingUnknownTypes_Type = Counter32
_CienaCesTacacsClientGlobalAccountingUnknownTypes_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingUnknownTypes = _CienaCesTacacsClientGlobalAccountingUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 26),
    _CienaCesTacacsClientGlobalAccountingUnknownTypes_Type()
)
cienaCesTacacsClientGlobalAccountingUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingUnknownTypes.setStatus("current")
_CienaCesTacacsClientGlobalAccountingBadHeaderSequence_Type = Counter32
_CienaCesTacacsClientGlobalAccountingBadHeaderSequence_Object = MibTableColumn
cienaCesTacacsClientGlobalAccountingBadHeaderSequence = _CienaCesTacacsClientGlobalAccountingBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 27),
    _CienaCesTacacsClientGlobalAccountingBadHeaderSequence_Type()
)
cienaCesTacacsClientGlobalAccountingBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalAccountingBadHeaderSequence.setStatus("current")


class _CienaCesTacacsClientGlobalServerClearStatistics_Type(CienaStatsClear):
    """Custom type cienaCesTacacsClientGlobalServerClearStatistics based on CienaStatsClear"""
    defaultValue = 0


_CienaCesTacacsClientGlobalServerClearStatistics_Type.__name__ = "CienaStatsClear"
_CienaCesTacacsClientGlobalServerClearStatistics_Object = MibTableColumn
cienaCesTacacsClientGlobalServerClearStatistics = _CienaCesTacacsClientGlobalServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 3, 1, 1, 28),
    _CienaCesTacacsClientGlobalServerClearStatistics_Type()
)
cienaCesTacacsClientGlobalServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientGlobalServerClearStatistics.setStatus("current")
_CienaCesTacacsClientAuthentication_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientAuthentication = _CienaCesTacacsClientAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4)
)
_CienaCesTacacsClientAuthenticationServerTable_Object = MibTable
cienaCesTacacsClientAuthenticationServerTable = _CienaCesTacacsClientAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerTable.setStatus("current")
_CienaCesTacacsClientAuthenticationServerEntry_Object = MibTableRow
cienaCesTacacsClientAuthenticationServerEntry = _CienaCesTacacsClientAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1)
)
cienaCesTacacsClientAuthenticationServerEntry.setIndexNames(
    (0, "CIENA-CES-TACACS-CLIENT-MIB", "cienaCesTacacsClientAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerEntry.setStatus("current")


class _CienaCesTacacsClientAuthenticationServerIndex_Type(Integer32):
    """Custom type cienaCesTacacsClientAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesTacacsClientAuthenticationServerIndex_Type.__name__ = "Integer32"
_CienaCesTacacsClientAuthenticationServerIndex_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerIndex = _CienaCesTacacsClientAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 1),
    _CienaCesTacacsClientAuthenticationServerIndex_Type()
)
cienaCesTacacsClientAuthenticationServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerIndex.setStatus("current")


class _CienaCesTacacsClientAuthenticationServerAddr_Type(DisplayString):
    """Custom type cienaCesTacacsClientAuthenticationServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CienaCesTacacsClientAuthenticationServerAddr_Type.__name__ = "DisplayString"
_CienaCesTacacsClientAuthenticationServerAddr_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerAddr = _CienaCesTacacsClientAuthenticationServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 2),
    _CienaCesTacacsClientAuthenticationServerAddr_Type()
)
cienaCesTacacsClientAuthenticationServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerAddr.setStatus("current")
_CienaCesTacacsClientAuthenticationServerResolvedAddr_Type = IpAddress
_CienaCesTacacsClientAuthenticationServerResolvedAddr_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerResolvedAddr = _CienaCesTacacsClientAuthenticationServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 3),
    _CienaCesTacacsClientAuthenticationServerResolvedAddr_Type()
)
cienaCesTacacsClientAuthenticationServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerResolvedAddr.setStatus("current")


class _CienaCesTacacsClientAuthenticationServerPriority_Type(Integer32):
    """Custom type cienaCesTacacsClientAuthenticationServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesTacacsClientAuthenticationServerPriority_Type.__name__ = "Integer32"
_CienaCesTacacsClientAuthenticationServerPriority_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerPriority = _CienaCesTacacsClientAuthenticationServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 4),
    _CienaCesTacacsClientAuthenticationServerPriority_Type()
)
cienaCesTacacsClientAuthenticationServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerPriority.setStatus("current")


class _CienaCesTacacsClientAuthenticationServerAuthPort_Type(Integer32):
    """Custom type cienaCesTacacsClientAuthenticationServerAuthPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesTacacsClientAuthenticationServerAuthPort_Type.__name__ = "Integer32"
_CienaCesTacacsClientAuthenticationServerAuthPort_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerAuthPort = _CienaCesTacacsClientAuthenticationServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 5),
    _CienaCesTacacsClientAuthenticationServerAuthPort_Type()
)
cienaCesTacacsClientAuthenticationServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerAuthPort.setStatus("current")
_CienaCesTacacsClientAuthenticationServerAccessRequests_Type = Counter32
_CienaCesTacacsClientAuthenticationServerAccessRequests_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerAccessRequests = _CienaCesTacacsClientAuthenticationServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 6),
    _CienaCesTacacsClientAuthenticationServerAccessRequests_Type()
)
cienaCesTacacsClientAuthenticationServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerAccessRequests.setStatus("current")
_CienaCesTacacsClientAuthenticationServerAccessRetransmissions_Type = Counter32
_CienaCesTacacsClientAuthenticationServerAccessRetransmissions_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerAccessRetransmissions = _CienaCesTacacsClientAuthenticationServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 7),
    _CienaCesTacacsClientAuthenticationServerAccessRetransmissions_Type()
)
cienaCesTacacsClientAuthenticationServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerAccessRetransmissions.setStatus("current")
_CienaCesTacacsClientAuthenticationServerAccessAccepts_Type = Counter32
_CienaCesTacacsClientAuthenticationServerAccessAccepts_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerAccessAccepts = _CienaCesTacacsClientAuthenticationServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 8),
    _CienaCesTacacsClientAuthenticationServerAccessAccepts_Type()
)
cienaCesTacacsClientAuthenticationServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerAccessAccepts.setStatus("current")
_CienaCesTacacsClientAuthenticationServerAccessRejects_Type = Counter32
_CienaCesTacacsClientAuthenticationServerAccessRejects_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerAccessRejects = _CienaCesTacacsClientAuthenticationServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 9),
    _CienaCesTacacsClientAuthenticationServerAccessRejects_Type()
)
cienaCesTacacsClientAuthenticationServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerAccessRejects.setStatus("current")
_CienaCesTacacsClientAuthenticationServerMalformedAccessResponses_Type = Counter32
_CienaCesTacacsClientAuthenticationServerMalformedAccessResponses_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerMalformedAccessResponses = _CienaCesTacacsClientAuthenticationServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 10),
    _CienaCesTacacsClientAuthenticationServerMalformedAccessResponses_Type()
)
cienaCesTacacsClientAuthenticationServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerMalformedAccessResponses.setStatus("current")
_CienaCesTacacsClientAuthenticationServerBadAuthenticators_Type = Counter32
_CienaCesTacacsClientAuthenticationServerBadAuthenticators_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerBadAuthenticators = _CienaCesTacacsClientAuthenticationServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 11),
    _CienaCesTacacsClientAuthenticationServerBadAuthenticators_Type()
)
cienaCesTacacsClientAuthenticationServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerBadAuthenticators.setStatus("current")
_CienaCesTacacsClientAuthenticationServerTimeouts_Type = Counter32
_CienaCesTacacsClientAuthenticationServerTimeouts_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerTimeouts = _CienaCesTacacsClientAuthenticationServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 13),
    _CienaCesTacacsClientAuthenticationServerTimeouts_Type()
)
cienaCesTacacsClientAuthenticationServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerTimeouts.setStatus("current")
_CienaCesTacacsClientAuthenticationServerUnknownTypes_Type = Counter32
_CienaCesTacacsClientAuthenticationServerUnknownTypes_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerUnknownTypes = _CienaCesTacacsClientAuthenticationServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 14),
    _CienaCesTacacsClientAuthenticationServerUnknownTypes_Type()
)
cienaCesTacacsClientAuthenticationServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerUnknownTypes.setStatus("current")
_CienaCesTacacsClientAuthenticationServerBadHeaderSequence_Type = Counter32
_CienaCesTacacsClientAuthenticationServerBadHeaderSequence_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerBadHeaderSequence = _CienaCesTacacsClientAuthenticationServerBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 15),
    _CienaCesTacacsClientAuthenticationServerBadHeaderSequence_Type()
)
cienaCesTacacsClientAuthenticationServerBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerBadHeaderSequence.setStatus("current")
_CienaCesTacacsClientAuthenticationServerStatus_Type = RowStatus
_CienaCesTacacsClientAuthenticationServerStatus_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerStatus = _CienaCesTacacsClientAuthenticationServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 16),
    _CienaCesTacacsClientAuthenticationServerStatus_Type()
)
cienaCesTacacsClientAuthenticationServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerStatus.setStatus("current")


class _CienaCesTacacsClientAuthenticationServerApplication_Type(Integer32):
    """Custom type cienaCesTacacsClientAuthenticationServerApplication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userLogin", 1),
          ("dot1x", 2),
          ("all", 3))
    )


_CienaCesTacacsClientAuthenticationServerApplication_Type.__name__ = "Integer32"
_CienaCesTacacsClientAuthenticationServerApplication_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerApplication = _CienaCesTacacsClientAuthenticationServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 17),
    _CienaCesTacacsClientAuthenticationServerApplication_Type()
)
cienaCesTacacsClientAuthenticationServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerApplication.setStatus("deprecated")


class _CienaCesTacacsClientAuthenticationServerClearStatistics_Type(CienaStatsClear):
    """Custom type cienaCesTacacsClientAuthenticationServerClearStatistics based on CienaStatsClear"""
    defaultValue = 0


_CienaCesTacacsClientAuthenticationServerClearStatistics_Type.__name__ = "CienaStatsClear"
_CienaCesTacacsClientAuthenticationServerClearStatistics_Object = MibTableColumn
cienaCesTacacsClientAuthenticationServerClearStatistics = _CienaCesTacacsClientAuthenticationServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 4, 1, 1, 18),
    _CienaCesTacacsClientAuthenticationServerClearStatistics_Type()
)
cienaCesTacacsClientAuthenticationServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthenticationServerClearStatistics.setStatus("current")
_CienaCesTacacsClientAuthorization_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientAuthorization = _CienaCesTacacsClientAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5)
)
_CienaCesTacacsClientAuthorizationServerTable_Object = MibTable
cienaCesTacacsClientAuthorizationServerTable = _CienaCesTacacsClientAuthorizationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerTable.setStatus("current")
_CienaCesTacacsClientAuthorizationServerEntry_Object = MibTableRow
cienaCesTacacsClientAuthorizationServerEntry = _CienaCesTacacsClientAuthorizationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1)
)
cienaCesTacacsClientAuthorizationServerEntry.setIndexNames(
    (0, "CIENA-CES-TACACS-CLIENT-MIB", "cienaCesTacacsClientAuthorizationServerIndex"),
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerEntry.setStatus("current")


class _CienaCesTacacsClientAuthorizationServerIndex_Type(Integer32):
    """Custom type cienaCesTacacsClientAuthorizationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesTacacsClientAuthorizationServerIndex_Type.__name__ = "Integer32"
_CienaCesTacacsClientAuthorizationServerIndex_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerIndex = _CienaCesTacacsClientAuthorizationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 1),
    _CienaCesTacacsClientAuthorizationServerIndex_Type()
)
cienaCesTacacsClientAuthorizationServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerIndex.setStatus("current")


class _CienaCesTacacsClientAuthorizationServerAddr_Type(DisplayString):
    """Custom type cienaCesTacacsClientAuthorizationServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CienaCesTacacsClientAuthorizationServerAddr_Type.__name__ = "DisplayString"
_CienaCesTacacsClientAuthorizationServerAddr_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerAddr = _CienaCesTacacsClientAuthorizationServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 2),
    _CienaCesTacacsClientAuthorizationServerAddr_Type()
)
cienaCesTacacsClientAuthorizationServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerAddr.setStatus("current")
_CienaCesTacacsClientAuthorizationServerResolvedAddr_Type = IpAddress
_CienaCesTacacsClientAuthorizationServerResolvedAddr_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerResolvedAddr = _CienaCesTacacsClientAuthorizationServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 3),
    _CienaCesTacacsClientAuthorizationServerResolvedAddr_Type()
)
cienaCesTacacsClientAuthorizationServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerResolvedAddr.setStatus("current")


class _CienaCesTacacsClientAuthorizationServerPriority_Type(Integer32):
    """Custom type cienaCesTacacsClientAuthorizationServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesTacacsClientAuthorizationServerPriority_Type.__name__ = "Integer32"
_CienaCesTacacsClientAuthorizationServerPriority_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerPriority = _CienaCesTacacsClientAuthorizationServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 4),
    _CienaCesTacacsClientAuthorizationServerPriority_Type()
)
cienaCesTacacsClientAuthorizationServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerPriority.setStatus("current")


class _CienaCesTacacsClientAuthorizationServerAuthPort_Type(Integer32):
    """Custom type cienaCesTacacsClientAuthorizationServerAuthPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesTacacsClientAuthorizationServerAuthPort_Type.__name__ = "Integer32"
_CienaCesTacacsClientAuthorizationServerAuthPort_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerAuthPort = _CienaCesTacacsClientAuthorizationServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 5),
    _CienaCesTacacsClientAuthorizationServerAuthPort_Type()
)
cienaCesTacacsClientAuthorizationServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerAuthPort.setStatus("current")
_CienaCesTacacsClientAuthorizationServerAccessRequests_Type = Counter32
_CienaCesTacacsClientAuthorizationServerAccessRequests_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerAccessRequests = _CienaCesTacacsClientAuthorizationServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 6),
    _CienaCesTacacsClientAuthorizationServerAccessRequests_Type()
)
cienaCesTacacsClientAuthorizationServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerAccessRequests.setStatus("current")
_CienaCesTacacsClientAuthorizationServerAccessRetransmissions_Type = Counter32
_CienaCesTacacsClientAuthorizationServerAccessRetransmissions_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerAccessRetransmissions = _CienaCesTacacsClientAuthorizationServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 7),
    _CienaCesTacacsClientAuthorizationServerAccessRetransmissions_Type()
)
cienaCesTacacsClientAuthorizationServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerAccessRetransmissions.setStatus("current")
_CienaCesTacacsClientAuthorizationServerAccessAccepts_Type = Counter32
_CienaCesTacacsClientAuthorizationServerAccessAccepts_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerAccessAccepts = _CienaCesTacacsClientAuthorizationServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 8),
    _CienaCesTacacsClientAuthorizationServerAccessAccepts_Type()
)
cienaCesTacacsClientAuthorizationServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerAccessAccepts.setStatus("current")
_CienaCesTacacsClientAuthorizationServerAccessRejects_Type = Counter32
_CienaCesTacacsClientAuthorizationServerAccessRejects_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerAccessRejects = _CienaCesTacacsClientAuthorizationServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 9),
    _CienaCesTacacsClientAuthorizationServerAccessRejects_Type()
)
cienaCesTacacsClientAuthorizationServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerAccessRejects.setStatus("current")
_CienaCesTacacsClientAuthorizationServerMalformedAccessResponses_Type = Counter32
_CienaCesTacacsClientAuthorizationServerMalformedAccessResponses_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerMalformedAccessResponses = _CienaCesTacacsClientAuthorizationServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 10),
    _CienaCesTacacsClientAuthorizationServerMalformedAccessResponses_Type()
)
cienaCesTacacsClientAuthorizationServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerMalformedAccessResponses.setStatus("current")
_CienaCesTacacsClientAuthorizationServerBadAuthenticators_Type = Counter32
_CienaCesTacacsClientAuthorizationServerBadAuthenticators_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerBadAuthenticators = _CienaCesTacacsClientAuthorizationServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 11),
    _CienaCesTacacsClientAuthorizationServerBadAuthenticators_Type()
)
cienaCesTacacsClientAuthorizationServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerBadAuthenticators.setStatus("current")
_CienaCesTacacsClientAuthorizationServerTimeouts_Type = Counter32
_CienaCesTacacsClientAuthorizationServerTimeouts_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerTimeouts = _CienaCesTacacsClientAuthorizationServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 12),
    _CienaCesTacacsClientAuthorizationServerTimeouts_Type()
)
cienaCesTacacsClientAuthorizationServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerTimeouts.setStatus("current")
_CienaCesTacacsClientAuthorizationServerUnknownTypes_Type = Counter32
_CienaCesTacacsClientAuthorizationServerUnknownTypes_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerUnknownTypes = _CienaCesTacacsClientAuthorizationServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 13),
    _CienaCesTacacsClientAuthorizationServerUnknownTypes_Type()
)
cienaCesTacacsClientAuthorizationServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerUnknownTypes.setStatus("current")
_CienaCesTacacsClientAuthorizationServerBadHeaderSequence_Type = Counter32
_CienaCesTacacsClientAuthorizationServerBadHeaderSequence_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerBadHeaderSequence = _CienaCesTacacsClientAuthorizationServerBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 14),
    _CienaCesTacacsClientAuthorizationServerBadHeaderSequence_Type()
)
cienaCesTacacsClientAuthorizationServerBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerBadHeaderSequence.setStatus("current")
_CienaCesTacacsClientAuthorizationServerStatus_Type = RowStatus
_CienaCesTacacsClientAuthorizationServerStatus_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerStatus = _CienaCesTacacsClientAuthorizationServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 15),
    _CienaCesTacacsClientAuthorizationServerStatus_Type()
)
cienaCesTacacsClientAuthorizationServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerStatus.setStatus("current")


class _CienaCesTacacsClientAuthorizationServerApplication_Type(Integer32):
    """Custom type cienaCesTacacsClientAuthorizationServerApplication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userLogin", 1),
          ("dot1x", 2),
          ("all", 3))
    )


_CienaCesTacacsClientAuthorizationServerApplication_Type.__name__ = "Integer32"
_CienaCesTacacsClientAuthorizationServerApplication_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerApplication = _CienaCesTacacsClientAuthorizationServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 16),
    _CienaCesTacacsClientAuthorizationServerApplication_Type()
)
cienaCesTacacsClientAuthorizationServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerApplication.setStatus("deprecated")


class _CienaCesTacacsClientAuthorizationServerClearStatistics_Type(CienaStatsClear):
    """Custom type cienaCesTacacsClientAuthorizationServerClearStatistics based on CienaStatsClear"""
    defaultValue = 0


_CienaCesTacacsClientAuthorizationServerClearStatistics_Type.__name__ = "CienaStatsClear"
_CienaCesTacacsClientAuthorizationServerClearStatistics_Object = MibTableColumn
cienaCesTacacsClientAuthorizationServerClearStatistics = _CienaCesTacacsClientAuthorizationServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 5, 1, 1, 17),
    _CienaCesTacacsClientAuthorizationServerClearStatistics_Type()
)
cienaCesTacacsClientAuthorizationServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAuthorizationServerClearStatistics.setStatus("current")
_CienaCesTacacsClientAccounting_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientAccounting = _CienaCesTacacsClientAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6)
)
_CienaCesTacacsClientAccountingServerTable_Object = MibTable
cienaCesTacacsClientAccountingServerTable = _CienaCesTacacsClientAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerTable.setStatus("current")
_CienaCesTacacsClientAccountingServerEntry_Object = MibTableRow
cienaCesTacacsClientAccountingServerEntry = _CienaCesTacacsClientAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1)
)
cienaCesTacacsClientAccountingServerEntry.setIndexNames(
    (0, "CIENA-CES-TACACS-CLIENT-MIB", "cienaCesTacacsClientAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerEntry.setStatus("current")


class _CienaCesTacacsClientAccountingServerIndex_Type(Integer32):
    """Custom type cienaCesTacacsClientAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesTacacsClientAccountingServerIndex_Type.__name__ = "Integer32"
_CienaCesTacacsClientAccountingServerIndex_Object = MibTableColumn
cienaCesTacacsClientAccountingServerIndex = _CienaCesTacacsClientAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 1),
    _CienaCesTacacsClientAccountingServerIndex_Type()
)
cienaCesTacacsClientAccountingServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerIndex.setStatus("current")


class _CienaCesTacacsClientAccountingServerAddr_Type(DisplayString):
    """Custom type cienaCesTacacsClientAccountingServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CienaCesTacacsClientAccountingServerAddr_Type.__name__ = "DisplayString"
_CienaCesTacacsClientAccountingServerAddr_Object = MibTableColumn
cienaCesTacacsClientAccountingServerAddr = _CienaCesTacacsClientAccountingServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 2),
    _CienaCesTacacsClientAccountingServerAddr_Type()
)
cienaCesTacacsClientAccountingServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerAddr.setStatus("current")
_CienaCesTacacsClientAccountingServerResolvedAddr_Type = IpAddress
_CienaCesTacacsClientAccountingServerResolvedAddr_Object = MibTableColumn
cienaCesTacacsClientAccountingServerResolvedAddr = _CienaCesTacacsClientAccountingServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 3),
    _CienaCesTacacsClientAccountingServerResolvedAddr_Type()
)
cienaCesTacacsClientAccountingServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerResolvedAddr.setStatus("current")


class _CienaCesTacacsClientAccountingServerPriority_Type(Integer32):
    """Custom type cienaCesTacacsClientAccountingServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesTacacsClientAccountingServerPriority_Type.__name__ = "Integer32"
_CienaCesTacacsClientAccountingServerPriority_Object = MibTableColumn
cienaCesTacacsClientAccountingServerPriority = _CienaCesTacacsClientAccountingServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 4),
    _CienaCesTacacsClientAccountingServerPriority_Type()
)
cienaCesTacacsClientAccountingServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerPriority.setStatus("current")


class _CienaCesTacacsClientAccountingServerAuthPort_Type(Integer32):
    """Custom type cienaCesTacacsClientAccountingServerAuthPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesTacacsClientAccountingServerAuthPort_Type.__name__ = "Integer32"
_CienaCesTacacsClientAccountingServerAuthPort_Object = MibTableColumn
cienaCesTacacsClientAccountingServerAuthPort = _CienaCesTacacsClientAccountingServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 5),
    _CienaCesTacacsClientAccountingServerAuthPort_Type()
)
cienaCesTacacsClientAccountingServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerAuthPort.setStatus("current")
_CienaCesTacacsClientAccountingServerAccessRequests_Type = Counter32
_CienaCesTacacsClientAccountingServerAccessRequests_Object = MibTableColumn
cienaCesTacacsClientAccountingServerAccessRequests = _CienaCesTacacsClientAccountingServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 6),
    _CienaCesTacacsClientAccountingServerAccessRequests_Type()
)
cienaCesTacacsClientAccountingServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerAccessRequests.setStatus("current")
_CienaCesTacacsClientAccountingServerAccessRetransmissions_Type = Counter32
_CienaCesTacacsClientAccountingServerAccessRetransmissions_Object = MibTableColumn
cienaCesTacacsClientAccountingServerAccessRetransmissions = _CienaCesTacacsClientAccountingServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 7),
    _CienaCesTacacsClientAccountingServerAccessRetransmissions_Type()
)
cienaCesTacacsClientAccountingServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerAccessRetransmissions.setStatus("current")
_CienaCesTacacsClientAccountingServerAccessAccepts_Type = Counter32
_CienaCesTacacsClientAccountingServerAccessAccepts_Object = MibTableColumn
cienaCesTacacsClientAccountingServerAccessAccepts = _CienaCesTacacsClientAccountingServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 8),
    _CienaCesTacacsClientAccountingServerAccessAccepts_Type()
)
cienaCesTacacsClientAccountingServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerAccessAccepts.setStatus("current")
_CienaCesTacacsClientAccountingServerAccessRejects_Type = Counter32
_CienaCesTacacsClientAccountingServerAccessRejects_Object = MibTableColumn
cienaCesTacacsClientAccountingServerAccessRejects = _CienaCesTacacsClientAccountingServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 9),
    _CienaCesTacacsClientAccountingServerAccessRejects_Type()
)
cienaCesTacacsClientAccountingServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerAccessRejects.setStatus("current")
_CienaCesTacacsClientAccountingServerMalformedAccessResponses_Type = Counter32
_CienaCesTacacsClientAccountingServerMalformedAccessResponses_Object = MibTableColumn
cienaCesTacacsClientAccountingServerMalformedAccessResponses = _CienaCesTacacsClientAccountingServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 10),
    _CienaCesTacacsClientAccountingServerMalformedAccessResponses_Type()
)
cienaCesTacacsClientAccountingServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerMalformedAccessResponses.setStatus("current")
_CienaCesTacacsClientAccountingServerBadAuthenticators_Type = Counter32
_CienaCesTacacsClientAccountingServerBadAuthenticators_Object = MibTableColumn
cienaCesTacacsClientAccountingServerBadAuthenticators = _CienaCesTacacsClientAccountingServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 11),
    _CienaCesTacacsClientAccountingServerBadAuthenticators_Type()
)
cienaCesTacacsClientAccountingServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerBadAuthenticators.setStatus("current")
_CienaCesTacacsClientAccountingServerTimeouts_Type = Counter32
_CienaCesTacacsClientAccountingServerTimeouts_Object = MibTableColumn
cienaCesTacacsClientAccountingServerTimeouts = _CienaCesTacacsClientAccountingServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 12),
    _CienaCesTacacsClientAccountingServerTimeouts_Type()
)
cienaCesTacacsClientAccountingServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerTimeouts.setStatus("current")
_CienaCesTacacsClientAccountingServerUnknownTypes_Type = Counter32
_CienaCesTacacsClientAccountingServerUnknownTypes_Object = MibTableColumn
cienaCesTacacsClientAccountingServerUnknownTypes = _CienaCesTacacsClientAccountingServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 13),
    _CienaCesTacacsClientAccountingServerUnknownTypes_Type()
)
cienaCesTacacsClientAccountingServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerUnknownTypes.setStatus("current")
_CienaCesTacacsClientAccountingServerBadHeaderSequence_Type = Counter32
_CienaCesTacacsClientAccountingServerBadHeaderSequence_Object = MibTableColumn
cienaCesTacacsClientAccountingServerBadHeaderSequence = _CienaCesTacacsClientAccountingServerBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 14),
    _CienaCesTacacsClientAccountingServerBadHeaderSequence_Type()
)
cienaCesTacacsClientAccountingServerBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerBadHeaderSequence.setStatus("current")
_CienaCesTacacsClientAccountingServerStatus_Type = RowStatus
_CienaCesTacacsClientAccountingServerStatus_Object = MibTableColumn
cienaCesTacacsClientAccountingServerStatus = _CienaCesTacacsClientAccountingServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 15),
    _CienaCesTacacsClientAccountingServerStatus_Type()
)
cienaCesTacacsClientAccountingServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerStatus.setStatus("current")


class _CienaCesTacacsClientAccountingServerApplication_Type(Integer32):
    """Custom type cienaCesTacacsClientAccountingServerApplication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userLogin", 1),
          ("dot1x", 2),
          ("all", 3))
    )


_CienaCesTacacsClientAccountingServerApplication_Type.__name__ = "Integer32"
_CienaCesTacacsClientAccountingServerApplication_Object = MibTableColumn
cienaCesTacacsClientAccountingServerApplication = _CienaCesTacacsClientAccountingServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 16),
    _CienaCesTacacsClientAccountingServerApplication_Type()
)
cienaCesTacacsClientAccountingServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerApplication.setStatus("deprecated")


class _CienaCesTacacsClientAccountingServerClearStatistics_Type(CienaStatsClear):
    """Custom type cienaCesTacacsClientAccountingServerClearStatistics based on CienaStatsClear"""
    defaultValue = 0


_CienaCesTacacsClientAccountingServerClearStatistics_Type.__name__ = "CienaStatsClear"
_CienaCesTacacsClientAccountingServerClearStatistics_Object = MibTableColumn
cienaCesTacacsClientAccountingServerClearStatistics = _CienaCesTacacsClientAccountingServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 1, 1, 6, 1, 1, 17),
    _CienaCesTacacsClientAccountingServerClearStatistics_Type()
)
cienaCesTacacsClientAccountingServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesTacacsClientAccountingServerClearStatistics.setStatus("current")
_CienaCesTacacsClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientMIBNotificationPrefix = _CienaCesTacacsClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 2)
)
_CienaCesTacacsClientMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientMIBNotifications = _CienaCesTacacsClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 2, 0)
)
_CienaCesTacacsClientMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientMIBConformance = _CienaCesTacacsClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 3)
)
_CienaCesTacacsClientMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientMIBCompliances = _CienaCesTacacsClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 3, 1)
)
_CienaCesTacacsClientMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesTacacsClientMIBGroups = _CienaCesTacacsClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 3, 2)
)

# Managed Objects groups


# Notification objects

cienaCesTacacsClientConnectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 2, 2, 0, 1)
)
cienaCesTacacsClientConnectionFailed.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-TACACS-CLIENT-MIB", "cienaCesTacacsClientServerResolvedInetAddrType"),
        ("CIENA-CES-TACACS-CLIENT-MIB", "cienaCesTacacsClientServerResolvedInetAddr"))
)
if mibBuilder.loadTexts:
    cienaCesTacacsClientConnectionFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-TACACS-CLIENT-MIB",
    **{"TacacsString": TacacsString,
       "cienaCesTacacsClientMIB": cienaCesTacacsClientMIB,
       "cienaCesTacacsClientMIBObjects": cienaCesTacacsClientMIBObjects,
       "cienaCesTacacsClient": cienaCesTacacsClient,
       "cienaCesTacacsClientGlobal": cienaCesTacacsClientGlobal,
       "cienaCesTacacsClientAdminState": cienaCesTacacsClientAdminState,
       "cienaCesTacacsClientOperState": cienaCesTacacsClientOperState,
       "cienaCesTacacsClientTimeout": cienaCesTacacsClientTimeout,
       "cienaCesTacacsClientRetries": cienaCesTacacsClientRetries,
       "cienaCesTacacsClientPrivilegeLevelAdmin": cienaCesTacacsClientPrivilegeLevelAdmin,
       "cienaCesTacacsClientPrivilegeLevelRW": cienaCesTacacsClientPrivilegeLevelRW,
       "cienaCesTacacsClientPrivilegeLevelDiag": cienaCesTacacsClientPrivilegeLevelDiag,
       "cienaCesTacacsClientAuthKey": cienaCesTacacsClientAuthKey,
       "cienaCesTacacsClientAuthenticationAdminState": cienaCesTacacsClientAuthenticationAdminState,
       "cienaCesTacacsClientAuthorizationAdminState": cienaCesTacacsClientAuthorizationAdminState,
       "cienaCesTacacsClientAccountingAdminState": cienaCesTacacsClientAccountingAdminState,
       "cienaCesTacacsClientSyslogAdminState": cienaCesTacacsClientSyslogAdminState,
       "cienaCesTacacsClientAccountingSession": cienaCesTacacsClientAccountingSession,
       "cienaCesTacacsClientAccountingCommand": cienaCesTacacsClientAccountingCommand,
       "cienaCesTacacsClientGlobalServers": cienaCesTacacsClientGlobalServers,
       "cienaCesTacacsClientSearchMethod": cienaCesTacacsClientSearchMethod,
       "cienaCesTacacsClientAuthKeyUnset": cienaCesTacacsClientAuthKeyUnset,
       "cienaCesTacacsClientKeyMinLen": cienaCesTacacsClientKeyMinLen,
       "cienaCesTacacsClientServer": cienaCesTacacsClientServer,
       "cienaCesTacacsClientServerTable": cienaCesTacacsClientServerTable,
       "cienaCesTacacsClientServerEntry": cienaCesTacacsClientServerEntry,
       "cienaCesTacacsClientServerIndex": cienaCesTacacsClientServerIndex,
       "cienaCesTacacsClientServerAddr": cienaCesTacacsClientServerAddr,
       "cienaCesTacacsClientServerResolvedAddr": cienaCesTacacsClientServerResolvedAddr,
       "cienaCesTacacsClientServerPriority": cienaCesTacacsClientServerPriority,
       "cienaCesTacacsClientServerAuthPort": cienaCesTacacsClientServerAuthPort,
       "cienaCesTacacsClientServerApplication": cienaCesTacacsClientServerApplication,
       "cienaCesTacacsClientServerStatus": cienaCesTacacsClientServerStatus,
       "cienaCesTacacsClientServerResolvedInetAddrType": cienaCesTacacsClientServerResolvedInetAddrType,
       "cienaCesTacacsClientServerResolvedInetAddr": cienaCesTacacsClientServerResolvedInetAddr,
       "cienaCesTacacsClientGlobalStatistics": cienaCesTacacsClientGlobalStatistics,
       "cienaCesTacacsClientGlobalStatisticsTable": cienaCesTacacsClientGlobalStatisticsTable,
       "cienaCesTacacsClientGlobalStatisticsEntry": cienaCesTacacsClientGlobalStatisticsEntry,
       "cienaCesTacacsClientGlobalAuthenticationAccessRequests": cienaCesTacacsClientGlobalAuthenticationAccessRequests,
       "cienaCesTacacsClientGlobalAuthenticationAccessRetransmissions": cienaCesTacacsClientGlobalAuthenticationAccessRetransmissions,
       "cienaCesTacacsClientGlobalAuthenticationAccessAccepts": cienaCesTacacsClientGlobalAuthenticationAccessAccepts,
       "cienaCesTacacsClientGlobalAuthenticationAccessRejects": cienaCesTacacsClientGlobalAuthenticationAccessRejects,
       "cienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses": cienaCesTacacsClientGlobalAuthenticationMalformedAccessResponses,
       "cienaCesTacacsClientGlobalAuthenticationBadAuthenticators": cienaCesTacacsClientGlobalAuthenticationBadAuthenticators,
       "cienaCesTacacsClientGlobalAuthenticationTimeouts": cienaCesTacacsClientGlobalAuthenticationTimeouts,
       "cienaCesTacacsClientGlobalAuthenticationUnknownTypes": cienaCesTacacsClientGlobalAuthenticationUnknownTypes,
       "cienaCesTacacsClientGlobalAuthenticationBadHeaderSequence": cienaCesTacacsClientGlobalAuthenticationBadHeaderSequence,
       "cienaCesTacacsClientGlobalAuthorizationAccessRequests": cienaCesTacacsClientGlobalAuthorizationAccessRequests,
       "cienaCesTacacsClientGlobalAuthorizationAccessRetransmissions": cienaCesTacacsClientGlobalAuthorizationAccessRetransmissions,
       "cienaCesTacacsClientGlobalAuthorizationAccessAccepts": cienaCesTacacsClientGlobalAuthorizationAccessAccepts,
       "cienaCesTacacsClientGlobalAuthorizationAccessRejects": cienaCesTacacsClientGlobalAuthorizationAccessRejects,
       "cienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons": cienaCesTacacsClientGlobalAuthorizationMalformedAccessRespons,
       "cienaCesTacacsClientGlobalAuthorizationBadAuthenticators": cienaCesTacacsClientGlobalAuthorizationBadAuthenticators,
       "cienaCesTacacsClientGlobalAuthorizationTimeouts": cienaCesTacacsClientGlobalAuthorizationTimeouts,
       "cienaCesTacacsClientGlobalAuthorizationUnknownTypes": cienaCesTacacsClientGlobalAuthorizationUnknownTypes,
       "cienaCesTacacsClientGlobalAuthorizationBadHeaderSequence": cienaCesTacacsClientGlobalAuthorizationBadHeaderSequence,
       "cienaCesTacacsClientGlobalAccountingAccessRequests": cienaCesTacacsClientGlobalAccountingAccessRequests,
       "cienaCesTacacsClientGlobalAccountingAccessRetransmissions": cienaCesTacacsClientGlobalAccountingAccessRetransmissions,
       "cienaCesTacacsClientGlobalAccountingAccessAccepts": cienaCesTacacsClientGlobalAccountingAccessAccepts,
       "cienaCesTacacsClientGlobalAccountingAccessRejects": cienaCesTacacsClientGlobalAccountingAccessRejects,
       "cienaCesTacacsClientGlobalAccountingMalformedAccessResponses": cienaCesTacacsClientGlobalAccountingMalformedAccessResponses,
       "cienaCesTacacsClientGlobalAccountingBadAuthenticators": cienaCesTacacsClientGlobalAccountingBadAuthenticators,
       "cienaCesTacacsClientGlobalAccountingTimeouts": cienaCesTacacsClientGlobalAccountingTimeouts,
       "cienaCesTacacsClientGlobalAccountingUnknownTypes": cienaCesTacacsClientGlobalAccountingUnknownTypes,
       "cienaCesTacacsClientGlobalAccountingBadHeaderSequence": cienaCesTacacsClientGlobalAccountingBadHeaderSequence,
       "cienaCesTacacsClientGlobalServerClearStatistics": cienaCesTacacsClientGlobalServerClearStatistics,
       "cienaCesTacacsClientAuthentication": cienaCesTacacsClientAuthentication,
       "cienaCesTacacsClientAuthenticationServerTable": cienaCesTacacsClientAuthenticationServerTable,
       "cienaCesTacacsClientAuthenticationServerEntry": cienaCesTacacsClientAuthenticationServerEntry,
       "cienaCesTacacsClientAuthenticationServerIndex": cienaCesTacacsClientAuthenticationServerIndex,
       "cienaCesTacacsClientAuthenticationServerAddr": cienaCesTacacsClientAuthenticationServerAddr,
       "cienaCesTacacsClientAuthenticationServerResolvedAddr": cienaCesTacacsClientAuthenticationServerResolvedAddr,
       "cienaCesTacacsClientAuthenticationServerPriority": cienaCesTacacsClientAuthenticationServerPriority,
       "cienaCesTacacsClientAuthenticationServerAuthPort": cienaCesTacacsClientAuthenticationServerAuthPort,
       "cienaCesTacacsClientAuthenticationServerAccessRequests": cienaCesTacacsClientAuthenticationServerAccessRequests,
       "cienaCesTacacsClientAuthenticationServerAccessRetransmissions": cienaCesTacacsClientAuthenticationServerAccessRetransmissions,
       "cienaCesTacacsClientAuthenticationServerAccessAccepts": cienaCesTacacsClientAuthenticationServerAccessAccepts,
       "cienaCesTacacsClientAuthenticationServerAccessRejects": cienaCesTacacsClientAuthenticationServerAccessRejects,
       "cienaCesTacacsClientAuthenticationServerMalformedAccessResponses": cienaCesTacacsClientAuthenticationServerMalformedAccessResponses,
       "cienaCesTacacsClientAuthenticationServerBadAuthenticators": cienaCesTacacsClientAuthenticationServerBadAuthenticators,
       "cienaCesTacacsClientAuthenticationServerTimeouts": cienaCesTacacsClientAuthenticationServerTimeouts,
       "cienaCesTacacsClientAuthenticationServerUnknownTypes": cienaCesTacacsClientAuthenticationServerUnknownTypes,
       "cienaCesTacacsClientAuthenticationServerBadHeaderSequence": cienaCesTacacsClientAuthenticationServerBadHeaderSequence,
       "cienaCesTacacsClientAuthenticationServerStatus": cienaCesTacacsClientAuthenticationServerStatus,
       "cienaCesTacacsClientAuthenticationServerApplication": cienaCesTacacsClientAuthenticationServerApplication,
       "cienaCesTacacsClientAuthenticationServerClearStatistics": cienaCesTacacsClientAuthenticationServerClearStatistics,
       "cienaCesTacacsClientAuthorization": cienaCesTacacsClientAuthorization,
       "cienaCesTacacsClientAuthorizationServerTable": cienaCesTacacsClientAuthorizationServerTable,
       "cienaCesTacacsClientAuthorizationServerEntry": cienaCesTacacsClientAuthorizationServerEntry,
       "cienaCesTacacsClientAuthorizationServerIndex": cienaCesTacacsClientAuthorizationServerIndex,
       "cienaCesTacacsClientAuthorizationServerAddr": cienaCesTacacsClientAuthorizationServerAddr,
       "cienaCesTacacsClientAuthorizationServerResolvedAddr": cienaCesTacacsClientAuthorizationServerResolvedAddr,
       "cienaCesTacacsClientAuthorizationServerPriority": cienaCesTacacsClientAuthorizationServerPriority,
       "cienaCesTacacsClientAuthorizationServerAuthPort": cienaCesTacacsClientAuthorizationServerAuthPort,
       "cienaCesTacacsClientAuthorizationServerAccessRequests": cienaCesTacacsClientAuthorizationServerAccessRequests,
       "cienaCesTacacsClientAuthorizationServerAccessRetransmissions": cienaCesTacacsClientAuthorizationServerAccessRetransmissions,
       "cienaCesTacacsClientAuthorizationServerAccessAccepts": cienaCesTacacsClientAuthorizationServerAccessAccepts,
       "cienaCesTacacsClientAuthorizationServerAccessRejects": cienaCesTacacsClientAuthorizationServerAccessRejects,
       "cienaCesTacacsClientAuthorizationServerMalformedAccessResponses": cienaCesTacacsClientAuthorizationServerMalformedAccessResponses,
       "cienaCesTacacsClientAuthorizationServerBadAuthenticators": cienaCesTacacsClientAuthorizationServerBadAuthenticators,
       "cienaCesTacacsClientAuthorizationServerTimeouts": cienaCesTacacsClientAuthorizationServerTimeouts,
       "cienaCesTacacsClientAuthorizationServerUnknownTypes": cienaCesTacacsClientAuthorizationServerUnknownTypes,
       "cienaCesTacacsClientAuthorizationServerBadHeaderSequence": cienaCesTacacsClientAuthorizationServerBadHeaderSequence,
       "cienaCesTacacsClientAuthorizationServerStatus": cienaCesTacacsClientAuthorizationServerStatus,
       "cienaCesTacacsClientAuthorizationServerApplication": cienaCesTacacsClientAuthorizationServerApplication,
       "cienaCesTacacsClientAuthorizationServerClearStatistics": cienaCesTacacsClientAuthorizationServerClearStatistics,
       "cienaCesTacacsClientAccounting": cienaCesTacacsClientAccounting,
       "cienaCesTacacsClientAccountingServerTable": cienaCesTacacsClientAccountingServerTable,
       "cienaCesTacacsClientAccountingServerEntry": cienaCesTacacsClientAccountingServerEntry,
       "cienaCesTacacsClientAccountingServerIndex": cienaCesTacacsClientAccountingServerIndex,
       "cienaCesTacacsClientAccountingServerAddr": cienaCesTacacsClientAccountingServerAddr,
       "cienaCesTacacsClientAccountingServerResolvedAddr": cienaCesTacacsClientAccountingServerResolvedAddr,
       "cienaCesTacacsClientAccountingServerPriority": cienaCesTacacsClientAccountingServerPriority,
       "cienaCesTacacsClientAccountingServerAuthPort": cienaCesTacacsClientAccountingServerAuthPort,
       "cienaCesTacacsClientAccountingServerAccessRequests": cienaCesTacacsClientAccountingServerAccessRequests,
       "cienaCesTacacsClientAccountingServerAccessRetransmissions": cienaCesTacacsClientAccountingServerAccessRetransmissions,
       "cienaCesTacacsClientAccountingServerAccessAccepts": cienaCesTacacsClientAccountingServerAccessAccepts,
       "cienaCesTacacsClientAccountingServerAccessRejects": cienaCesTacacsClientAccountingServerAccessRejects,
       "cienaCesTacacsClientAccountingServerMalformedAccessResponses": cienaCesTacacsClientAccountingServerMalformedAccessResponses,
       "cienaCesTacacsClientAccountingServerBadAuthenticators": cienaCesTacacsClientAccountingServerBadAuthenticators,
       "cienaCesTacacsClientAccountingServerTimeouts": cienaCesTacacsClientAccountingServerTimeouts,
       "cienaCesTacacsClientAccountingServerUnknownTypes": cienaCesTacacsClientAccountingServerUnknownTypes,
       "cienaCesTacacsClientAccountingServerBadHeaderSequence": cienaCesTacacsClientAccountingServerBadHeaderSequence,
       "cienaCesTacacsClientAccountingServerStatus": cienaCesTacacsClientAccountingServerStatus,
       "cienaCesTacacsClientAccountingServerApplication": cienaCesTacacsClientAccountingServerApplication,
       "cienaCesTacacsClientAccountingServerClearStatistics": cienaCesTacacsClientAccountingServerClearStatistics,
       "cienaCesTacacsClientMIBNotificationPrefix": cienaCesTacacsClientMIBNotificationPrefix,
       "cienaCesTacacsClientMIBNotifications": cienaCesTacacsClientMIBNotifications,
       "cienaCesTacacsClientConnectionFailed": cienaCesTacacsClientConnectionFailed,
       "cienaCesTacacsClientMIBConformance": cienaCesTacacsClientMIBConformance,
       "cienaCesTacacsClientMIBCompliances": cienaCesTacacsClientMIBCompliances,
       "cienaCesTacacsClientMIBGroups": cienaCesTacacsClientMIBGroups}
)
