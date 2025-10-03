# SNMP MIB module (HH3C-8021X-EXT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-8021X-EXT2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:40 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3c8021XExt2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153)
)
if mibBuilder.loadTexts:
    hh3c8021XExt2.setRevisions(
        ("2017-10-10 00:00",
         "2014-03-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3c8021XExt2MibObjects_ObjectIdentity = ObjectIdentity
hh3c8021XExt2MibObjects = _Hh3c8021XExt2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1)
)
_Hh3c8021XExt2System_ObjectIdentity = ObjectIdentity
hh3c8021XExt2System = _Hh3c8021XExt2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 1)
)


class _Hh3c8021XExt2AuthQuietPeriod_Type(Unsigned32):
    """Custom type hh3c8021XExt2AuthQuietPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_Hh3c8021XExt2AuthQuietPeriod_Type.__name__ = "Unsigned32"
_Hh3c8021XExt2AuthQuietPeriod_Object = MibScalar
hh3c8021XExt2AuthQuietPeriod = _Hh3c8021XExt2AuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 1, 1),
    _Hh3c8021XExt2AuthQuietPeriod_Type()
)
hh3c8021XExt2AuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthQuietPeriod.setStatus("current")


class _Hh3c8021XExt2AuthTxPeriod_Type(Unsigned32):
    """Custom type hh3c8021XExt2AuthTxPeriod based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Hh3c8021XExt2AuthTxPeriod_Type.__name__ = "Unsigned32"
_Hh3c8021XExt2AuthTxPeriod_Object = MibScalar
hh3c8021XExt2AuthTxPeriod = _Hh3c8021XExt2AuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 1, 2),
    _Hh3c8021XExt2AuthTxPeriod_Type()
)
hh3c8021XExt2AuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthTxPeriod.setStatus("current")


class _Hh3c8021XExt2AuthSuppTimeout_Type(Unsigned32):
    """Custom type hh3c8021XExt2AuthSuppTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Hh3c8021XExt2AuthSuppTimeout_Type.__name__ = "Unsigned32"
_Hh3c8021XExt2AuthSuppTimeout_Object = MibScalar
hh3c8021XExt2AuthSuppTimeout = _Hh3c8021XExt2AuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 1, 3),
    _Hh3c8021XExt2AuthSuppTimeout_Type()
)
hh3c8021XExt2AuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthSuppTimeout.setStatus("current")


class _Hh3c8021XExt2AuthServerTimeout_Type(Unsigned32):
    """Custom type hh3c8021XExt2AuthServerTimeout based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300),
    )


_Hh3c8021XExt2AuthServerTimeout_Type.__name__ = "Unsigned32"
_Hh3c8021XExt2AuthServerTimeout_Object = MibScalar
hh3c8021XExt2AuthServerTimeout = _Hh3c8021XExt2AuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 1, 4),
    _Hh3c8021XExt2AuthServerTimeout_Type()
)
hh3c8021XExt2AuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthServerTimeout.setStatus("current")


class _Hh3c8021XExt2AuthMaxReq_Type(Unsigned32):
    """Custom type hh3c8021XExt2AuthMaxReq based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3c8021XExt2AuthMaxReq_Type.__name__ = "Unsigned32"
_Hh3c8021XExt2AuthMaxReq_Object = MibScalar
hh3c8021XExt2AuthMaxReq = _Hh3c8021XExt2AuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 1, 5),
    _Hh3c8021XExt2AuthMaxReq_Type()
)
hh3c8021XExt2AuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthMaxReq.setStatus("current")


class _Hh3c8021XExt2AuthReAuthPeriod_Type(Unsigned32):
    """Custom type hh3c8021XExt2AuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_Hh3c8021XExt2AuthReAuthPeriod_Type.__name__ = "Unsigned32"
_Hh3c8021XExt2AuthReAuthPeriod_Object = MibScalar
hh3c8021XExt2AuthReAuthPeriod = _Hh3c8021XExt2AuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 1, 6),
    _Hh3c8021XExt2AuthReAuthPeriod_Type()
)
hh3c8021XExt2AuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthReAuthPeriod.setStatus("current")


