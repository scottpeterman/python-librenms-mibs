# SNMP MIB module (RUCKUS-HWINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-HWINFO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:41 2025
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

(ruckusCommonHwInfoModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonHwInfoModule")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusHwInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusHwInfoObjects_ObjectIdentity = ObjectIdentity
ruckusHwInfoObjects = _RuckusHwInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1)
)
_RuckusHwInfo_ObjectIdentity = ObjectIdentity
ruckusHwInfo = _RuckusHwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1)
)


class _RuckusHwInfoModelNumber_Type(DisplayString):
    """Custom type ruckusHwInfoModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RuckusHwInfoModelNumber_Type.__name__ = "DisplayString"
_RuckusHwInfoModelNumber_Object = MibScalar
ruckusHwInfoModelNumber = _RuckusHwInfoModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 1),
    _RuckusHwInfoModelNumber_Type()
)
ruckusHwInfoModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHwInfoModelNumber.setStatus("current")


class _RuckusHwInfoSerialNumber_Type(DisplayString):
    """Custom type ruckusHwInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RuckusHwInfoSerialNumber_Type.__name__ = "DisplayString"
_RuckusHwInfoSerialNumber_Object = MibScalar
ruckusHwInfoSerialNumber = _RuckusHwInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 2),
    _RuckusHwInfoSerialNumber_Type()
)
ruckusHwInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHwInfoSerialNumber.setStatus("current")


class _RuckusHwInfoCustomerID_Type(DisplayString):
    """Custom type ruckusHwInfoCustomerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusHwInfoCustomerID_Type.__name__ = "DisplayString"
_RuckusHwInfoCustomerID_Object = MibScalar
ruckusHwInfoCustomerID = _RuckusHwInfoCustomerID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 3),
    _RuckusHwInfoCustomerID_Type()
)
ruckusHwInfoCustomerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHwInfoCustomerID.setStatus("current")
_RuckusHwInfoHWMajorRevision_Type = Unsigned32
_RuckusHwInfoHWMajorRevision_Object = MibScalar
ruckusHwInfoHWMajorRevision = _RuckusHwInfoHWMajorRevision_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 4),
    _RuckusHwInfoHWMajorRevision_Type()
)
ruckusHwInfoHWMajorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHwInfoHWMajorRevision.setStatus("current")
_RuckusHwInfoHWMinorRevision_Type = Unsigned32
_RuckusHwInfoHWMinorRevision_Object = MibScalar
ruckusHwInfoHWMinorRevision = _RuckusHwInfoHWMinorRevision_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 5),
    _RuckusHwInfoHWMinorRevision_Type()
)
ruckusHwInfoHWMinorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHwInfoHWMinorRevision.setStatus("current")
_RuckusHwInfoEvents_ObjectIdentity = ObjectIdentity
ruckusHwInfoEvents = _RuckusHwInfoEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-HWINFO-MIB",
    **{"ruckusHwInfoMIB": ruckusHwInfoMIB,
       "ruckusHwInfoObjects": ruckusHwInfoObjects,
       "ruckusHwInfo": ruckusHwInfo,
       "ruckusHwInfoModelNumber": ruckusHwInfoModelNumber,
       "ruckusHwInfoSerialNumber": ruckusHwInfoSerialNumber,
       "ruckusHwInfoCustomerID": ruckusHwInfoCustomerID,
       "ruckusHwInfoHWMajorRevision": ruckusHwInfoHWMajorRevision,
       "ruckusHwInfoHWMinorRevision": ruckusHwInfoHWMinorRevision,
       "ruckusHwInfoEvents": ruckusHwInfoEvents}
)
