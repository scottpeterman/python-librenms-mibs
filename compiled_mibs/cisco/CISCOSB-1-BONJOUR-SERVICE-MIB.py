# SNMP MIB module (CISCOSB-1-BONJOUR-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-1-BONJOUR-SERVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:11 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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

rlCustom1BonjourService = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143)
)
if mibBuilder.loadTexts:
    rlCustom1BonjourService.setRevisions(
        ("2009-03-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlCustom1BonjourServiceTable_Object = MibTable
rlCustom1BonjourServiceTable = _RlCustom1BonjourServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143, 1)
)
if mibBuilder.loadTexts:
    rlCustom1BonjourServiceTable.setStatus("current")
_RlCustom1BonjourServiceEntry_Object = MibTableRow
rlCustom1BonjourServiceEntry = _RlCustom1BonjourServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143, 1, 1)
)
rlCustom1BonjourServiceEntry.setIndexNames(
    (1, "CISCOSB-1-BONJOUR-SERVICE-MIB", "rlCustom1BonjourServiceTypeName"),
)
if mibBuilder.loadTexts:
    rlCustom1BonjourServiceEntry.setStatus("current")


class _RlCustom1BonjourServiceTypeName_Type(DisplayString):
    """Custom type rlCustom1BonjourServiceTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 14),
    )


_RlCustom1BonjourServiceTypeName_Type.__name__ = "DisplayString"
_RlCustom1BonjourServiceTypeName_Object = MibTableColumn
rlCustom1BonjourServiceTypeName = _RlCustom1BonjourServiceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143, 1, 1, 1),
    _RlCustom1BonjourServiceTypeName_Type()
)
rlCustom1BonjourServiceTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCustom1BonjourServiceTypeName.setStatus("current")


class _RlCustom1BonjourServiceTransport_Type(Integer32):
    """Custom type rlCustom1BonjourServiceTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2))
    )


_RlCustom1BonjourServiceTransport_Type.__name__ = "Integer32"
_RlCustom1BonjourServiceTransport_Object = MibTableColumn
rlCustom1BonjourServiceTransport = _RlCustom1BonjourServiceTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143, 1, 1, 2),
    _RlCustom1BonjourServiceTransport_Type()
)
rlCustom1BonjourServiceTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCustom1BonjourServiceTransport.setStatus("current")


class _RlCustom1BonjourServicePort_Type(Integer32):
    """Custom type rlCustom1BonjourServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlCustom1BonjourServicePort_Type.__name__ = "Integer32"
_RlCustom1BonjourServicePort_Object = MibTableColumn
rlCustom1BonjourServicePort = _RlCustom1BonjourServicePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143, 1, 1, 3),
    _RlCustom1BonjourServicePort_Type()
)
rlCustom1BonjourServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCustom1BonjourServicePort.setStatus("current")
_RlCustom1BonjourServiceEnable_Type = TruthValue
_RlCustom1BonjourServiceEnable_Object = MibTableColumn
rlCustom1BonjourServiceEnable = _RlCustom1BonjourServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143, 1, 1, 4),
    _RlCustom1BonjourServiceEnable_Type()
)
rlCustom1BonjourServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCustom1BonjourServiceEnable.setStatus("current")


class _RlCustom1BonjourServiceOptions_Type(Bits):
    """Custom type rlCustom1BonjourServiceOptions based on Bits"""
    namedValues = NamedValues(
        *(("serviceCanBeDeleted", 0),
          ("serviceCanBeDisabled", 1),
          ("portCanBeConfigured", 2))
    )

_RlCustom1BonjourServiceOptions_Type.__name__ = "Bits"
_RlCustom1BonjourServiceOptions_Object = MibTableColumn
rlCustom1BonjourServiceOptions = _RlCustom1BonjourServiceOptions_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143, 1, 1, 5),
    _RlCustom1BonjourServiceOptions_Type()
)
rlCustom1BonjourServiceOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCustom1BonjourServiceOptions.setStatus("current")
_RlCustom1BonjourServiceStatus_Type = RowStatus
_RlCustom1BonjourServiceStatus_Object = MibTableColumn
rlCustom1BonjourServiceStatus = _RlCustom1BonjourServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143, 1, 1, 6),
    _RlCustom1BonjourServiceStatus_Type()
)
rlCustom1BonjourServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCustom1BonjourServiceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-1-BONJOUR-SERVICE-MIB",
    **{"rlCustom1BonjourService": rlCustom1BonjourService,
       "rlCustom1BonjourServiceTable": rlCustom1BonjourServiceTable,
       "rlCustom1BonjourServiceEntry": rlCustom1BonjourServiceEntry,
       "rlCustom1BonjourServiceTypeName": rlCustom1BonjourServiceTypeName,
       "rlCustom1BonjourServiceTransport": rlCustom1BonjourServiceTransport,
       "rlCustom1BonjourServicePort": rlCustom1BonjourServicePort,
       "rlCustom1BonjourServiceEnable": rlCustom1BonjourServiceEnable,
       "rlCustom1BonjourServiceOptions": rlCustom1BonjourServiceOptions,
       "rlCustom1BonjourServiceStatus": rlCustom1BonjourServiceStatus}
)