class _Hh3c8021XExt2AuthMethod_Type(Integer32):
    """Custom type hh3c8021XExt2AuthMethod based on Integer32"""
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
        *(("chap", 1),
          ("pap", 2),
          ("eap", 3))
    )


_Hh3c8021XExt2AuthMethod_Type.__name__ = "Integer32"
_Hh3c8021XExt2AuthMethod_Object = MibScalar
hh3c8021XExt2AuthMethod = _Hh3c8021XExt2AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 1, 7),
    _Hh3c8021XExt2AuthMethod_Type()
)
hh3c8021XExt2AuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthMethod.setStatus("current")
_Hh3c8021XExt2Authenticator_ObjectIdentity = ObjectIdentity
hh3c8021XExt2Authenticator = _Hh3c8021XExt2Authenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2)
)
_Hh3c8021XExt2AuthConfigExtTable_Object = MibTable
hh3c8021XExt2AuthConfigExtTable = _Hh3c8021XExt2AuthConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthConfigExtTable.setStatus("current")
_Hh3c8021XExt2AuthConfigExtEntry_Object = MibTableRow
hh3c8021XExt2AuthConfigExtEntry = _Hh3c8021XExt2AuthConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1, 1)
)
hh3c8021XExt2AuthConfigExtEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    hh3c8021XExt2AuthConfigExtEntry.setStatus("current")


class _Hh3c8021XExt2PaePortAuthAdminStatus_Type(TruthValue):
    """Custom type hh3c8021XExt2PaePortAuthAdminStatus based on TruthValue"""
    defaultValue = 2


_Hh3c8021XExt2PaePortAuthAdminStatus_Type.__name__ = "TruthValue"
_Hh3c8021XExt2PaePortAuthAdminStatus_Object = MibTableColumn
hh3c8021XExt2PaePortAuthAdminStatus = _Hh3c8021XExt2PaePortAuthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1, 1, 1),
    _Hh3c8021XExt2PaePortAuthAdminStatus_Type()
)
hh3c8021XExt2PaePortAuthAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2PaePortAuthAdminStatus.setStatus("current")


class _Hh3c8021XExt2PaePortControlledType_Type(Integer32):
    """Custom type hh3c8021XExt2PaePortControlledType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portbased", 1),
          ("macbased", 2))
    )


_Hh3c8021XExt2PaePortControlledType_Type.__name__ = "Integer32"
_Hh3c8021XExt2PaePortControlledType_Object = MibTableColumn
hh3c8021XExt2PaePortControlledType = _Hh3c8021XExt2PaePortControlledType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1, 1, 2),
    _Hh3c8021XExt2PaePortControlledType_Type()
)
hh3c8021XExt2PaePortControlledType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2PaePortControlledType.setStatus("current")


class _Hh3c8021XExt2PaePortMaxUserNum_Type(Unsigned32):
    """Custom type hh3c8021XExt2PaePortMaxUserNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3c8021XExt2PaePortMaxUserNum_Type.__name__ = "Unsigned32"
_Hh3c8021XExt2PaePortMaxUserNum_Object = MibTableColumn
hh3c8021XExt2PaePortMaxUserNum = _Hh3c8021XExt2PaePortMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1, 1, 3),
    _Hh3c8021XExt2PaePortMaxUserNum_Type()
)
hh3c8021XExt2PaePortMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2PaePortMaxUserNum.setStatus("current")
_Hh3c8021XExt2PaePortUserNumNow_Type = Unsigned32
_Hh3c8021XExt2PaePortUserNumNow_Object = MibTableColumn
hh3c8021XExt2PaePortUserNumNow = _Hh3c8021XExt2PaePortUserNumNow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1, 1, 4),
    _Hh3c8021XExt2PaePortUserNumNow_Type()
)
hh3c8021XExt2PaePortUserNumNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c8021XExt2PaePortUserNumNow.setStatus("current")


