# SNMP MIB module (DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:37 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwNetworkProtocolPortProtectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 194)
)
if mibBuilder.loadTexts:
    dlinkSwNetworkProtocolPortProtectMIB.setRevisions(
        ("2017-11-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DNetworkProtocolPortProtectObjects_ObjectIdentity = ObjectIdentity
dNetworkProtocolPortProtectObjects = _DNetworkProtocolPortProtectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 194, 1)
)
_DNetworkProtocolPortProtectCtrl_ObjectIdentity = ObjectIdentity
dNetworkProtocolPortProtectCtrl = _DNetworkProtocolPortProtectCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1)
)


class _DNetworkProtocolPortProtectTCPState_Type(TruthValue):
    """Custom type dNetworkProtocolPortProtectTCPState based on TruthValue"""
    defaultValue = 1


_DNetworkProtocolPortProtectTCPState_Type.__name__ = "TruthValue"
_DNetworkProtocolPortProtectTCPState_Object = MibScalar
dNetworkProtocolPortProtectTCPState = _DNetworkProtocolPortProtectTCPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1, 1),
    _DNetworkProtocolPortProtectTCPState_Type()
)
dNetworkProtocolPortProtectTCPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNetworkProtocolPortProtectTCPState.setStatus("current")


class _DNetworkProtocolPortProtectUDPState_Type(TruthValue):
    """Custom type dNetworkProtocolPortProtectUDPState based on TruthValue"""
    defaultValue = 1


_DNetworkProtocolPortProtectUDPState_Type.__name__ = "TruthValue"
_DNetworkProtocolPortProtectUDPState_Object = MibScalar
dNetworkProtocolPortProtectUDPState = _DNetworkProtocolPortProtectUDPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1, 2),
    _DNetworkProtocolPortProtectUDPState_Type()
)
dNetworkProtocolPortProtectUDPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNetworkProtocolPortProtectUDPState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB",
    **{"dlinkSwNetworkProtocolPortProtectMIB": dlinkSwNetworkProtocolPortProtectMIB,
       "dNetworkProtocolPortProtectObjects": dNetworkProtocolPortProtectObjects,
       "dNetworkProtocolPortProtectCtrl": dNetworkProtocolPortProtectCtrl,
       "dNetworkProtocolPortProtectTCPState": dNetworkProtocolPortProtectTCPState,
       "dNetworkProtocolPortProtectUDPState": dNetworkProtocolPortProtectUDPState}
)
