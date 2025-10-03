# SNMP MIB module (AtiStackInfo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AtiStackInfo-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:40 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alliedTelesis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)


# Types definitions



class MACAddress(OctetString):
    """Custom type MACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_AtiStackInfoMib_ObjectIdentity = ObjectIdentity
atiStackInfoMib = _AtiStackInfoMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 16)
)
_AtiswitchEnhancedStacking_ObjectIdentity = ObjectIdentity
atiswitchEnhancedStacking = _AtiswitchEnhancedStacking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1)
)


class _AtiswitchEnhStackMode_Type(Integer32):
    """Custom type atiswitchEnhStackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unavailable", 3))
    )


_AtiswitchEnhStackMode_Type.__name__ = "Integer32"
_AtiswitchEnhStackMode_Object = MibScalar
atiswitchEnhStackMode = _AtiswitchEnhStackMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 1),
    _AtiswitchEnhStackMode_Type()
)
atiswitchEnhStackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchEnhStackMode.setStatus("current")
_AtiswitchEnhStackRemoteNumber_Type = Integer32
_AtiswitchEnhStackRemoteNumber_Object = MibScalar
atiswitchEnhStackRemoteNumber = _AtiswitchEnhStackRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 3),
    _AtiswitchEnhStackRemoteNumber_Type()
)
atiswitchEnhStackRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackRemoteNumber.setStatus("current")
_AtiswitchEnhStackTable_Object = MibTable
atiswitchEnhStackTable = _AtiswitchEnhStackTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4)
)
if mibBuilder.loadTexts:
    atiswitchEnhStackTable.setStatus("current")
_AtiswitchEnhStackEntry_Object = MibTableRow
atiswitchEnhStackEntry = _AtiswitchEnhStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1)
)
atiswitchEnhStackEntry.setIndexNames(
    (0, "AtiStackInfo-MIB", "atiswitchEnhStackSwId"),
)
if mibBuilder.loadTexts:
    atiswitchEnhStackEntry.setStatus("current")


class _AtiswitchEnhStackSwId_Type(Integer32):
    """Custom type atiswitchEnhStackSwId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiswitchEnhStackSwId_Type.__name__ = "Integer32"
_AtiswitchEnhStackSwId_Object = MibTableColumn
atiswitchEnhStackSwId = _AtiswitchEnhStackSwId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 1),
    _AtiswitchEnhStackSwId_Type()
)
atiswitchEnhStackSwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwId.setStatus("current")
_AtiswitchEnhStackSwMacAddr_Type = MACAddress
_AtiswitchEnhStackSwMacAddr_Object = MibTableColumn
atiswitchEnhStackSwMacAddr = _AtiswitchEnhStackSwMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 2),
    _AtiswitchEnhStackSwMacAddr_Type()
)
atiswitchEnhStackSwMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwMacAddr.setStatus("current")


class _AtiswitchEnhStackSwName_Type(DisplayString):
    """Custom type atiswitchEnhStackSwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchEnhStackSwName_Type.__name__ = "DisplayString"
_AtiswitchEnhStackSwName_Object = MibTableColumn
atiswitchEnhStackSwName = _AtiswitchEnhStackSwName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 3),
    _AtiswitchEnhStackSwName_Type()
)
atiswitchEnhStackSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwName.setStatus("current")


class _AtiswitchEnhStackSwMode_Type(DisplayString):
    """Custom type atiswitchEnhStackSwMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchEnhStackSwMode_Type.__name__ = "DisplayString"
_AtiswitchEnhStackSwMode_Object = MibTableColumn
atiswitchEnhStackSwMode = _AtiswitchEnhStackSwMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 4),
    _AtiswitchEnhStackSwMode_Type()
)
atiswitchEnhStackSwMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwMode.setStatus("current")


class _AtiswitchEnhStackSwSoftwareVersion_Type(DisplayString):
    """Custom type atiswitchEnhStackSwSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchEnhStackSwSoftwareVersion_Type.__name__ = "DisplayString"
_AtiswitchEnhStackSwSoftwareVersion_Object = MibTableColumn
atiswitchEnhStackSwSoftwareVersion = _AtiswitchEnhStackSwSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 5),
    _AtiswitchEnhStackSwSoftwareVersion_Type()
)
atiswitchEnhStackSwSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwSoftwareVersion.setStatus("current")


class _AtiswitchEnhStackSwModel_Type(DisplayString):
    """Custom type atiswitchEnhStackSwModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchEnhStackSwModel_Type.__name__ = "DisplayString"
_AtiswitchEnhStackSwModel_Object = MibTableColumn
atiswitchEnhStackSwModel = _AtiswitchEnhStackSwModel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 6),
    _AtiswitchEnhStackSwModel_Type()
)
atiswitchEnhStackSwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwModel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AtiStackInfo-MIB",
    **{"MACAddress": MACAddress,
       "alliedTelesis": alliedTelesis,
       "mibObject": mibObject,
       "atiStackInfoMib": atiStackInfoMib,
       "atiswitchEnhancedStacking": atiswitchEnhancedStacking,
       "atiswitchEnhStackMode": atiswitchEnhStackMode,
       "atiswitchEnhStackRemoteNumber": atiswitchEnhStackRemoteNumber,
       "atiswitchEnhStackTable": atiswitchEnhStackTable,
       "atiswitchEnhStackEntry": atiswitchEnhStackEntry,
       "atiswitchEnhStackSwId": atiswitchEnhStackSwId,
       "atiswitchEnhStackSwMacAddr": atiswitchEnhStackSwMacAddr,
       "atiswitchEnhStackSwName": atiswitchEnhStackSwName,
       "atiswitchEnhStackSwMode": atiswitchEnhStackSwMode,
       "atiswitchEnhStackSwSoftwareVersion": atiswitchEnhStackSwSoftwareVersion,
       "atiswitchEnhStackSwModel": atiswitchEnhStackSwModel}
)
