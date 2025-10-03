# SNMP MIB module (STORMSHIELD-AUTHUSERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-AUTHUSERS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:01 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsUsers = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2)
)
if mibBuilder.loadTexts:
    snsUsers.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsAuthUsersTable_Object = MibTable
snsAuthUsersTable = _SnsAuthUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snsAuthUsersTable.setStatus("current")
_SnsAuthUsersEntry_Object = MibTableRow
snsAuthUsersEntry = _SnsAuthUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1)
)
snsAuthUsersEntry.setIndexNames(
    (0, "STORMSHIELD-AUTHUSERS-MIB", "snsAuthUsersIPAddr"),
)
if mibBuilder.loadTexts:
    snsAuthUsersEntry.setStatus("current")


class _SnsAuthUsersIPAddr_Type(DisplayString):
    """Custom type snsAuthUsersIPAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsAuthUsersIPAddr_Type.__name__ = "DisplayString"
_SnsAuthUsersIPAddr_Object = MibTableColumn
snsAuthUsersIPAddr = _SnsAuthUsersIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 1),
    _SnsAuthUsersIPAddr_Type()
)
snsAuthUsersIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAuthUsersIPAddr.setStatus("current")
_SnsAuthUsersTimeOut_Type = Counter64
_SnsAuthUsersTimeOut_Object = MibTableColumn
snsAuthUsersTimeOut = _SnsAuthUsersTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 2),
    _SnsAuthUsersTimeOut_Type()
)
snsAuthUsersTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAuthUsersTimeOut.setStatus("current")
_SnsAuthUsersName_Type = SnmpAdminString
_SnsAuthUsersName_Object = MibTableColumn
snsAuthUsersName = _SnsAuthUsersName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 3),
    _SnsAuthUsersName_Type()
)
snsAuthUsersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAuthUsersName.setStatus("current")
_SnsAuthUsersDomain_Type = SnmpAdminString
_SnsAuthUsersDomain_Object = MibTableColumn
snsAuthUsersDomain = _SnsAuthUsersDomain_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 4),
    _SnsAuthUsersDomain_Type()
)
snsAuthUsersDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAuthUsersDomain.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-AUTHUSERS-MIB",
    **{"snsUsers": snsUsers,
       "snsAuthUsersTable": snsAuthUsersTable,
       "snsAuthUsersEntry": snsAuthUsersEntry,
       "snsAuthUsersIPAddr": snsAuthUsersIPAddr,
       "snsAuthUsersTimeOut": snsAuthUsersTimeOut,
       "snsAuthUsersName": snsAuthUsersName,
       "snsAuthUsersDomain": snsAuthUsersDomain}
)
