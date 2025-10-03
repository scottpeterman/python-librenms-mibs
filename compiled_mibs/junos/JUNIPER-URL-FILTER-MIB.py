# SNMP MIB module (JUNIPER-URL-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-URL-FILTER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:00 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

(jnxURLFMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxURLFMibRoot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxURLFMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1)
)
if mibBuilder.loadTexts:
    jnxURLFMIB.setRevisions(
        ("2014-11-20 20:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxURLFilterStatistics_ObjectIdentity = ObjectIdentity
jnxURLFilterStatistics = _JnxURLFilterStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1)
)
_JnxURLFilterStatisticsProfTable_Object = MibTable
jnxURLFilterStatisticsProfTable = _JnxURLFilterStatisticsProfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxURLFilterStatisticsProfTable.setStatus("current")
_JnxURLFilterProfStatsEntryObj_Object = MibTableRow
jnxURLFilterProfStatsEntryObj = _JnxURLFilterProfStatsEntryObj_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1)
)
jnxURLFilterProfStatsEntryObj.setIndexNames(
    (0, "JUNIPER-URL-FILTER-MIB", "jnxURLFilterProfileName"),
)
if mibBuilder.loadTexts:
    jnxURLFilterProfStatsEntryObj.setStatus("current")
_JnxURLFilterProfileName_Type = DisplayString
_JnxURLFilterProfileName_Object = MibTableColumn
jnxURLFilterProfileName = _JnxURLFilterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 1),
    _JnxURLFilterProfileName_Type()
)
jnxURLFilterProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterProfileName.setStatus("current")
_JnxURLFilterActionAccept_Type = Counter64
_JnxURLFilterActionAccept_Object = MibTableColumn
jnxURLFilterActionAccept = _JnxURLFilterActionAccept_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 2),
    _JnxURLFilterActionAccept_Type()
)
jnxURLFilterActionAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionAccept.setStatus("current")
_JnxURLFilterActionAcceptULPktCount_Type = Counter64
_JnxURLFilterActionAcceptULPktCount_Object = MibTableColumn
jnxURLFilterActionAcceptULPktCount = _JnxURLFilterActionAcceptULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 3),
    _JnxURLFilterActionAcceptULPktCount_Type()
)
jnxURLFilterActionAcceptULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionAcceptULPktCount.setStatus("current")
_JnxURLFilterActionAcceptDLPktCount_Type = Counter64
_JnxURLFilterActionAcceptDLPktCount_Object = MibTableColumn
jnxURLFilterActionAcceptDLPktCount = _JnxURLFilterActionAcceptDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 4),
    _JnxURLFilterActionAcceptDLPktCount_Type()
)
jnxURLFilterActionAcceptDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionAcceptDLPktCount.setStatus("current")
_JnxURLFilterActionAcceptULBytes_Type = Counter64
_JnxURLFilterActionAcceptULBytes_Object = MibTableColumn
jnxURLFilterActionAcceptULBytes = _JnxURLFilterActionAcceptULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 5),
    _JnxURLFilterActionAcceptULBytes_Type()
)
jnxURLFilterActionAcceptULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionAcceptULBytes.setStatus("current")
_JnxURLFilterActionAcceptDLBytes_Type = Counter64
_JnxURLFilterActionAcceptDLBytes_Object = MibTableColumn
jnxURLFilterActionAcceptDLBytes = _JnxURLFilterActionAcceptDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 6),
    _JnxURLFilterActionAcceptDLBytes_Type()
)
jnxURLFilterActionAcceptDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionAcceptDLBytes.setStatus("current")
_JnxURLFilterActionCustomPage_Type = Counter64
_JnxURLFilterActionCustomPage_Object = MibTableColumn
jnxURLFilterActionCustomPage = _JnxURLFilterActionCustomPage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 7),
    _JnxURLFilterActionCustomPage_Type()
)
jnxURLFilterActionCustomPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionCustomPage.setStatus("current")
_JnxURLFilterActionCustomPageULPktCount_Type = Counter64
_JnxURLFilterActionCustomPageULPktCount_Object = MibTableColumn
jnxURLFilterActionCustomPageULPktCount = _JnxURLFilterActionCustomPageULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 8),
    _JnxURLFilterActionCustomPageULPktCount_Type()
)
jnxURLFilterActionCustomPageULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionCustomPageULPktCount.setStatus("current")
_JnxURLFilterActionCustomPageDLPktCount_Type = Counter64
_JnxURLFilterActionCustomPageDLPktCount_Object = MibTableColumn
jnxURLFilterActionCustomPageDLPktCount = _JnxURLFilterActionCustomPageDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 9),
    _JnxURLFilterActionCustomPageDLPktCount_Type()
)
jnxURLFilterActionCustomPageDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionCustomPageDLPktCount.setStatus("current")
_JnxURLFilterActionCustomPageULBytes_Type = Counter64
_JnxURLFilterActionCustomPageULBytes_Object = MibTableColumn
jnxURLFilterActionCustomPageULBytes = _JnxURLFilterActionCustomPageULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 10),
    _JnxURLFilterActionCustomPageULBytes_Type()
)
jnxURLFilterActionCustomPageULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionCustomPageULBytes.setStatus("current")
_JnxURLFilterActionCustomPageDLBytes_Type = Counter64
_JnxURLFilterActionCustomPageDLBytes_Object = MibTableColumn
jnxURLFilterActionCustomPageDLBytes = _JnxURLFilterActionCustomPageDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 11),
    _JnxURLFilterActionCustomPageDLBytes_Type()
)
jnxURLFilterActionCustomPageDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionCustomPageDLBytes.setStatus("current")
_JnxURLFilterActionHTTPStatusCode_Type = Counter64
_JnxURLFilterActionHTTPStatusCode_Object = MibTableColumn
jnxURLFilterActionHTTPStatusCode = _JnxURLFilterActionHTTPStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 12),
    _JnxURLFilterActionHTTPStatusCode_Type()
)
jnxURLFilterActionHTTPStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionHTTPStatusCode.setStatus("current")
_JnxURLFilterActionHTTPStatusCodeULPktCount_Type = Counter64
_JnxURLFilterActionHTTPStatusCodeULPktCount_Object = MibTableColumn
jnxURLFilterActionHTTPStatusCodeULPktCount = _JnxURLFilterActionHTTPStatusCodeULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 13),
    _JnxURLFilterActionHTTPStatusCodeULPktCount_Type()
)
jnxURLFilterActionHTTPStatusCodeULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionHTTPStatusCodeULPktCount.setStatus("current")
_JnxURLFilterActionHTTPStatusCodeDLPktCount_Type = Counter64
_JnxURLFilterActionHTTPStatusCodeDLPktCount_Object = MibTableColumn
jnxURLFilterActionHTTPStatusCodeDLPktCount = _JnxURLFilterActionHTTPStatusCodeDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 14),
    _JnxURLFilterActionHTTPStatusCodeDLPktCount_Type()
)
jnxURLFilterActionHTTPStatusCodeDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionHTTPStatusCodeDLPktCount.setStatus("current")
_JnxURLFilterActionHTTPStatusCodeULBytes_Type = Counter64
_JnxURLFilterActionHTTPStatusCodeULBytes_Object = MibTableColumn
jnxURLFilterActionHTTPStatusCodeULBytes = _JnxURLFilterActionHTTPStatusCodeULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 15),
    _JnxURLFilterActionHTTPStatusCodeULBytes_Type()
)
jnxURLFilterActionHTTPStatusCodeULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionHTTPStatusCodeULBytes.setStatus("current")
_JnxURLFilterActionHTTPStatusCodeDLBytes_Type = Counter64
_JnxURLFilterActionHTTPStatusCodeDLBytes_Object = MibTableColumn
jnxURLFilterActionHTTPStatusCodeDLBytes = _JnxURLFilterActionHTTPStatusCodeDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 16),
    _JnxURLFilterActionHTTPStatusCodeDLBytes_Type()
)
jnxURLFilterActionHTTPStatusCodeDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionHTTPStatusCodeDLBytes.setStatus("current")
_JnxURLFilterActionRedirect_Type = Counter64
_JnxURLFilterActionRedirect_Object = MibTableColumn
jnxURLFilterActionRedirect = _JnxURLFilterActionRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 17),
    _JnxURLFilterActionRedirect_Type()
)
jnxURLFilterActionRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionRedirect.setStatus("current")
_JnxURLFilterActionRedirectULPktCount_Type = Counter64
_JnxURLFilterActionRedirectULPktCount_Object = MibTableColumn
jnxURLFilterActionRedirectULPktCount = _JnxURLFilterActionRedirectULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 18),
    _JnxURLFilterActionRedirectULPktCount_Type()
)
jnxURLFilterActionRedirectULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionRedirectULPktCount.setStatus("current")
_JnxURLFilterActionRedirectDLPktCount_Type = Counter64
_JnxURLFilterActionRedirectDLPktCount_Object = MibTableColumn
jnxURLFilterActionRedirectDLPktCount = _JnxURLFilterActionRedirectDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 19),
    _JnxURLFilterActionRedirectDLPktCount_Type()
)
jnxURLFilterActionRedirectDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionRedirectDLPktCount.setStatus("current")
_JnxURLFilterActionRedirectULBytes_Type = Counter64
_JnxURLFilterActionRedirectULBytes_Object = MibTableColumn
jnxURLFilterActionRedirectULBytes = _JnxURLFilterActionRedirectULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 20),
    _JnxURLFilterActionRedirectULBytes_Type()
)
jnxURLFilterActionRedirectULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionRedirectULBytes.setStatus("current")
_JnxURLFilterActionRedirectDLBytes_Type = Counter64
_JnxURLFilterActionRedirectDLBytes_Object = MibTableColumn
jnxURLFilterActionRedirectDLBytes = _JnxURLFilterActionRedirectDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 21),
    _JnxURLFilterActionRedirectDLBytes_Type()
)
jnxURLFilterActionRedirectDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionRedirectDLBytes.setStatus("current")
_JnxURLFilterActionTCPReset_Type = Counter64
_JnxURLFilterActionTCPReset_Object = MibTableColumn
jnxURLFilterActionTCPReset = _JnxURLFilterActionTCPReset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 22),
    _JnxURLFilterActionTCPReset_Type()
)
jnxURLFilterActionTCPReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionTCPReset.setStatus("current")
_JnxURLFilterActionTCPResetULPktCount_Type = Counter64
_JnxURLFilterActionTCPResetULPktCount_Object = MibTableColumn
jnxURLFilterActionTCPResetULPktCount = _JnxURLFilterActionTCPResetULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 23),
    _JnxURLFilterActionTCPResetULPktCount_Type()
)
jnxURLFilterActionTCPResetULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionTCPResetULPktCount.setStatus("current")
_JnxURLFilterActionTCPResetDLPktCount_Type = Counter64
_JnxURLFilterActionTCPResetDLPktCount_Object = MibTableColumn
jnxURLFilterActionTCPResetDLPktCount = _JnxURLFilterActionTCPResetDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 24),
    _JnxURLFilterActionTCPResetDLPktCount_Type()
)
jnxURLFilterActionTCPResetDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionTCPResetDLPktCount.setStatus("current")
_JnxURLFilterActionTCPResetULBytes_Type = Counter64
_JnxURLFilterActionTCPResetULBytes_Object = MibTableColumn
jnxURLFilterActionTCPResetULBytes = _JnxURLFilterActionTCPResetULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 25),
    _JnxURLFilterActionTCPResetULBytes_Type()
)
jnxURLFilterActionTCPResetULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionTCPResetULBytes.setStatus("current")
_JnxURLFilterActionTCPResetDLBytes_Type = Counter64
_JnxURLFilterActionTCPResetDLBytes_Object = MibTableColumn
jnxURLFilterActionTCPResetDLBytes = _JnxURLFilterActionTCPResetDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 26),
    _JnxURLFilterActionTCPResetDLBytes_Type()
)
jnxURLFilterActionTCPResetDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionTCPResetDLBytes.setStatus("current")
_JnxURLFilterActionBypass_Type = Counter64
_JnxURLFilterActionBypass_Object = MibTableColumn
jnxURLFilterActionBypass = _JnxURLFilterActionBypass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 27),
    _JnxURLFilterActionBypass_Type()
)
jnxURLFilterActionBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionBypass.setStatus("current")
_JnxURLFilterActionDUIFV4Accepted_Type = Counter64
_JnxURLFilterActionDUIFV4Accepted_Object = MibTableColumn
jnxURLFilterActionDUIFV4Accepted = _JnxURLFilterActionDUIFV4Accepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 28),
    _JnxURLFilterActionDUIFV4Accepted_Type()
)
jnxURLFilterActionDUIFV4Accepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV4Accepted.setStatus("current")
_JnxURLFilterActionDUIFV4ULPktCount_Type = Counter64
_JnxURLFilterActionDUIFV4ULPktCount_Object = MibTableColumn
jnxURLFilterActionDUIFV4ULPktCount = _JnxURLFilterActionDUIFV4ULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 29),
    _JnxURLFilterActionDUIFV4ULPktCount_Type()
)
jnxURLFilterActionDUIFV4ULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV4ULPktCount.setStatus("current")
_JnxURLFilterActionDUIFV4DLPktCount_Type = Counter64
_JnxURLFilterActionDUIFV4DLPktCount_Object = MibTableColumn
jnxURLFilterActionDUIFV4DLPktCount = _JnxURLFilterActionDUIFV4DLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 30),
    _JnxURLFilterActionDUIFV4DLPktCount_Type()
)
jnxURLFilterActionDUIFV4DLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV4DLPktCount.setStatus("current")
_JnxURLFilterActionDUIFV4ULBytes_Type = Counter64
_JnxURLFilterActionDUIFV4ULBytes_Object = MibTableColumn
jnxURLFilterActionDUIFV4ULBytes = _JnxURLFilterActionDUIFV4ULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 31),
    _JnxURLFilterActionDUIFV4ULBytes_Type()
)
jnxURLFilterActionDUIFV4ULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV4ULBytes.setStatus("current")
_JnxURLFilterActionDUIFV4DLBytes_Type = Counter64
_JnxURLFilterActionDUIFV4DLBytes_Object = MibTableColumn
jnxURLFilterActionDUIFV4DLBytes = _JnxURLFilterActionDUIFV4DLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 32),
    _JnxURLFilterActionDUIFV4DLBytes_Type()
)
jnxURLFilterActionDUIFV4DLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV4DLBytes.setStatus("current")
_JnxURLFilterActionDUIFV6Accepted_Type = Counter64
_JnxURLFilterActionDUIFV6Accepted_Object = MibTableColumn
jnxURLFilterActionDUIFV6Accepted = _JnxURLFilterActionDUIFV6Accepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 33),
    _JnxURLFilterActionDUIFV6Accepted_Type()
)
jnxURLFilterActionDUIFV6Accepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV6Accepted.setStatus("current")
_JnxURLFilterActionDUIFV6ULPktCount_Type = Counter64
_JnxURLFilterActionDUIFV6ULPktCount_Object = MibTableColumn
jnxURLFilterActionDUIFV6ULPktCount = _JnxURLFilterActionDUIFV6ULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 34),
    _JnxURLFilterActionDUIFV6ULPktCount_Type()
)
jnxURLFilterActionDUIFV6ULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV6ULPktCount.setStatus("current")
_JnxURLFilterActionDUIFV6DLPktCount_Type = Counter64
_JnxURLFilterActionDUIFV6DLPktCount_Object = MibTableColumn
jnxURLFilterActionDUIFV6DLPktCount = _JnxURLFilterActionDUIFV6DLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 35),
    _JnxURLFilterActionDUIFV6DLPktCount_Type()
)
jnxURLFilterActionDUIFV6DLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV6DLPktCount.setStatus("current")
_JnxURLFilterActionDUIFV6ULBytes_Type = Counter64
_JnxURLFilterActionDUIFV6ULBytes_Object = MibTableColumn
jnxURLFilterActionDUIFV6ULBytes = _JnxURLFilterActionDUIFV6ULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 36),
    _JnxURLFilterActionDUIFV6ULBytes_Type()
)
jnxURLFilterActionDUIFV6ULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV6ULBytes.setStatus("current")
_JnxURLFilterActionDUIFV6DLBytes_Type = Counter64
_JnxURLFilterActionDUIFV6DLBytes_Object = MibTableColumn
jnxURLFilterActionDUIFV6DLBytes = _JnxURLFilterActionDUIFV6DLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 1, 1, 37),
    _JnxURLFilterActionDUIFV6DLBytes_Type()
)
jnxURLFilterActionDUIFV6DLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterActionDUIFV6DLBytes.setStatus("current")
_JnxURLFilterStatisticsTempTable_Object = MibTable
jnxURLFilterStatisticsTempTable = _JnxURLFilterStatisticsTempTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxURLFilterStatisticsTempTable.setStatus("current")
_JnxURLFilterTempStatsEntryObj_Object = MibTableRow
jnxURLFilterTempStatsEntryObj = _JnxURLFilterTempStatsEntryObj_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1)
)
jnxURLFilterTempStatsEntryObj.setIndexNames(
    (0, "JUNIPER-URL-FILTER-MIB", "jnxURLFilterTempProfileName"),
    (0, "JUNIPER-URL-FILTER-MIB", "jnxURLFilterTemplateName"),
)
if mibBuilder.loadTexts:
    jnxURLFilterTempStatsEntryObj.setStatus("current")
