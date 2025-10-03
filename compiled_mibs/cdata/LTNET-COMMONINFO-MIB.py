# SNMP MIB module (LTNET-COMMONINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\LTNET-COMMONINFO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:55 2025
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

(ltnetRoot,) = mibBuilder.importSymbols(
    "LTNET-ROOT",
    "ltnetRoot")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LtnetCommonInfoGroup_ObjectIdentity = ObjectIdentity
ltnetCommonInfoGroup = _LtnetCommonInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33826, 3)
)
_LtnetIpSimpleInfo_ObjectIdentity = ObjectIdentity
ltnetIpSimpleInfo = _LtnetIpSimpleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33826, 3, 1)
)
_LtnetIpNetAddress_Type = IpAddress
_LtnetIpNetAddress_Object = MibScalar
ltnetIpNetAddress = _LtnetIpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 33826, 3, 1, 1),
    _LtnetIpNetAddress_Type()
)
ltnetIpNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltnetIpNetAddress.setStatus("mandatory")


class _LtnetIpMask_Type(Integer32):
    """Custom type ltnetIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LtnetIpMask_Type.__name__ = "Integer32"
_LtnetIpMask_Object = MibScalar
ltnetIpMask = _LtnetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 33826, 3, 1, 2),
    _LtnetIpMask_Type()
)
ltnetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltnetIpMask.setStatus("mandatory")
_LtnetIpDefaultGateway_Type = IpAddress
_LtnetIpDefaultGateway_Object = MibScalar
ltnetIpDefaultGateway = _LtnetIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 33826, 3, 1, 3),
    _LtnetIpDefaultGateway_Type()
)
ltnetIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltnetIpDefaultGateway.setStatus("mandatory")
_LtnetIpDns_Type = IpAddress
_LtnetIpDns_Object = MibScalar
ltnetIpDns = _LtnetIpDns_Object(
    (1, 3, 6, 1, 4, 1, 33826, 3, 1, 4),
    _LtnetIpDns_Type()
)
ltnetIpDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltnetIpDns.setStatus("optional")
_LtnetIpPhysicalAddress_Type = OctetString
_LtnetIpPhysicalAddress_Object = MibScalar
ltnetIpPhysicalAddress = _LtnetIpPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 33826, 3, 1, 5),
    _LtnetIpPhysicalAddress_Type()
)
ltnetIpPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltnetIpPhysicalAddress.setStatus("mandatory")
_LtnetSubJoinedInfo_ObjectIdentity = ObjectIdentity
ltnetSubJoinedInfo = _LtnetSubJoinedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33826, 3, 4)
)


class _LtnetCommIdentifyNum_Type(OctetString):
    """Custom type ltnetCommIdentifyNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 10),
    )


_LtnetCommIdentifyNum_Type.__name__ = "OctetString"
_LtnetCommIdentifyNum_Object = MibScalar
ltnetCommIdentifyNum = _LtnetCommIdentifyNum_Object(
    (1, 3, 6, 1, 4, 1, 33826, 3, 4, 1),
    _LtnetCommIdentifyNum_Type()
)
ltnetCommIdentifyNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltnetCommIdentifyNum.setStatus("optional")
_LtnetCommonTime_Type = Integer32
_LtnetCommonTime_Object = MibScalar
ltnetCommonTime = _LtnetCommonTime_Object(
    (1, 3, 6, 1, 4, 1, 33826, 3, 4, 2),
    _LtnetCommonTime_Type()
)
ltnetCommonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltnetCommonTime.setStatus("mandatory")


class _LtnetAlarmDelayTime_Type(Integer32):
    """Custom type ltnetAlarmDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_LtnetAlarmDelayTime_Type.__name__ = "Integer32"
_LtnetAlarmDelayTime_Object = MibScalar
ltnetAlarmDelayTime = _LtnetAlarmDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 33826, 3, 4, 3),
    _LtnetAlarmDelayTime_Type()
)
ltnetAlarmDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltnetAlarmDelayTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LTNET-COMMONINFO-MIB",
    **{"ltnetCommonInfoGroup": ltnetCommonInfoGroup,
       "ltnetIpSimpleInfo": ltnetIpSimpleInfo,
       "ltnetIpNetAddress": ltnetIpNetAddress,
       "ltnetIpMask": ltnetIpMask,
       "ltnetIpDefaultGateway": ltnetIpDefaultGateway,
       "ltnetIpDns": ltnetIpDns,
       "ltnetIpPhysicalAddress": ltnetIpPhysicalAddress,
       "ltnetSubJoinedInfo": ltnetSubJoinedInfo,
       "ltnetCommIdentifyNum": ltnetCommIdentifyNum,
       "ltnetCommonTime": ltnetCommonTime,
       "ltnetAlarmDelayTime": ltnetAlarmDelayTime}
)
