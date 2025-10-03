# SNMP MIB module (LAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\peplink\LAN
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:41 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lanInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortSpeedType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("auto", 1),
          ("fullDulplex10", 2),
          ("halfDulplex10", 3),
          ("fullDulplex100", 4),
          ("halfDulplex100", 5),
          ("fullDulplex1000", 6),
          ("halfDulplex1000", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Peplink_ObjectIdentity = ObjectIdentity
peplink = _Peplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695)
)
_ProductMib_ObjectIdentity = ObjectIdentity
productMib = _ProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200)
)
_GeneralMib_ObjectIdentity = ObjectIdentity
generalMib = _GeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1)
)
_LanMib_ObjectIdentity = ObjectIdentity
lanMib = _LanMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 3)
)
_LanStatus_ObjectIdentity = ObjectIdentity
lanStatus = _LanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1)
)
_LanIp_Type = IpAddress
_LanIp_Object = MibScalar
lanIp = _LanIp_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 1),
    _LanIp_Type()
)
lanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanIp.setStatus("current")
_LanSubnetMask_Type = IpAddress
_LanSubnetMask_Object = MibScalar
lanSubnetMask = _LanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 2),
    _LanSubnetMask_Type()
)
lanSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSubnetMask.setStatus("current")
_LanSpeed_Type = PortSpeedType
_LanSpeed_Object = MibScalar
lanSpeed = _LanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 3),
    _LanSpeed_Type()
)
lanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSpeed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN",
    **{"PortSpeedType": PortSpeedType,
       "peplink": peplink,
       "productMib": productMib,
       "generalMib": generalMib,
       "lanMib": lanMib,
       "lanInfo": lanInfo,
       "lanStatus": lanStatus,
       "lanIp": lanIp,
       "lanSubnetMask": lanSubnetMask,
       "lanSpeed": lanSpeed}
)