_JnxURLFilterTempProfileName_Type = DisplayString
_JnxURLFilterTempProfileName_Object = MibTableColumn
jnxURLFilterTempProfileName = _JnxURLFilterTempProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 1),
    _JnxURLFilterTempProfileName_Type()
)
jnxURLFilterTempProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempProfileName.setStatus("current")
_JnxURLFilterTemplateName_Type = DisplayString
_JnxURLFilterTemplateName_Object = MibTableColumn
jnxURLFilterTemplateName = _JnxURLFilterTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 2),
    _JnxURLFilterTemplateName_Type()
)
jnxURLFilterTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTemplateName.setStatus("current")
_JnxURLFilterTempActionAccept_Type = Counter64
_JnxURLFilterTempActionAccept_Object = MibTableColumn
jnxURLFilterTempActionAccept = _JnxURLFilterTempActionAccept_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 3),
    _JnxURLFilterTempActionAccept_Type()
)
jnxURLFilterTempActionAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionAccept.setStatus("current")
_JnxURLFilterTempActionAcceptULPktCount_Type = Counter64
_JnxURLFilterTempActionAcceptULPktCount_Object = MibTableColumn
jnxURLFilterTempActionAcceptULPktCount = _JnxURLFilterTempActionAcceptULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 4),
    _JnxURLFilterTempActionAcceptULPktCount_Type()
)
jnxURLFilterTempActionAcceptULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionAcceptULPktCount.setStatus("current")
_JnxURLFilterTempActionAcceptDLPktCount_Type = Counter64
_JnxURLFilterTempActionAcceptDLPktCount_Object = MibTableColumn
jnxURLFilterTempActionAcceptDLPktCount = _JnxURLFilterTempActionAcceptDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 5),
    _JnxURLFilterTempActionAcceptDLPktCount_Type()
)
jnxURLFilterTempActionAcceptDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionAcceptDLPktCount.setStatus("current")
_JnxURLFilterTempActionAcceptULBytes_Type = Counter64
_JnxURLFilterTempActionAcceptULBytes_Object = MibTableColumn
jnxURLFilterTempActionAcceptULBytes = _JnxURLFilterTempActionAcceptULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 6),
    _JnxURLFilterTempActionAcceptULBytes_Type()
)
jnxURLFilterTempActionAcceptULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionAcceptULBytes.setStatus("current")
_JnxURLFilterTempActionAcceptDLBytes_Type = Counter64
_JnxURLFilterTempActionAcceptDLBytes_Object = MibTableColumn
jnxURLFilterTempActionAcceptDLBytes = _JnxURLFilterTempActionAcceptDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 7),
    _JnxURLFilterTempActionAcceptDLBytes_Type()
)
jnxURLFilterTempActionAcceptDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionAcceptDLBytes.setStatus("current")
_JnxURLFilterTempActionCustomPage_Type = Counter64
_JnxURLFilterTempActionCustomPage_Object = MibTableColumn
jnxURLFilterTempActionCustomPage = _JnxURLFilterTempActionCustomPage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 8),
    _JnxURLFilterTempActionCustomPage_Type()
)
jnxURLFilterTempActionCustomPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionCustomPage.setStatus("current")
_JnxURLFilterTempActionCustomPageULPktCount_Type = Counter64
_JnxURLFilterTempActionCustomPageULPktCount_Object = MibTableColumn
jnxURLFilterTempActionCustomPageULPktCount = _JnxURLFilterTempActionCustomPageULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 9),
    _JnxURLFilterTempActionCustomPageULPktCount_Type()
)
jnxURLFilterTempActionCustomPageULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionCustomPageULPktCount.setStatus("current")
_JnxURLFilterTempActionCustomPageDLPktCount_Type = Counter64
_JnxURLFilterTempActionCustomPageDLPktCount_Object = MibTableColumn
jnxURLFilterTempActionCustomPageDLPktCount = _JnxURLFilterTempActionCustomPageDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 10),
    _JnxURLFilterTempActionCustomPageDLPktCount_Type()
)
jnxURLFilterTempActionCustomPageDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionCustomPageDLPktCount.setStatus("current")
_JnxURLFilterTempActionCustomPageULBytes_Type = Counter64
_JnxURLFilterTempActionCustomPageULBytes_Object = MibTableColumn
jnxURLFilterTempActionCustomPageULBytes = _JnxURLFilterTempActionCustomPageULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 11),
    _JnxURLFilterTempActionCustomPageULBytes_Type()
)
jnxURLFilterTempActionCustomPageULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionCustomPageULBytes.setStatus("current")
_JnxURLFilterTempActionCustomPageDLBytes_Type = Counter64
_JnxURLFilterTempActionCustomPageDLBytes_Object = MibTableColumn
jnxURLFilterTempActionCustomPageDLBytes = _JnxURLFilterTempActionCustomPageDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 12),
    _JnxURLFilterTempActionCustomPageDLBytes_Type()
)
jnxURLFilterTempActionCustomPageDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionCustomPageDLBytes.setStatus("current")
_JnxURLFilterTempActionHTTPStatusCode_Type = Counter64
_JnxURLFilterTempActionHTTPStatusCode_Object = MibTableColumn
jnxURLFilterTempActionHTTPStatusCode = _JnxURLFilterTempActionHTTPStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 13),
    _JnxURLFilterTempActionHTTPStatusCode_Type()
)
jnxURLFilterTempActionHTTPStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionHTTPStatusCode.setStatus("current")
_JnxURLFilterTempActionHTTPStatusCodeULPktCount_Type = Counter64
_JnxURLFilterTempActionHTTPStatusCodeULPktCount_Object = MibTableColumn
jnxURLFilterTempActionHTTPStatusCodeULPktCount = _JnxURLFilterTempActionHTTPStatusCodeULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 14),
    _JnxURLFilterTempActionHTTPStatusCodeULPktCount_Type()
)
jnxURLFilterTempActionHTTPStatusCodeULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionHTTPStatusCodeULPktCount.setStatus("current")
_JnxURLFilterTempActionHTTPStatusCodeDLPktCount_Type = Counter64
_JnxURLFilterTempActionHTTPStatusCodeDLPktCount_Object = MibTableColumn
jnxURLFilterTempActionHTTPStatusCodeDLPktCount = _JnxURLFilterTempActionHTTPStatusCodeDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 15),
    _JnxURLFilterTempActionHTTPStatusCodeDLPktCount_Type()
)
jnxURLFilterTempActionHTTPStatusCodeDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionHTTPStatusCodeDLPktCount.setStatus("current")
_JnxURLFilterTempActionHTTPStatusCodeULBytes_Type = Counter64
_JnxURLFilterTempActionHTTPStatusCodeULBytes_Object = MibTableColumn
jnxURLFilterTempActionHTTPStatusCodeULBytes = _JnxURLFilterTempActionHTTPStatusCodeULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 16),
    _JnxURLFilterTempActionHTTPStatusCodeULBytes_Type()
)
jnxURLFilterTempActionHTTPStatusCodeULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionHTTPStatusCodeULBytes.setStatus("current")
_JnxURLFilterTempActionHTTPStatusCodeDLBytes_Type = Counter64
_JnxURLFilterTempActionHTTPStatusCodeDLBytes_Object = MibTableColumn
jnxURLFilterTempActionHTTPStatusCodeDLBytes = _JnxURLFilterTempActionHTTPStatusCodeDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 17),
    _JnxURLFilterTempActionHTTPStatusCodeDLBytes_Type()
)
jnxURLFilterTempActionHTTPStatusCodeDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionHTTPStatusCodeDLBytes.setStatus("current")
_JnxURLFilterTempActionRedirect_Type = Counter64
_JnxURLFilterTempActionRedirect_Object = MibTableColumn
jnxURLFilterTempActionRedirect = _JnxURLFilterTempActionRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 18),
    _JnxURLFilterTempActionRedirect_Type()
)
jnxURLFilterTempActionRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionRedirect.setStatus("current")
_JnxURLFilterTempActionRedirectULPktCount_Type = Counter64
_JnxURLFilterTempActionRedirectULPktCount_Object = MibTableColumn
jnxURLFilterTempActionRedirectULPktCount = _JnxURLFilterTempActionRedirectULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 19),
    _JnxURLFilterTempActionRedirectULPktCount_Type()
)
jnxURLFilterTempActionRedirectULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionRedirectULPktCount.setStatus("current")
_JnxURLFilterTempActionRedirectDLPktCount_Type = Counter64
_JnxURLFilterTempActionRedirectDLPktCount_Object = MibTableColumn
jnxURLFilterTempActionRedirectDLPktCount = _JnxURLFilterTempActionRedirectDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 20),
    _JnxURLFilterTempActionRedirectDLPktCount_Type()
)
jnxURLFilterTempActionRedirectDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionRedirectDLPktCount.setStatus("current")
_JnxURLFilterTempActionRedirectULBytes_Type = Counter64
_JnxURLFilterTempActionRedirectULBytes_Object = MibTableColumn
jnxURLFilterTempActionRedirectULBytes = _JnxURLFilterTempActionRedirectULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 21),
    _JnxURLFilterTempActionRedirectULBytes_Type()
)
jnxURLFilterTempActionRedirectULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionRedirectULBytes.setStatus("current")
_JnxURLFilterTempActionRedirectDLBytes_Type = Counter64
_JnxURLFilterTempActionRedirectDLBytes_Object = MibTableColumn
jnxURLFilterTempActionRedirectDLBytes = _JnxURLFilterTempActionRedirectDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 22),
    _JnxURLFilterTempActionRedirectDLBytes_Type()
)
jnxURLFilterTempActionRedirectDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionRedirectDLBytes.setStatus("current")
_JnxURLFilterTempActionTCPReset_Type = Counter64
_JnxURLFilterTempActionTCPReset_Object = MibTableColumn
jnxURLFilterTempActionTCPReset = _JnxURLFilterTempActionTCPReset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 23),
    _JnxURLFilterTempActionTCPReset_Type()
)
jnxURLFilterTempActionTCPReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionTCPReset.setStatus("current")
_JnxURLFilterTempActionTCPResetULPktCount_Type = Counter64
_JnxURLFilterTempActionTCPResetULPktCount_Object = MibTableColumn
jnxURLFilterTempActionTCPResetULPktCount = _JnxURLFilterTempActionTCPResetULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 24),
    _JnxURLFilterTempActionTCPResetULPktCount_Type()
)
jnxURLFilterTempActionTCPResetULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionTCPResetULPktCount.setStatus("current")
_JnxURLFilterTempActionTCPResetDLPktCount_Type = Counter64
_JnxURLFilterTempActionTCPResetDLPktCount_Object = MibTableColumn
jnxURLFilterTempActionTCPResetDLPktCount = _JnxURLFilterTempActionTCPResetDLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 25),
    _JnxURLFilterTempActionTCPResetDLPktCount_Type()
)
jnxURLFilterTempActionTCPResetDLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionTCPResetDLPktCount.setStatus("current")
_JnxURLFilterTempActionTCPResetULBytes_Type = Counter64
_JnxURLFilterTempActionTCPResetULBytes_Object = MibTableColumn
jnxURLFilterTempActionTCPResetULBytes = _JnxURLFilterTempActionTCPResetULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 26),
    _JnxURLFilterTempActionTCPResetULBytes_Type()
)
jnxURLFilterTempActionTCPResetULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionTCPResetULBytes.setStatus("current")
_JnxURLFilterTempActionTCPResetDLBytes_Type = Counter64
_JnxURLFilterTempActionTCPResetDLBytes_Object = MibTableColumn
jnxURLFilterTempActionTCPResetDLBytes = _JnxURLFilterTempActionTCPResetDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 27),
    _JnxURLFilterTempActionTCPResetDLBytes_Type()
)
jnxURLFilterTempActionTCPResetDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionTCPResetDLBytes.setStatus("current")
_JnxURLFilterTempActionDUIFV4Accepted_Type = Counter64
_JnxURLFilterTempActionDUIFV4Accepted_Object = MibTableColumn
jnxURLFilterTempActionDUIFV4Accepted = _JnxURLFilterTempActionDUIFV4Accepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 28),
    _JnxURLFilterTempActionDUIFV4Accepted_Type()
)
jnxURLFilterTempActionDUIFV4Accepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV4Accepted.setStatus("current")
_JnxURLFilterTempActionDUIFV4ULPktCount_Type = Counter64
_JnxURLFilterTempActionDUIFV4ULPktCount_Object = MibTableColumn
jnxURLFilterTempActionDUIFV4ULPktCount = _JnxURLFilterTempActionDUIFV4ULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 29),
    _JnxURLFilterTempActionDUIFV4ULPktCount_Type()
)
jnxURLFilterTempActionDUIFV4ULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV4ULPktCount.setStatus("current")
_JnxURLFilterTempActionDUIFV4DLPktCount_Type = Counter64
_JnxURLFilterTempActionDUIFV4DLPktCount_Object = MibTableColumn
jnxURLFilterTempActionDUIFV4DLPktCount = _JnxURLFilterTempActionDUIFV4DLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 30),
    _JnxURLFilterTempActionDUIFV4DLPktCount_Type()
)
jnxURLFilterTempActionDUIFV4DLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV4DLPktCount.setStatus("current")
_JnxURLFilterTempActionDUIFV4ULBytes_Type = Counter64
_JnxURLFilterTempActionDUIFV4ULBytes_Object = MibTableColumn
jnxURLFilterTempActionDUIFV4ULBytes = _JnxURLFilterTempActionDUIFV4ULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 31),
    _JnxURLFilterTempActionDUIFV4ULBytes_Type()
)
jnxURLFilterTempActionDUIFV4ULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV4ULBytes.setStatus("current")
_JnxURLFilterTempActionDUIFV4DLBytes_Type = Counter64
_JnxURLFilterTempActionDUIFV4DLBytes_Object = MibTableColumn
jnxURLFilterTempActionDUIFV4DLBytes = _JnxURLFilterTempActionDUIFV4DLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 32),
    _JnxURLFilterTempActionDUIFV4DLBytes_Type()
)
jnxURLFilterTempActionDUIFV4DLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV4DLBytes.setStatus("current")
_JnxURLFilterTempActionDUIFV6Accepted_Type = Counter64
_JnxURLFilterTempActionDUIFV6Accepted_Object = MibTableColumn
jnxURLFilterTempActionDUIFV6Accepted = _JnxURLFilterTempActionDUIFV6Accepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 33),
    _JnxURLFilterTempActionDUIFV6Accepted_Type()
)
jnxURLFilterTempActionDUIFV6Accepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV6Accepted.setStatus("current")
_JnxURLFilterTempActionDUIFV6ULPktCount_Type = Counter64
_JnxURLFilterTempActionDUIFV6ULPktCount_Object = MibTableColumn
jnxURLFilterTempActionDUIFV6ULPktCount = _JnxURLFilterTempActionDUIFV6ULPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 34),
    _JnxURLFilterTempActionDUIFV6ULPktCount_Type()
)
jnxURLFilterTempActionDUIFV6ULPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV6ULPktCount.setStatus("current")
_JnxURLFilterTempActionDUIFV6DLPktCount_Type = Counter64
_JnxURLFilterTempActionDUIFV6DLPktCount_Object = MibTableColumn
jnxURLFilterTempActionDUIFV6DLPktCount = _JnxURLFilterTempActionDUIFV6DLPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 35),
    _JnxURLFilterTempActionDUIFV6DLPktCount_Type()
)
jnxURLFilterTempActionDUIFV6DLPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV6DLPktCount.setStatus("current")
_JnxURLFilterTempActionDUIFV6ULBytes_Type = Counter64
_JnxURLFilterTempActionDUIFV6ULBytes_Object = MibTableColumn
jnxURLFilterTempActionDUIFV6ULBytes = _JnxURLFilterTempActionDUIFV6ULBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 36),
    _JnxURLFilterTempActionDUIFV6ULBytes_Type()
)
jnxURLFilterTempActionDUIFV6ULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV6ULBytes.setStatus("current")
_JnxURLFilterTempActionDUIFV6DLBytes_Type = Counter64
_JnxURLFilterTempActionDUIFV6DLBytes_Object = MibTableColumn
jnxURLFilterTempActionDUIFV6DLBytes = _JnxURLFilterTempActionDUIFV6DLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 85, 1, 1, 2, 1, 37),
    _JnxURLFilterTempActionDUIFV6DLBytes_Type()
)
jnxURLFilterTempActionDUIFV6DLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxURLFilterTempActionDUIFV6DLBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-URL-FILTER-MIB",
    **{"jnxURLFMIB": jnxURLFMIB,
       "jnxURLFilterStatistics": jnxURLFilterStatistics,
       "jnxURLFilterStatisticsProfTable": jnxURLFilterStatisticsProfTable,
       "jnxURLFilterProfStatsEntryObj": jnxURLFilterProfStatsEntryObj,
       "jnxURLFilterProfileName": jnxURLFilterProfileName,
       "jnxURLFilterActionAccept": jnxURLFilterActionAccept,
       "jnxURLFilterActionAcceptULPktCount": jnxURLFilterActionAcceptULPktCount,
       "jnxURLFilterActionAcceptDLPktCount": jnxURLFilterActionAcceptDLPktCount,
       "jnxURLFilterActionAcceptULBytes": jnxURLFilterActionAcceptULBytes,
       "jnxURLFilterActionAcceptDLBytes": jnxURLFilterActionAcceptDLBytes,
       "jnxURLFilterActionCustomPage": jnxURLFilterActionCustomPage,
       "jnxURLFilterActionCustomPageULPktCount": jnxURLFilterActionCustomPageULPktCount,
       "jnxURLFilterActionCustomPageDLPktCount": jnxURLFilterActionCustomPageDLPktCount,
       "jnxURLFilterActionCustomPageULBytes": jnxURLFilterActionCustomPageULBytes,
       "jnxURLFilterActionCustomPageDLBytes": jnxURLFilterActionCustomPageDLBytes,
       "jnxURLFilterActionHTTPStatusCode": jnxURLFilterActionHTTPStatusCode,
       "jnxURLFilterActionHTTPStatusCodeULPktCount": jnxURLFilterActionHTTPStatusCodeULPktCount,
       "jnxURLFilterActionHTTPStatusCodeDLPktCount": jnxURLFilterActionHTTPStatusCodeDLPktCount,
       "jnxURLFilterActionHTTPStatusCodeULBytes": jnxURLFilterActionHTTPStatusCodeULBytes,
       "jnxURLFilterActionHTTPStatusCodeDLBytes": jnxURLFilterActionHTTPStatusCodeDLBytes,
       "jnxURLFilterActionRedirect": jnxURLFilterActionRedirect,
       "jnxURLFilterActionRedirectULPktCount": jnxURLFilterActionRedirectULPktCount,
       "jnxURLFilterActionRedirectDLPktCount": jnxURLFilterActionRedirectDLPktCount,
       "jnxURLFilterActionRedirectULBytes": jnxURLFilterActionRedirectULBytes,
       "jnxURLFilterActionRedirectDLBytes": jnxURLFilterActionRedirectDLBytes,
       "jnxURLFilterActionTCPReset": jnxURLFilterActionTCPReset,
       "jnxURLFilterActionTCPResetULPktCount": jnxURLFilterActionTCPResetULPktCount,
       "jnxURLFilterActionTCPResetDLPktCount": jnxURLFilterActionTCPResetDLPktCount,
       "jnxURLFilterActionTCPResetULBytes": jnxURLFilterActionTCPResetULBytes,
       "jnxURLFilterActionTCPResetDLBytes": jnxURLFilterActionTCPResetDLBytes,
       "jnxURLFilterActionBypass": jnxURLFilterActionBypass,
       "jnxURLFilterActionDUIFV4Accepted": jnxURLFilterActionDUIFV4Accepted,
       "jnxURLFilterActionDUIFV4ULPktCount": jnxURLFilterActionDUIFV4ULPktCount,
       "jnxURLFilterActionDUIFV4DLPktCount": jnxURLFilterActionDUIFV4DLPktCount,
       "jnxURLFilterActionDUIFV4ULBytes": jnxURLFilterActionDUIFV4ULBytes,
       "jnxURLFilterActionDUIFV4DLBytes": jnxURLFilterActionDUIFV4DLBytes,
       "jnxURLFilterActionDUIFV6Accepted": jnxURLFilterActionDUIFV6Accepted,
       "jnxURLFilterActionDUIFV6ULPktCount": jnxURLFilterActionDUIFV6ULPktCount,
       "jnxURLFilterActionDUIFV6DLPktCount": jnxURLFilterActionDUIFV6DLPktCount,
       "jnxURLFilterActionDUIFV6ULBytes": jnxURLFilterActionDUIFV6ULBytes,
       "jnxURLFilterActionDUIFV6DLBytes": jnxURLFilterActionDUIFV6DLBytes,
       "jnxURLFilterStatisticsTempTable": jnxURLFilterStatisticsTempTable,
       "jnxURLFilterTempStatsEntryObj": jnxURLFilterTempStatsEntryObj,
       "jnxURLFilterTempProfileName": jnxURLFilterTempProfileName,
       "jnxURLFilterTemplateName": jnxURLFilterTemplateName,
       "jnxURLFilterTempActionAccept": jnxURLFilterTempActionAccept,
       "jnxURLFilterTempActionAcceptULPktCount": jnxURLFilterTempActionAcceptULPktCount,
       "jnxURLFilterTempActionAcceptDLPktCount": jnxURLFilterTempActionAcceptDLPktCount,
       "jnxURLFilterTempActionAcceptULBytes": jnxURLFilterTempActionAcceptULBytes,
       "jnxURLFilterTempActionAcceptDLBytes": jnxURLFilterTempActionAcceptDLBytes,
       "jnxURLFilterTempActionCustomPage": jnxURLFilterTempActionCustomPage,
       "jnxURLFilterTempActionCustomPageULPktCount": jnxURLFilterTempActionCustomPageULPktCount,
       "jnxURLFilterTempActionCustomPageDLPktCount": jnxURLFilterTempActionCustomPageDLPktCount,
       "jnxURLFilterTempActionCustomPageULBytes": jnxURLFilterTempActionCustomPageULBytes,
       "jnxURLFilterTempActionCustomPageDLBytes": jnxURLFilterTempActionCustomPageDLBytes,
       "jnxURLFilterTempActionHTTPStatusCode": jnxURLFilterTempActionHTTPStatusCode,
       "jnxURLFilterTempActionHTTPStatusCodeULPktCount": jnxURLFilterTempActionHTTPStatusCodeULPktCount,
       "jnxURLFilterTempActionHTTPStatusCodeDLPktCount": jnxURLFilterTempActionHTTPStatusCodeDLPktCount,
       "jnxURLFilterTempActionHTTPStatusCodeULBytes": jnxURLFilterTempActionHTTPStatusCodeULBytes,
       "jnxURLFilterTempActionHTTPStatusCodeDLBytes": jnxURLFilterTempActionHTTPStatusCodeDLBytes,
       "jnxURLFilterTempActionRedirect": jnxURLFilterTempActionRedirect,
       "jnxURLFilterTempActionRedirectULPktCount": jnxURLFilterTempActionRedirectULPktCount,
       "jnxURLFilterTempActionRedirectDLPktCount": jnxURLFilterTempActionRedirectDLPktCount,
       "jnxURLFilterTempActionRedirectULBytes": jnxURLFilterTempActionRedirectULBytes,
       "jnxURLFilterTempActionRedirectDLBytes": jnxURLFilterTempActionRedirectDLBytes,
       "jnxURLFilterTempActionTCPReset": jnxURLFilterTempActionTCPReset,
       "jnxURLFilterTempActionTCPResetULPktCount": jnxURLFilterTempActionTCPResetULPktCount,
       "jnxURLFilterTempActionTCPResetDLPktCount": jnxURLFilterTempActionTCPResetDLPktCount,
       "jnxURLFilterTempActionTCPResetULBytes": jnxURLFilterTempActionTCPResetULBytes,
       "jnxURLFilterTempActionTCPResetDLBytes": jnxURLFilterTempActionTCPResetDLBytes,
       "jnxURLFilterTempActionDUIFV4Accepted": jnxURLFilterTempActionDUIFV4Accepted,
       "jnxURLFilterTempActionDUIFV4ULPktCount": jnxURLFilterTempActionDUIFV4ULPktCount,
       "jnxURLFilterTempActionDUIFV4DLPktCount": jnxURLFilterTempActionDUIFV4DLPktCount,
       "jnxURLFilterTempActionDUIFV4ULBytes": jnxURLFilterTempActionDUIFV4ULBytes,
       "jnxURLFilterTempActionDUIFV4DLBytes": jnxURLFilterTempActionDUIFV4DLBytes,
       "jnxURLFilterTempActionDUIFV6Accepted": jnxURLFilterTempActionDUIFV6Accepted,
       "jnxURLFilterTempActionDUIFV6ULPktCount": jnxURLFilterTempActionDUIFV6ULPktCount,
       "jnxURLFilterTempActionDUIFV6DLPktCount": jnxURLFilterTempActionDUIFV6DLPktCount,
       "jnxURLFilterTempActionDUIFV6ULBytes": jnxURLFilterTempActionDUIFV6ULBytes,
       "jnxURLFilterTempActionDUIFV6DLBytes": jnxURLFilterTempActionDUIFV6DLBytes}
)