class _Hh3c8021XExt2PaePortClearStatistics_Type(Integer32):
    """Custom type hh3c8021XExt2PaePortClearStatistics based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 0),
          ("clear", 1))
    )


_Hh3c8021XExt2PaePortClearStatistics_Type.__name__ = "Integer32"
_Hh3c8021XExt2PaePortClearStatistics_Object = MibTableColumn
hh3c8021XExt2PaePortClearStatistics = _Hh3c8021XExt2PaePortClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1, 1, 5),
    _Hh3c8021XExt2PaePortClearStatistics_Type()
)
hh3c8021XExt2PaePortClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2PaePortClearStatistics.setStatus("current")


class _Hh3c8021XExt2PaePortMcastTrigStatus_Type(TruthValue):
    """Custom type hh3c8021XExt2PaePortMcastTrigStatus based on TruthValue"""
    defaultValue = 1


_Hh3c8021XExt2PaePortMcastTrigStatus_Type.__name__ = "TruthValue"
_Hh3c8021XExt2PaePortMcastTrigStatus_Object = MibTableColumn
hh3c8021XExt2PaePortMcastTrigStatus = _Hh3c8021XExt2PaePortMcastTrigStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1, 1, 6),
    _Hh3c8021XExt2PaePortMcastTrigStatus_Type()
)
hh3c8021XExt2PaePortMcastTrigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2PaePortMcastTrigStatus.setStatus("current")


class _Hh3c8021XExt2PaePortHandshakeStatus_Type(TruthValue):
    """Custom type hh3c8021XExt2PaePortHandshakeStatus based on TruthValue"""
    defaultValue = 1


_Hh3c8021XExt2PaePortHandshakeStatus_Type.__name__ = "TruthValue"
_Hh3c8021XExt2PaePortHandshakeStatus_Object = MibTableColumn
hh3c8021XExt2PaePortHandshakeStatus = _Hh3c8021XExt2PaePortHandshakeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153, 1, 2, 1, 1, 7),
    _Hh3c8021XExt2PaePortHandshakeStatus_Type()
)
hh3c8021XExt2PaePortHandshakeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c8021XExt2PaePortHandshakeStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-8021X-EXT2-MIB",
    **{"hh3c8021XExt2": hh3c8021XExt2,
       "hh3c8021XExt2MibObjects": hh3c8021XExt2MibObjects,
       "hh3c8021XExt2System": hh3c8021XExt2System,
       "hh3c8021XExt2AuthQuietPeriod": hh3c8021XExt2AuthQuietPeriod,
       "hh3c8021XExt2AuthTxPeriod": hh3c8021XExt2AuthTxPeriod,
       "hh3c8021XExt2AuthSuppTimeout": hh3c8021XExt2AuthSuppTimeout,
       "hh3c8021XExt2AuthServerTimeout": hh3c8021XExt2AuthServerTimeout,
       "hh3c8021XExt2AuthMaxReq": hh3c8021XExt2AuthMaxReq,
       "hh3c8021XExt2AuthReAuthPeriod": hh3c8021XExt2AuthReAuthPeriod,
       "hh3c8021XExt2AuthMethod": hh3c8021XExt2AuthMethod,
       "hh3c8021XExt2Authenticator": hh3c8021XExt2Authenticator,
       "hh3c8021XExt2AuthConfigExtTable": hh3c8021XExt2AuthConfigExtTable,
       "hh3c8021XExt2AuthConfigExtEntry": hh3c8021XExt2AuthConfigExtEntry,
       "hh3c8021XExt2PaePortAuthAdminStatus": hh3c8021XExt2PaePortAuthAdminStatus,
       "hh3c8021XExt2PaePortControlledType": hh3c8021XExt2PaePortControlledType,
       "hh3c8021XExt2PaePortMaxUserNum": hh3c8021XExt2PaePortMaxUserNum,
       "hh3c8021XExt2PaePortUserNumNow": hh3c8021XExt2PaePortUserNumNow,
       "hh3c8021XExt2PaePortClearStatistics": hh3c8021XExt2PaePortClearStatistics,
       "hh3c8021XExt2PaePortMcastTrigStatus": hh3c8021XExt2PaePortMcastTrigStatus,
       "hh3c8021XExt2PaePortHandshakeStatus": hh3c8021XExt2PaePortHandshakeStatus}
)
